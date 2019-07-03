from task_class import Task
file_object = open("tasks.txt", "w")
file_object.close()


tasks = []

task_number = input("Press 1 to add task; Press 2 to delete task; Press 3 to view all tasks; Press q to quit: ")

def add_task():
  task_name = input("Task: ")
  task_priority = input("Priority: ")
  task = Task(task_name, task_priority)
  tasks.append(task)

  with open("tasks.txt", "a") as file_object:
    file_object.write(f"{task_name} {task_priority} \n") 

def delete_task():
  for index in range(0, len(tasks)):
     print(f"{index+1} - {tasks[index].title} - {tasks[index].priority}") 
  
  item_to_delete = int(input("Delete which task? "))
    
  del tasks[item_to_delete-1]

def list_tasks():
  for index in range(0, len(tasks)):
     print(f"{index+1} - {tasks[index].title} - {tasks[index].priority}") 


while task_number != "q":

  if task_number == "1":
    add_task()
    
  if task_number == "2":
    delete_task()

  if task_number == "3":
   list_tasks()

  task_number = input("Press 1 to add task; Press 2 to delete task; Press 3 to view all tasks; Press q to quit: ")

