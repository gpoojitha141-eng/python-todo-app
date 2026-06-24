try:
    with open("tasks.txt","r")as file:
     tasks=file.read().splitlines()
except FileNotFoundError:
 tasks= []
while True :
    print("---to do app---")
    print("1.add task")
    print("2.view tasks")
    print("3.remove task")
    print("4.exit")  
    choice=input("enter a number: ") 
    if choice=="1":
        task=input("enter a task: ")
        tasks.append(task)
        with open("tasks.txt","w")as file:
            for task in tasks:
                file.write(task+"\n")
        print("task is added successfully")
    elif choice=="2":
       print("\ntasks:")
       for i,task in enumerate(tasks):
           print(f"{i+1}. {task}")
    elif choice=="3":
        for i,task in enumerate(tasks,start=1):
            print(i,".",task)
        num=int(input("enter the task number to remove: "))
        tasks.pop(num-1)
        with open("tasks.txt","w")as file:
            for task in tasks:
                file.write(task+"\n")
        print("task is removed successfully")
    elif choice=="4":
            print("good bye!")
            break
               