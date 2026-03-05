# A simple to-do list application

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

# Function to view all tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to remove a task
def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks to remove.")
        return
    
    try:
        task_number = int(input("Enter the task number to remove: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
        else:
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from the list.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the to-do list application
def main():
    tasks = []  # Empty list to store tasks
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
