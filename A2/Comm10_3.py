Skills = [
    "Environmental Knowledge",
    "First Aid and CPR",
    "Communication",
    "Customer Service",
    "Law Enforcement",
    "Fire Management",
    "Navigation",
    "Maintenance Skills",
    "Education and Interpretation",
    "Wildlife Management",
    "Physical Fitness",
    "Report Writing",
    "Technical Skills",
    "Problem-Solving",
    "Public Speaking",
    "Cultural Awareness"
]


Days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
T = range(len(Days))

# Jobs to be completed (duration is in hours)
Jobs = [
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4, 'day': 0 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4, 'day': 0 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4, 'day': 0 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 4, 'day': 0 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 5, 'day': 0 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6, 'day': 0 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 1, 'day': 0 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 4, 'day': 0 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 4, 'day': 0 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3, 'day': 0 },
    {'title': 'Event Planning', 'skills': [14,3,13], 'rangers': 1, 'duration': 3, 'day': 0 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 2, 'day': 0 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 1, 'duration': 3, 'day': 0 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 2, 'duration': 4, 'day': 0 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 1, 'duration': 3, 'day': 0 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3, 'day': 0 },
    {'title': 'Search and Rescue Operations', 'skills': [6,1,2], 'rangers': 3, 'duration': 5, 'day': 0 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4, 'day': 1 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 3, 'day': 1 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 2, 'duration': 3, 'day': 1 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 1, 'day': 1 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3, 'day': 1 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 5, 'day': 1 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6, 'day': 1 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 3, 'day': 1 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 2, 'day': 1 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 1, 'duration': 5, 'day': 1 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 2, 'day': 1 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 5, 'day': 2 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6, 'day': 2 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 2, 'day': 2 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 2, 'duration': 3, 'day': 2 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 4, 'day': 2 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 1, 'duration': 3, 'day': 2 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 3, 'day': 3 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 5, 'day': 3 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 4, 'day': 3 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 2, 'day': 3 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3, 'day': 3 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 2, 'day': 3 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 4, 'day': 3 },
    {'title': 'Trail Guidebook Creation', 'skills': [11,6,0], 'rangers': 1, 'duration': 2, 'day': 3 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 2, 'duration': 3, 'day': 3 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4, 'day': 3 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 2, 'day': 3 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 5, 'day': 3 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 2, 'day': 3 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 3, 'day': 3 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 1, 'duration': 4, 'day': 3 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3, 'day': 4 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 1, 'duration': 4, 'day': 4 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 3, 'day': 4 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 1, 'day': 4 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 1, 'duration': 4, 'day': 4 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 4, 'day': 4 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 3, 'day': 4 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 2, 'day': 4 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4, 'day': 4 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 3, 'day': 4 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 1, 'day': 4 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 4, 'day': 4 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 2, 'duration': 3, 'day': 4 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 3, 'day': 4 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 4, 'day': 4 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 1, 'day': 4 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 2, 'duration': 5, 'day': 4 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 4, 'day': 4 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6, 'day': 5 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3, 'day': 5 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 2, 'day': 5 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 5, 'day': 5 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 5, 'day': 5 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 4, 'day': 5 },
    {'title': 'Visitor Surveys', 'skills': [3,2,11], 'rangers': 2, 'duration': 2, 'day': 5 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 1, 'day': 5 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 4, 'day': 5 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4, 'day': 5 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 5, 'day': 5 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 2, 'duration': 3, 'day': 5 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3, 'day': 5 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 2, 'day': 5 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 2, 'day': 5 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 1, 'duration': 2, 'day': 6 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 3, 'day': 6 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 3, 'day': 6 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 3, 'day': 6 },
    {'title': 'Trail Guidebook Creation', 'skills': [11,6,0], 'rangers': 1, 'duration': 2, 'day': 6 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 3, 'day': 6 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 3, 'day': 6 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 3, 'day': 6 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 2, 'day': 6 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 5, 'day': 6 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 3, 'day': 6 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3, 'day': 6 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 1, 'day': 6 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 1, 'duration': 3, 'day': 6 }
]

