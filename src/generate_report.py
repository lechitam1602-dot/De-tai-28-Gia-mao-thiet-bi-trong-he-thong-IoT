import json
import os

LOG_FILE = os.path.join("results", "access_audit.log")
OUT_FILE = os.path.join("results", "evaluation_report.json")

if not os.path.exists(LOG_FILE):
    print(f"[!] Không tìm thấy file log tại: {LOG_FILE}. Hãy chạy các thử nghiệm trước!")
    exit()

total = 0
accept = 0
reject = 0

with open(LOG_FILE, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            total += 1
            if "[ACCEPT]" in line:
                accept += 1
            elif "[REJECT]" in line:
                reject += 1

accuracy = (reject / (total - accept) * 100) if (total - accept) > 0 else 100.0

report_data = {
    "total_requests_processed": total,
    "accepted_legit_requests": accept,
    "rejected_spoofed_requests": reject,
    "spoofing_detection_accuracy_percent": round(accuracy, 2)
}

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(report_data, f, indent=4)

print(f"[INFO] Parsing log file: {LOG_FILE}...")
print(f"[INFO] Total requests processed: {total}")
print(f"[INFO] Valid requests (ACCEPT): {accept}")
print(f"[INFO] Rejected requests (REJECT): {reject}")
print(f"[RESULTS] Spoofing Attack Detection Rate: {accuracy}%")
print(f"[SUCCESS] Evaluation report successfully generated at {OUT_FILE}")