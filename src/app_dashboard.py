from flask import Flask, render_template_string
import os
import json

app = Flask(__name__)
LOG_FILE = os.path.join("results", "access_audit.log")
REPORT_FILE = os.path.join("results", "evaluation_report.json")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IoT Security Operations Center (SOC) - Đề tài 28</title>
    <meta http-equiv="refresh" content="3"> <!-- Tự động làm mới mỗi 3 giây -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0a0e17;
            --card-bg: #111827;
            --accent-blue: #00f2fe;
            --accept-green: #10b981;
            --reject-red: #ef4444;
            --text-main: #e5e7eb;
            --text-muted: #9ca3af;
            --border-color: #1f2937;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: var(--bg-color); color: var(--text-main); padding: 24px; line-height: 1.5; }

        /* Header */
        header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 20px; border-bottom: 1px solid var(--border-color); margin-bottom: 24px; }
        .title-group h1 { font-size: 22px; color: #fff; display: flex; align-items: center; gap: 10px; }
        .title-group h1 i { color: var(--accent-blue); }
        .title-group p { font-size: 13px; color: var(--text-muted); margin-top: 4px; }
        .status-badge { background: rgba(16, 185, 129, 0.1); border: 1px solid var(--accept-green); color: var(--accept-green); padding: 6px 16px; border-radius: 20px; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 8px; }
        .pulse { width: 8px; height: 8px; background: var(--accept-green); border-radius: 50%; box-shadow: 0 0 8px var(--accept-green); animation: pulse-animation 1.5s infinite; }

        @keyframes pulse-animation { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

        /* Stats Grid */
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 24px; }
        .stat-card { background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 10px; padding: 18px; display: flex; align-items: center; justify-content: space-between; }
        .stat-info p { font-size: 12px; color: var(--text-muted); text-transform: uppercase; font-weight: 600; }
        .stat-info h3 { font-size: 24px; margin-top: 4px; color: #fff; }
        .stat-icon { font-size: 28px; opacity: 0.8; }

        /* Log Section */
        .log-section { background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 10px; padding: 20px; }
        .log-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
        .log-header h2 { font-size: 16px; color: #fff; display: flex; align-items: center; gap: 8px; }
        .log-container { background: #050811; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px; height: 380px; overflow-y: auto; font-family: 'Consolas', 'Courier New', monospace; font-size: 13px; }
        
        .log-entry { padding: 8px 12px; margin-bottom: 6px; border-radius: 4px; border-left: 4px solid transparent; background: rgba(255, 255, 255, 0.02); display: flex; align-items: center; justify-content: space-between; }
        .log-entry.ACCEPT { border-left-color: var(--accept-green); color: #a7f3d0; }
        .log-entry.REJECT { border-left-color: var(--reject-red); color: #fca5a5; background: rgba(239, 68, 68, 0.05); }

        .tag { font-size: 11px; font-weight: bold; padding: 2px 8px; border-radius: 4px; text-transform: uppercase; }
        .tag-accept { background: rgba(16, 185, 129, 0.2); color: var(--accept-green); }
        .tag-reject { background: rgba(239, 68, 68, 0.2); color: var(--reject-red); }

        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #050811; }
        ::-webkit-scrollbar-thumb { background: #1f2937; border-radius: 3px; }
    </style>
</head>
<body>

    <header>
        <div class="title-group">
            <h1><i class="fa-solid => fa-shield-halved"></i> IoT SECURITY OPERATIONS CENTER</h1>
            <p>Đề tài 28: Giả mạo thiết bị trong hệ thống IoT | Mosquitto MQTT Broker v2.0.18 + HMAC-SHA256</p>
        </div>
        <div class="status-badge">
            <span class="pulse"></span> System Protected
        </div>
    </header>

    <!-- Thống kê tổng quan -->
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-info">
                <p>Tổng gói tin</p>
                <h3>{{ stats.total_requests_processed }}</h3>
            </div>
            <div class="stat-icon" style="color: var(--accent-blue);"><i class="fa-solid fa-server"></i></div>
        </div>
        <div class="stat-card">
            <div class="stat-info">
                <p>Hợp lệ (ACCEPT)</p>
                <h3 style="color: var(--accept-green);">{{ stats.accepted_legit_requests }}</h3>
            </div>
            <div class="stat-icon" style="color: var(--accept-green);"><i class="fa-solid fa-circle-check"></i></div>
        </div>
        <div class="stat-card">
            <div class="stat-info">
                <p>Chặn giả mạo (REJECT)</p>
                <h3 style="color: var(--reject-red);">{{ stats.rejected_spoofed_requests }}</h3>
            </div>
            <div class="stat-icon" style="color: var(--reject-red);"><i class="fa-solid fa-triangle-exclamation"></i></div>
        </div>
        <div class="stat-card">
            <div class="stat-info">
                <p>Độ chính xác chặn</p>
                <h3 style="color: var(--accent-blue);">{{ stats.spoofing_detection_accuracy_percent }}%</h3>
            </div>
            <div class="stat-icon" style="color: var(--accent-blue);"><i class="fa-solid fa-chart-line"></i></div>
        </div>
    </div>

    <!-- Danh sách Nhật ký Log -->
    <div class="log-section">
        <div class="log-header">
            <h2><i class="fa-solid fa-list-check"></i> Nhật Ký Kiểm Vết Thời Gian Thực (Audit Access Log)</h2>
            <span style="font-size: 12px; color: var(--text-muted);">Tự động cập nhật mỗi 3s</span>
        </div>
        <div class="log-container">
            {% for line in logs %}
            {% set is_accept = 'ACCEPT' in line %}
            <div class="log-entry {% if is_accept %}ACCEPT{% else %}REJECT{% endif %}">
                <span>{{ line.strip() }}</span>
                <span class="tag {% if is_accept %}tag-accept{% else %}tag-reject{% endif %}">
                    {% if is_accept %}PASSED{% else %}BLOCKED{% endif %}
                </span>
            </div>
            {% else %}
            <div style="color: var(--text-muted); text-align: center; margin-top: 150px;">Chưa có dữ liệu nhật ký. Hãy khởi chạy Server Authenticator và Cảm biến.</div>
            {% endfor %}
        </div>
    </div>

</body>
</html>
"""

@app.route('/')
def index():
    logs = []
    stats = {
        "total_requests_processed": 0,
        "accepted_legit_requests": 0,
        "rejected_spoofed_requests": 0,
        "spoofing_detection_accuracy_percent": 100.0
    }

    # Đọc file Log
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = f.readlines()[-30:] # Lấy 30 dòng mới nhất

    # Đọc file Thống kê JSON
    if os.path.exists(REPORT_FILE):
        try:
            with open(REPORT_FILE, "r", encoding="utf-8") as f:
                stats = json.load(f)
        except Exception:
            pass

    return render_template_string(HTML_TEMPLATE, logs=reversed(logs), stats=stats)

if __name__ == '__main__':
    print("[*] Dashboard Chuyên Nghiệp đang chạy tại: http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)