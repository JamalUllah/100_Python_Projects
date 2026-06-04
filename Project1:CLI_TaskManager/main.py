# CLI Task Manager
import json
import os
from colorama import init, Fore, Style
# Colorama is used to write colored text in CLI
init(autoreset=True)

class TaskManager:

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_name):
        new_task = {
            "name": task_name,
            "completed": False 
        }
        self.tasks.append(new_task)
        self.save_tasks() # To save ourself from any data loss
        print(Fore.GREEN + f"Succes! {task_name} Added")

    def veiw_tasks(self):
        if not self.tasks:
            print(Fore.CYAN + "List is empty")
            return
        
        print(Fore.YELLOW + "-----Your Tasks------")
        for i, task in enumerate(self.tasks, start=1): # start =1 so i may not be 0
            status = "[X]" if task["completed"] else "[ ]"

            if task["completed"]:
                print(Fore.GREEN + f"{i} {status} {task["name"]}")
            else:
                print(Style.RESET_ALL + f"{i} {status} {task["name"]}")

    def complete_task(self, task_number):
    #index
        index = task_number - 1
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print(Fore.GREEN + f"Awesome! Task {self.tasks[index]['name']} mark as completed") 
        else:
            print(Fore.RED + "Error! Invalid Input")



def main():

    manager = TaskManager()

    while True:
        print(Style.BRIGHT + "\n ==== CLI Task Manager =====")
        print("1. Add a task")
        print("2. Veiw Tasks")
        print("3. Complete a task")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            task_name = input("Enter the task description: ")
            manager.add_task(task_name)

        elif choice == "2":
            manager.veiw_tasks()
        
        elif choice == "3":
            manager.veiw_tasks()
            try:
                task_num = int(input("Enter the number of task to complete: "))
                manager.complete_task(task_num)
            except ValueError:
                print(Fore.RED + "Error, Invalid Input")

        elif choice == "4":
            print(Fore.MAGENTA + "Goodbye!") 
            break

        else:
            print(Fore.RED + "Invalid Choice")


if __name__ == "__main__":
    main()
