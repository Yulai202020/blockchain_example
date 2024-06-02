import hashlib

NONCE_LIMIT = 10000000000
zeros = 6

def main(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number)+ transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith("0" * zeros):
            return hash_try
    
    return -1

block_number = 24
transactions = "76123fcc2142"
previous_hash = "87de8756b967c87"

combined_text = str(block_number) + transactions + previous_hash + str(107617)

print(main(block_number, transactions, previous_hash))