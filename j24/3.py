import tkinter as tk
from tkinter import ttk
import requests


def get_crypto_price(crypto, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    return data[crypto][currency]


def convert():
    crypto = crypto_var.get().lower()
    currency = currency_var.get().lower()
    amount = float(amount_var.get())

    price = get_crypto_price(crypto, currency)
    result = amount * price
    result_label.config(text=f"{amount} {crypto} = {result:.2f} {currency}")


# Set up the main window
root = tk.Tk()
root.title("Cryptocurrency Converter")

# Variables
crypto_var = tk.StringVar()
currency_var = tk.StringVar()
amount_var = tk.StringVar()

# Labels and Entry Widgets
ttk.Label(root, text="Cryptocurrency (e.g. bitcoin):").grid(
    column=0, row=0, padx=10, pady=10
)
crypto_entry = ttk.Entry(root, textvariable=crypto_var).grid(column=1, row=0)

ttk.Label(root, text="Currency (e.g. usd):").grid(column=0, row=1, padx=10, pady=10)
currency_entry = ttk.Entry(root, textvariable=currency_var).grid(column=1, row=1)

ttk.Label(root, text="Amount:").grid(column=0, row=2, padx=10, pady=10)
amount_entry = ttk.Entry(root, textvariable=amount_var).grid(column=1, row=2)

# Convert Button
convert_button = ttk.Button(root, text="Convert", command=convert).grid(
    column=0, row=3, columnspan=2, pady=10
)

# Result Label
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=4, columnspan=2, pady=10)

root.mainloop()
