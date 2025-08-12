
import requests
import random
import string
import time
import datetime

BOT_TOKEN = "8421919502:AAF3gBDJ28mrV1nmQOhWZe6biuRUiDyaqhE"
CHAT_ID = "7589607982"

first_names = ["Michael", "Emily", "Daniel", "Sarah", "David", "Jessica", "Matthew", "Ashley", "Christopher", "Amanda"]
last_names = ["Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez"]
states = ["California", "Texas", "Florida", "New York", "Illinois", "Pennsylvania", "Ohio", "Georgia", "North Carolina", "Michigan"]
statuses = ["Active ✅", "Pending ⏳", "Verified 🗸", "Unverified ⚠️"]

def random_phone():
    return f"+1-{random.randint(200,999)}-{random.randint(200,999)}-{random.randint(1000,9999)}"

def random_email(first, last):
    domains = ["gmail.com", "yahoo.com", "outlook.com", "icloud.com", "aol.com"]
    return f"{first.lower()}.{last.lower()}{random.randint(10,99)}@{random.choice(domains)}"

def generate_unique_data(count):
    results = []
    for _ in range(count):
        first = random.choice(first_names)
        last = random.choice(last_names)
        state = random.choice(states)
        status = random.choice(statuses)
        entry = f"""🗽 USA Lead Record
👤 Full Name: {first} {last}
📧 Email: {random_email(first,last)}
📞 Phone: {random_phone()}
🏠 Address: {random.randint(100,9999)} {last} Street, {state}
🌎 State: {state}
📦 Status: {status}
🕒 Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""
        results.append(entry)
    return results

def send_to_telegram(data):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    for item in data:
        payload = {"chat_id": CHAT_ID, "text": item}
        try:
            requests.post(url, data=payload)
        except Exception as e:
            print("Error:", e)
        time.sleep(3)

if __name__ == "__main__":
    leads = generate_unique_data(2000)
    send_to_telegram(leads)
