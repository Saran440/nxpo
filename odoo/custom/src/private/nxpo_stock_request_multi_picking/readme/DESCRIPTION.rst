This module adds the following functions:

 - เบิกสินค้าบางส่วน
    - กรณีเบิกสินค้าบางส่วนและยกเลิกส่วนที่เหลือให้ระบบเปลี่ยนสถานะเป็น Done
    - กรณีทำการ validate picking ด้วยจำนวนบางส่วน พร้อมทั้งไม่สร้าง backorder เพราะที่เหลือไม่ต้องการเบิกแล้ว ให้ระบบเปลี่ยนสถานะเป็น Done
 - ยกเลิกเบิกสินค้า
    - กรณี  cancel picking ให้ระบบ auto cancel stock request
