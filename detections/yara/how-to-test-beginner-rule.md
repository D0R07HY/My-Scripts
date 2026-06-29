# How To Test The Beginner YARA Rule

ไฟล์นี้อธิบายวิธีลองใช้ YARA rule ตัวแรกกับไฟล์ตัวอย่างแบบทีละขั้น

ไฟล์ที่ใช้:

- rule: `detections/yara/beginner_text_marker_rule.yar`
- sample: `samples/educational-text-marker-sample.txt`

## สิ่งที่เรากำลังทำ

เราจะให้ YARA ตรวจว่าไฟล์ตัวอย่างมีข้อความที่ตรงกับ rule หรือไม่

ใน rule นี้ YARA จะมองหา 3 ข้อความ:

- `FOR EDUCATIONAL PURPOSES ONLY`
- `Malware Analysis`
- `Cyber Security`

และเงื่อนไขคือ:

- ถ้าเจออย่างน้อย 2 ข้อความ ให้ถือว่า match

## Step 1: เปิด terminal ใน root ของรีโป

ตัวอย่าง PowerShell:

```powershell
cd <path-to-your-My-Scripts-repo>
```

## Step 2: เช็กว่ามี YARA อยู่ในเครื่องหรือไม่

```powershell
yara --version
```

ถ้าคำสั่งนี้รันได้ แปลว่าพร้อมทดสอบ

ถ้ารันไม่ได้ แปลว่ายังไม่มี YARA ในเครื่อง และควรติดตั้งก่อน

## Step 3: รัน rule กับไฟล์ตัวอย่าง

```powershell
yara detections\yara\beginner_text_marker_rule.yar samples\educational-text-marker-sample.txt
```

## Step 4: ดูผลลัพธ์

ถ้า match คุณจะเห็นผลลัพธ์ประมาณนี้:

```text
Beginner_Text_Marker_Rule samples\educational-text-marker-sample.txt
```

ความหมายคือ:

- `Beginner_Text_Marker_Rule` คือชื่อ rule ที่ match
- `samples\educational-text-marker-sample.txt` คือไฟล์ที่ถูกจับได้

## Step 5: ลองแก้ไฟล์ sample เพื่อฝึก

ลองลบข้อความบางบรรทัดออก แล้วรันใหม่

ตัวอย่าง:

- ลบ `Cyber Security`
- ลบ `Malware Analysis`

ถ้าเหลือข้อความตรงกับ rule ไม่ถึง 2 ตัว rule ก็จะไม่ match

## Step 6: ลองแก้ condition ใน rule

จากเดิม:

```yara
2 of ($marker*)
```

ลองเปลี่ยนเป็น:

```yara
all of ($marker*)
```

ความหมายคือ:

ไฟล์จะต้องมีครบทุกข้อความในกลุ่ม `$marker` จึงจะ match

## สิ่งที่ควรเรียนรู้จากการทดลองนี้

หลังลองรันแล้ว คุณควรเริ่มเข้าใจว่า:

- YARA ใช้ค้นหา pattern ในไฟล์
- `strings` คือสิ่งที่เราต้องการให้ YARA หา
- `condition` คือกติกาตัดสิน
- การเปลี่ยน condition ทำให้กฎเข้มหรือกว้างขึ้นได้

## ถ้ายังไม่มี YARA

คุณยังสามารถเรียนจาก:

- การอ่าน rule
- การอ่านไฟล์อธิบาย `beginner_text_marker_rule_explained.md`
- การแก้ string และ condition เล่นในไฟล์ก่อน

เมื่อมี YARA ในเครื่องค่อยกลับมาลองรันจริง
