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

# initial data
initial_pop = 67
total_traps = 27
max_weekly_traps = 4 
weeks = 52

# value 
_V = {}

def V(t, x, n):
    # Check if this state has been computed before
    if (t, x, n) in _V:
        return _V[t, x, n]
    
    # Base case: end of planning horizon
    if t >= weeks:
        # Com 11
        # return (0,0) 
        terminal_cost_per_pig = x * 50
        return (terminal_cost_per_pig, 0)
    
    # Calculate immediate damage at current state
    immediate_damage = x * damage(t)
    
    # If no pigs, no future choice to make
    if x == 0:
        future_damage, _ = V(t+1, 0, n)
        _V[t, x, n] = (immediate_damage + future_damage, 0)
        return _V[t, x, n]
    
    # Try all possible trap deployments and choose the best
    min_future_damage = float('inf')
    optimal_traps = 0
    
    # Try using 0 to min(max_weekly_traps, n) traps
    for traps_used in range(min(max_weekly_traps, n) + 1):
        # Calculate resulting population after reproduction and trapping
        pigs_removed = traps_used * trap(x)
        next_population = max(0, reprod(x) - pigs_removed)
        
        # Recursively find the optimal future damage
        future_damage, _ = V(t+1, next_population, n - traps_used)
        total_damage = future_damage
        
        # Update if this is better than current best
        if total_damage < min_future_damage:
            min_future_damage = total_damage
            optimal_traps = traps_used
    
    # Store result in memoisation dictionary
    _V[t, x, n] = (immediate_damage + min_future_damage, optimal_traps)
    return _V[t, x, n]


V(0, initial_pop, total_traps)

print(V(0, initial_pop, total_traps))