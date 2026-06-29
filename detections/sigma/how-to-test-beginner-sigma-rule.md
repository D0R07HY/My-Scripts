# How To Test The Beginner Sigma Rule

ไฟล์นี้อธิบายวิธีทำความเข้าใจและลองทดสอบ Sigma rule ตัวแรกแบบทีละขั้น

ไฟล์ที่ใช้:

- rule: `detections/sigma/proc_creation_win_beginner_analysis_scripts.yml`
- explained: `detections/sigma/proc_creation_win_beginner_analysis_scripts_explained.md`

## ก่อนเริ่ม ต้องเข้าใจก่อนว่า Sigma คืออะไร

Sigma ไม่ได้สแกนเนื้อไฟล์แบบ YARA

Sigma ใช้กับ "log" หรือ "event" ของระบบ

พูดง่าย ๆ:

- YARA = ดูข้างในไฟล์
- Sigma = ดูเหตุการณ์ที่เกิดขึ้นในระบบ

ดังนั้น การทดสอบ Sigma จึงไม่ใช่การเอา rule ไปยิงใส่ไฟล์ `.txt`
แต่คือการดูว่า ถ้ามี event แบบที่เรากำหนดไว้ rule จะ match หรือไม่

## Rule นี้จับอะไร

rule นี้พยายามจับกรณีที่:

1. มี `python.exe` ถูกเรียกใช้งาน
2. ใน command line มี
   - `analysis\scripts\hash_report.py`
   - หรือ `analysis\scripts\basic_strings.py`

แปลแบบง่าย:

ถ้ามีคนรันสคริปต์วิเคราะห์ของรีโปนี้ผ่าน Python บน Windows
rule นี้ควร match

## สิ่งที่ต้องมีเพื่อทดสอบ Sigma จริง

ถ้าจะทดสอบแบบจริงจัง คุณต้องมีอย่างน้อยหนึ่งอย่าง:

- process creation logs จาก Windows
- Sysmon Event ID 1
- หรือ Security Event 4688

และต้องมีระบบหรือเครื่องมือที่รองรับการใช้ Sigma ต่อ

ตัวอย่างเช่น:

- SIEM
- Sigma conversion tools
- ระบบ log lab ที่ map field แล้ว

## สำหรับมือใหม่ ควรทดสอบแบบไหนดี

ผมแนะนำให้เริ่ม 2 ระดับ:

### ระดับที่ 1: ทดสอบแบบอ่าน logic

ยังไม่ต้องมี SIEM
ยังไม่ต้องมี log pipeline เต็ม

แค่ฝึกอ่านว่า rule นี้ match กับ event แบบไหน

### ระดับที่ 2: ทดสอบกับ process creation log ใน lab

เมื่อคุณเริ่มมี Windows lab และ log ที่เหมาะสมแล้ว
ค่อยทดลองกับ event จริง

## Step 1: อ่านตัว rule ก่อน

เปิดไฟล์:

- `detections/sigma/proc_creation_win_beginner_analysis_scripts.yml`

ให้มอง 3 จุดหลัก:

1. `logsource`
2. `detection`
3. `condition`

## Step 2: เข้าใจ logsource

ใน rule นี้:

```yaml
logsource:
    category: process_creation
    product: windows
```

ความหมายคือ:

- เรากำลังดู log การสร้าง process
- และ log นี้มาจาก Windows

นั่นแปลว่า ถ้าไม่มี process creation log ต่อให้มี rule นี้ก็ยังทดสอบไม่ได้จริง

## Step 3: เข้าใจ detection

ใน rule นี้:

```yaml
selection_image:
    Image|endswith: '\python.exe'
selection_commandline:
    CommandLine|contains:
        - 'analysis\scripts\hash_report.py'
        - 'analysis\scripts\basic_strings.py'
condition: selection_image and selection_commandline
```

อ่านแบบภาษาคนคือ:

- process ต้องเป็น `python.exe`
- และ command line ต้องมีชื่อสคริปต์ตัวใดตัวหนึ่ง

ถ้าตรงทั้งสองข้อพร้อมกัน = match

## Step 4: ลองคิด event ตัวอย่างด้วยตัวเอง

### กรณีที่ควร match

```text
Image: C:\Python313\python.exe
CommandLine: python analysis\scripts\hash_report.py LICENSE
```

เหตุผล:

- ลงท้ายด้วย `python.exe`
- command line มี `analysis\scripts\hash_report.py`

ดังนั้น match

### อีกกรณีที่ควร match

```text
Image: C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe
CommandLine: python analysis\scripts\basic_strings.py LICENSE --min-length 6
```

เหตุผล:

- เป็น `python.exe`
- มี `analysis\scripts\basic_strings.py`

ดังนั้น match

### กรณีที่ไม่ควร match

```text
Image: C:\Python313\python.exe
CommandLine: python some_other_script.py
```

เหตุผล:

- ถึงจะเป็น `python.exe`
- แต่ไม่ได้รัน `hash_report.py` หรือ `basic_strings.py`

ดังนั้นไม่ match

### อีกกรณีที่ไม่ควร match

```text
Image: C:\Windows\System32\cmd.exe
CommandLine: cmd /c analysis\scripts\hash_report.py
```

เหตุผล:

- command line มีชื่อ script
- แต่ process ไม่ใช่ `python.exe`

ดังนั้นไม่ match

## Step 5: ทดสอบใน Windows lab แบบง่าย

ถ้าคุณมี Windows lab ให้ลองทำแบบนี้:

1. เปิด process creation logging
2. รันคำสั่งนี้ใน repo:

```powershell
python analysis\scripts\hash_report.py LICENSE
python analysis\scripts\basic_strings.py LICENSE --min-length 6
```

3. เก็บ log ที่ได้
4. ดูว่า event มี field ที่สอดคล้องกับ:
   - `Image`
   - `CommandLine`

## Step 6: เทียบกับ rule

เมื่อได้ log แล้ว ให้ถามตัวเอง:

- field `Image` ลงท้ายด้วย `python.exe` ไหม
- field `CommandLine` มี path ของ script ไหม

ถ้าทั้งสองข้อใช่
แปลว่า rule นี้ควร match

## Step 7: สิ่งที่คุณควรเรียนรู้จากการทดสอบ

หลังทำขั้นตอนนี้ คุณควรเริ่มเข้าใจว่า:

- Sigma ต้องอาศัย log
- การเขียน rule ต้องรู้ก่อนว่าจะใช้ field ไหน
- `condition` ใช้รวมหลายเงื่อนไข
- การ match ของ Sigma ไม่ได้ดู "ตัวไฟล์" แต่ดู "เหตุการณ์"

## ถ้ายังไม่มี log หรือ SIEM

ก็ยังเรียน Sigma ได้โดย:

- อ่าน rule
- ลองคิด event ที่ควร match / ไม่ควร match
- เขียนตัวอย่าง event แบบ text ของตัวเอง
- ค่อยไปต่อเรื่อง log pipeline ภายหลัง

นี่เป็นวิธีเริ่มต้นที่เหมาะกับมือใหม่มาก

## ขั้นต่อไปที่แนะนำ

เมื่อคุณเข้าใจ rule นี้แล้ว ลองทำต่อ:

1. เปลี่ยนชื่อ script ใน rule
2. เพิ่ม script ใหม่อีก 1 ตัวใน `CommandLine|contains`
3. ลองสร้าง simulator แล้วเขียน Sigma rule จับมัน

นี่จะช่วยให้คุณเริ่มคิดแบบ detection engineering ได้ดีขึ้น
