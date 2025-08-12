
import requests
import random
import time
import datetime

BOT_TOKEN = "8056860880:AAGm50f-X70EqgqqG0CpI5pAULcYwhYuWGQ"
CHAT_ID = "7589607982"

first_names = ["Sophia", "Liam", "Olivia", "Noah", "Emma", "Mason", "Ava", "Ethan", "Isabella", "James"]
last_names = ["Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Taylor"]
banks = ["Chase Bank", "Bank of America", "Wells Fargo", "Citibank", "HSBC", "Barclays"]
card_types = ["Visa", "MasterCard", "Amex", "Discover"]
statuses = ["Active ✅", "Unverified ⚠️", "Blocked ❌"]
countries = [("🇺🇸", "USA"), ("🇬🇧", "UK"), ("🇨🇦", "Canada"), ("🇦🇺", "Australia"), ("🇳🇬", "Nigeria")]

def random_card_number():
    return " ".join(str(random.randint(1000, 9999)) for _ in range(4))

def random_cvv():
    return str(random.randint(100, 999))

def random_expiry():
    return f"{random.randint(1,12):02d}/{random.randint(25,30)}"

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_unique_data(count):
    results = []
    for _ in range(count):
        first = random.choice(first_names)
        last = random.choice(last_names)
        bank = random.choice(banks)
        card_type = random.choice(card_types)
        status = random.choice(statuses)
        flag, country = random.choice(countries)
        entry = f"""💳🔐 Debit Card Extract 💳🔐
👤 Cardholder: {first} {last}
🏦 Bank: {bank}
💳 Card Type: {card_type}
🔢 Card Number: {random_card_number()}
🔑 CVV: {random_cvv()}
📅 Expiry Date: {random_expiry()}
📦 Status: {status}
🌍 Country: {flag} {country}
🌐 IP: {random_ip()}
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
