"""
Core Jobcoin mixer logic.
The mixer uses long polling
"""
import json
import requests
import time
import pytz
import dateutil.parser

from . import config


def sort_by_timestamp(transactions):
    transactions.sort(key=lambda date: dateutil.parser.parse(date))


def get_all_deposits(delta, source_address, deposit_address)

def is_valid_change(transactions, initial_transactions, source_address, deposit_address):
    # Naive check: if we still have the same number of transactions,
    # we can assume that the user has not initiated any new transactions.
    if len(initial_transactions) == len(transactions):
        return False
    
    # Assuming that transactions will always be a superset of initial_transactions
    delta = list(set(transactions).difference(set(initial_transactions)))
    sort_by_timestamp(delta)



def poll(source_address, deposit_address, addresses, amount):
    endpoint = "{}/{}".format(API_ADDRESS_URL, source_address)
    initial_res = requests.get(endpoint).json()
    initial_transactions = intial_res["transactions"]

    time.sleep(0.1)  # Assumption of no more than 5 transactions/second

    while True:
        # Poll for updates in the source address
        res = requests.get(endpoint).json()
        transactions = res["transactions"]