# Skill scores for each ranger
Rangers = [
    [12,9,1,6,8,4,17,8,0,17,12,1,6,1,0,3],
    [12,12,6,0,0,15,2,1,7,4,4,13,18,7,0,11],
    [9,1,4,11,7,11,14,5,6,8,0,14,5,2,5,0],
    [13,10,1,8,18,3,10,15,0,11,0,7,1,4,3,2],
    [1,3,12,16,3,1,2,10,3,6,9,16,4,11,4,5],
    [9,1,6,0,5,12,8,11,7,9,15,0,12,8,2,4],
    [5,12,5,8,3,5,4,6,0,16,4,7,16,2,8,12],
    [0,19,3,2,11,12,7,3,9,2,2,8,13,8,3,6],
    [14,13,3,3,2,0,17,7,3,6,8,2,6,3,11,8],
    [13,13,3,7,4,1,7,10,4,9,6,3,11,2,2,7],
    [11,10,11,7,6,4,11,9,6,9,4,2,0,0,5,12],
    [14,1,6,3,9,0,10,2,16,0,7,2,11,6,12,7],
    [10,3,6,1,13,2,18,0,0,11,2,6,6,20,1,4],
    [0,8,17,0,0,4,5,3,5,4,9,16,15,8,5,9],
    [9,6,6,9,11,9,7,8,7,1,10,8,0,1,12,0],
    [14,18,3,4,5,7,11,12,6,0,6,2,8,8,3,2],
    [15,14,9,4,2,16,3,6,6,0,2,0,16,0,10,7],
    [16,1,8,8,1,19,3,13,7,11,6,0,6,0,3,8],
    [5,1,8,1,11,0,5,15,13,0,0,8,16,17,6,0],
    [6,8,3,16,2,9,19,6,4,5,0,1,12,2,1,10],
    [12,7,12,2,0,0,1,5,14,10,3,8,8,8,19,3]
]

from gurobipy import *

S = range(len(Skills))
J = range(len(Jobs))
R = range(len(Rangers))
T = range(len(Days))

min_days_off = 2
avoid_pairs = [(11,20), (1,3), (4,20), (1,10)]
Weekly_max_hours = 36
Daily_max_hours = 10
no_consecutive_rangers = [0, 2, 3, 5, 11]

m = Model()

job_score = {}
for j in J:
    for r in R:
        job_score[j, r] = sum(Rangers[r][skill] for skill in Jobs[j]['skills'])

# Variables
# X[j, r, t] = 1 if job j is assigned to ranger r on day t, 0 otherwise
X = {(j, r, t): m.addVar(vtype=GRB.BINARY, name=f"assign_job{j}_ranger{r}_day{t}") for j in J for r in R for t in T}
# Y[r, t] = 1 if ranger r is assigned to work on day t, 0 otherwise
Y = {(r, t): m.addVar(vtype=GRB.BINARY, name=f"assign_ranger{r}_day{t}") for r in R for t in T}
# W[j, t] = 1 if job j is scheduled on day t, 0 otherwise
W = {(j, t): m.addVar(vtype=GRB.BINARY, name=f"job_scheduled{r}_day{t}") for j in J for t in T}

m.update()

# Objective function
m.setObjective(quicksum(X[j, r, t] * job_score[j, r] for j in J for r in R for t in T), GRB.MAXIMIZE)

# Constraints

# 1. Weekly hours limit (36 hours)
for r in R:
    m.addConstr(quicksum(X[j, r, t] * Jobs[j]['duration'] for j in J for t in T) <= Weekly_max_hours, name=f"weekly_hours_limit_ranger{r}")

# 2. Daily hours limit (10 hours)
for r in R:
    for t in T:
        m.addConstr(quicksum(X[j, r, t] * Jobs[j]['duration'] for j in J) <= Daily_max_hours, name=f"daily_hours_limit_ranger{r}_day{t}")

