import json
from task_class import Task
file_object = open("tasks.txt", "w")
file_object.close()


tasks = []

task_number = input("Press 1 to add task; Press 2 to delete task; Press 3 to view all tasks; Press q to quit: ")

def add_task():
  task_name = input("Task: ")
  task_priority = input("Priority: ")
  task = Task(task_name, task_priority)
  tasks.append(task.__dict__)

  with open("tasks.json", "w") as file_object:
    json.dump(tasks,file_object) 


def delete_task():
  with open("tasks.json") as file_object:
    some_tasks = json.load(file_object)

  for index in range(0, len(some_tasks)):
    task_index = index + 1
    task_title = some_tasks[index]["title"]
    task_priority = some_tasks[index]["priority"]

    print(f"{task_index} - {task_title} - {task_priority}")  
  
  item_to_delete = int(input("Delete which task? "))
    
  del some_tasks[item_to_delete-1]


def list_tasks():
  with open("tasks.json") as file_object:
     some_tasks = json.load(file_object)

  for index in range(0, len(some_tasks)):
    task_index = index + 1
    task_title = some_tasks[index]["title"]
    task_priority = some_tasks[index]["priority"]

    print(f"{task_index} - {task_title} - {task_priority}")


while task_number != "q":

  if task_number == "1":
    add_task()
    
  if task_number == "2":
    delete_task()

  if task_number == "3":
   list_tasks()

  task_number = input("Press 1 to add task; Press 2 to delete task; Press 3 to view all tasks; Press q to quit: ")

