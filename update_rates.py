import requests
from datetime import datetime

url = "https://api.exchangerate-api.com/v4/latest/EGP"
response = requests.get(url).json()

rates = response["rates"]
currencies         = ["USD",     "GBP",     "EUR",     "CAD",     "AED"]
currencies_symbols = {"USD":"💲", "GBP":"£", "EUR":"€", "CAD":"🍁", "AED":"🐪"}

today_str = datetime.now().strftime("%Y-%m-%d")

readme_content = f"# EGP Exchange Rates\n\n"
readme_content += f"**Last Updated:** {today_str}\n\n"
readme_content += "| Currency | Rate (1 EGP →) | Reverse Rate (1 → X EGP) |\n"
readme_content += "|---------|----------------|------------------------|\n"

for cur in currencies:
    rate = rates.get(cur)
    if rate:
        readme_content += f"| {cur} {currencies_symbols[cur]} | {rate:.3f} | {1/rate:.3f}\n"
    else:
        readme_content += f"| {cur} {currencies_symbols[cur]} | *No data* |   |\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("README updated ✅")
