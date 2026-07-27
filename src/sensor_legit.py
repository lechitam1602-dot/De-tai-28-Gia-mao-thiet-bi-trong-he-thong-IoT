import time
import json
import hmac
import hashlib
import os
import csv
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/data"

CLIENT_ID = "SENSOR_01"
SECRET_KEY = b"MySuperSecretKey123"  # Khóa bí mật Pre-Shared Key
DATA_FILE = os.path.join("data", "dataset_sensors.csv")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Legit_Device")
client.connect(BROKER, PORT)

print(f"[*] Cảm biến thật ({CLIENT_ID}) đang khởi động và đọc dữ liệu từ {DATA_FILE}...")

try:
    with open(DATA_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            temp = float(row["temperature"])
            timestamp = int(time.time())
            
            # Đóng gói Message theo định dạng chuẩn: "Client_ID:Temp:Timestamp"
            message = f"{CLIENT_ID}:{temp}:{timestamp}"
            
            # Tạo chữ ký mã hóa HMAC-SHA256
            signature = hmac.new(SECRET_KEY, message.encode('utf-8'), hashlib.sha256).hexdigest()
            
            payload = {
                "client_id": CLIENT_ID,
                "temperature": temp,
                "timestamp": timestamp,
                "signature": signature
            }
            
            client.publish(TOPIC, json.dumps(payload))
            print(f"[SENT - LEGIT] Payload: {payload}")
            time.sleep(5)  # Gửi định kỳ 5 giây/lần

except FileNotFoundError:
    print(f"[!] Không tìm thấy file dữ liệu {DATA_FILE}. Vui lòng kiểm tra thư mục data!")
except KeyboardInterrupt:
    print("\n[!] Dừng thiết bị cảm biến.")
    client.disconnect()