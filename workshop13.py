def inputdata():
    id = input("รหัสนักเรียน : ")
    name = input("ชื่อนักเรียน : ")
    gpa = float(input("เกรดเฉลี่ย : "))

    if gpa < 2.00:
        print(f"Student ID {id}, {name}: สอบไม่ผ่าน")
                
    else:
        print(f"Student ID {id}, {name}: สอบผ่าน")

def gpaset(id, name, gpa):
    if gpa < 2.00:
        print(f"Student ID {id}, {name}: สอบไม่ผ่าน")
        
    else:
        print(f"Student ID {id}, {name}: สอบผ่าน")
    
print("-----------------------------------")
print("-----------ตรวจสอบผลการเรียน--------")
print("-----------------------------------")
inputdata()