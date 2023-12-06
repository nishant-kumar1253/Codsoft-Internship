#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

# Function to display the To-Do list
def display_todo_list(todo_list):
    print("\n----- To-Do List -----")
    if not todo_list:
        print("No tasks.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. [{task['status']}] {task['description']}")
    print("----------------------")

# Function to add a task to the To-Do list
def add_task(todo_list):
    task_description = input("Enter task description: ")
    todo_list.append({"description": task_description, "status": " "})
    print("Task added successfully!")

# Function to mark a task as completed
def complete_task(todo_list):
    display_todo_list(todo_list)
    task_number = int(input("Enter the task number to mark as completed: ")) - 1

    if 0 <= task_number < len(todo_list):
        todo_list[task_number]["status"] = "X"
        print(f"Task '{todo_list[task_number]['description']}' marked as completed!")
    else:
        print("Invalid task number.")

# Main function
def main():
    todo_list = []

    while True:
        print("\n----- To-Do List Menu -----")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            complete_task(todo_list)
        elif choice == "4":
            print("Exiting To-Do List program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


# In[ ]:




