import requests
import pandas as pd
import json

def get_block_transactions(infura_url, block_number):
    """
    Fetches all transactions in a given block from the Ethereum blockchain.
    """
    try:
        block_number_hex = hex(block_number)
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBlockByNumber",
            "params": [block_number_hex, True],
            "id": 1
        }
        response = requests.post(infura_url, json=payload)

        response.raise_for_status()  
        block_data = response.json()
        if 'error' in block_data:
            print(f"Error from Infura: {block_data['error']}")
            return None

        transactions = block_data['result']['transactions']
        return transactions

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except KeyError:
        print("Error: 'result' or 'transactions' not found in the response.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON response.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def process_transactions(transactions):
    """
    Processes the transaction data to extract relevant fields and calculate totals.
    """
    processed_transactions = []
    unique_addresses = set()
    total_value = 0

    for tx in transactions:
        from_address = tx.get('from')
        to_address = tx.get('to')
        value = int(tx.get('value', '0'), 16)  # Convert hex to int, default to 0 if 'value' is missing

        if from_address:
            unique_addresses.add(from_address)

        total_value += value

        processed_transactions.append({
            'from_address': from_address,
            'to_address': to_address,
            'value': value,
        })

    df = pd.DataFrame(processed_transactions)
    unique_address_count = len(unique_addresses)

    return df, unique_address_count, total_value


def write_data(df, unique_address_count, total_value):
    """
    Writes the processed transaction data and totals to Parquet files.
    """
    try:
        df.to_parquet('transactions.parquet')
        totals_data = {
            'count_unique_addresses': [unique_address_count],
            'sum_value': [total_value],
        }
        totals_df = pd.DataFrame(totals_data)
        totals_df.to_parquet('totals.parquet')

        print("Data written to transactions.parquet and totals.parquet")

    except Exception as e:
        print(f"Error writing to Parquet files: {e}")