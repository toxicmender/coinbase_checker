#!/usr/bin/env python3

from coinbase.wallet.client import Client
import json
import creds
import datetime

current_datetime = datetime.datetime.now()
print("[+] Current Datetime: {}".format(current_datetime))
client = Client(creds.api_key, creds.api_secret)
accounts = client.get_accounts()
total_inr = 0.00
for account in accounts["data"]:
    balance = account["balance"]
    price = client.get_sell_price(currency_pair = balance["currency"]+'-INR')
    native_currency = float(str(balance["amount"])) * float(str(price["amount"]))
    print("[+] You have {0} {1} valued {2} INR at {3} per {1}".format(balance["amount"],
                                                                 balance["currency"],
                                                                 native_currency,
                                                                 price["amount"]))
    total_inr += native_currency
print("[+] Total inr worth is: {} ".format(float(total_inr)))

with open("log.csv", "a") as f:
     message = "{}, {}\n".format(current_datetime, total_inr)
     f.write(message)
