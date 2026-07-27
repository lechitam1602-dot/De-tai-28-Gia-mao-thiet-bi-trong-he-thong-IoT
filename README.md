**Họ và tên: Lê Chí Tâm**

**MSSV: 231A010500**



**ĐỀ TÀI 28 – GIẢ MẠO THIẾT BỊ TRONG HỆ THỐNG IOT**



**# Mục tiêu của đề tài là:**

&#x09;- Mô phỏng hệ thống IoT bằng Python.

&#x09;- Thực hiện kịch bản giả mạo thiết bị.

&#x09;- Phát hiện và từ chối các request giả mạo.

&#x09;- Lưu log và thống kê kết quả thử nghiệm.

&#x09;- Đánh giá hiệu quả giải pháp bảo mật.



**# Mô tả hệ thống:**

&#x09;				IoT Sensor

&#x09;				   |

&#x20;                                          |

&#x09;				MQTT Broker (Mosquitto)

&#x09;				   |

&#x09;				   |

&#x09;				Server Authenticator

&#x20;    					   │

&#x20;  					   ├── Kiểm tra HMAC

&#x20;  					   ├── Kiểm tra Timestamp

&#x20;					   ├── Lưu Log

&#x20; 					   └── Dashboard

1.Thiết bị hợp lệ gửi dữ liệu cảm biến đến Server.

2.Kẻ tấn công sẽ giả mạo Device ID để gửi dữ liệu giả.

3\. Server xác thực:

&#x09;- Device ID

&#x09;- HMAC

&#x09;- Timestamp

4\. Nếu hợp lệ: ACCEPT

5\. Nếu không hợp lệ: REJECT đồng thời ghi vào Audit Log.



**# Cấu trúc thư mục**



De-tai-28-Gia-mao-thiet-bi-trong-he-thong-IoT

│

├── configs/

│   ├── mosquitto.conf

│   └── security\_policy.json

│

├── data/

│   └── dataset\_sensors.csv

│

├── references/

│   └── link\_nguon.md

│

├── report/

│   ├── 231A010500\_LeChiTam\_DeTai28\_TieuLuan\_CuoiKy.docx

│   └── 231A010500\_LeChiTam\_DeTai28\_TieuLuan\_CuoiKy.pdf

│

├── results/

│   ├── screenshots/

│   ├── access\_audit.log

│   └── evaluation\_report.json

│

├── src/

│   ├── app\_dashboard.py

│   ├── attacker\_spoof.py

│   ├── generate\_report.py

│   ├── sensor\_legit.py

│   └── server\_authenticator.py

└── README.md

**# Công nghệ sử dụng**

&#x09;- Python

&#x09;- Flask

&#x09;- Eclipse Mosquitto MQTT Broker

&#x09;- Docker

&#x09;- Wireshark

**# QUY TRÌNH KIỂM THỬ HỆ THỐNG** 

1\. Khởi chạy Docker Broker

Mở 1 cửa sổ Command Prompt (CMD) và nhập:

cd "C:\\Users\\Dell\\Documents\\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"

docker start mosquitto-broker



(Nếu chưa tạo container trước đó, chạy: docker run -d --name mosquitto-broker -p 1883:1883 -v "%cd%/configs/mosquitto.conf:/mosquitto/config/mosquitto.conf" eclipse-mosquitto:2.0.18)

2\. Mở Wireshark bắt gói tin

&#x09;a) Mở phần mềm Wireshark.

&#x09;b) Nhấp đôi vào Adapter for loopback traffic capture.

&#x09;c) Tại ô tìm kiếm filter ở trên cùng, gõ mqtt rồi nhấn Enter.

3\. Mở 4 cửa sổ CMD chạy các thành phần

Hãy chia màn hình hoặc mở 4 cửa sổ CMD riêng biệt:

&#x09;• CMD 1 - Chạy Server Authenticator:

cd "C:\\Users\\Dell\\Documents\\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"

python src/server\_authenticator.py

(Màn hình hiện: \[\*] Server Authenticator đang hoạt động...)



&#x09;• CMD 2 - Chạy Flask Web Dashboard:

cd "C:\\Users\\Dell\\Documents\\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"

python src/app\_dashboard.py

(Mở trình duyệt truy cập: (http://127.0.0.1:5000)



&#x09;• CMD 3 - Chạy Cảm biến thật (TC-01):

cd "C:\\Users\\Dell\\Documents\\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"

python src/sensor\_legit.py

(Quan sát CMD 1 và Web Dashboard xuất hiện dòng log màu xanh \[ACCEPT])



&#x09;• CMD 4 - Chạy Kẻ tấn công giả mạo (TC-02, TC-03, TC-04):

cd "C:\\Users\\Dell\\Documents\\Đề tài 28 – Giả mạo thiết bị trong hệ thống IoT"

python src/attacker\_spoof.py

(Quan sát CMD 1 và Web Dashboard xuất hiện ngay 3 dòng log màu đỏ \[REJECT] do bị chặn)



4\. Sinh Báo cáo Thống kê

Mở thêm 1 CMD (hoặc ở CMD 4 sau khi chạy xong) gõ:

python src/generate\_report.py

&#x20;



