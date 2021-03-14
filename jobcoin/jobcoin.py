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
from typing import List


# def sort_by_timestamp(transactions):
#     transactions.sort(key=lambda date: dateutil.parser.parse(date))

class Mixer:
    # Ideally this would be stored in a full-fledged wallet
    house_address = "house_address"

    def __init__(self):
        self.deposit_addresses = set()

    def mix(self):


def get_delta(transactions, initial_transactions, deposit_address) -> List:
    """ 
    Gets the change in transactions between polling periods
    and filters for transactions to the deposit address.
    """
    # Naive check: if we still have the same number of transactions,
    # we can assume that the user has not initiated any new transactions.
    if len(initial_transactions) == len(transactions):
        return []
    
    # Assuming that transactions will always be a superset of initial_transactions
    unfiltered_delta = initial_transactions[len(transactions):]

    # Filter out transactions that are not related to the mixer
    delta = []
    for transaction in unfiltered_delta:
        if transaction["toAddress"] != deposit_address:
            continue

        delta.append(transaction)

    return delta


def poll(source_address, deposit_address, addresses, amount):
    endpoint = "{}/{}".format(API_ADDRESS_URL, source_address)
    initial_res = requests.get(endpoint).json()
    initial_transactions = intial_res["transactions"]

    time.sleep(0.1)  # Assumption of no more than an average of 10 transactions/second

    try:
        while True:
            # Poll for updates in the source address
            res = requests.get(endpoint).json()
            transactions = res["transactions"]

            delta = get_delta(transactions, initial_transactions, deposit_address)

            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
