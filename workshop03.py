# รับชื่อสินค้า ราคา แสดงผลคำนวณภาษี

def inputData( ) :
    Productname = input('ชื่อสินค้า : ')
    Productprice = float(input('ราคาสินค้า : '))
    return Productname, Productprice

def A(Productprice):
    PC = 7
    TAX = (Productprice * PC ) / 100
    return TAX

def E(Productname, Productprice, TAX):
    print(f"ป้อนชื่อสินค้า : {Productname}")
    print(f"ป้อนราคาสินค้า : {Productprice:.2f} บาท")
    print(f"ภาษีเป็นเงิน : {TAX:.2f} บาท")

print("=====================================")
print("========== ค่าคำนวณภาษีสินค้า======")    
print("=====================================")
Productname, Productprice = inputData()
print("=====================================")
TAX = A(Productprice)
E(Productname, Productprice, TAX )
print("=====================================")