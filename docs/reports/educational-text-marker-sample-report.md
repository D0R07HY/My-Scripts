
## Sample Overview

Sample name or alias: Test

File name: README.md

File type: Plain text

File size: 6817 bytes

SHA256: 95590a427b050232d307e8b76fc291bb3c6d7c393fc8ad6e677b20d03d717b45

MD5: 734de86ec6e9549be58a7d2a4693e8c3

SHA1: cb43d54eb63ef40ff5696e04b24e7544a08ef437

## Context
ไฟล์นี้เป็นไฟล์ข้อความที่ใช้เป็น sample ปลอดภัยสำหรับฝึก static analysis

ใช้ทดสอบการดึง strings และการทดลอง YARA rule เบื้องต้น

ไม่มีพฤติกรรมอันตรายและถูกสร้างขึ้นเพื่อการเรียนรู้

## Static Analysis Notes
จดสิ่งที่เห็นจากการวิเคราะห์แบบไม่รันไฟล์ เช่น: เป็นไฟล์ข้อความที่เป็นภาพรวมของรีโปนี้

path ที่พบ : C:\Users\M S I\Documents\Codex\2026-06-29\d\work\My-Scripts\README.md

เป็นไฟล์ text/markdown

มี strings จำนวนมาก

พบคำที่น่าสนใจ เช่น Cyber Security, Malware Analysis, IOC, YARA, Sigma

ไม่พบสิ่งที่บ่งชี้ว่าเป็น executable หรือ binary

ไฟล์นี้เหมาะกับการใช้เป็น sample สำหรับฝึก extraction และ pattern matching

## Indicators of Compromise
filename: README.md

Hashes: MD5 , SHA1 , SHA256 

File paths: C:\Users\M S I\Documents\Codex\2026-06-29\d\work\My-Scripts\README.md

ไม่พบ IOC ที่เป็นอันตราย

พบเพียง artifact พื้นฐาน เช่น filename, path, hash

พบข้อความ marker ที่ใช้เพื่อการศึกษา

## Detection Ideas

สามารถสร้าง YARA rule ที่ตรวจหาคำว่า FOR EDUCATIONAL PURPOSES ONLY

สามารถใช้คำว่า Malware Analysis และ Cyber Security เป็น text markers

ถ้าไฟล์มีข้อความ marker อย่างน้อย 2 จุด อาจถือว่า match ตามกฎทดลองได้


