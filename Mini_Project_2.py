# Initialize an empty list to store the tasks
tasks = []

# Start an infinite loop to keep the program running until the user chooses to exit
while True:
    # Print an empty line for better visual spacing in the console
    print()
    # Display the title of the To-Do List menu
    print("--- TO-DO LIST MENU ---")
    # Display the option to add a task
    print("1. Add Task")
    # Display the option to view all tasks
    print("2. View Tasks")
    # Display the option to delete a task
    print("3. Delete Task")
    # Display the option to exit the program
    print("4. Exit")

    # Prompt the user to input their choice and store it as a string
    choice = input("Enter your choice (1-4): ")

    # Check if the user selected option 1 (Add Task)
    if choice == "1":
        # Prompt the user to type the new task
        new_task = input("Enter the task: ")
        # Append the new task to the 'tasks' list
        tasks.append(new_task)
        # Inform the user that the task was added successfully
        print(f"Task '{new_task}' added successfully!")

    # Check if the user selected option 2 (View Tasks)
    elif choice == "2":
        # Check if the 'tasks' list is empty
        if len(tasks) == 0:
            # Inform the user that there are currently no tasks to show
            print("Your to-do list is empty.")
        # If the list is not empty, execute the following block
        else:
            # Display a header for the list of tasks
            print("\nYour Current Tasks:")
            # Loop through the list using 'enumerate' to get both index and task content
            for index, task in enumerate(tasks, start=1):
                # Print each task with its corresponding list number
                print(f"{index}. {task}")

    # Check if the user selected option 3 (Delete Task)
    elif choice == "3":
        # Check if the 'tasks' list is empty before trying to delete anything
        if len(tasks) == 0:
            # Inform the user that deletion is impossible because the list is empty
            print("No tasks to delete.")
        # If there are tasks available to delete, execute the following block
        else:
            # Display a header for the tasks available for deletion
            print("\nYour Current Tasks:")
            # Loop through and display the tasks so the user knows which number to pick
            for index, task in enumerate(tasks, start=1):
                # Print each task with its number
                print(f"{index}. {task}")

            # Use a try-except block to handle potential input errors (like typing letters)
            try:
                # Ask the user for the task number to delete and convert it to an integer
                task_num = int(
                    input("Enter the number of the task to delete: ")
                )
                # Check if the entered number corresponds to a valid list index
                if 1 <= task_num <= len(tasks):
                    # Remove the task from the list (subtract 1 because Python lists start at index 0)
                    removed_task = tasks.pop(task_num - 1)
                    # Confirm to the user which task was successfully removed
                    print(f"Task '{removed_task}' deleted successfully!")
                # If the number is outside the range of the list, execute this block
                else:
                    # Inform the user that the number they entered does not exist in the list
                    print("Invalid task number.")
            # Catch ValueError exceptions if the user inputs non-numeric characters
            except ValueError:
                # Inform the user that they must enter a valid number
                print("Please enter a valid numeric task number.")

    # Check if the user selected option 4 (Exit)
    elif choice == "4":
        # Print a goodbye message to the user
        print("Thank you for using the To-Do List Program. Goodbye!")
        # Break out of the infinite 'while' loop to terminate the program
        break

    # Handle cases where the user inputs something other than 1, 2, 3, or 4
    else:
        # Inform the user that their menu selection was invalid
        print("Invalid choice! Please select a number between 1 and 4.")