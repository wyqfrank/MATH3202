import math

def new_reprod(x_val): # x_val is an integer from the DP state
    x = float(x_val) # Use float for calculations
    if x <= 0:
        return 0.0
    else:
        return x + x * (420.0 - x) / 5000.0

def new_trap(x_val): # x_val is an integer from the DP state
    x = float(x_val) # Use float for calculations
    if x <= 0:
        return 0.0
    return 0.03 * x

# Damage Function
def damage(t):
    d = 2.0
    dt1 = min(abs(t - 12), abs((52 + t) - 12), abs(t - (52 + 12)))
    if dt1 < 10:
        d += 8.0 * (1.0 - (dt1 / 10.0)**2)**2
    dt2 = min(abs(t - 48), abs((52 + t) - 48), abs(t - (52 + 48)))
    if dt2 < 7:
        d += 6.0 * (1.0 - (dt2 / 7.0)**2)**2
    return d

# Global Parameters 
INITIAL_PIGS = 67
TOTAL_TRAPS_BUDGET = 27
MAX_TRAPS_PER_WEEK = 4
NUM_WEEKS = 52  # Simulating weeks 0 to 51

# --- Memoisation Dictionary for Communication 14 ---
memo_c14 = {}

def solve_communication_14(week, current_pigs_int, traps_left, deployed_traps_last_week):
    """
    Calculates the minimum expected total environmental damage for Communication 14.
    current_pigs_int is always an integer (result of prior stochastic rounding).
    """
    state = (week, current_pigs_int, traps_left, deployed_traps_last_week)
    if state in memo_c14:
        return memo_c14[state]

    # Base Case: End of the year
    if week == NUM_WEEKS:
        return float(current_pigs_int * 50) # Expected damage is deterministic here

    # Damage from pigs in the current week (deterministic for this state)
    damage_from_pigs_this_week = float(current_pigs_int * damage(week))

    min_expected_total_damage_from_this_state = float('inf')

    for k_traps_to_deploy_this_week in range(min(MAX_TRAPS_PER_WEEK, traps_left) + 1):
        
        # Damage from trap deployment activity (deterministic for this choice k)
        damage_from_trap_deployment_activity = 0.0
        if k_traps_to_deploy_this_week > 0 and not deployed_traps_last_week:
            damage_from_trap_deployment_activity = float(k_traps_to_deploy_this_week * 4 * damage(week))

        # --- Calculate population for the start of the NEXT week (as a float) ---
        pigs_after_reproduction_float = new_reprod(current_pigs_int)
        pigs_eliminated_by_k_traps_float = k_traps_to_deploy_this_week * new_trap(current_pigs_int)
        
        next_week_pigs_float = max(0.0, pigs_after_reproduction_float - pigs_eliminated_by_k_traps_float)

        # --- Stochastic Rounding and Expected Future Damage Calculation ---
        floor_pigs_val = math.floor(next_week_pigs_float)
        ceil_pigs_val = math.ceil(next_week_pigs_float)
        
        expected_damage_from_future_weeks = 0.0
        
        # Arguments for recursive calls, common to both floor and ceil paths
        common_args_for_next_state = {
            "traps_left": traps_left - k_traps_to_deploy_this_week,
            "deployed_traps_last_week": (k_traps_to_deploy_this_week > 0)
        }

        if floor_pigs_val == ceil_pigs_val:
            # This means next_week_pigs_float was (or is treated as) an integer.
            # Deterministic transition to int(floor_pigs_val) pigs.
            expected_damage_from_future_weeks = solve_communication_14(
                week + 1,
                int(floor_pigs_val), # Next state's pig count is an integer
                **common_args_for_next_state
            )
        else:
            # Stochastic transition based on the fractional part
            prob_round_up = next_week_pigs_float - floor_pigs_val # This is 'p'
            prob_round_down = 1.0 - prob_round_up
            
            damage_if_ceil = solve_communication_14(
                week + 1,
                int(ceil_pigs_val), # Next state's pig count is an integer
                **common_args_for_next_state
            )
            damage_if_floor = solve_communication_14(
                week + 1,
                int(floor_pigs_val), # Next state's pig count is an integer
                **common_args_for_next_state
            )
            expected_damage_from_future_weeks = (prob_round_up * damage_if_ceil) + \
                                                (prob_round_down * damage_if_floor)
        
        # Total expected damage for this choice of k_traps_to_deploy_this_week
        current_choice_total_expected_damage = (damage_from_pigs_this_week +
                                                damage_from_trap_deployment_activity +
                                                expected_damage_from_future_weeks)

        if current_choice_total_expected_damage < min_expected_total_damage_from_this_state:
            min_expected_total_damage_from_this_state = current_choice_total_expected_damage
            
    memo_c14[state] = min_expected_total_damage_from_this_state
    return min_expected_total_damage_from_this_state

# Initial Call for Communication 14
# Start at week 0, with INITIAL_PIGS (integer), TOTAL_TRAPS_BUDGET, 
# and False (no traps deployed before week 0).
final_expected_total_damage_c14 = solve_communication_14(0, INITIAL_PIGS, TOTAL_TRAPS_BUDGET, False)

print(f"{final_expected_total_damage_c14}")