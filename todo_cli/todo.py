#!/usr/bin/env python3
"""
Simple command line todo list stored in a local JSON file. 
"""

import json
from pathlib import Path

TASKS_FILE = Path.cwd() / "tasks.json"

def load_tasks():
    try:
        with TASKS_FILE.open("r") as f:
            return {int(k): v for k, v in json.load(f).items()}
    except (json.JSONDecodeError, ValueError, FileNotFoundError): 
        return {}


def save_tasks(tasks): 
    with TASKS_FILE.open("w") as f:
        json.dump({str(k): v for k, v in tasks.items()}, f, indent=2)


def add_task():
    tasks = load_tasks()
    new_id = max(tasks.keys(), default=0) + 1
    description = input("Task: ").strip()
    if not description:
        print("No description entered.")
        return
    tasks[new_id] = description
    save_tasks(tasks)
    print("Added!")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    print("\n--- Your Tasks ---")
    for k, v in tasks.items():
        print(f"{k}. {v}")

def tick_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    
    try:
        idx = int(input("Task number to tick off: ").strip() or "1")
    except ValueError:
        print("Invalid number.")
        return
    
    if idx not in tasks:
        print("No such task.")
        return

    done = tasks.pop(idx)
    reordered = {}
    for new_idx, original_idx in enumerate(sorted(tasks.keys()), start=1):
        reordered[new_idx] = tasks[original_idx]

    save_tasks(reordered)
    print(f"Completed: {done}") 


def wipe_tasks():
    confirm = input("Are you sure? Y/n ").strip().lower()
    if confirm == "y":
        save_tasks({})
        print("Wiped.")
    else:
        print("Cancelled.")

def main():
    while True:
        print("\n1. Add task\n2. View tasks\n3. Tick task off\n4. Wipe tasks\n5. Exit")
        choice = input("Please choose: ").strip() or "1"

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            tick_task()
        elif choice == "4":
            wipe_tasks()
        elif choice == "5" or choice.lower() == "q":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()