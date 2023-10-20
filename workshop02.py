def inputData( ) :
    name = input('ป้อนชื่อ : ') 
    codenumber = input('ป้อนรหัสนักศึกษา : ')
    return name, codenumber

def inputnumber( ) :
    n1=int(input('คะแนนสอบครั้งที่ 1 :'))
    n2=int(input('คะแนนสอบครั้งที่ 2 :'))
    n3=int(input('คะแนนสอบครั้งที่ 3 :'))
    return n1, n2, n3,

def Averageofnumber(n1, n2, n3 ):
    Averageofnumber = ((n1+n2+n3)/3)
    return Averageofnumber

def show(n1,n2,n3,Averageofnumber):
    print(f'ค่าเฉลี่ยของคะแนนสอบทั้ง 3 : {Averageofnumber} ')
    

print("=========================================")
name, codenumber = inputData()
print("======== ผลคะแนนสอบ 3 ครั้ง===============")
print("=========================================")
n1,n2,n3 = inputnumber()
print("=========================================")
Averageofnumber = Averageofnumber(n1,n2,n3)
show(n1,n2,n3,Averageofnumber)