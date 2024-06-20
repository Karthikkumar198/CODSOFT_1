print("1. Add task\n2. Remove\n3. Update\n4. Display\n5. Quit\n")
list1 = []
count = 0
while (True):
    choice = int(input("Enter choice : "))
    if(choice == 1):
        x = input("Enter the task : ")
        list1.append(x)
    elif(choice == 2):

        x = int(input("Enter task number to be removed : "))
        if(x>0 and x<=len(list1)):
            list1.remove(list1[x-1])
        else:
            print("Task number not found")
    elif(choice == 3):
        x = int(input("Enter task number to be updated : "))

        if(x>0 and x<=len(list1)):
            s = input("Enter the task : ")
            list1[x-1]= s
        else:
            print("Task number not found")
    elif(choice == 4):
        if(len(list1) > 0):
            print("Tasks are : ")
            count = 1
            for i in list1:
                print(str(count)+". "+i)
                count = count+1
        else:
            print("No tasks found\n")
    elif(choice == 5):
        print("Program terminated\n")
        break
    else:
        print("Invalid choice")