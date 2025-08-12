
import requests
import random
import time
import datetime
import string

BOT_TOKEN = "8389410364:AAEVhmLO9rLTJoz2RdJN3rApEcYv_cOvsZs"
CHAT_ID = "7589607982"

first_names = ["Sophia", "Liam", "Olivia", "Noah", "Emma", "Mason", "Ava", "Ethan", "Isabella", "James"]
last_names = ["Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Taylor"]
companies = ["Quantum Finance LLC", "TechNova Inc", "CyberCore Systems", "DarkNet Solutions", "RedMoon Enterprises", "Global Enterprises Ltd", "NextGen Holdings"]
statuses = ["Processing 🔄", "Awaiting Approval 🕐", "Cancelled ❌", "Approved ✅"]
countries = [("🇺🇸", "USA"), ("🇬🇧", "UK"), ("🇨🇦", "Canada"), ("🇦🇺", "Australia"), ("🇳🇬", "Nigeria")]

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_invoice_id():
    return f"INV-{random.randint(100000,999999)}"

def random_identification_number():
    return "PINV-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def generate_unique_data(count):
    results = []
    for i in range(count):
        first = random.choice(first_names)
        last = random.choice(last_names)
        company = random.choice(companies)
        status = statuses[i % len(statuses)]  # evenly rotate statuses
        flag, country = random.choice(countries)
        amount = random.randint(1000000, 50000000)
        entry = "💻🦠 Invoice Tech Extract 👹💀\n"
        entry += f"🧾 Invoice ID: {random_invoice_id()}"
        if "Awaiting Approval" in status:
            entry += f"\n🔑 Invoice Identification Number: {random_identification_number()}"
        entry += f"\n👤 Client: {first} {last}"
        entry += f"\n🏢 Company: {company}"
        entry += f"\n💰 Amount: ${amount:,}"
        entry += f"\n📦 Status: {status}"
        entry += f"\n📅 Due Date: {datetime.date.today() + datetime.timedelta(days=random.randint(1,30))}"
        entry += f"\n🌍 Country: {flag} {country}"
        entry += f"\n🌐 IP: {random_ip()}"
        entry += f"\n🕒 Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        if "Awaiting Approval" in status:
            entry += "\n⚠️ This invoice can still be updated before payment."
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
