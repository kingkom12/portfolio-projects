def delete_task(tasks):
   view_tasks(tasks)
   if not tasks:
      return
   number = input("Enter the task number to delete: ").strip()
   if not number.isdigit():
      print("Invalid input.")
      return
   
   idx = int(number)
   if idx < 1 or idx > len(tasks):
      print("Out of range.")
      return
 
   removed = tasks.pop(idx -1)
   save_tasks(tasks)
   print(f" Deleted: {removed}")
   
def task_count(tasks):
     count = len(tasks)
     print("Total tasks:", count)
     if count > 0:
        print("Next index:", count + 1)



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
   if not task:
      print("Task cannot be empty!")
      return
     
   lower_tasks = [t.lower() for t in tasks]
   if task.lower() in lower_tasks:
      print("That task already exists.")
      return
   tasks.append(task)
   save_tasks(tasks)
   print(f"Added : {task}")

def confirm_quit():
   choice = input("Are you sure you want to quit? (y/n): ").strip().lower()
   if choice == "y":
      return True
   else:
      return False
   

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
      print("2. Add Task")
      print("3. Quit")
      print("4. Delete Task")
      print("5. Task Count")

      user = input("Choose (1-5): ").strip()
      if user in ("1", "2", "3", "4", "5"):
         return user
      else:
         print('Please Choose "1","2","3","4","5". Try again.')

tasks = load_tasks()
while True:
   choice = get_choice()

   if choice == "1":
     view_tasks(tasks)
   elif choice == "2":
     add_task(tasks)
   elif choice == "3":
      if confirm_quit():
         print("Goodbye!")
         break
   elif choice == "4":
     delete_task(tasks)
   elif choice == "5":
     task_count(tasks)

         
           
  
   
   