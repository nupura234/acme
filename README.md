## Acme Wallet

### Description
* A system that allows a user to signup for an automatically scaling wallet
service (called "Acme Wallet") that'll give them $ 1,000 on signup.
* This service will
allow the user to use their wallet username/password on any app or website that
integrates with Acme Wallet to verify their Acme Wallet balance.
  
### Dependencies
- install flask
- install python3

### Run
- python3 app.py

### Postman
- /GET
  - url : http://192.168.0.105:8080/userdetails
    - Authorization : Bearer Token ( Use token from `valid_tokens` in app.py)