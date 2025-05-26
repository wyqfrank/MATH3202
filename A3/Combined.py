import math

def reprod(x):
    if x <= 0:
        return 0
    else:
        return round(x + x*(420-x)/5000)
    
def damage(t):
    d = 2
    dt = min(abs(t-12), abs((52+t)-12), abs(t-(52+12)))
    if dt < 10:
        d += 8*(1-(dt/10)**2)**2
    dt = min(abs(t-48), abs((52+t)-48), abs(t-(52+48)))
    if dt < 7:
        d += 6*(1-(dt/7)**2)**2
    return d

def trap(x):
    return round(.03*x)

def reprod2(x):
    if x <= 0:
        return 0
    else:
        return x + x*(420-x)/5000
        
def trap2(x):
    return .03*x


# initial problems parameters (data from Frank Wu)
initial_pop = 67
total_traps = 27
max_weekly_traps = 4 
weeks = 52

#---------------------------Communication 11---------------------------------#
_Com11 = {}
def solve_communication_11(week, current_pigs, traps_left, deployed_traps_last_week):
    current_pigs = round(current_pigs)
    if current_pigs < 0:
        current_pigs = 0
        
    state = (week, current_pigs, traps_left)
    if state in _Com11:
        return _Com11[state]

    # base case: end of planning horizon
    if week >= weeks:
        return 0
    
    # calculate immediate damage from current pig population
    damage_from_pigs_this_week = current_pigs * damage(week)
    
    # if no pigs, no future decisions needed
    if current_pigs == 0:
        future_damage = solve_communication_11(week + 1, 0, traps_left, False)
        result = damage_from_pigs_this_week + future_damage
        _Com11[state] = result
        return result
    
    min_total_damage = float('inf')
    
    # try all possible trap deployments
    for k_traps_this_week in range(min(max_weekly_traps, traps_left) + 1):
        # calculate population dynamics
        pigs_after_reproduction = reprod(current_pigs)
        pigs_eliminated = k_traps_this_week * trap(current_pigs)
        next_week_pigs = max(0, pigs_after_reproduction - pigs_eliminated)
        
        # recursive call for future weeks
        future_damage = solve_communication_11(week + 1, next_week_pigs, traps_left - k_traps_this_week, k_traps_this_week > 0)
        total_damage = damage_from_pigs_this_week + future_damage
        
        min_total_damage = min(min_total_damage, total_damage)
    
    _Com11[state] = min_total_damage
    return min_total_damage

# Calculate final results
final_expected_total_damage_c11 = solve_communication_11(0, initial_pop, total_traps, False)
print(f"Communication 11: {final_expected_total_damage_c11}")



#---------------------------Communication 12---------------------------------#
_Com12 = {}
def solve_communication_12(week, current_pigs, traps_left, deployed_traps_last_week):
    current_pigs = round(current_pigs)
    if current_pigs < 0:
        current_pigs = 0
        
    state = (week, current_pigs, traps_left)
    if state in _Com12:
        return _Com12[state]

    # base case: end of planning horizon
    if week >= weeks:
        terminal_cost = current_pigs * 50
        return terminal_cost
    
    # calculate immediate damage from current pig population
    damage_from_pigs_this_week = current_pigs * damage(week)
    
    # if no pigs, no future decisions needed
    if current_pigs == 0:
        future_damage = solve_communication_12(week + 1, 0, traps_left, False)
        result = damage_from_pigs_this_week + future_damage
        _Com12[state] = result
        return result
    
    min_total_damage = float('inf')
    
    # try all possible trap deployments
    for k_traps_this_week in range(min(max_weekly_traps, traps_left) + 1):
        # calculate population dynamics
        pigs_after_reproduction = reprod(current_pigs)
        pigs_eliminated = k_traps_this_week * trap(current_pigs)
        next_week_pigs = max(0, pigs_after_reproduction - pigs_eliminated)
        
        # recursive call for future weeks
        future_damage = solve_communication_12(week + 1, next_week_pigs, traps_left - k_traps_this_week, k_traps_this_week > 0)
        total_damage = damage_from_pigs_this_week + future_damage
        
        min_total_damage = min(min_total_damage, total_damage)
    
    _Com12[state] = min_total_damage
    return min_total_damage

# Calculate final results

final_expected_total_damage_c12 = solve_communication_12(0, initial_pop, total_traps, False)
print(f"Communication 12: {final_expected_total_damage_c12}")

