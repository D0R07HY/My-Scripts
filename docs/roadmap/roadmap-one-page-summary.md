# Roadmap One-Page Summary

## ใครควรใช้แผนนี้

เหมาะกับ:

- นักศึกษาที่เพิ่งเริ่ม Cyber Security
- คนที่มีพื้นฐานเขียนโค้ดเล็กน้อย
- คนที่อยากมีโปรเจคลง GitHub แบบปลอดภัยและดูเป็นระบบ

## เป้าหมายของแผนนี้

ไม่ใช่การทำของยากที่สุด

แต่คือการสร้างรีโปที่แสดงให้เห็นว่า:

- คุณเรียนรู้อย่างเป็นระบบ
- คุณเข้าใจเรื่องความปลอดภัย
- คุณเริ่มทำ analysis และ detection ได้จริง

## เส้นทางแบบสั้นที่สุด

1. ตั้ง lab ให้ปลอดภัย
2. ฝึกดูไฟล์และจดข้อมูล
3. ใช้สคริปต์ช่วยวิเคราะห์
4. เริ่มเขียน YARA และ Sigma
5. สร้าง simulator ที่ปลอดภัย
6. รวมทุกอย่างเป็น portfolio piece

## คุณควรมีอะไรเมื่อทำครบ

- lab setup note
- report template
- IOC template
- Python scripts 2-3 ตัว
- YARA rules 1-3 ตัว
- Sigma rules 1-2 ตัว
- simulator 1 ตัว
- report จริง 1-2 ชิ้น

## Phase 1

### ตั้งฐานให้ปลอดภัยและเป็นระบบ

ช่วงเวลา:

- สัปดาห์ 1-2

ทำอะไร:

- เติม `docs/lab-setup/overview.md`
- ใช้ `docs/reports/report-template.md`
- ใช้ `docs/iocs/ioc-template.md`

ผลลัพธ์:

- มีวิธีทำงานที่ปลอดภัย
- มี template พร้อมใช้

## Phase 2

### เริ่มเป็นนักวิเคราะห์จากงานเล็ก ๆ

ช่วงเวลา:

- สัปดาห์ 3-5

ทำอะไร:

- รัน `hash_report.py`
- รัน `basic_strings.py`
- จดสิ่งที่พบลง report

ผลลัพธ์:

- เริ่มเข้าใจ hash
- เริ่มอ่าน strings ได้
- เริ่มมองหา IOC ได้

## Phase 3

### เริ่มคิดแบบคนเขียน Detection

ช่วงเวลา:

- สัปดาห์ 6-8

ทำอะไร:

- เขียน YARA rule ตัวแรก
- เขียน Sigma rule ตัวแรก
- อธิบายว่ากฎนั้นจับอะไร

ผลลัพธ์:

- เริ่มแปลงสิ่งที่เห็นให้เป็นกฎตรวจจับได้

## Phase 4

### สร้าง Simulator ที่ปลอดภัย

ช่วงเวลา:

- สัปดาห์ 9-10

ทำอะไร:

- สร้าง script จำลอง file activity ในโฟลเดอร์แล็บ
- ห้ามแตะไฟล์จริง
- ห้ามมี persistence
- ห้ามมี network beacon

ผลลัพธ์:

- มี mini project ที่ปลอดภัย
- มี artifact สำหรับเอาไปทำ report และ detection

## Phase 5

### รวมให้เป็น Portfolio Piece

ช่วงเวลา:

- สัปดาห์ 11-12

ทำอะไร:

- เขียน report จริง
- อธิบาย IOC
- เชื่อม simulator กับ detection
- ปรับ README และจัดรีโปให้อ่านง่าย

ผลลัพธ์:

- รีโปดูมีทิศทางชัด
- ใช้เป็น portfolio ได้ดีขึ้น

## สิ่งที่ยังไม่ต้องรีบทำ

- เขียน malware
- ทำ persistence
- ทำ evasion
- ทำ process injection
- ไปงาน reverse ระดับลึกทันที

## สิ่งที่ควรโฟกัสตอนนี้

- VM
- Snapshot
- Hash
- Strings
- IOC
- Report writing
- Detection basics

## ถ้ารู้สึกว่ายาก ให้เริ่มแค่นี้

1. เติมข้อมูลใน `docs/lab-setup/overview.md`
2. รัน `hash_report.py` กับไฟล์ 3 ไฟล์
3. รัน `basic_strings.py` กับไฟล์ 2 ไฟล์
4. เปิด issue แรกจาก `docs/issues/`
5. เขียน report แรกจาก public writeup 1 ชิ้น

## ประโยคสรุปของ roadmap นี้

เป้าหมายของคุณตอนนี้คือ:

"เป็น beginner ที่จริงจัง มีวินัย และมีผลงานที่อธิบายได้"
