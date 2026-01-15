#Open the file and read tasks
file = open("text.txt","r")
tasks = file.readlines()
file.close()

#Show tasks
print("You Todo List:")
for task in tasks:
  print(task.strip())

#Ask the user for new Tasks
new_tasks = input("Enter new Task:")