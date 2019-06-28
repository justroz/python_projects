option = input("Press 1 to add tasks; Press 2 to delete tasks; Press 3 to view all tasks; Press q to quit: ")
tasks = []

while option != "q":

#Pressing 1 to add tasks
  if option == "1":
    title = input("Enter your task: ")
    priority = input("High, Medium, or Low priority: ")

    task = {
      "title": title,
      "priority": priority
    }
    # add dictionary to tasks[]
    tasks.append(task)
    
#Pressing 2 to delete tasks
  elif option == "2":
    for index in range(0, len(tasks)):
      task_dict = tasks[index]
      task_title = task_dict["title"]
      task_priority = task_dict["priority"]
      print(f"{index}  {task_title}  {task_priority}")
      
    task_to_delete = int(input("Which task do you want to delete? "))

    del tasks[task_to_delete]

#Pressing 3 to view all tasks
  elif option == "3":
    for index in range(0, len(tasks)):
      task_dict = tasks[index]
      task_title = task_dict["title"]
      task_priority = task_dict["priority"]
      print(f"{index}  {task_title}  {task_priority}")
      
#if wrong button is pressed
  else:
    print("Please press 1, 2, 3, or q")

  option = input("Press 1 to add tasks; Press 2 to delete tasks; Press 3 to view all tasks; Press q to quit: ")



