import time
import json
import hmac
import hashlib
import os
import paho.mqtt.client as mqtt

# --- ĐỌC CẤU HÌNH TỪ SECURITY_POLICY.JSON ---
POLICY_FILE = os.path.join("configs", "security_policy.json")

try:
    with open(POLICY_FILE, "r", encoding="utf-8") as f:
        policy = json.load(f)
    
    SECRET_KEY = policy["authentication"]["secret_key"].encode('utf-8')
    MAX_DELTA = policy["authentication"]["max_timestamp_delta_seconds"]
    LOG_FILE = policy["logging"]["log_file"]
    print(f"[*] Đã tải chính sách bảo mật thành công từ {POLICY_FILE}")
except Exception as e:
    print(f"[!] Lỗi tải {POLICY_FILE}, dùng cấu hình mặc định: {e}")
    SECRET_KEY = b"MySuperSecretKey123"
    MAX_DELTA = 5
    LOG_FILE = os.path.join("results", "access_audit.log")

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/data"

os.makedirs("results", exist_ok=True)

def log_event(status, client_id, temp, reason=""):
    timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp_str}] [{status}] Client: {client_id} | Temp: {temp} | Note: {reason}\n"
    print(log_line.strip())
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode('utf-8'))
        c_id = data.get("client_id")
        temp = data.get("temperature")
        ts = data.get("timestamp", 0)
        sig = data.get("signature", "")
        
        current_ts = int(time.time())
        
        # 1. KIỂM TRA TIMESTAMP DỰA TRÊN POLICY (Chống Replay Attack)
        if abs(current_ts - ts) > MAX_DELTA:
            log_event("REJECT", c_id, temp, f"Timestamp Expired (> {MAX_DELTA}s) / Replay Attack")
            return

        # 2. KIỂM TRA HMAC-SHA256 DỰA TRÊN POLICY (Chống Device Spoofing)
        expected_msg = f"{c_id}:{temp}:{ts}"
        computed_sig = hmac.new(SECRET_KEY, expected_msg.encode('utf-8'), hashlib.sha256).hexdigest()
        
        if hmac.compare_digest(computed_sig, sig):
            log_event("ACCEPT", c_id, temp, "HMAC Validated Successfully")
        else:
            log_event("REJECT", c_id, temp, "Invalid HMAC Signature / Spoofing Detected!")

    except Exception as e:
        log_event("REJECT", "UNKNOWN", 0, f"Malformed Payload: {str(e)}")

server = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="IoT_Security_Server")
server.on_message = on_message
server.connect(BROKER, PORT)
server.subscribe(TOPIC)

print("[*] Server Authenticator đang hoạt động và giám sát dữ liệu...")
server.loop_forever()