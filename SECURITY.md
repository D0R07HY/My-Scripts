# Security Policy

## จุดประสงค์

รีโปนี้ถูกดูแลเพื่อใช้ในการศึกษา งานวิจัยเชิงป้องกัน การฝึก Malware Analysis และการเก็บแบบฝึกเขียนโค้ดทั่วไปในขอบเขตที่ปลอดภัย

รีโปนี้ต้องไม่ถูกใช้เพื่อแจกจ่าย live malware, สนับสนุนการเข้าถึงโดยไม่ได้รับอนุญาต, สนับสนุน persistence หรือ evasion, หรือสร้างความเสียหายกับระบบจริง

## เนื้อหาที่รองรับ

- บันทึกการวิเคราะห์
- กฎ YARA
- กฎ Sigma
- เอกสาร IOC
- benign simulators
- utility scripts ที่ปลอดภัย
- เอกสารการตั้ง isolated lab
- แบบฝึก Java และ Python ทั่วไป

## เนื้อหาที่ไม่ควรถูก commit

- live malware samples
- droppers หรือ loaders
- โค้ด ransomware, wiper, worm, หรือ botnet
- โค้ดขโมยข้อมูลรับรองหรือ data exfiltration
- persistence, stealth, หรือ defense evasion features
- exploit chaining ที่มุ่งใช้โจมตีระบบจริง
- archive ที่ใส่รหัสผ่านและมีเนื้อหาอันตราย
- compiled suspicious binaries

## การรายงานปัญหา

หากพบว่าเนื้อหาในรีโปนี้ไม่ปลอดภัย หลุดขอบเขต หรือเสี่ยงต่อการถูกนำไปใช้ผิดวัตถุประสงค์ กรุณาแจ้ง maintainer โดยตรงหรือใช้ private reporting channel ของ GitHub หากเปิดใช้งานไว้

## แนวทางการใช้งาน

ผู้ร่วมพัฒนาและผู้ใช้งานควร:

- ทำงานเฉพาะใน isolated lab
- หลีกเลี่ยงการทดสอบบนระบบที่ไม่ได้รับอนุญาต
- ไม่อัปโหลด malicious artifact จริงเข้ามาในรีโปนี้
- ให้ความสำคัญกับ hash, screenshot, IOC, และรายงานเชิงข้อความ มากกว่าการปล่อย binary
- ปฏิบัติตามกฎหมายและนโยบายของแพลตฟอร์ม
