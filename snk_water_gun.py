import random
print("Press 1 for Snake.\nPress 2 for Water.\nPress 3 for Gun.")
ch=int(input("Enter your choice:"))
if ch<1 or ch>3:
    print("Invalid choice!")
    exit()
comp=random.randint(1,3)
print("Your choice : ",ch)
print("Choice of Computer : ",comp)
print("Result :",end=" ")
if ch==comp:
    print("Draw")
elif comp-ch==1 or comp-ch==-2:
    print("You win!")
else:
    print("You lose!")
