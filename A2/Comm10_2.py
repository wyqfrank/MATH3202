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

# Parameters
min_days_off = 2
avoid_pairs = [(11, 20), (1, 3), (4, 20), (1, 10)]
Weekly_max_hours = 36
Daily_max_hours = 10
non_consecutive_work_days = [0, 2, 3, 5, 11]

# Model
m = Model()

# Job skill score calculation
jobscore = {(j, r): sum(Rangers[r][skill] for skill in Jobs[j]['skills']) for j in J for r in R}

# Variables
X = {(j, r): m.addVar(vtype=GRB.BINARY) for j in J for r in R}  # Ranger r assigned to job j
Z = {(j, t): m.addVar(vtype=GRB.BINARY) for j in J for t in T}  # Job j scheduled on day t
Y = {(r, t): m.addVar(vtype=GRB.BINARY) for r in R for t in T}  # Ranger r works on day t
W = {(j, r, t): m.addVar(vtype=GRB.BINARY) for j in J for r in R for t in T}  # W[j,r,t] = X[j,r] * Z[j,t]

# Objective: Maximize total skill score
m.setObjective(quicksum(jobscore[j, r] * X[j, r] for j in J for r in R), GRB.MAXIMIZE)

# Constraints
# 1. Assign required number of rangers to each job
for j in J:
    m.addConstr(quicksum(X[j, r] for r in R) == Jobs[j]['rangers'])

# 2. Each job is assigned to exactly one day
for j in J:
    m.addConstr(quicksum(Z[j, t] for t in T) == 1)

# 3. Link X and Z via W[j,r,t] = X[j,r] * Z[j,t]
for j in J:
    for r in R:
        for t in T:
            m.addConstr(W[j, r, t] <= X[j, r])
            m.addConstr(W[j, r, t] <= Z[j, t])
            m.addConstr(W[j, r, t] >= X[j, r] + Z[j, t] - 1)

# 4. Weekly hours limit (36 hours)
for r in R:
    m.addConstr(quicksum(X[j, r] * Jobs[j]['duration'] for j in J) <= Weekly_max_hours)

# 5. Daily hours limit (10 hours)
for r in R:
    for t in T:
        m.addConstr(quicksum(W[j, r, t] * Jobs[j]['duration'] for j in J) <= Daily_max_hours)

# 6. At least 2 days off per ranger
for r in R:
    m.addConstr(quicksum(Y[r, t] for t in T) <= len(T) - min_days_off)

# 7. Link Y[r,t] to W[j,r,t] (if r works any job on day t, Y[r,t]=1)
for r in R:
    for t in T:
        m.addConstr(Y[r, t] <= quicksum(W[j, r, t] for j in J))
        m.addConstr(quicksum(W[j, r, t] for j in J) <= 100 * Y[r, t])

# 8. Avoid specific ranger pairs
for j in J:
    for (r1, r2) in avoid_pairs:
        m.addConstr(X[j, r1] + X[j, r2] <= 1)

# 9. Non-consecutive work days (including Sun->Mon)
for r in non_consecutive_work_days:
    for t in range(len(T) - 1):
        m.addConstr(Y[r, t] + Y[r, t + 1] <= 1)
    m.addConstr(Y[r, 6] + Y[r, 0] <= 1)  # Sun->Mon

# Solve
m.optimize()

# Results
if m.status == GRB.OPTIMAL:
    print(f"Optimal total skill score: {m.objVal}")
else:
    print("No solution found.")