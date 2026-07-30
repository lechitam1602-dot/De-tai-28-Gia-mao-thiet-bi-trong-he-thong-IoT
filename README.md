<div align="center">

### Đề tài 28 - Giả mạo thiết bị trong hệ thống IoT

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker\&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-Mosquitto-green)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?logo=flask)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

# 📖 Mục lục

* [Giới thiệu](#-giới-thiệu)
* [Mục tiêu](#-mục-tiêu)
* [Chức năng](#-chức-năng)
* [Kiến trúc hệ thống](#-kiến-trúc-hệ-thống)
* [Công nghệ sử dụng](#-công-nghệ-sử-dụng)
* [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
* [Cài đặt](#-cài-đặt)
* [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
* [Kịch bản kiểm thử](#-kịch-bản-kiểm-thử)
* [Kết quả](#-kết-quả)
* [Hướng phát triển](#-hướng-phát-triển)
* [Tài liệu tham khảo](#-tài-liệu-tham-khảo)
* [Tác giả](#-tác-giả)

---

# 📖 Giới thiệu

Internet of Things (IoT) đang được ứng dụng rộng rãi trong nhiều lĩnh vực như nhà thông minh, công nghiệp, y tế và giao thông. Tuy nhiên, cùng với sự phát triển đó là nhiều nguy cơ mất an toàn thông tin, trong đó **Device Spoofing (Giả mạo thiết bị)** là một hình thức tấn công phổ biến.

Dự án xây dựng một môi trường Lab mô phỏng hệ thống IoT sử dụng giao thức MQTT, triển khai thiết bị hợp lệ và thiết bị giả mạo, đồng thời áp dụng cơ chế xác thực **HMAC-SHA256 kết hợp Timestamp** để phát hiện và ngăn chặn các cuộc tấn công giả mạo thiết bị.

---

# 🎯 Mục tiêu

* Nghiên cứu kiến trúc hệ thống IoT.
* Tìm hiểu giao thức MQTT.
* Phân tích tấn công Device Spoofing.
* Xây dựng môi trường Lab mô phỏng.
* Triển khai MQTT Broker bằng Docker.
* Mô phỏng thiết bị IoT hợp lệ.
* Mô phỏng thiết bị giả mạo.
* Triển khai xác thực HMAC-SHA256.
* Chống Replay Attack bằng Timestamp.
* Ghi nhận Audit Log.
* Xây dựng Dashboard giám sát.
* Đánh giá hiệu quả giải pháp.

---

# ✨ Chức năng

## Thiết bị hợp lệ

* Gửi dữ liệu cảm biến.
* Sinh chữ ký HMAC.
* Gửi Timestamp.
* Publish dữ liệu lên MQTT Broker.

### Thiết bị giả mạo

* Gửi dữ liệu không có HMAC.
* Gửi HMAC sai.
* Giả mạo Client ID.
* Replay Attack.
* Gửi dữ liệu giả.

### Authentication Server

* Xác thực Client ID.
* Kiểm tra Timestamp.
* Kiểm tra HMAC.
* Chấp nhận dữ liệu hợp lệ.
* Từ chối thiết bị giả mạo.
* Ghi Audit Log.

### Dashboard

* Hiển thị dữ liệu cảm biến.
* Hiển thị trạng thái ACCEPT/REJECT.
* Theo dõi thiết bị đang hoạt động.
* Hiển thị cảnh báo khi phát hiện tấn công.

---

# 🏗 Kiến trúc hệ thống

```text
                Legitimate Sensor
                        │
                        ▼
                 MQTT Broker
                        │
                        ▼
            Authentication Server
             (HMAC + Timestamp)
              │              │
              ▼              ▼
       Flask Dashboard   Audit Log
              ▲
              │
       Fake Device (Attacker)
```

---

# 🛠 Công nghệ sử dụng

| Công nghệ         | Mục đích               |
| ----------------- | ---------------------- |
| Python 3.11       | Ngôn ngữ lập trình     |
| Flask             | Dashboard              |
| Docker            | Triển khai MQTT Broker |
| Docker Compose    | Quản lý container      |
| Eclipse Mosquitto | MQTT Broker            |
| Paho MQTT         | MQTT Client            |
| HMAC-SHA256       | Xác thực dữ liệu       |
| JSON              | Lưu báo cáo            |
| Wireshark         | Phân tích gói tin      |

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
├── report/
│   ├── BaoCao.docx
│   └── BaoCao.pdf
│
├── results/
│   ├── access_audit.log
│   └── evaluation_report.json
│
├── src/
│   ├── sensor_legit.py
│   ├── attacker_spoof.py
│   ├── server_authenticator.py
│   ├── app_dashboard.py
│   └── generate_report.py
└── README.md
```

---

# ⚙ Cài đặt

Clone dự án

```bash
git clone https://github.com/lechitam1602-dot/De-tai-28-Gia-mao-thiet-bi-trong-he-thong-IoT.git
```

Di chuyển vào thư mục

```bash
cd De-tai-28-Gia-mao-thiet-bi-trong-he-thong-IoT
```

Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

# ▶ Hướng dẫn sử dụng

Khởi động MQTT Broker

```bash
docker compose up -d
```

Chạy Authentication Server

```bash
python src/server_authenticator.py
```

Chạy Dashboard

```bash
python src/app_dashboard.py
```

Truy cập Dashboard

```
http://127.0.0.1:5000
```

Chạy thiết bị hợp lệ

```bash
python src/sensor_legit.py
```

Chạy thiết bị giả mạo

```bash
python src/attacker_spoof.py
```

Sinh báo cáo

```bash
python src/generate_report.py
```

---

# 🧪 Kịch bản kiểm thử

| Test Case | Mô tả             | Kết quả mong đợi |
| --------- | ----------------- | ---------------- |
| TC-01     | Thiết bị hợp lệ   | ACCEPT           |
| TC-02     | Thiếu HMAC        | REJECT           |
| TC-03     | HMAC không hợp lệ | REJECT           |
| TC-04     | Replay Attack     | REJECT           |

---

# 📊 Kết quả

* Hoàn thành môi trường Lab IoT.
* Triển khai thành công MQTT Broker bằng Docker.
* Mô phỏng thiết bị hợp lệ và thiết bị giả mạo.
* Phát hiện hiệu quả Device Spoofing.
* Ngăn chặn Replay Attack bằng Timestamp.
* Xác thực dữ liệu bằng HMAC-SHA256.
* Ghi nhận đầy đủ Audit Log.
* Dashboard theo dõi trạng thái thiết bị.
* Sinh báo cáo đánh giá dưới định dạng JSON.

---

# 🚀 Hướng phát triển

* Triển khai trên ESP32 hoặc Raspberry Pi.
* Áp dụng TLS hoặc Mutual TLS.
* Quản lý khóa bằng PKI.
* Tích hợp cơ sở dữ liệu MySQL hoặc PostgreSQL.
* Kết nối hệ thống SIEM.
* Tích hợp IDS/IPS.
* Hỗ trợ nhiều MQTT Broker.
* Mở rộng Dashboard với biểu đồ thời gian thực.

---

# 📚 Tài liệu tham khảo

1. William Stallings, *Cryptography and Network Security: Principles and Practice*, Pearson.
2. Arshdeep Bahga & Vijay Madisetti, *Internet of Things: A Hands-On Approach*.
3. Adam Shostack, *Threat Modeling: Designing for Security*.
4. Eclipse Mosquitto Documentation.
5. Eclipse Paho MQTT Documentation.
6. Docker Documentation.
7. Python Documentation.
8. OWASP Internet of Things Project.

---

# 👨‍💻 Tác giả

**Lê Chí Tâm**

* **MSSV:** 231A010500
* **Trường:** Đại học Văn Hiến
* **Khoa:** Công nghệ Thông tin
* **Ngành:** An toàn thông tin

---

<div align="center">

</div>
