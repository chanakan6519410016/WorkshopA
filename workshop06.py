def A(name, loan):
    if loan >= 1000:
        interest = 2.5  
    else:
        interest = 5.5  

    CI = (interest / 100) * loan

    print("ผู้กู้:", name)
    print("อัตราดอกเบี้ยที่คำนวณได้:", interest, "%")
    print("จำนวนดอกเบี้ยที่ต้องจ่าย:", CI, "บาท")

print("---------------------------------")
print("-------คำนวณอัตราดอกเบี้ยเงินกู้-------")
print("---------------------------------")
name = input("ป้อนชื่อผู้กู้: ")
loan = float(input("ป้อนจำนวนเงินกู้ (บาท): "))
A(name, loan)