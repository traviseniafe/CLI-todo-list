# Testing out first PR workflow with a simple to-do list.
# A simple command-line to-do list. Tasks are saved to tasks.json.

import json
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    # Read tasks from disk. Return an empty list if there's no file yet.
    if TASKS_FILE.exists():
        return json.loads(TASKS_FILE.read_text())
    return []


def save_tasks(tasks):
    # Write the current list of tasks to disk.
    TASKS_FILE.write_text(json.dumps(tasks, indent=2))


def show_tasks(tasks):
    # Print every task with a number and a [x] / [ ] checkbox.
    if not tasks:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{number}. [{mark}] {task['title']}")


def add_task(tasks):
    # Ask for a title and add a new, not-yet-done task.
    title = input("Task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Added.")
    else:
        print("Nothing added.")


def pick_task(tasks, prompt):
    # Show the list and ask for a task number. Return its index, or None.
    if not tasks:
        print("No tasks yet.")
        return None
    show_tasks(tasks)
    choice = input(prompt).strip()
    if choice.isdigit() and 1 <= int(choice) <= len(tasks):
        return int(choice) - 1
    print("That's not a valid number.")
    return None


def complete_task(tasks):
    index = pick_task(tasks, "Number to mark done: ")
    if index is not None:
        tasks[index]["done"] = True
        print("Marked as done.")


def delete_task(tasks):
    index = pick_task(tasks, "Number to delete: ")
    if index is not None:
        removed = tasks.pop(index)
        print(f"Deleted '{removed['title']}'.")


def main():
    tasks = load_tasks()
    while True:
        print("\n1) Show  2) Add  3) Complete  4) Delete  5) Quit")
        choice = input("> ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Saved. Bye!")
            break
        else:
            print("Please choose 1-5.")

        save_tasks(tasks)

if __name__ == "__main__":
    main()
