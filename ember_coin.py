import hashlib as hasher  # Importing hashlib for hashing
import datetime as date  # Importing datetime for timestamping
import json  # Importing json for data serialization
import requests  # Importing requests for HTTP requests
from flask import Flask, request  # Importing Flask and request for creating a web server

node = Flask(__name__)  # Initializing the Flask application

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        # Initializing a block with index, timestamp, data, and the hash of the previous block
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()  # Generating the hash for this block

    def hash_block(self):
        # Creating a SHA-256 hash of the block's contents
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

def create_genesis_block():
    # Creating the first block (genesis block) of the blockchain
    return Block(0, date.datetime.now(), {"proof-of-work": 1, "data": "Genesis Block"}, "0")

def next_block(last_block):
    # Generating the next block in the blockchain
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    last_proof = last_block.data["proof-of-work"] if isinstance(last_block.data, dict) else 1
    this_proof = proof_of_work(last_proof)  # Finding proof of work for the new block
    this_data = {
        "proof-of-work": this_proof,
        "data": "Hey! I'm block " + str(this_index)
    }
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

def proof_of_work(last_proof):
    # A simple proof of work algorithm
    if last_proof == 0:
        raise ValueError("Invalid last_proof value: 0")
    incrementor = last_proof + 1
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    return incrementor

@node.route("/mine", methods=["GET"])
def mine():
    # Mining a new block and adding it to the blockchain
    last_block = blockchain[-1]
    last_proof = last_block.data["proof-of-work"] if isinstance(last_block.data, dict) else 0
    proof = proof_of_work(last_proof)
    miner_address = "miner_address"  # Placeholder for miner's address
    this_nodes_transactions.append({
        "from": "network", 
        "to": miner_address, 
        "amount": 1
    })
    new_block_data = {"proof-of-work": proof, "transactions": list(this_nodes_transactions)}
    new_block_index = last_block.index + 1
    new_block_timestamp = date.datetime.now()
    last_block_hash = last_block.hash

    this_nodes_transactions[:] = []  # Clearing the transactions after mining

    mined_block = Block(new_block_index, new_block_timestamp, new_block_data, last_block_hash)
    blockchain.append(mined_block)  # Adding the new block to the blockchain
    return json.dumps({"index": new_block_index, "timestamp": str(new_block_timestamp)})

# Initializing the blockchain with the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
num_of_blocks_to_add = 20

# Adding blocks to the blockchain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print(f"Block #{block_to_add.index} has been added to the blockchain!")
    print(f"Hash: {block_to_add.hash}\n")

this_nodes_transactions = []  # Placeholder for transactions

@node.route("/blocks", methods=["GET"])
def get_blocks():
    # Returning the entire blockchain as JSON
    chain_to_send = json.dumps([{
        "index": block.index,
        "timestamp": str(block.timestamp),
        "data": block.data,
        "hash": block.hash
    } for block in blockchain])
    return chain_to_send

def find_new_chains():
    # Finding and fetching chains from peer nodes
    other_chains = []
    for node_url in peer_nodes:
        response = requests.get(f"{node_url}/blocks")
        if response.status_code == 200:
            block = json.loads(response.content)
            other_chains.append(block)
    return other_chains

def consensus():
    # Consensus algorithm to maintain the longest chain
    other_chains = find_new_chains()
    longest_chain = blockchain
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain

peer_nodes = ["http://127.0.0.1:5001", "http://127.0.0.1:5002"]  # List of peer nodes

@node.route("/txion", methods=["POST"])
def transaction():
    # Handling new transactions and appending them to the node's transaction list
    if request.method == "POST":
        new_txion = request.get_json()
        this_nodes_transactions.append(new_txion)
        print(f"New transaction\nFROM: {new_txion['from']}\nTO: {new_txion['to']}\nAMOUNT: {new_txion['amount']}")
        return "Transaction submission successful\n"

if __name__ == "__main__":
    node.run()  # Running the Flask application

