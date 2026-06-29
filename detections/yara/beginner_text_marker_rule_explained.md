# Beginner YARA Rule Explained

ไฟล์นี้อธิบาย YARA rule ตัวแรกของรีโปแบบทีละบรรทัด

ไฟล์ rule คือ:

- `detections/yara/beginner_text_marker_rule.yar`

## ตัว rule

```yara
rule Beginner_Text_Marker_Rule
{
    meta:
        author = "D0R07HY"
        description = "Beginner-friendly YARA rule that matches a simple educational text marker"
        purpose = "Learning YARA structure with a safe text-based example"

    strings:
        $marker1 = "FOR EDUCATIONAL PURPOSES ONLY"
        $marker2 = "Malware Analysis"
        $marker3 = "Cyber Security"

    condition:
        2 of ($marker*)
}
```

## อธิบายทีละบรรทัด

### `rule Beginner_Text_Marker_Rule`

บรรทัดนี้คือชื่อของ rule

มันบอกเราว่ากฎนี้ชื่ออะไร และใช้เรียกอ้างอิงกฎนี้ในภายหลัง

### `{`

เริ่มต้นขอบเขตของ rule

ทุกอย่างของกฎนี้จะอยู่ภายในวงเล็บปีกกา

### `meta:`

ส่วนนี้ใช้เก็บข้อมูลอธิบาย rule

มันไม่ได้ใช้ตัดสินว่าไฟล์ match หรือไม่ แต่ช่วยให้คนอ่านเข้าใจว่า rule นี้มีไว้ทำอะไร

### `author = "D0R07HY"`

บอกว่าใครเป็นคนเขียน rule

### `description = "Beginner-friendly YARA rule that matches a simple educational text marker"`

อธิบายสั้น ๆ ว่า rule นี้พยายามจับอะไร

### `purpose = "Learning YARA structure with a safe text-based example"`

อธิบายเป้าหมายของ rule นี้

ในที่นี้คือใช้เรียนโครงสร้าง YARA จากตัวอย่างที่ปลอดภัย

### `strings:`

ส่วนนี้คือรายการข้อความที่ YARA จะใช้ค้นหาในไฟล์

### `$marker1 = "FOR EDUCATIONAL PURPOSES ONLY"`

บอกให้ YARA มองหาข้อความนี้

`$marker1` เป็นชื่อที่เราตั้งให้ string ตัวนี้

### `$marker2 = "Malware Analysis"`

มองหาข้อความ `Malware Analysis`

### `$marker3 = "Cyber Security"`

มองหาข้อความ `Cyber Security`

### `condition:`

ส่วนนี้คือเงื่อนไขหลักของ rule

มันบอกว่าไฟล์ต้องมีคุณสมบัติแบบไหนจึงจะถือว่า match

### `2 of ($marker*)`

ประโยคนี้แปลว่า:

"ถ้าในไฟล์มีข้อความตรงกับอย่างน้อย 2 ตัว จากกลุ่ม `$marker` ให้ถือว่า match"

กลุ่ม `$marker*` ในที่นี้หมายถึง:

- `$marker1`
- `$marker2`
- `$marker3`

ดังนั้น ถ้าไฟล์มีข้อความตรงกับ 2 ใน 3 ตัวนี้ rule จะ match

## ทำไม rule นี้เหมาะกับมือใหม่

เพราะมันสอนส่วนสำคัญของ YARA ครบ:

- ชื่อ rule
- meta
- strings
- condition

และยังไม่แตะตัวอย่างที่เสี่ยงหรือซับซ้อนเกินไป

## สิ่งที่คุณควรได้จาก rule นี้

1. เข้าใจว่า YARA ใช้หาข้อความหรือ pattern ในไฟล์
2. เข้าใจว่า `strings` คือสิ่งที่เราต้องการค้นหา
3. เข้าใจว่า `condition` คือกติกาตัดสินสุดท้าย
4. เริ่มมองออกว่าการเขียน rule ไม่ได้มีไว้แค่จับ malware เท่านั้น แต่ใช้ฝึก logic ได้ด้วย

## วิธีฝึกต่อ

ลองแก้ rule นี้เอง เช่น:

- เปลี่ยน `2 of ($marker*)` เป็น `all of ($marker*)`
- เพิ่ม string ใหม่อีก 1 ตัว
- ลองใช้ข้อความจาก report template มาสร้าง rule ทดลอง
