# Coinbase Wallet Checker
A python3 utility script to check and log coinbase balances.
It utilises the [coinbase API](https://developers.coinbase.com/api/v2) through coinbase [python client module](https://github.com/coinbase/coinbase-python)


## Dependencies
Check `requirements.txt` for required python modules.

## Setup
Clone the repository using git:
- Over `HTTPS`
```sh
git clone "https://github.com/toxicmender/coinbase_checker.git"
```
- Over `SSH`
```sh
git clone "git@github.com:toxicmender/coinbase_checker.git"
```

## Configuration
You will need to set up an API key/secret on [Coinbase](https://www.coinbase.com/signin) settings->API.
Put these in `creds.py`. They just need read-balance privs.

## Usage
Just execute `account_checker.py`. it dumps out date/total-inr to a csv.

example run:  
```sh
$ python3 account_checker.py 
[+] Current Datetime: 2017-09-11 15:19:44.097024
[+] You have [REDACTED] LTC valued [REDACTED] inr at [REDACTED] per LTC
[+] You have [REDACTED] ETH valued [REDACTED] inr at [REDACTED] per ETH
[+] You have [REDACTED] BTH valued [REDACTED] inr at [REDACTED] per BTH
[+] You have [REDACTED] BTC valued [REDACTED] inr at [REDACTED] per BTC
[+] Total inr worth is: [REDACTED] 

```

## Getting involved
1. Fork the repository on Github.
2. Clone your fork on your machine.
3. checkout into a new branch.
4. work on the repository.
5. stage, commit & review the changes made.
6. merge the branch to master (with --no-ff flag).
7. push changes & create a [pull request]().
8. Then graefully wait for a response & then accomodate them as best as you can.

## Getting Help
For API key/secret contact coinbase support/help-desk.
For the python program, file an issue on [Github](https://github.com/toxicmender/Scratches/issues).
But please search & check if the issue wasn't already reported by someone else.

## References
[Coinbase Wallet API Docs](https://developers.coinbase.com/api/v2?python#)
[Coinbase API python client module](https://github.com/coinbase/coinbase-python)
