Ember Coin Blockchain Tutorial
Hey there! Follow these steps to run, mine, and perform transactions with the provided code.

Prerequisites:
Before you begin, make sure you have the following installed:

Python 3.7+: You can download Python from here.
Flask: To install Flask, run:
bash
Copy code
pip install Flask
Requests: You can install this by running:
bash
Copy code
pip install requests
Running the Blockchain
Clone the repository: First, clone the repository to your local machine using Git:

bash
Copy code
git clone https://github.com/<Your-Username>/<Repository-Name>.git
Navigate to the project folder:

bash
Copy code
cd <Repository-Name>
Start the blockchain: Run the Python file that contains the blockchain code. For example, if your main file is ember_coin.py, run:

bash
Copy code
python ember_coin.py
Access the blockchain: Once the program is running, you can interact with the blockchain through the following endpoints:

Mine a new block: Navigate to:

bash
Copy code
curl "localhost:5000/mine"
This will mine a new block, append it to the blockchain, and reward the miner.

View all blocks: View the current state of the blockchain by visiting:

bash
Copy code
curl "localhost:5000/blocks"
Make a transaction: You can submit a transaction by using the /txion endpoint:

bash
Copy code
curl -X POST "localhost:5000/txion" \
-H "Content-Type: application/json" \
-d '{
      "from": "71238uqirbfh894-random-public-key-a-alkjdflakjfewn204ij",
      "to": "93j4ivnqiopvh43-random-public-key-b-qjrgvnoeirbnferinfo",
      "amount": 3
    }'
Peer-to-Peer Networking
The blockchain code also includes peer nodes where you can connect to other blockchain nodes to share and validate blocks. By default, the peer nodes are:

http://127.0.0.1:5001
http://127.0.0.1:5002
You can change the peer node URLs in the code under the peer_nodes variable.

Security of Transactions
Your JSON file does not contain actual public/private keys but instead random strings representing addresses. This is a simulated environment. You can replace these with actual keys if you want a more realistic blockchain implementation.

Further Development
Feel free to fork this project, add your own features, or scale it for production use.