#---------------------------Communication 13---------------------------------#
_Com13 = {}
def solve_communication_13(week, current_pigs, traps_left, deployed_traps_last_week):
    current_pigs = round(current_pigs)
    if current_pigs < 0:
        current_pigs = 0

    state = (week, current_pigs, traps_left, deployed_traps_last_week)
    if state in _Com13:
        return _Com13[state]

    # base case: end of planning horizon
    if week >= weeks:
        terminal_cost = current_pigs * 50
        return terminal_cost

    # calculate immediate damage from current pig population
    damage_from_pigs_this_week = current_pigs * damage(week)
    min_total_damage = float('inf')

    # try all possible trap deployments
    for k_traps_this_week in range(min(max_weekly_traps, traps_left) + 1):
        
        # calculate trap deployment penalty (COM13 specific)
        damage_from_trap_deployment = 0
        if k_traps_this_week > 0 and not deployed_traps_last_week:
            damage_from_trap_deployment = k_traps_this_week * 4 * damage(week)

        # calculate population dynamics
        pigs_after_reproduction = reprod(current_pigs)
        pigs_eliminated = k_traps_this_week * trap(current_pigs)
        next_week_pigs = max(0, pigs_after_reproduction - pigs_eliminated)

        # determine state for next week
        traps_deployed_this_week = (k_traps_this_week > 0)
        remaining_traps = traps_left - k_traps_this_week
        
        # recursive call for future weeks
        future_damage = solve_communication_13(
            week + 1,
            next_week_pigs,
            remaining_traps,
            traps_deployed_this_week
        )

        total_damage = (damage_from_pigs_this_week + 
                       damage_from_trap_deployment + 
                       future_damage)

        min_total_damage = min(min_total_damage, total_damage)

    _Com13[state] = min_total_damage
    return min_total_damage

final_expected_total_damage_c13 = solve_communication_13(0, initial_pop, total_traps, False)
print(f"Communication 13: {final_expected_total_damage_c13}")


#---------------------------Communication 14---------------------------------#
_Com14 = {}
def solve_communication_14(week, current_pigs_int, traps_left, deployed_traps_last_week):
    """
    Communication 14 strategy - adds stochastic rounding to COM13
    State: (week, current_pigs, traps_left, deployed_traps_last_week)
    """
    state = (week, current_pigs_int, traps_left, deployed_traps_last_week)
    if state in _Com14:
        return _Com14[state]

    # Base case: end of planning horizon
    if week >= weeks:
        terminal_cost = current_pigs_int * 50
        return float(terminal_cost)

    # Calculate immediate damage from current pig population
    damage_from_pigs_this_week = float(current_pigs_int * damage(week))
    min_expected_total_damage = float('inf')

    # Try all possible trap deployments
    for k_traps_this_week in range(min(max_weekly_traps, traps_left) + 1):
        
        # Calculate trap deployment penalty
        damage_from_trap_deployment = 0.0
        if k_traps_this_week > 0 and not deployed_traps_last_week:
            damage_from_trap_deployment = float(k_traps_this_week * 4 * damage(week))

        # Calculate population dynamics (as float)
        pigs_after_reproduction_float = reprod2(current_pigs_int)
        pigs_eliminated_float = k_traps_this_week * trap2(current_pigs_int)
        next_week_pigs_float = max(0.0, pigs_after_reproduction_float - pigs_eliminated_float)

        # Stochastic rounding for expected future damage
        floor_pigs = math.floor(next_week_pigs_float)
        ceil_pigs = math.ceil(next_week_pigs_float)
        
        # Common arguments for recursive calls
        common_args = {
            "traps_left": traps_left - k_traps_this_week,
            "deployed_traps_last_week": (k_traps_this_week > 0)
        }

        if floor_pigs == ceil_pigs:
            # Deterministic case
            expected_future_damage = solve_communication_14(
                week + 1,
                int(floor_pigs),
                **common_args
            )
        else:
            # Stochastic case
            prob_round_up = next_week_pigs_float - floor_pigs
            prob_round_down = 1.0 - prob_round_up
            
            damage_if_ceil = solve_communication_14(
                week + 1,
                int(ceil_pigs),
                **common_args
            )
            damage_if_floor = solve_communication_14(
                week + 1,
                int(floor_pigs),
                **common_args
            )
            expected_future_damage = (prob_round_up * damage_if_ceil + 
                                    prob_round_down * damage_if_floor)
        
        total_expected_damage = (damage_from_pigs_this_week + 
                               damage_from_trap_deployment + 
                               expected_future_damage)

        min_expected_total_damage = min(min_expected_total_damage, total_expected_damage)
            
    _Com14[state] = min_expected_total_damage
    return min_expected_total_damage

final_expected_total_damage_c14 = solve_communication_14(0, initial_pop, total_traps, False)
print(f"Communication 14: {final_expected_total_damage_c14}")


