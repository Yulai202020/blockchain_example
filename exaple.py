import hashlib

class BlockChain:
    def __init__(self, previous_block_hash, transport_list):
        self.previous_block_hash = previous_block_hash
        self.transport_list = transport_list

        self.block_data = "-".join(transport_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigit()

