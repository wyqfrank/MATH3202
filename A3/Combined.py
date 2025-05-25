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

# initial problems parameters 
initial_pop = 67
total_traps = 27
max_weekly_traps = 4 
weeks = 52

#---------------------------Communication 11---------------------------------#
_Com11 = {}

def solve_communication_11(week, current_pigs_raw, traps_left, deployed_traps_last_week):
    pass 