#---------------------------Communication 15---------------------------------#
def hunter(x):
    return 0.2*x

max_hunting_weeks = 2

_Com15 = {}
def solve_communication_15(week, current_pigs_int, traps_left, deployed_traps_last_week, hunting_weeks_used):
    """
    Communication 15 strategy - adds hunting option to COM14
    State: (week, current_pigs, traps_left, deployed_traps_last_week, hunting_weeks_used)
    """
    state = (week, current_pigs_int, traps_left, deployed_traps_last_week, hunting_weeks_used)
    if state in _Com15:
        return _Com15[state]

    # Base case: end of planning horizon
    if week >= weeks:
        terminal_cost = current_pigs_int * 50
        return float(terminal_cost)

    # Calculate immediate damage from current pig population
    damage_from_pigs_this_week = float(current_pigs_int * damage(week))
    min_total_damage = float('inf')

    # Option 1: Deploy traps (same logic as COM14)
    for k_traps_this_week in range(min(max_weekly_traps, traps_left) + 1):
        # Calculate trap deployment penalty
        damage_from_trap_deployment = 0.0
        if k_traps_this_week > 0 and not deployed_traps_last_week:
            damage_from_trap_deployment = float(k_traps_this_week * 4 * damage(week))

        # Calculate population dynamics with traps
        pigs_after_reproduction_float = reprod2(current_pigs_int)
        pigs_eliminated_float = k_traps_this_week * trap2(current_pigs_int)
        next_week_pigs_float = max(0.0, pigs_after_reproduction_float - pigs_eliminated_float)

        # Stochastic rounding for traps option
        floor_pigs = math.floor(next_week_pigs_float)
        ceil_pigs = math.ceil(next_week_pigs_float)
        
        common_args_traps = {
            "traps_left": traps_left - k_traps_this_week,
            "deployed_traps_last_week": (k_traps_this_week > 0),
            "hunting_weeks_used": hunting_weeks_used
        }

        if floor_pigs == ceil_pigs:
            expected_future_damage_traps = solve_communication_15(
                week + 1,
                int(floor_pigs),
                **common_args_traps
            )
        else:
            prob_round_up = next_week_pigs_float - floor_pigs
            prob_round_down = 1.0 - prob_round_up
            
            damage_if_ceil = solve_communication_15(
                week + 1,
                int(ceil_pigs),
                **common_args_traps
            )
            damage_if_floor = solve_communication_15(
                week + 1,
                int(floor_pigs),
                **common_args_traps
            )
            expected_future_damage_traps = (prob_round_up * damage_if_ceil + 
                                          prob_round_down * damage_if_floor)
        
        total_damage_traps = (damage_from_pigs_this_week + 
                            damage_from_trap_deployment + 
                            expected_future_damage_traps)
        min_total_damage = min(min_total_damage, total_damage_traps)

    # Option 2: Hunt (if hunting weeks available)
    if hunting_weeks_used < max_hunting_weeks:
        # Calculate population dynamics with hunting
        pigs_after_reproduction_float = reprod2(current_pigs_int)
        pigs_eliminated_by_hunting = hunter(current_pigs_int)
        next_week_pigs_float = max(0.0, pigs_after_reproduction_float - pigs_eliminated_by_hunting)

        # Stochastic rounding for hunting option
        floor_pigs = math.floor(next_week_pigs_float)
        ceil_pigs = math.ceil(next_week_pigs_float)

        common_args_hunt = {
            "traps_left": traps_left,
            "deployed_traps_last_week": False,  # Hunting doesn't trigger trap deployment penalty
            "hunting_weeks_used": hunting_weeks_used + 1
        }

        if floor_pigs == ceil_pigs:
            expected_future_damage_hunt = solve_communication_15(
                week + 1,
                int(floor_pigs),
                **common_args_hunt
            )
        else:
            prob_round_up = next_week_pigs_float - floor_pigs
            prob_round_down = 1.0 - prob_round_up
            
            damage_if_ceil = solve_communication_15(
                week + 1,
                int(ceil_pigs),
                **common_args_hunt
            )
            damage_if_floor = solve_communication_15(
                week + 1,
                int(floor_pigs),
                **common_args_hunt
            )
            expected_future_damage_hunt = (prob_round_up * damage_if_ceil + 
                                         prob_round_down * damage_if_floor)
        
        total_damage_hunt = damage_from_pigs_this_week + expected_future_damage_hunt
        min_total_damage = min(min_total_damage, total_damage_hunt)
        
    _Com15[state] = min_total_damage
    return min_total_damage

final_expected_total_damage_c15 = solve_communication_15(0, initial_pop, total_traps, False, 0)
print(f"Communication 15: {final_expected_total_damage_c15}")