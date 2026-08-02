<div align="center">

# 🔐 ĐỀ TÀI 28
# GIẢ MẠO THIẾT BỊ TRONG HỆ THỐNG IoT

### Device Spoofing Attack Detection in IoT using MQTT + HMAC Authentication

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

Đề tài mô phỏng một hệ thống Internet of Things (IoT) sử dụng giao thức MQTT, trong đó Server sẽ xác thực các thiết bị gửi dữ liệu nhằm phát hiện các hành vi **giả mạo Device ID**.

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

## Bước 1. Khởi động MQTT Broker

```bash
cd "C:\Users\Dell\Documents\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"

docker start mosquitto-broker
```

Nếu chưa tạo container:

```bash
docker run -d --name mosquitto-broker ^
-p 1883:1883 ^
-v "%cd%/configs/mosquitto.conf:/mosquitto/config/mosquitto.conf" ^
eclipse-mosquitto:2.0.18
```

---

## Bước 2. Bắt gói tin bằng Wireshark

- Mở Wireshark
- Chọn **Adapter for loopback traffic capture**
- Filter:

```text
mqtt
```

---

## Bước 3. Chạy Server Authenticator

```bash
python src/server_authenticator.py
```

Kết quả

```
[*] Server Authenticator đang hoạt động...
```

---

## Bước 4. Chạy Dashboard

```bash
python src/app_dashboard.py
```

Mở trình duyệt

```
http://127.0.0.1:5000
```

---

## Bước 5. Chạy cảm biến hợp lệ (TC-01)

```bash
python src/sensor_legit.py
```

Kết quả mong đợi

```
[ACCEPT]
```

Log hiển thị màu xanh.

---

## Bước 6. Chạy chương trình giả mạo (TC-02, TC-03, TC-04)

```bash
python src/attacker_spoof.py
```

Kết quả mong đợi

```
[REJECT]
[REJECT]
[REJECT]
```

Log hiển thị màu đỏ.

---

## Bước 7. Sinh báo cáo

```bash
python src/generate_report.py
```

Sinh file:

```
evaluation_report.json
```

---

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
