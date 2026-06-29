
MAX_ADDRESS = 255
while True:
    Ip = input("ป้อน IP Address ของคุณ : ")
    try:

        
        # 1. ตัดแบ่งข้อความเป็น List ของ String
        cutting=Ip.split(".")

        # 2. เช็คเบื้องต้นว่ามี 4 ชุดหรือไม่
        if len(cutting) != 4:
            print("Incorrect: IP Address ต้องมี 4 ชุด (แยกด้วยจุด)")
            continue # เริ่มลูปใหม่ทันที

        # 3. แปลงทุกตัวเป็น int (ถ้ามีตัวอักษรปน จะเด้งไปที่ except ValueError ทันที)
        IntChange = [int(x) for x in cutting]

        # 4. เช็คว่ามีตัวไหนเกินค่าที่กำหนดไหม
        has_error = False
        for num in IntChange:
            if num > MAX_ADDRESS or num < 0:
                print(f"Incorrect!")
                has_error=True
                break # เจอตัวเดียวที่เกินก็ให้หยุดเช็คตัวที่เหลือในรอบนี้

            # 5. ถ้าไม่มีอะไรผิดพลาดเลย ให้หยุดลูป while
        if not has_error:
                print("Correct!")
                break #ออกจาก while loop
            
    except ValueError:
        print("Incorrect!")
# นำข้อมูลไปใช้ต่อ
# --- ส่วนการแสดงผลสุดท้าย ---
print("IP ADDRESS : ", end="") #end="" คือการบอก Python ว่า ไม่ต้องขึ้นบรรทัดใหม่
# ใช้ join เพื่อความสวยงาม (แปลง int กลับเป็น str ก่อน join)
print(".".join(map(str, IntChange))) # map(str, IntChange) = แปลงทุกอย่างใน List ให้เป็นข้อความ (String)
                                     # "...".join(...) การเอาสมาชิกใน List มา "เชื่อม" กันด้วยอักขระที่เรากำหนด = "ตัวเชื่อม".join(ลิสต์ของข้อความ)



