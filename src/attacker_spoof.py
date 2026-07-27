import time
import json
import hmac
import hashlib
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/data"

CLIENT_ID_SPOOF = "SENSOR_01"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Attacker_Device")
client.connect(BROKER, PORT)

print(f"[!] Kẻ tấn công bắt đầu mạo danh thiết bị: {CLIENT_ID_SPOOF}\n")

# KỊCH BẢN TC-02: Spoofing Thiếu HMAC
payload_tc02 = {
    "client_id": CLIENT_ID_SPOOF,
    "temperature": 99.0,
    "timestamp": int(time.time()),
    "signature": ""
}
print("[ATTACK TC-02] Gửi gói tin mạo danh KHÔNG có HMAC...")
client.publish(TOPIC, json.dumps(payload_tc02))
time.sleep(3)

# KỊCH BẢN TC-03: Spoofing Dùng Sai Secret Key / HMAC Giả
payload_tc03 = {
    "client_id": CLIENT_ID_SPOOF,
    "temperature": 99.0,
    "timestamp": int(time.time()),
    "signature": "a1b2c3d4e5f678901234567890abcdefa1b2c3d4e5f678901234567890abcdef"
}
print("[ATTACK TC-03] Gửi gói tin mạo danh với HMAC GIẢ...")
client.publish(TOPIC, json.dumps(payload_tc03))
time.sleep(3)

# KỊCH BẢN TC-04: Replay Attack (Gói tin hết hạn Timestamp)
old_ts = int(time.time()) - 20
old_msg = f"{CLIENT_ID_SPOOF}:28.5:{old_ts}"
valid_key = b"MySuperSecretKey123"
old_sig = hmac.new(valid_key, old_msg.encode('utf-8'), hashlib.sha256).hexdigest()

payload_tc04 = {
    "client_id": CLIENT_ID_SPOOF,
    "temperature": 28.5,
    "timestamp": old_ts,
    "signature": old_sig
}
print("[ATTACK TC-04] Gửi gói tin phát lại đã HẾT HẠN Timestamp...")
client.publish(TOPIC, json.dumps(payload_tc04))

client.disconnect()
print("\n[+] Hoàn tất thực thi các kịch bản tấn công.")