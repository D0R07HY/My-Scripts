# Malware Analysis Lab Setup

## Purpose

เอกสารนี้ใช้สรุปภาพรวมของแล็บสำหรับการศึกษา malware analysis และงานทดลองเชิงป้องกันในสภาพแวดล้อมที่แยกจากระบบจริง

## Lab Goals

- ทดลองและศึกษาไฟล์หรือพฤติกรรมที่น่าสงสัยในสภาพแวดล้อมที่ควบคุมได้
- ฝึกบันทึก IOC, behavior, และ detection ideas
- ใช้เป็นพื้นที่เรียนรู้โดยไม่กระทบเครื่องหลักหรือระบบผู้อื่น

## Recommended VM Layout

### Windows Analysis VM

ใช้สำหรับ:

- เปิดดูพฤติกรรมของโปรแกรมในสภาพแวดล้อม Windows
- เก็บ screenshot, process note, file activity note
- ใช้กับเครื่องมือ monitoring ที่เหมาะกับการเรียนรู้

ตัวอย่างที่ควรมี:

- Windows 10 หรือ Windows 11 VM
- snapshot สะอาดก่อนเริ่มทุกครั้ง
- โฟลเดอร์สำหรับข้อมูลทดสอบโดยเฉพาะ

### Linux Analysis VM

ใช้สำหรับ:

- งาน static analysis เบื้องต้น
- งานคำนวณ hash, strings, metadata
- งานเขียน report และ script

ตัวอย่าง:

- REMnux หรือ Linux VM ที่เตรียมเครื่องมือพื้นฐานไว้แล้ว

## Network Isolation

แนะนำให้ใช้:

- Host-only network
- Internal network

หลีกเลี่ยง:

- Bridged mode
- การปล่อย VM ออก Internet โดยไม่จำเป็น

ถ้าจำเป็นต้องใช้อินเทอร์เน็ตเพื่อดาวน์โหลดเครื่องมือ:

- ทำเฉพาะช่วง setup
- ปิดหรือแยก network ตอนทำการทดลองจริง

## Safety Rules

- ห้ามใช้เครื่องหลักเป็นที่ทดสอบ
- ห้ามใช้ไฟล์งานจริงหรือข้อมูลส่วนตัวในแล็บ
- ห้ามเปิด shared clipboard หรือ drag-and-drop ถ้าไม่จำเป็น
- ห้ามอัปโหลดไฟล์น่าสงสัยขึ้น GitHub
- ห้ามทดสอบกับระบบที่ไม่ได้รับอนุญาต

## Snapshot Workflow

1. สร้าง snapshot สะอาด
2. รันการทดลอง
3. เก็บ note, hash, และ screenshot
4. revert snapshot
5. บันทึกสิ่งที่เรียนรู้ลง report

## Tools I Plan To Learn

- Hashing tools
- Strings extraction tools
- Process monitoring tools
- YARA
- Sigma

## My Current Skill Level

- Java: basic
- C: basic
- Network: beginner
- Cyber Security: beginner with strong interest

## Notes

เป้าหมายของแล็บนี้ไม่ใช่การสร้าง malware แต่คือการฝึกคิดแบบนักวิเคราะห์และนักป้องกันระบบ
