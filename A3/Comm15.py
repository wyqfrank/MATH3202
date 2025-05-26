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
    dt = min(abs(t-12), abs((52+t)-12), abs(t-(52+12)))
    if dt < 10:
        d += 8*(1-(dt/10)**2)**2
    dt = min(abs(t-48), abs((52+t)-48), abs(t-(52+48)))
    if dt < 7:
        d += 6*(1-(dt/7)**2)**2
    return d

def hunter(x):
    return .2*x

# Data
INITIAL_PIGS = 67
TOTAL_TRAPS_BUDGET = 27
MAX_TRAPS_PER_WEEK = 4
NUM_WEEKS = 52 
MAX_HUNTING_WEEKS = 2

memo_c15 = {}

def solve_communication_15(week, current_pigs, traps_left, deployed_traps_last_week, hunting_weeks_used):
    state = (week, current_pigs, traps_left, deployed_traps_last_week, hunting_weeks_used)
    if state in memo_c15:
        return memo_c15[state]

    # Base Case: End of the year
    if week == NUM_WEEKS:
        return float(current_pigs * 50)  # Expected damage from pigs left

    damage_from_pigs_this_week = float(current_pigs * damage(week))
    min_total_damage_for_state = float('inf')

    # Standard week (deploy traps)
    for k_traps_this_week in range(min(MAX_TRAPS_PER_WEEK, traps_left) + 1):
        damage_from_trap_deployment_activity = 0.0
        if k_traps_this_week > 0 and not deployed_traps_last_week:
            damage_from_trap_deployment_activity = float(k_traps_this_week * 4 * damage(week))

        pigs_after_reproduction_float = reprod(current_pigs)  
        pigs_eliminated_by_k_traps_float = k_traps_this_week * trap(current_pigs)
        next_week_pigs_float_traps = max(0.0, pigs_after_reproduction_float - pigs_eliminated_by_k_traps_float)

        # Stochastic Rounding
        floor_pigs_traps = math.floor(next_week_pigs_float_traps)
        ceil_pigs_traps = math.ceil(next_week_pigs_float_traps)
        
        expected_damage_from_future_weeks_traps = 0.0
        
        common_args_for_next_state_traps = {
            "traps_left": traps_left - k_traps_this_week,
            "deployed_traps_last_week": (k_traps_this_week > 0),
            "hunting_weeks_used": hunting_weeks_used
        }

        if floor_pigs_traps == ceil_pigs_traps:
            expected_damage_from_future_weeks_traps = solve_communication_15(
                week + 1,
                int(floor_pigs_traps),
                **common_args_for_next_state_traps
            )
        else:
            prob_round_up_traps = next_week_pigs_float_traps - floor_pigs_traps
            prob_round_down_traps = 1.0 - prob_round_up_traps
            
            damage_if_ceil_traps = solve_communication_15(
                week + 1,
                int(ceil_pigs_traps),
                **common_args_for_next_state_traps
            )
            damage_if_floor_traps = solve_communication_15(
                week + 1,
                int(floor_pigs_traps),
                **common_args_for_next_state_traps
            )
            expected_damage_from_future_weeks_traps = (prob_round_up_traps * damage_if_ceil_traps +
                                                     prob_round_down_traps * damage_if_floor_traps)
        
        current_total_damage_traps_option = (damage_from_pigs_this_week +
                                           damage_from_trap_deployment_activity +
                                           expected_damage_from_future_weeks_traps)
        min_total_damage_for_state = min(min_total_damage_for_state, current_total_damage_traps_option)

    # Hunting week
    if hunting_weeks_used < MAX_HUNTING_WEEKS:
        pigs_after_reproduction_float_hunt = reprod(current_pigs)
        pigs_eliminated_by_hunting_float = hunter(current_pigs)
        next_week_pigs_float_hunt = max(0.0, pigs_after_reproduction_float_hunt - pigs_eliminated_by_hunting_float)

        floor_pigs_hunt = math.floor(next_week_pigs_float_hunt)
        ceil_pigs_hunt = math.ceil(next_week_pigs_float_hunt)

        common_args_for_next_state_hunt = {
            "traps_left": traps_left,
            "deployed_traps_last_week": False,
            "hunting_weeks_used": hunting_weeks_used + 1
        }

        if floor_pigs_hunt == ceil_pigs_hunt:
            expected_damage_from_future_weeks_hunt = solve_communication_15(
                week + 1,
                int(floor_pigs_hunt),
                **common_args_for_next_state_hunt
            )
        else:
            prob_round_up_hunt = next_week_pigs_float_hunt - floor_pigs_hunt
            prob_round_down_hunt = 1.0 - prob_round_up_hunt
            
            damage_if_ceil_hunt = solve_communication_15(
                week + 1,
                int(ceil_pigs_hunt),
                **common_args_for_next_state_hunt
            )
            damage_if_floor_hunt = solve_communication_15(
                week + 1,
                int(floor_pigs_hunt),
                **common_args_for_next_state_hunt
            )
            expected_damage_from_future_weeks_hunt = (prob_round_up_hunt * damage_if_ceil_hunt +
                                                    prob_round_down_hunt * damage_if_floor_hunt)
        
        current_total_damage_hunt_option = damage_from_pigs_this_week + expected_damage_from_future_weeks_hunt
        min_total_damage_for_state = min(min_total_damage_for_state, current_total_damage_hunt_option)
        
    memo_c15[state] = min_total_damage_for_state
    return min_total_damage_for_state

# Calculate final result
final_expected_total_damage_c15 = solve_communication_15(0, INITIAL_PIGS, TOTAL_TRAPS_BUDGET, False, 0)
print(f"{final_expected_total_damage_c15}")