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


# Jobs to be completed (duration is in hours)
Jobs = [
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 4 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 5 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 1 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 4 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3 },
    {'title': 'Event Planning', 'skills': [14,3,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 2 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 1, 'duration': 3 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 2, 'duration': 4 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Search and Rescue Operations', 'skills': [6,1,2], 'rangers': 3, 'duration': 5 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 3 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 2, 'duration': 3 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 1 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 5 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 3 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 2 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 1, 'duration': 5 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 2 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 5 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 2, 'duration': 3 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 4 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 1, 'duration': 3 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 3 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 5 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 4 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 4 },
    {'title': 'Trail Guidebook Creation', 'skills': [11,6,0], 'rangers': 1, 'duration': 2 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 2, 'duration': 3 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 2 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 5 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 2 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 3 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 1, 'duration': 4 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 1, 'duration': 4 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 3 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 1 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 1, 'duration': 4 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 4 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 3 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 2 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 3 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 1 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 4 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 2, 'duration': 3 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 3 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 4 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 1 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 2, 'duration': 5 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 4 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 6 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 2 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 5 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 5 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 4 },
    {'title': 'Visitor Surveys', 'skills': [3,2,11], 'rangers': 2, 'duration': 2 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 1 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 5 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 2, 'duration': 3 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 2 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 2 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 3 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 3 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Trail Guidebook Creation', 'skills': [11,6,0], 'rangers': 1, 'duration': 2 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 3 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 3 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 3 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 2 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 5 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 3 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 1 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 1, 'duration': 3 }
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
avoid_pairs = [(11,20), (1,3), (4,20), (1,10)]

max_hours = 36


m = Model()


# Create dataset for the total sum of each ranger-job combination 
Jobscore = {}
for j in J:
    for r in R:
        # Sum the ranger's scores for the skills required by the job
        Jobscore[j, r] = sum(Rangers[r][skill] for skill in Jobs[j]['skills'])

# Variables 
X = {(j,r): m.addVar(vtype=GRB.BINARY, name=f"assign_job{j}_ranger{r}") for j in J for r in R}
m.update()

# Objective Function
# Maximize the total skill score
m.setObjective(quicksum(Jobscore[j, r] * X[j,r] for j in J for r in R), GRB.MAXIMIZE)

# Constraints 
# Max work hours 
for r in R:
    m.addConstr(quicksum(X[j,r] * Jobs[j]['duration'] for j in J) <= max_hours, 
                name=f"hours_ranger_{r}")
    
# Ranger requirement for each job 
for j in J:
    m.addConstr(quicksum(X[j,r] for r in R) == Jobs[j]['rangers'], 
                name=f"job_requirement_{j}")

# Rangers that cannot work together 
for j in J:
    for r1, r2 in avoid_pairs:
        m.addConstr(X[j,r1] + X[j,r2] <= 1, 
                    name=f"kinship_avoid_{j}_{r1}_{r2}")
        
# Solve the model
m.optimize()

# Print the results

print(f"Optimal total skill score: {m.objVal}")
    # each jobs assigned rangers
for j in J:
    assigned_rangers = [r for r in R if X[j,r].x > 0.5]
    print(f"Job {j}: {Jobs[j]['title']}, Assigned Rangers: {assigned_rangers}")
    # job score of assigned ranger for the job
    for r in assigned_rangers:
        print(f"  Ranger {r}: Skill Score = {Jobscore[j, r]}")
for r in R:
    assigned_jobs = [j for j in J if X[j,r].x > 0.5]
    total_hours = sum(Jobs[j]['duration'] for j in assigned_jobs)
    print(f"Ranger {r}: {len(assigned_jobs)} jobs, {total_hours} hours")


    

