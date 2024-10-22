# Task 1: To-Do List Application

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to update: "))
            if 1 <= task_number <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_number - 1] = new_task
                print(f"Task {task_number} updated.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


