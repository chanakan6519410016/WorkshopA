import random

def A():
    return 25  

def B(user, number):
    return user == number

def C():
    number = A()
    print("ยินดีต้อนรับสู่ Game bingo")

    while True:
        user = int(input("ใส่เลข : "))

        if user == 25:
            print("ถูก")
            break

        if B(user, number):
            print("Correct, You are the winner")
            break
        else:
            print("ไม่ถูก")
print("---------------------------------")
print("---------------------------------")
print("---------------------------------")
C()