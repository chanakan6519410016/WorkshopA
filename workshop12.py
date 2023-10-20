def expenses() :
    print('ค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยวของกรุ๊ปทัวร์')

def inputData() :
    number_of_people = int(input('ป้อนจำวนคน : '))
    return number_of_people 

def C(acount) :
    if count <= 2 :
        print(f'จำนวน{acount}คน คิดแพ็กเกจละ 300 บาทต่อคน')
    elif count >= 3 and count <= 5 :
        print(f'จำนวน{acount}คน คิดแพ็กเกจละ 250 บาทต่อคน')
    elif count >= 6 and count <= 10 :
        print(f'จำนวน{count}คน คิดแพ็กเกจละ 210 บาทต่อคน')    
    else :
        print(f'จำนวน{count}คน คิดแพ็กเกจละ 150 บาทต่อคน')
print("-----------------------------------")
expenses()
print("-----------------------------------")
count =inputData()
print("-----------------------------------")
C(count)