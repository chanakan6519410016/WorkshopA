def A(P, PV):
    if PV >= 7 and PV <= 8:
        R = "Result is Normal"
    elif PV > 8:
        R = "Result is Acid"
    else:
        R = "Result is Alkali"

    print(f"Province: {P}")
    print(f"pH Value: {PV}")
    print(f"Result: {R}")

print("---------------------------------")
print("--------- ตรวจสอบค่า PH ----------")
print("---------------------------------")
name = input("ใส่ชื่อจังหวัด : ")
pv = float(input("ค่า pH : "))
A(name, pv)