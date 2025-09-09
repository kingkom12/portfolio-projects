


def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = [line.strip() for line in f]
        return tasks
    except FileNotFoundError:
     return []  


def save_tasks(tasks):
   with open("tasks.txt", "w") as f:
      for task in tasks:
         f.write(task + "\n")


def add_task(tasks):
   task = input("enter a task: ").strip()
   if task:
      tasks.append(task)
      save_tasks(tasks)
      print(f"Added: {task}")
   else:
      print("Task cannot be empty!")   

def view_tasks(tasks):
   if not tasks:
      print("No tasks yet!")
   else:
      print("\n--- To-Do List ---")
      for i, task in enumerate(tasks, start=1):
         print(f"{i}. {task}")
      print("-------------------\n")         

def get_choice():
   while True:
      print("1. View Tasks")
      print("2 Add Task")
      print("3. Quit")
      user = input("Choose (1-3): ").strip()
      if user in ("1", "2", "3"):
         return user
      else:
         print("Please Choose 1,2 or 3. Try again.")

tasks = load_tasks()
while True:
   choice = get_choice()

   if choice == "1":
     view_tasks(tasks)
   elif choice == "2":
     add_task(tasks)
   elif choice == "3":
      print("Goodbye!")
      break             
  
   
   