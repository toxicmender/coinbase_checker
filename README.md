# coinbase_checker
utility script to check and log coinbase balances

see `requirements.txt` for required libs.

you will need to set up an API key/secret. put these in `creds.py`. they just need read-balance privs.

to run, just run `account_checker.py`. it dumps out date/total-euro-value to a csv.

example run:  
```
$ python account_checker.py 
[+] Current Datetime: 2017-09-11 15:19:44.097024
[+] You have [REDACTED] LTC valued [REDACTED] inr at [REDACTED] per LTC
[+] You have [REDACTED] ETH valued [REDACTED] inr at [REDACTED] per ETH
[+] You have [REDACTED] BTH valued [REDACTED] inr at [REDACTED] per BTH
[+] You have [REDACTED] BTC valued [REDACTED] inr at [REDACTED] per BTC
[+] Total euro worth is: [REDACTED] 
$
```
