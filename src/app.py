from flask import Flask

# Tạo ứng dụng Flask
app = Flask(__name__)

# Trang chủ
@app.route("/")
def home():
    return "IoT Device Authentication API is running."

# Chạy chương trình
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
