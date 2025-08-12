
import requests
import random
import time
import datetime

BOT_TOKEN = "8078838571:AAFtigY0zJ5GaKBw9yN6xDleMBs4McfWJ4E"
CHAT_ID = "7589607982"

first_names = ["John", "Sophia", "Michael", "Emma", "Liam", "Olivia", "Noah", "Ava", "Mason", "Isabella"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Taylor"]
loan_types = ["Personal Loan", "Auto Loan", "Mortgage Loan", "Business Loan", "Student Loan"]
statuses = ["Approved ✅", "Pending Review ⏳", "Rejected ❌", "Processing 🔄"]
banks = ["Chase", "Bank of America", "Wells Fargo", "Citibank", "PNC Bank", "Capital One"]
countries = [("🇺🇸", "USA"), ("🇬🇧", "UK"), ("🇨🇦", "Canada"), ("🇦🇺", "Australia"), ("🇳🇬", "Nigeria")]

def random_email(first, last):
    domains = ["gmail.com", "yahoo.com", "outlook.com", "icloud.com"]
    return f"{first.lower()}{random.randint(100,999)}@{random.choice(domains)}"

def generate_unique_data(count):
    results = []
    for _ in range(count):
        first = random.choice(first_names)
        last = random.choice(last_names)
        loan_type = random.choice(loan_types)
        status = random.choice(statuses)
        bank = random.choice(banks)
        flag, country = random.choice(countries)
        entry = f"""💵 Loan Application
👤 Applicant: {first} {last}
🏦 Bank: {bank}
📧 Email: {random_email(first,last)}
💳 Loan Type: {loan_type}
💰 Amount Requested: ${random.randint(2000, 50000):,}
📦 Status: {status}
🌍 Country: {flag} {country}
🕒 Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""
        if "Pending Review" in status:
            entry += "\n⚠️ This loan application can still be adjusted."
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
        time.sleep(3)  # delay between sends

if __name__ == "__main__":
    leads = generate_unique_data(2000)
    send_to_telegram(leads)
