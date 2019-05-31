#!/bin/bash

# 5 minutes
TIME_MS=300000
# 10 seconds
# TIME_MS=10000

echo "Generating account details, accounts, customers, banks."
pipenv run python3 fake.py \
    --template resources/account-details.json \
    --ms $TIME_MS \
    --mps 20 \
    --topic accountdetails > accountdetails.log 2>&1

echo "Starting account transfer feed"
pipenv run python3 fake.py \
    --template resources/account-transfer.json \
    --ms $TIME_MS \
    --mps 20 \
    --topic accounttransfer > accounttransfer.log 2>&1 & 