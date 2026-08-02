<div align="center">

# 🔐 ĐỀ TÀI 28
# GIẢ MẠO THIẾT BỊ TRONG HỆ THỐNG IoT


![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Dashboard-black?logo=flask)
![MQTT](https://img.shields.io/badge/MQTT-Mosquitto-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![Wireshark](https://img.shields.io/badge/Wireshark-Network%20Analysis-blue?logo=wireshark)
![License](https://img.shields.io/badge/Status-Educational-success)

---

**Sinh viên:** Lê Chí Tâm

**MSSV:** 231A010500

</div>

---

# 📖 Giới thiệu

  Trong các hệ thống Internet of Things (IoT) hiện đại như nhà thông minh (Smart Home), nông nghiệp thông minh và giám sát công nghiệp, các thiết bị đầu cuối (cảm biến, actuator) liên tục thu thập và gửi dữ liệu về trung tâm xử lý qua các giao thức như MQTT, HTTP hoặc CoAP. Tuy nhiên, do hạn chế về tài năng phần cứng và chi phí sản xuất, nhiều thiết bị IoT không được trang bị các cơ chế xác thực nguồn gốc đủ mạnh.
  Tấn công Giả mạo thiết bị (Device Spoofing) xảy ra khi kẻ tấn công đánh cắp hoặc mạo danh các thông số định danh của thiết bị hợp lệ (như địa chỉ MAC, IP, Client ID, hoặc API Key) để gửi dữ liệu giả mạo hoặc thực hiện các lệnh điều khiển trái phép. Hậu quả của dạng tấn công này vô cùng nghiêm trọng, có thể dẫn đến việc sai lệch dữ liệu giám sát, kích hoạt các kịch bản điều khiển sai mục đích hoặc gây mất an toàn cho toàn bộ hạ tầng. Do đó, việc nghiên cứu cơ chế tấn công giả mạo thiết bị IoT, đồng thời xây dựng giải pháp phòng chống và giám sát thời gian thực là vô cùng cần thiết.

Hệ thống áp dụng cơ chế:

- 🔑 HMAC Authentication
- ⏰ Timestamp Validation
- 📋 Audit Log
- 📊 Dashboard theo dõi kết quả
- 🚫 Từ chối các request giả mạo

---

# 🎯 Mục tiêu

- ✅ Mô phỏng hệ thống IoT bằng Python
- ✅ Thực hiện kịch bản giả mạo thiết bị
- ✅ Phát hiện và từ chối request giả mạo
- ✅ Ghi Audit Log
- ✅ Sinh báo cáo thống kê
- ✅ Đánh giá hiệu quả giải pháp bảo mật

---

# 🏗️ Kiến trúc hệ thống

```text
             IoT Sensor
                 │
                 │
        MQTT Broker (Mosquitto)
                 │
                 │
      Server Authenticator
       ├── Kiểm tra Device ID
       ├── Kiểm tra HMAC
       ├── Kiểm tra Timestamp
       ├── Audit Log
       └── Dashboard
```

---

# 🔄 Quy trình hoạt động

### Thiết bị hợp lệ

```
Sensor
   │
   ▼
MQTT Broker
   │
   ▼
Authenticator
   │
   ├── Device ID ✔
   ├── HMAC ✔
   ├── Timestamp ✔
   ▼
 ACCEPT
```

---

### Thiết bị giả mạo

```
Attacker
   │
   ▼
MQTT Broker
   │
   ▼
Authenticator
   │
   ├── Device ID ✖
   ├── HMAC ✖
   ├── Timestamp ✖
   ▼
 REJECT
```

---

# 📂 Cấu trúc thư mục

```text
De-tai-28-Gia-mao-thiet-bi-trong-he-thong-IoT
│
├── configs/
│   ├── mosquitto.conf
│   └── security_policy.json
│
├── data/
│   └── dataset_sensors.csv
│
├── references/
│   └── link_nguon.md
│
├── report/
│   ├── 231A010500_LeChiTam_DeTai28_TieuLuan_CuoiKy.docx
│   └── 231A010500_LeChiTam_DeTai28_TieuLuan_CuoiKy.pdf
│
├── results/
│   ├── screenshots/
│   ├── access_audit.log
│   └── evaluation_report.json
│
├── src/
│   ├── app_dashboard.py
│   ├── attacker_spoof.py
│   ├── generate_report.py
│   ├── sensor_legit.py
│   └── server_authenticator.py
│
└── README.md
```

---

# 🛠 Công nghệ sử dụng

| Công nghệ | Vai trò |
|-----------|----------|
| Python | Xây dựng toàn bộ hệ thống |
| Flask | Dashboard Web |
| Eclipse Mosquitto | MQTT Broker |
| Docker | Chạy Broker |
| Wireshark | Phân tích gói tin |
| MQTT | Truyền dữ liệu IoT |

---

# 🚀 Hướng dẫn chạy Demo

---

# 1. Chuẩn bị môi trường

Máy tính cần cài đặt các phần mềm sau:

| Phần mềm | Phiên bản khuyến nghị |
|----------|-----------------------|
| Python | 3.10 trở lên |
| Docker Desktop | Mới nhất |
| Wireshark | Mới nhất |
| Google Chrome hoặc Edge | Bất kỳ |
| Visual Studio Code (khuyến nghị) | Mới nhất |

Sau khi cài xong hãy khởi động lại máy tính.

---

# 2. Tải mã nguồn

Clone repository

```bash
git clone https://github.com/lechitam1602-dot/De-tai-28-Gia-mao-thiet-bi-trong-he-thong-IoT.git
```

Hoặc tải file ZIP từ GitHub rồi giải nén.

Sau khi giải nén sẽ có thư mục

```
De-tai-28-Gia-mao-thiet-bi-trong-he-thong-IoT
```

---

# 3. Mở Command Prompt

Nhấn

```
Windows + R
```

gõ

```
cmd
```

rồi nhấn Enter.

---

# 4. Di chuyển tới thư mục dự án

Ví dụ dự án được lưu tại

```
C:\Users\Dell\Documents\
```

gõ

```bash
cd "C:\Users\Dell\Documents\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"
```

Muốn kiểm tra đã vào đúng thư mục chưa

```bash
dir
```

Nếu thấy các thư mục

```
configs
src
results
README.md
```

thì là đúng.

---

# 5. Cài đặt thư viện Python


Trong CMD nhập

```bash
pip install flask
```

Tiếp tục

```bash
pip install paho-mqtt
```

Nếu dùng Python Launcher

```bash
py -m pip install flask
py -m pip install paho-mqtt
```

Kiểm tra Python

```bash
python --version
```

Ví dụ

```
Python 3.12.2
```

---

# 6. Kiểm tra Docker

Mở Docker Desktop.

Đợi đến khi xuất hiện

```
Docker Desktop is running
```

Kiểm tra bằng CMD

```bash
docker --version
```

Ví dụ

```
Docker version 28.x
```

---

# 7. Tạo MQTT Broker (chỉ lần đầu)

Nếu chưa từng tạo Broker hãy chạy

```bash
docker run -d ^ --name mosquitto-broker ^ -p 1883:1883 ^ -v "%cd%/configs/mosquitto.conf:/mosquitto/config/mosquitto.conf" ^ eclipse-mosquitto:2.0.18
```

Đợi vài giây.

Kiểm tra

```bash
docker ps
```

Nếu thấy

```
mosquitto-broker
```

là thành công.

---

# 8. Khởi động MQTT Broker

Nếu Broker đã tạo từ trước thì chỉ cần

```bash
docker start mosquitto-broker
```

Kiểm tra

```bash
docker ps
```

Phải thấy

```
STATUS Up
```

---

# 9. Mở Wireshark

Mở Wireshark.

Chọn

```
Adapter for loopback traffic capture
```

hoặc

```
Npcap Loopback Adapter
```

Nhấp đôi để bắt gói tin.

Tại ô Filter nhập

```
mqtt
```

rồi nhấn Enter.

Giữ nguyên cửa sổ Wireshark.

---

# 10. Mở 4 cửa sổ CMD

Mở tổng cộng **4 cửa sổ Command Prompt**.

---

# CMD số 1

Di chuyển tới thư mục dự án

```bash
cd "C:\Users\Dell\Documents\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"
```

Chạy

```bash
python src/server_authenticator.py
```

Nếu thành công sẽ thấy

```
[*] Server Authenticator đang hoạt động...
```

Không đóng cửa sổ này.

---

# CMD số 2

Di chuyển tới thư mục dự án

```bash
cd "C:\Users\Dell\Documents\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"
```

Chạy

```bash
python src/app_dashboard.py
```

Màn hình hiện

```
Running on http://127.0.0.1:5000
```

Mở trình duyệt

```
http://127.0.0.1:5000
```

Giữ nguyên Dashboard.

---

# CMD số 3

Di chuyển tới thư mục dự án

```bash
cd "C:\Users\Dell\Documents\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"
```

Chạy

```bash
python src/sensor_legit.py
```

Kết quả mong đợi

Server hiển thị

```
ACCEPT
```

Dashboard xuất hiện dòng log màu xanh.

Wireshark xuất hiện các gói MQTT.

---

# CMD số 4

Di chuyển tới thư mục dự án

```bash
cd "C:\Users\Dell\Documents\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"
```

Chạy

```bash
python src/attacker_spoof.py
```

Kết quả

Server sẽ hiện

```
REJECT
REJECT
REJECT
```

Dashboard hiển thị log màu đỏ.

Audit Log được ghi lại.

---

# 11. Sinh báo cáo

Mở CMD mới hoặc dùng lại CMD số 4.

Nhập

```bash
python src/generate_report.py
```

Sau khi hoàn thành sẽ sinh file

```
results/evaluation_report.json
```

---

# 12. Kiểm tra kết quả

Mở thư mục

```
results
```

Kiểm tra các file

```
access_audit.log

evaluation_report.json

screenshots/
```

Nếu các file được tạo thành công nghĩa là hệ thống hoạt động đúng.

---

# Kết quả mong đợi

| Thành phần | Kết quả |
|------------|----------|
| MQTT Broker | Đang chạy |
| Dashboard | Truy cập được |
| Sensor hợp lệ | ACCEPT |
| Thiết bị giả mạo | REJECT |
| Audit Log | Được ghi |
| evaluation_report.json | Được tạo |
| Wireshark | Hiển thị gói MQTT |

---

# Dừng hệ thống

Đóng tất cả cửa sổ CMD.

Dừng Docker

```bash
docker stop mosquitto-broker
```

Nếu muốn xóa Broker

```bash
docker rm mosquitto-broker
```

---

# Một số lỗi thường gặp

## Lỗi

```
python is not recognized
```

**Cách khắc phục**

Cài đặt Python và tích chọn **Add Python to PATH**.

---

## Lỗi

```
docker is not recognized
```

**Cách khắc phục**

Cài Docker Desktop và khởi động lại máy.

---

## Lỗi

```
Connection Refused
```

**Nguyên nhân**

Broker MQTT chưa chạy.

**Khắc phục**

```bash
docker start mosquitto-broker
```

---

## Lỗi

```
No module named flask
```

**Khắc phục**

```bash
pip install flask
```

---

## Lỗi

```
No module named paho
```

**Khắc phục**

```bash
pip install paho-mqtt
```

---

## Lỗi Dashboard không mở được

Kiểm tra chương trình

```
app_dashboard.py
```

đã chạy hay chưa.

Sau đó truy cập lại

```
http://127.0.0.1:5000
```

# 📊 Kết quả mong đợi

| Kiểm thử | Kết quả |
|----------|----------|
| Sensor hợp lệ | ✅ ACCEPT |
| Sai Device ID | ❌ REJECT |
| Sai HMAC      | ❌ REJECT |
| Timestamp hết hạn | ❌ REJECT |
| Audit Log | ✅ Ghi đầy đủ |
| Dashboard | ✅ Hiển thị thời gian thực |

---

# 📁 Kết quả đầu ra

```
results/
├── access_audit.log
├── evaluation_report.json
└── screenshots/
```

---

# 🔒 Giải pháp bảo mật

Hệ thống sử dụng nhiều lớp bảo vệ:

- Xác thực Device ID
- Kiểm tra HMAC
- Kiểm tra Timestamp
- Ghi Audit Log
- Dashboard giám sát
- Phát hiện hành vi giả mạo

---

# 📚 Tài liệu tham khảo

Các tài liệu được lưu tại

```
references/link_nguon.md
```

---

# 👨‍🎓 Thông tin sinh viên

| Nội dung  | Thông tin |
|---------- |-----------|
| Họ và tên | Lê Chí Tâm|
| MSSV      | 231A010500|
| Đề tài    | Giả mạo thiết bị trong hệ thống IoT |
| Ngôn ngữ  | Python |
| Framework | Flask |
| Broker    | Eclipse Mosquitto |

---

<div align="center">


</div>
