import math

def reprod(x):
    if x <= 0:
        return 0
    else:
        return x + x*(420-x)/5000

def trap(x):
    return .03*x

def damage(t): 
    d = 2
    dt_val_for_12 = min(abs(t-12), abs((52+t)-12), abs(t-(52+12)))
    if dt_val_for_12 < 10:
        d += 8*(1-(dt_val_for_12/10)**2)**2
    dt_val_for_48 = min(abs(t-48), abs((52+t)-48), abs(t-(52+48)))
    if dt_val_for_48 < 7:
        d += 6*(1-(dt_val_for_48/7)**2)**2
    return d 

def hunter(x):
    return .2*x


INITIAL_PIGS = 67
TOTAL_TRAPS_BUDGET = 27
MAX_TRAPS_PER_WEEK = 4
NUM_WEEKS = 52  # Simulating weeks 0 to 51

# --- Memoisation Dictionary ---
memo_c14 = {}

def solve_communication_14(week, current_pigs, traps_left, deployed_traps_last_week):
    """
    Calculates the minimum expected total environmental damage.
    current_pigs_int is always an integer (result of prior stochastic rounding).
    """
    state = (week, current_pigs, traps_left, deployed_traps_last_week)
    if state in memo_c14:
        return memo_c14[state]

    # Base Case: End of the year
    if week == NUM_WEEKS:
        return float(current_pigs * 50.0) # Expected damage is deterministic here

    # Current pigs as float for calculations
    current_pigs_float = float(current_pigs)

    # Damage from pigs in the current week
    # damage(week) can return int or float. Multiplying by current_pigs_float ensures result is float.
    damage_from_pigs_this_week = current_pigs_float * damage(week)

    min_expected_total_damage_from_this_state = float('inf')

    for k_traps_to_deploy_this_week in range(min(MAX_TRAPS_PER_WEEK, traps_left) + 1):

        damage_from_trap_deployment_activity = 0.0
        if k_traps_to_deploy_this_week > 0 and not deployed_traps_last_week:
            # damage(week) can return int or float. Result will be float due to 4.0 and multiplication.
            damage_from_trap_deployment_activity = float(k_traps_to_deploy_this_week * 4.0) * damage(week)

        # Calculate population for the start of the NEXT week (as a float)
        # reprod and trap are called with current_pigs_float.
        # reprod will return float (or int 0 if input <=0).
        # trap will return float.
        pigs_after_reproduction_float = reprod(current_pigs_float)
        pigs_eliminated_by_k_traps_float = float(k_traps_to_deploy_this_week) * trap(current_pigs_float)
        
        # Ensure pigs_after_reproduction_float is float for subtraction if it was int 0
        next_week_pigs_float = max(0.0, float(pigs_after_reproduction_float) - pigs_eliminated_by_k_traps_float)


        # Stochastic Rounding and Expected Future Damage Calculation
        floor_pigs_val = math.floor(next_week_pigs_float)
        ceil_pigs_val = math.ceil(next_week_pigs_float)

        expected_damage_from_future_weeks = 0.0

        common_args_for_next_state = {
            "traps_left": traps_left - k_traps_to_deploy_this_week,
            "deployed_traps_last_week": (k_traps_to_deploy_this_week > 0)
        }

        if floor_pigs_val == ceil_pigs_val:
            expected_damage_from_future_weeks = solve_communication_14(
                week + 1,
                int(floor_pigs_val),
                **common_args_for_next_state
            )
        else:
            prob_round_up = next_week_pigs_float - floor_pigs_val
            prob_round_down = 1.0 - prob_round_up
            
            damage_if_ceil = solve_communication_14(
                week + 1,
                int(ceil_pigs_val),
                **common_args_for_next_state
            )
            damage_if_floor = solve_communication_14(
                week + 1,
                int(floor_pigs_val),
                **common_args_for_next_state
            )
            expected_damage_from_future_weeks = (prob_round_up * damage_if_ceil) + \
                                              (prob_round_down * damage_if_floor)
        
        current_choice_total_expected_damage = (damage_from_pigs_this_week +
                                              damage_from_trap_deployment_activity +
                                              expected_damage_from_future_weeks)

        if current_choice_total_expected_damage < min_expected_total_damage_from_this_state:
            min_expected_total_damage_from_this_state = current_choice_total_expected_damage
            
    memo_c14[state] = min_expected_total_damage_from_this_state
    return min_expected_total_damage_from_this_state

final_expected_total_damage_c14 = solve_communication_14(0, INITIAL_PIGS, TOTAL_TRAPS_BUDGET, False)

print(f"{final_expected_total_damage_c14}")