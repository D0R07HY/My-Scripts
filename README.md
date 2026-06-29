# My-Scripts

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://openjdk.org/)
[![Status](https://img.shields.io/badge/Status-Educational%20Lab-0A7E8C?style=for-the-badge)](#)

รีโปนี้เป็นพื้นที่รวมงานฝึกเขียนโค้ดส่วนตัว สคริปต์ขนาดเล็ก และบันทึกการศึกษาเชิงป้องกันด้าน Cyber Security ในสภาพแวดล้อมที่ควบคุมได้

โครงของรีโปนี้ถูกปรับให้แยกระหว่าง:

- แบบฝึก Java และ Python ทั่วไป
- งานวิเคราะห์เชิงป้องกันด้าน malware
- เอกสาร lab, IOC, roadmap, glossary, และ detection rules

รีโปนี้ไม่มีไว้สำหรับเผยแพร่ live malware, payload ที่รันได้จริง, persistence tooling, ransomware logic, หรือโค้ดที่มีเป้าหมายเพื่อเข้าถึงหรือทำลายระบบของผู้อื่น

## Start Here

ถ้าคุณเพิ่งเข้ามาในรีโปนี้และยังไม่แน่ใจว่าควรอ่านไฟล์ไหนก่อน ให้เริ่มตามลำดับนี้:

1. `README.md`
   เพื่อเข้าใจภาพรวมของรีโป
2. `SECURITY.md`
   เพื่อเข้าใจขอบเขตและข้อจำกัดด้านความปลอดภัย
3. `docs/roadmap/roadmap-one-page-summary.md`
   เพื่อดูภาพรวม roadmap แบบสั้น
4. `docs/roadmap/student-cybersecurity-roadmap.md`
   เพื่อดู roadmap แบบเต็ม
5. `docs/roadmap/roadmap-for-beginners-explained.md`
   เพื่ออ่านคำอธิบาย roadmap แบบภาษาคนเริ่มต้น
6. `docs/glossary/beginner-cybersecurity-glossary.md`
   เพื่อทำความเข้าใจคำศัพท์ที่ใช้ในรีโป
7. `docs/lab-setup/overview.md`
   เพื่อดูโครง lab และกติกาความปลอดภัย
8. `docs/reports/report-template.md`
   เพื่อดูรูปแบบการเขียน report
9. `docs/iocs/ioc-template.md`
   เพื่อดูรูปแบบการเก็บ IOC
10. `analysis/scripts/hash_report.py` และ `analysis/scripts/basic_strings.py`
    เพื่อเริ่มใช้เครื่องมือช่วยวิเคราะห์ตัวแรกของรีโป

ถ้าคุณเป็นมือใหม่มาก ๆ แนะนำให้อ่าน 3 ไฟล์นี้ก่อน:

- `docs/roadmap/roadmap-one-page-summary.md`
- `docs/roadmap/roadmap-for-beginners-explained.md`
- `docs/glossary/beginner-cybersecurity-glossary.md`

## โครงสร้างรีโป

```text
.
|-- README.md
|-- SECURITY.md
|-- LICENSE
|-- .gitignore
|-- docs/
|   |-- glossary/
|   |-- issues/
|   |-- iocs/
|   |-- lab-setup/
|   |-- reports/
|   `-- roadmap/
|-- analysis/
|   `-- scripts/
|-- detections/
|   |-- yara/
|   `-- sigma/
|-- simulators/
|   `-- README.md
|-- samples/
|   `-- README.md
|-- java/
|   `-- practice/
|-- python/
|   `-- practice/
`-- tools/
```

## คำอธิบายแต่ละส่วน

### `java/practice/`

ใช้เก็บแบบฝึก Java, โค้ดทดลอง, และงานเรียนที่ไม่เกี่ยวกับการโจมตีหรือ payload อันตราย

### `python/practice/`

ใช้เก็บสคริปต์ Python ทั่วไป เช่น utility เล็ก ๆ, แบบฝึกการประมวลผลข้อมูล, หรือโปรแกรมตรวจสอบ input

### `docs/`

ใช้เก็บเอกสารตั้งแล็บ รายงานผลการวิเคราะห์ บันทึก IOC roadmap คำศัพท์ และ issue templates

### `analysis/`

ใช้เก็บสคริปต์ช่วยวิเคราะห์เชิงรับ เช่น hash, metadata, strings, และ report helpers

### `detections/`

ใช้เก็บ YARA และ Sigma rule ที่เขียนจากผลการวิจัยหรือการสังเกตในแล็บ

### `simulators/`

ใช้เก็บตัวจำลองพฤติกรรมที่ไม่เป็นอันตรายเพื่อการศึกษาและทดสอบการมองเห็นของระบบป้องกัน

### `samples/`

ใช้เก็บเฉพาะ metadata เช่น hash, alias, และแหล่งอ้างอิง ห้ามเก็บ live malware ใน public repo

## กติกาความปลอดภัย

- ใช้งานเฉพาะใน isolated lab
- ห้ามทดสอบกับระบบจริงที่ไม่ได้รับอนุญาต
- ห้าม commit ไฟล์ `.class`, `.exe`, `.dll`, หรือ binary ที่น่าสงสัย
- ห้ามอัปโหลด sample ที่เป็นอันตรายจริงขึ้น GitHub
- ให้ความสำคัญกับรายงาน, IOC, screenshot, และ detection content มากกว่า artifact ดิบ

## สิ่งที่เหมาะกับรีโปนี้

- แบบฝึก Java/Python
- รายงาน Malware Analysis
- IOC documentation
- YARA และ Sigma rules
- benign simulators
- lab notes และ workflow เชิงป้องกัน

## สิ่งที่ไม่ควรอยู่ในรีโปนี้

- live malware samples
- ransomware หรือ wiper logic
- credential theft code
- persistence หรือ evasion features
- exploit delivery tooling
- compiled suspicious artifacts

## License

รีโปนี้ใช้ license ตามไฟล์ `LICENSE` และใช้ `README.md` กับ `SECURITY.md` เพื่อกำกับขอบเขตการใช้งานอย่างชัดเจน
