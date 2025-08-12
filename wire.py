
import requests
import random
import string
import time
import datetime

BOT_TOKEN = "8056322867:AAHUOQz9EeMiDgu5YRETgamcapuOHQf2ViA"
CHAT_ID = "7589607982"

names = ["Isabella Garcia", "Liam Smith", "Olivia Johnson", "Noah Brown", "Emma Wilson", 
         "James Davis", "Sophia Miller", "Ethan Martinez", "Ava Taylor", "Mason Anderson"]
banks = ["TD Bank", "Chase Bank", "Wells Fargo", "Bank of America", "Citibank", 
         "HSBC", "Santander", "Royal Bank of Canada", "Barclays", "ANZ"]
countries = [("🇦🇺", "Australia"), ("🇺🇸", "USA"), ("🇨🇦", "Canada"), ("🇬🇧", "UK"), 
             ("🇩🇪", "Germany"), ("🇫🇷", "France"), ("🇳🇬", "Nigeria"), ("🇮🇳", "India"),
             ("🇯🇵", "Japan"), ("🇦🇪", "UAE")]
statuses = ["Completed ✅", "Pending ⏳", "Processing 🔄"]

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_device():
    devices = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Linux; Android 11)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)",
        "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X)"
    ]
    return random.choice(devices)

def generate_unique_data(count):
    results = []
    for _ in range(count):
        name = random.choice(names)
        bank = random.choice(banks)
        flag, country = random.choice(countries)
        status = random.choice(statuses)
        entry = f"""🧾 Wire Transfer ID: WIRE-{''.join(random.choices(string.ascii_uppercase + string.digits, k=10))}
👤 Account Holder: {name}
🏦 Bank: {bank}
🏛️ Account #: {random.randint(1000000000, 9999999999)}
🔢 Routing #: {random.randint(100000000, 999999999)}
💳 IBAN: US{random.randint(10,99)}{bank[:4].upper()}{random.randint(1000000000000000,9999999999999999)}
💰 Amount: ${random.randint(1000, 99999):,}.00
📦 Status: {status}
🌍 Country: {flag} {country}
🌐 IP: {random_ip()}
🖥️ Device: {random_device()}
🕒 Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""
        if "Pending" in status:
            entry += "\n⚠️ This wire can still be adjusted to another account."
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
