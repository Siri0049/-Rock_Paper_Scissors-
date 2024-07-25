import random

user=int(input("CHOOSE:\n'0' for stone \n'1' for paper\n'2' for scissor\n"))
comp=random.randint(0,2)

def check(user,comp):
    if (user==comp):
        return 0
    elif(comp==0 and user==2):
        return -1
    elif(comp==1 and user==0):
        return -1
    elif(comp==2 and user ==1):
        return -1
    else:
        return 1
    
print(f"You Have Choose {user}")
print(f"The Computer Have chossen {comp}")
score=check(user,comp)
if(score==0):
    print("its a draw....")
elif(score==-1):
    print("SRY YOU LOOSE :(")
else:
    print("Congratulations!!!!,YOU WONN")