# 3. Each ranger must have atleast 2 days off a week
for r in R:
    m.addConstr(quicksum(Y[r, t] for t in T) <= len(T) - min_days_off,
                name=f"days_off_ranger{r}")

# 4. Avoid certain ranger pairs from working together
for j in J:
    for (r1, r2) in avoid_pairs:
        m.addConstr(X[j, r1, t] + X[j, r2, t] <= 1,
                    name=f"avoid_pair_{r1}_{r2}_job{j}_day{t}") # might need to tweak

# 5. Rangers 2, 3, 5, 11 cannot work 2 consecutive days
for r in no_consecutive_rangers:
    for t in T:
        next_t = (t + 1) % len(Days)
        m.addConstr(Y[r, t] + Y[r, next_t] <= 1,
                    name=f"no_consecutive_rangers_{r}_day{t}")

# 6. Link X and Y variables (if assigned any job on day t, Y[r,t]=1)
for r in R:
    for t in T:
        # If ranger r works on any job on day t, then Y[r,t] = 1
        m.addConstr(
            quicksum(X[j, r, t] for j in J) <= 100 * Y[r, t],
            f"WorkDay_Trigger_r{r}_d{t}"
        )
        
        # If Y[r,t] = 1, then ranger r works on at least 1 job on day t
        m.addConstr(
            quicksum(X[j, r, t] for j in J) >= Y[r, t],
            f"WorkDay_Require_r{r}_d{t}"
        )

# 7. Each job must be scheduled on exactly 1 day
for j in J:
    m.addConstr(quicksum(W[j, t] for t in T) == 1, f"job_{j}_one_day")

# 8. Each job must be assigned to the required number of rangers
for j in J:
    m.addConstr(quicksum(X[j, r, t] for r in R for t in T) == Jobs[j]['rangers'], f"job_{j}_ranger_count")

# 9. A ranger can only be assigned to a job if that job is scheduled on that day
for r in R:
    for j in J:
        for t in T:
            m.addConstr(X[j, r, t] <= W[j, t], f"job_{j}_ranger_{r}_day_{t}")

m.optimize()

# Print results
if m.status == GRB.OPTIMAL:
    print(f"Optimal skill score: {m.objVal}")
    
    # Print day assignments for jobs
    print("\nJob Day Assignments:")
    for j in J:
        for t in T:
            if W[j, t].x > 0.5:  # If job j is scheduled on day t
                print(f"Job {j} ({Jobs[j]['title']}) scheduled on {Days[t]}")
    
    # Print ranger assignments
    print("\nRanger Assignments:")
    for r in R:
        print(f"\nRanger {r} schedule:")
        for t in T:
            if Y[r, t].x > 0.5:  # If ranger i works on day t
                print(f"  {Days[t]}:", end=" ")
                for j in J:
                    if X[j, r, t].x > 0.5:  # If ranger i is assigned to job j on day t
                        print(f"{Jobs[j]['title']} ({Jobs[j]['duration']} hrs)", end=", ")
                print()
    
    # Calculate utilization statistics
    total_possible_hours = len(R) * 36  # 21 rangers × 36 hours max per week
    total_assigned_hours = sum(X[j, r, t].x * Jobs[j]['duration'] 
                              for r in R for j in J for t in T)
    utilization = (total_assigned_hours / total_possible_hours) * 100
    
    print(f"\nTotal ranger hours utilized: {total_assigned_hours} out of {total_possible_hours} ({utilization:.2f}%)")
    
    # Hours by day
    for t in T:
        day_hours = sum(X[j, r, t].x * Jobs[j]['duration'] for r in R for j in J)
        print(f"Hours on {Days[t]}: {day_hours}")
    
    # Rangers by day
    for t in T:
        rangers_working = sum(Y[r, t].x for r in R)
        print(f"Rangers working on {Days[t]}: {rangers_working} out of {len(R)}")
        
else:
    print("No optimal solution found.")