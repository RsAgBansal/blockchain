from flask import Flask, request, jsonify, send_from_directory
from algosdk import account, mnemonic
from algosdk.transaction import ApplicationNoOpTxn
from algosdk.v2client import algod
import os
from dotenv import load_dotenv
from deploy_contract import deploy_survey_contract

load_dotenv()

app = Flask(__name__, static_url_path='', static_folder='static')

# Initialize Algorand client
algod_token = os.getenv("TESTNET_ALGOD_TOKEN")
algod_url = os.getenv("TESTNET_ALGOD_URL")
algod_client = algod.AlgodClient(algod_token, algod_url)

# User's private key and application ID
user_private_key = os.getenv("PRIVATE_KEY")
user_address = os.getenv("ADDRESS")
app_id = int(os.getenv("APP_ID"))

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    private_key, address = account.generate_account()
    mnemonic_phrase = mnemonic.from_private_key(private_key)
    return jsonify(address=address, mnemonic=mnemonic_phrase)

@app.route('/create_survey', methods=['POST'])
def create_survey():
    #data = request.json
    #question = data['question']
    #option1 = data['option1']
    #option2 = data['option2']
   # params = algod_client.suggested_params()
    #app_args = [
     #   question.encode(),
     #   option1.encode(),
     #   option2.encode()
    #]
    #txn = ApplicationNoOpTxn(
     #   sender=user_address,
     #   sp=params,
     #   index=app_id,
     #   app_args=app_args
    #)
    #signed_txn = txn.sign(user_private_key)
   # txid = algod_client.send_transaction(signed_txn)
    #return jsonify(txid=txid)
    question = "What is your favorite color?"
    option1 = "Blue"
    option2 = "Green"

    app_id = deploy_survey_contract(question, option1, option2)
    return jsonify({'app_id': app_id})

@app.route('/submit_response', methods=['POST'])
def submit_response():
    data = request.json
    response = data['response']
    params = algod_client.suggested_params()
    app_args = [
        b"vote",
        response.encode()
    ]
    txn = ApplicationNoOpTxn(
        sender=user_address,
        sp=params,
        index=app_id,
        app_args=app_args
    )
    signed_txn = txn.sign(user_private_key)
    txid = algod_client.send_transaction(signed_txn)
    return jsonify(txid=txid)

if __name__ == '__main__':
    app.run(debug=True)