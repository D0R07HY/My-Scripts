# Beginner Sigma Rule Explained

ไฟล์นี้อธิบาย Sigma rule ตัวแรกของรีโปแบบภาษาคนเริ่มต้น

ไฟล์ rule คือ:

- `detections/sigma/proc_creation_win_beginner_analysis_scripts.yml`

## ตัว rule

```yaml
title: Beginner Analysis Script Execution
id: e7cb8791-96c7-4a66-91a8-11f6c1f54ff6
status: experimental
description: Detects execution of beginner-friendly local analysis scripts from this repository via python.exe
author: D0R07HY
date: 2026-06-29
references:
    - https://sigmahq.io/docs/basics/rules.html
    - https://sigmahq.io/docs/basics/log-sources.html
logsource:
    category: process_creation
    product: windows
detection:
    selection_image:
        Image|endswith: '\python.exe'
    selection_commandline:
        CommandLine|contains:
            - 'analysis\scripts\hash_report.py'
            - 'analysis\scripts\basic_strings.py'
    condition: selection_image and selection_commandline
falsepositives:
    - Expected local testing in a learning lab
level: low
```

## อธิบายทีละส่วน

### `title`

คือชื่อของกฎ

ควรตั้งให้พออ่านแล้วรู้ว่ากำลังจับอะไร

### `id`

คือรหัสประจำตัวของกฎ

Sigma นิยมใช้ UUID เพื่อให้แต่ละกฎมี id ไม่ซ้ำกัน

### `status: experimental`

แปลว่ากฎนี้ยังเป็นระดับทดลอง

เหมาะกับ rule สำหรับการเรียนรู้หรือ rule ที่ยังไม่ได้ผ่านการใช้งานจริงในหลาย environment

### `description`

คำอธิบายสั้น ๆ ว่ากฎนี้จับอะไร

ใน rule นี้ เรากำลังจับการรันสคริปต์ `hash_report.py` หรือ `basic_strings.py` ผ่าน `python.exe`

### `author`

คนเขียนกฎ

### `date`

วันที่สร้างกฎ

### `references`

ลิงก์อ้างอิง

ในที่นี้ผมใส่เอกสารทางการของ Sigma ไว้เพื่อให้คุณกลับไปอ่านต่อได้

### `logsource`

ส่วนนี้สำคัญมาก เพราะมันบอกว่าเราคาดหวังจะจับ event จาก log แบบไหน

#### `category: process_creation`

หมายถึงเรากำลังสนใจ event ประเภท "มี process ใหม่ถูกสร้าง"

พูดง่าย ๆ:

มีโปรแกรมตัวหนึ่งถูกเปิดขึ้นมา

#### `product: windows`

บอกว่ากฎนี้ออกแบบมาสำหรับ log ฝั่ง Windows

### `detection`

ส่วนนี้คือ logic หลักของ Sigma rule

### `selection_image`

เป็นกลุ่มเงื่อนไขชุดแรก

### `Image|endswith: '\python.exe'`

แปลว่า field `Image` ต้องลงท้ายด้วย `\python.exe`

พูดง่าย ๆ:

เราสนใจเฉพาะกรณีที่ process ที่ถูกรันคือ Python

### `selection_commandline`

เป็นกลุ่มเงื่อนไขชุดที่สอง

### `CommandLine|contains`

แปลว่า field `CommandLine` ต้องมีข้อความที่เราสนใจอยู่ข้างใน

ในที่นี้คือหนึ่งในสองข้อความนี้:

- `analysis\scripts\hash_report.py`
- `analysis\scripts\basic_strings.py`

พูดง่าย ๆ:

ถ้ามีการรัน Python พร้อมสั่งใช้หนึ่งในสองสคริปต์นี้ ก็จะเข้าเงื่อนไขชุดนี้

### `condition: selection_image and selection_commandline`

นี่คือเงื่อนไขสุดท้าย

แปลว่า:

ต้องตรงทั้งสองอย่างพร้อมกัน:

1. process เป็น `python.exe`
2. command line มีชื่อสคริปต์ที่เราสนใจ

ถ้าตรงแค่อย่างใดอย่างหนึ่ง ยังไม่ match

### `falsepositives`

ส่วนนี้ใช้บอกว่าอะไรที่อาจทำให้ rule แจ้งเตือน ทั้งที่จริงไม่ใช่เหตุผิดปกติ

ในที่นี้ false positive ไม่ได้แปลว่าเขียนผิด
แต่หมายถึงการ match ที่เกิดจากการใช้งานปกติในแล็บ

เช่น:

- คุณกำลังทดลองสคริปต์ด้วยตัวเอง

### `level: low`

คือระดับความรุนแรงของ alert

ใน rule นี้ตั้งเป็น `low` เพราะมันเป็นแค่การตรวจจับ activity เชิงการเรียนรู้ใน lab ไม่ใช่เหตุร้ายแรง

## สิ่งที่คุณควรได้จาก rule นี้

1. เข้าใจว่า Sigma ใช้กับ log ไม่ใช่ใช้กับเนื้อไฟล์โดยตรง
2. เข้าใจว่า `logsource` บอกว่ากำลังดู event แบบไหน
3. เข้าใจว่า `detection` คือ logic หลัก
4. เข้าใจว่า `condition` ใช้รวมหลาย selection เข้าด้วยกัน

## ถ้าจะทดลองในอนาคต

ถ้าคุณมี process creation logs จาก Windows เช่น Sysmon Event ID 1 หรือ Security 4688 ที่ถูก map แล้วเข้ากับ field มาตรฐานของ Sigma
คุณจะสามารถใช้ rule นี้แปลงไปเป็น query ของ backend ที่รองรับ Sigma ได้

## ทำไม rule นี้เหมาะกับมือใหม่

เพราะมัน:

- ปลอดภัย
- เข้าใจง่าย
- ผูกกับสคริปต์ในรีโปของคุณเอง
- เห็นภาพชัดว่า Sigma ใช้จับ "เหตุการณ์การรันโปรแกรม" ยังไง
