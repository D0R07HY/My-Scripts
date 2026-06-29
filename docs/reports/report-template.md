# Analysis Report Template

## Report Information

- Report title:
- Date:
- Analyst:
- Source or reference:

## Sample Overview

- Sample name or alias:
- File name:
- File type:
- File size:
- SHA256:
- MD5:
- SHA1:

## Context

อธิบายว่าไฟล์นี้คืออะไร มาจากไหน หรือวิเคราะห์จาก public writeup ไหน

## Static Analysis Notes

จดสิ่งที่เห็นจากการวิเคราะห์แบบไม่รันไฟล์ เช่น:

- strings ที่น่าสนใจ
- ชื่อฟังก์ชันหรือ library
- path ที่พบ
- URL, domain, IP ที่เกี่ยวข้อง
- compile time ถ้าพบ

## Behavior Notes

ถ้ามีการทดลองใน lab ให้บันทึก:

- process behavior
- file activity
- registry activity
- network behavior

ถ้ายังไม่ได้ทำ dynamic analysis ให้ระบุไว้ชัดเจน

## Indicators of Compromise

- Hashes:
- File paths:
- Registry keys:
- Domains:
- IP addresses:
- Process names:

## Detection Ideas

เขียนสิ่งที่สามารถต่อยอดเป็น detection ได้ เช่น:

- strings ที่เหมาะกับ YARA
- command line pattern ที่เหมาะกับ Sigma
- process chain ที่ควร alert

## Risk and Notes

สรุปความเสี่ยง สิ่งที่ยังไม่แน่ใจ และสิ่งที่ควรศึกษาเพิ่ม

## References

- Link 1:
- Link 2:
