# Create a local todo list with numbered tasks. Restarting the script and subsequently adding tasks overwrites tasks from previous runs.   

# Todo: 
# use script from global script folder.  
# save tasks beyond single usage? (append)
# tagged tasks. 
# sync tasks (with obsidian). 
# subgroup tasks (use json format). 

import json
import os

tasks = {}
curr_path = os.getcwd()
print(curr_path)

while True:
    print("\n1. Add task\n2. View tasks\n3. Tick task off\n4. Wipe tasks\n5. Exit")
    choice = input("Please choose: ") or "1"
    if choice == "1": # Add new task
        with open(f"{curr_path}/tasks.json", "a+") as f:
            f.seek(0) # Read mode: Bring pointer to beginning of file
            try:
                tasks = json.load(f) # Obtain existing tasks 
            except (json.JSONDecodeError, ValueError):
                tasks = {}  # File was empty or didn't exist
            num = len(tasks) + 1 # Task number of next task 
            task = input("Task: ") 
            tasks[num] = task # Update tasks dictionary 
            f.seek(0)
            f.truncate()  # Clear file before writing
            json.dump(tasks, f)
        print("Added!")

    elif choice == "2": # View tasks
        print("\n--- Your Tasks ---")
        try:
            with open(f"{curr_path}/tasks.json") as f: 
                tasks = json.load(f)
                print("\n".join(f"{k}. {v}" for k,v in tasks.items())) 
        except FileNotFoundError: 
            print("No tasks yet.")       
    
    elif choice == "3": # Tick off task
        indx_str = input("Task number to tick off: ") or "1"
        indx = int(indx_str)
        try:
            with open(f"{curr_path}/tasks.json", 'r+') as f:
                tasks = json.load(f)
                keys = [*tasks]
                task = tasks[str(indx)]
                try: 
                    tasks.pop(str(indx))
                    while indx < int(keys[-1]): 
                        tasks[str(indx)] = tasks.pop(str(indx + 1))
                        indx += 1
                except KeyError:
                     print("Task number is higher than number of tasks.")
                f.seek(0)
                json.dump(tasks, f)
                f.truncate()
                print(f'Well done! You completed: {task}!')
        except FileNotFoundError:
            print("No tasks yet.")

    elif choice == "4": # Wipe task list
        really = input("Are you sure Y/n?")
        if really == "Y" or really == "y":
            with open(f"{curr_path}/tasks.json", "w") as f: 
                f.seek(0)
                f.truncate()

    elif choice == "5": # Exit program
        break




