import os
import sys
import requests
import pandas as pd
import json
from utils import get_block_transactions, process_transactions, write_data

def main():
    infura_api_key = os.environ.get("INFURA_API_KEY")
    if not infura_api_key:
        print("Error: INFURA_API_KEY environment variable not set.")
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Usage: python main.py <block_number>")
        sys.exit(1)

    try:
        block_number = int(sys.argv[1])
    except ValueError:
        print("Error: Invalid block number. Please provide an integer.")
        sys.exit(1)

    infura_url = f"https://mainnet.infura.io/v3/{infura_api_key}"

    transactions = get_block_transactions(infura_url, block_number)
    if transactions:
        processed_data, unique_address_count, total_value = process_transactions(transactions)
        write_data(processed_data, unique_address_count, total_value)
    else:
        print(f"No transactions found in block {block_number}")


if __name__ == "__main__":
    main()