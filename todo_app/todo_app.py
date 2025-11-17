# Create a local todo list with numbered tasks. Restarting the script and subsequently adding tasks overwrites tasks from previous runs.   

# Todo: 
# use path to local folder of tasks list. 
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
# tasks = []
while True:
    print("\n1. Add task\n2. View tasks\n3. Tick task off\n4. Wipe tasks\n5. Exit")
    choice = input("Please choose: ") or "1"
    if choice == "1":
        # num = f"{len(tasks) + 1}. "
        num = len(tasks) + 1
        task = input("Task: ")
        # tasks.append(num + task)
        tasks[num] = task
        with open(f"{curr_path}/tasks.json", "w") as f:
            # f.write("\n".join(tasks))
            # f.write(f"\n{task}")
            # f.write("\n".join(f"{k}. {v}" for k,v in tasks.items()))
            json.dump(tasks, f)
        print("Added!")

    elif choice == "2":
        print("\n--- Your Tasks ---")
        try:
            with open(f"{curr_path}/tasks.json") as f: 
                # print(f.read())
                tasks = json.load(f)
                print("\n".join(f"{k}. {v}" for k,v in tasks.items())) 
        except FileNotFoundError: 
            print("No tasks yet.")       
    
    elif choice == "3":
        # new_tasks = []
        indx = int(input("Task number to tick off: ")) or 1
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

    elif choice == "4": 
        really = input("Are you sure Y/n?")
        if really == "Y" or really == "y":
            tasks = {}
            with open(f"{curr_path}/tasks.json", "w") as f: 
                json.dump(tasks, f)

    elif choice == "5": 
        break




