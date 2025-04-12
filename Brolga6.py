from gurobipy import *

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
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 3 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 1, 'duration': 4 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 3 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 3 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 2 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 3 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 2 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 3 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4 },
    {'title': 'Event Planning', 'skills': [14,3,13], 'rangers': 2, 'duration': 4 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Surveys', 'skills': [3,2,11], 'rangers': 1, 'duration': 2 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 4 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 3 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 4 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 1, 'duration': 4 },
    {'title': 'Visitor Surveys', 'skills': [3,2,11], 'rangers': 1, 'duration': 1 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 5 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 5 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 4 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 5 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 2, 'duration': 3 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 1, 'duration': 2 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 3 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 1, 'duration': 6 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 3 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 2 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 3 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 2 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 4 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 3 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 4 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 4 },
    {'title': 'Environmental Education Programs', 'skills': [8,14,0], 'rangers': 1, 'duration': 2 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 2 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 3 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 2 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 3 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 5 },
    {'title': 'Controling Invasive Plant Species', 'skills': [0,9,11], 'rangers': 2, 'duration': 5 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 4 },
    {'title': 'Clean-Up Initiatives', 'skills': [3,10,0], 'rangers': 1, 'duration': 2 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 2 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 2 },
    {'title': 'Trail Guidebook Creation', 'skills': [11,6,0], 'rangers': 1, 'duration': 3 },
    {'title': 'Guided Hikes', 'skills': [8,14,6], 'rangers': 2, 'duration': 3 },
    {'title': 'Maintenance and Repairs', 'skills': [7,12,13], 'rangers': 2, 'duration': 5 },
    {'title': 'Safety Audits', 'skills': [7,11,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 3, 'duration': 4 },
    {'title': 'Park Facility Inspections', 'skills': [7,12,11], 'rangers': 1, 'duration': 3 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Search and Rescue Operations', 'skills': [6,1,2], 'rangers': 2, 'duration': 6 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 5 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 3 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 3 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 2 },
    {'title': 'Signage Design', 'skills': [12,0,2], 'rangers': 1, 'duration': 2 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 2, 'duration': 5 },
    {'title': 'Visitor Surveys', 'skills': [3,2,11], 'rangers': 2, 'duration': 2 },
    {'title': 'Research Projects', 'skills': [0,11,13], 'rangers': 1, 'duration': 2 },
    {'title': 'Trail Guidebook Creation', 'skills': [11,6,0], 'rangers': 1, 'duration': 3 },
    {'title': 'Search and Rescue Operations', 'skills': [6,1,2], 'rangers': 3, 'duration': 7 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Center Operations', 'skills': [3,2,12], 'rangers': 1, 'duration': 4 },
    {'title': 'Wildlife Monitoring', 'skills': [0,9,11], 'rangers': 2, 'duration': 5 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 4 },
    {'title': 'Cultural Educational Programs', 'skills': [8,14,15], 'rangers': 1, 'duration': 3 },
    {'title': 'Feral Pig Control', 'skills': [0,9,10], 'rangers': 2, 'duration': 4 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 4 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 4 },
    {'title': 'Patrolling Park Boundaries', 'skills': [4,6,10], 'rangers': 2, 'duration': 5 },
    {'title': 'Cultural Heritage Preservation', 'skills': [15,0,11], 'rangers': 2, 'duration': 4 },
    {'title': 'Visitor Safety Briefings', 'skills': [14,3,2], 'rangers': 2, 'duration': 3 },
    {'title': 'Fire Management', 'skills': [5,10,13], 'rangers': 3, 'duration': 3 },
    {'title': 'Trail Maintenance', 'skills': [7,10,12], 'rangers': 3, 'duration': 4 },
    {'title': 'Water Safety Patrols', 'skills': [4,1,2], 'rangers': 3, 'duration': 2 },
    {'title': 'Wildlife Management', 'skills': [0,9,11], 'rangers': 2, 'duration': 5 },
    {'title': 'Park Promotion', 'skills': [14,2,3], 'rangers': 2, 'duration': 3 },
    {'title': 'Wildlife Rescue', 'skills': [9,1,13], 'rangers': 2, 'duration': 2 },
    {'title': 'Volunteer Coordination', 'skills': [3,2,13], 'rangers': 1, 'duration': 1 },
    {'title': 'Budget Management', 'skills': [13,11,2], 'rangers': 1, 'duration': 3 },
    {'title': 'Merchandise Sales', 'skills': [3,2,12], 'rangers': 1, 'duration': 3 }
]

# Skill scores for each ranger
Rangers = [
    [10,2,2,3,15,6,1,0,4,2,1,18,3,9,13,12],
    [8,1,8,8,10,9,2,2,2,4,12,0,19,14,12,0],
    [3,7,16,1,6,4,10,7,0,5,12,7,7,6,10,7],
    [17,1,1,8,11,3,5,1,5,12,2,11,0,7,2,16],
    [2,4,0,3,12,20,2,10,11,5,5,14,0,5,14,0],
    [4,16,10,3,15,11,0,3,3,2,8,1,3,18,5,5],
    [19,1,19,3,3,0,0,1,7,6,14,5,3,3,10,9],
    [1,4,4,9,9,16,2,10,7,0,0,0,1,20,11,15],
    [0,10,7,12,2,19,6,5,4,3,5,11,2,0,5,15],
    [7,11,2,0,1,11,4,10,10,9,6,5,13,0,11,2],
    [10,5,11,8,7,0,5,10,3,0,17,7,5,10,0,7],
    [1,2,11,12,1,0,16,9,16,1,2,2,17,4,9,0],
    [4,12,4,0,0,3,10,16,15,2,10,16,5,5,2,6],
    [9,2,19,2,13,8,6,2,13,0,0,2,10,2,2,11],
    [9,1,6,3,5,4,14,5,3,10,5,8,5,2,20,0],
    [5,5,5,7,2,9,2,7,6,9,4,7,7,10,5,7],
    [8,4,9,6,12,10,6,7,5,12,6,7,5,4,0,5],
    [2,8,8,10,9,6,3,8,9,0,13,2,1,0,9,14],
    [2,2,4,13,12,0,9,4,0,11,3,10,20,11,6,3],
    [2,17,17,0,7,11,7,5,0,7,0,6,14,1,4,5],
    [2,4,12,10,12,9,3,2,8,5,2,0,15,10,15,0]
]

S = range(len(Skills))
J = range(len(Jobs))
R = range(len(Rangers))

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


# Solve the model
m.optimize()

# Print the results

print(f"Optimal total skill score: {m.objVal}")
for r in R:
    assigned_jobs = [j for j in J if X[j,r].x > 0.5]
    total_hours = sum(Jobs[j]['duration'] for j in assigned_jobs)
    print(f"Ranger {r}: {len(assigned_jobs)} jobs, {total_hours} hours")
    




















    