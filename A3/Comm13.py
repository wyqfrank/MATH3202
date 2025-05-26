import math

# --- Helper Functions as provided in the problem ---
def reprod(x_float):
    # Ensure x is treated as a number; problem implies population can be non-integer until rounded
    x = float(x_float)
    if x <= 0:
        return 0
    else:
        # Result is rounded, implies discrete pigs for next step, but could be float from round()
        return round(x + x * (420.0 - x) / 5000.0)

def damage(t):
    d = 2.0  # Start with float for consistency in damage calculations
    
    # Peak 1 at week 12
    # The min(abs(t-X), abs((52+t)-X), abs(t-(52+X))) pattern correctly finds shortest distance on a circle
    dt1 = min(abs(t - 12), abs((52 + t) - 12), abs(t - (52 + 12)))
    if dt1 < 10:
        d += 8.0 * (1.0 - (dt1 / 10.0)**2)**2
    
    # Peak 2 at week 48
    dt2 = min(abs(t - 48), abs((52 + t) - 48), abs(t - (52 + 48)))
    if dt2 < 7:
        d += 6.0 * (1.0 - (dt2 / 7.0)**2)**2
    return d

def trap(x_float):
    x = float(x_float)
    if x <= 0:
        return 0
    # Result is rounded
    return round(0.03 * x)

# --- Global Parameters ---
INITIAL_PIGS = 67
TOTAL_TRAPS_BUDGET = 27
MAX_TRAPS_PER_WEEK = 4
NUM_WEEKS = 52  # Simulating weeks 0 to 51

# --- Memoization Dictionary ---
memo_c13 = {}

def solve_communication_13(week, current_pigs_raw, traps_left, deployed_traps_last_week):
    """
    Calculates the minimum total environmental damage for Communication 13.
    State: (week, current_pigs (as int), traps_left, deployed_traps_last_week)
    """
    # Pigs are discrete units; ensure integer representation for state and consistent calculations.
    # reprod/trap functions handle rounding, their output might be float (e.g., 72.0)
    current_pigs = int(round(current_pigs_raw))
    if current_pigs < 0: # Should not happen with max(0, ...) but as safeguard
        current_pigs = 0

    state = (week, current_pigs, traps_left, deployed_traps_last_week)
    if state in memo_c13:
        return memo_c13[state]

    # Base Case: End of the year (after week 51, which is the start of implicit week 52)
    if week == NUM_WEEKS:
        # Penalty for pigs remaining at the end of the year
        return float(current_pigs * 50)

    # --- Damage Calculation for the Current Week ---
    # 1. Damage from pigs themselves
    damage_from_pigs_this_week = float(current_pigs * damage(week))

    min_total_damage_from_this_state_onwards = float('inf')

    # Iterate over possible number of traps to deploy this week (k)
    for k_traps_to_deploy_this_week in range(min(MAX_TRAPS_PER_WEEK, traps_left) + 1):
        
        # 2. Damage from deploying traps THIS week (Communication 13 specific)
        damage_from_trap_deployment_activity = 0.0
        if k_traps_to_deploy_this_week > 0 and not deployed_traps_last_week:
            damage_from_trap_deployment_activity = k_traps_to_deploy_this_week * 4 * damage(week)

        # --- Population Update for the START of the NEXT week ---
        # Population after natural reproduction (based on current_pigs at start of *this* week)
        pigs_after_reproduction = reprod(current_pigs) 
        
        # Pigs removed by traps deployed this week (also based on current_pigs)
        pigs_eliminated_by_k_traps = k_traps_to_deploy_this_week * trap(current_pigs)
        
        # Population at start of next week
        next_week_pigs_raw = max(0, pigs_after_reproduction - pigs_eliminated_by_k_traps)
        # Next state will also convert this to int(round(next_week_pigs_raw))

        # --- Recursive Step ---
        # Determine if traps were deployed this turn (for the next state's 'deployed_traps_last_week')
        were_traps_deployed_this_turn = (k_traps_to_deploy_this_week > 0)
        traps_remaining_for_future = traps_left - k_traps_to_deploy_this_week
        
        # Recursively find the sum of damage from the next week onwards
        damage_from_future_weeks = solve_communication_13(
            week + 1,
            next_week_pigs_raw, # Pass the raw (potentially float) value
            traps_remaining_for_future,
            were_traps_deployed_this_turn
        )

        # Total damage if this choice (k_traps_to_deploy_this_week) is made
        current_choice_total_damage = (damage_from_pigs_this_week +
                                       damage_from_trap_deployment_activity +
                                       damage_from_future_weeks)

        if current_choice_total_damage < min_total_damage_from_this_state_onwards:
            min_total_damage_from_this_state_onwards = current_choice_total_damage

    memo_c13[state] = min_total_damage_from_this_state_onwards
    return min_total_damage_from_this_state_onwards

# --- Initial Call for Communication 13 ---
# Start at week 0, with INITIAL_PIGS, TOTAL_TRAPS_BUDGET, 
# and False (no traps deployed before week 0).
final_total_damage_c13 = solve_communication_13(0, INITIAL_PIGS, TOTAL_TRAPS_BUDGET, False)

print(f"{final_total_damage_c13}")