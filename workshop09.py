def A(Sales):
    if Sales <= 1000:
        Committion = 0.0
    elif Sales <= 2000:
        Committion = Sales * 0.01
    elif Sales <= 3000:
        Committion = Sales * 0.03
    else:
        Committion = Sales * 0.05
    
    return Committion

def B(Id, name, Committion):
    print("รหัสพนักงาน :", Id)
    print("ชื่อพนักงาน :", name)
    print("ยอดขาย :", Sales)
    print("ค่าคอมมิชชั่น :", Committion)
print("------------------------------------")
print("-----------คำนวณค่าคอมมิชชั่น---------")
print("------------------------------------")
Id = input("ใส่รหัสพนักงาน : ")
name = input("ใส่ชื่อพนักงาน : ")
Sales = float(input("ใส่ยอดขาย : "))

Committion = A(Sales)
B(Id, name, Committion)