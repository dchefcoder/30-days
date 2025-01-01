import os
FILE_NAME = "task.txt" # File name to store tasks

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, completed = line.strip().split("|")
                tasks.append({"task": task, "completed": completed == "True"})
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['task']} | {task['completed']}\n")
            
def show_menu():
    print("\nChoose an action")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. Exit")
    
def add_task(tasks):
    task_name = input("Enter task name: ")
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully!") 

def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "❌"
            print(f"{idx}. {task['task']} - {status}")

def mark_completed(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter task number to mark as completed: "))
    if 0 < task_no <= len(tasks):
        tasks[task_no - 1]["completed"] = True
        print(f"Task '{tasks[task_no - 1]['task']}' marked as completed!")
    else:
        print("Invalid task number!")
        
def remove_task(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter task number to remove: "))
    if 0 < task_no <= len(tasks):
        removed = tasks.pop(task_no -1)
        print(f"Task '{removed['task']}' removed successfully!")
    else:
        print("Invalid task number!")
        
        
def main():
    tasks = load_tasks() # Load tasks from file at the beginning
    while True:
        show_menu()
        choice = input("Enter your choice:")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Sorry to see you go!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
