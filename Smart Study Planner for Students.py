subjects = ["Math", "Science", "English"]
priority = {"Math":3, "Science":2, "English":1}

total_hours = 6

for sub in subjects:
    time = (priority[sub]/sum(priority.values())) * total_hours
    print(sub, "->", round(time,2), "hours")