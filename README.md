# My-Scripts

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://openjdk.org/)
[![Status](https://img.shields.io/badge/Status-Educational%20Lab-0A7E8C?style=for-the-badge)](#)

รีโปนี้เป็นพื้นที่รวมงานฝึกเขียนโค้ดส่วนตัว สคริปต์ขนาดเล็ก และบันทึกการศึกษาเชิงป้องกันด้าน Cyber Security ในสภาพแวดล้อมที่ควบคุมได้

โครงของรีโปนี้ถูกปรับให้แยกระหว่าง:

- แบบฝึก Java และ Python ทั่วไป
- งานวิเคราะห์เชิงป้องกันด้าน malware
- เอกสาร lab, IOC, และ detection rules

รีโปนี้ไม่มีไว้สำหรับเผยแพร่ live malware, payload ที่รันได้จริง, persistence tooling, ransomware logic, หรือโค้ดที่มีเป้าหมายเพื่อเข้าถึงหรือทำลายระบบของผู้อื่น

## โครงสร้างรีโป

```text
.
|-- README.md
|-- SECURITY.md
|-- LICENSE
|-- .gitignore
|-- docs/
|   |-- lab-setup/
|   |-- reports/
|   `-- iocs/
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

ใช้เก็บเอกสารตั้งแล็บ รายงานผลการวิเคราะห์ บันทึก IOC และโน้ตจากการศึกษา

### `analysis/`

ใช้เก็บสคริปต์ช่วยวิเคราะห์เชิงรับ เช่น hash, metadata, strings, import inspection, และ report helpers

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
