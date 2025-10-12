# Class wallet:
-FUNCTION __init__():
-private_key = generate_random_key()
-public-key = derive_public_key(private_key)
-addrss = hash(public_key)

Function sign_transaction(transaction):
signature = sign_with_priivate_key(transaction, private_key)
Return signature 

# Class Transaction:
Function __init__(sender,recipient, amount):
this.sender = sender
this.recipent = recipient
this.amount = amount
this.timestamp = current_time()
this.signature = Null

Function sign(wallet):
  transaction_data = sender + recipient + amount + timestamp
  this.signature = wallet.sign_transaction(transaction_data)

Function is valied():
IF sender == "GENESIS":
   RETURN TRUE
transaction_data = sender + recipient + amount + timestamp
Return verify_signature(sender,Transaction_data , signature)

# Class Block
  Function __init__(transection,previous_hash):
      this.timestamp == current_time()
      this.transactions = transactions
      this.previous_hash = previous_hash
      this.nounce = 0
      this.hash = this.calculate_hash()
 
  Function calculate_hash():
      block_string = previous_hash + timestamp + transactions + nonce
      Return SHA256(block_string)
  Function mine_block(difficulty):
    target = "0" * difficulty
    WHILE hash does not start with target:
    nonce += 1 
    hash = calculate_hash()

# Class Blockchain :
   Function __init__():
     this.chain = [ create_genesis_block()]
     this.difficulty = 4
     this.pending_transaction = []
     this.mining_reward_reward = 10
     this.balances = {}

   Function create_genesis_block():
     Return Block([], "0")
   Function add_transection(transaction):
    If NOT transaction.is valid():
     return  FALSE

    sender_balance = get_balance(transection.sender)
    IF sender != "Genesis" and sender_balance < transaction.amount:
       Return  False
    
    pending_transaction.append(transaction)
    Return True

    FUNCTION mine_pending_transactions(miner-address):
    block = Block(pending_transactions, get_latest_block().hash)
    block.mine_block(difficulty)

    chain.append(block)

    //Update balances
    FOR transaction IN block.transactions:
    balances[transaction.sender] -= transaction.amount
    balances[transaction.recipient] += transaction.amount

    //Reward miner
    pending_transactions = [Transaction("GENESIS", miner_address, mining_reward)]

    Function get_balance(address):
     if address not in balances:
     Return 0
    Return balances[address]

    Function is_chain_valid():
       for i From 1 to chain.length:
       current_block = chain[i]
       previous_block = chain[i-1]

       IF current_block.hash != current_block.calculate_hash():
           Return False
    
       IF current_block.previous_hash != previous_block.hash:
           Return False

       For transaction In  current_blocktransactions:
            If not transaction.is_valid():
               Return false
    Return True
# // Main Program 
  FUNCTION main():
  // Create blockchain
  blockchain = New blockchain()

  //Create wallets
  alice_wallet = New wallet()
  bob_wallet = New wallet()
  miner_wallet = New wallet()

//Genesis transaction (create initials supply)
genesis_tx = transaction("Genesis",alice_wallet.address , 1000)
blockchain.add_transaction(genesis_tx)
blockchain.mine_pending_transactions(miner_wallet.address)

//Alice sends to Bob
tx1 = transaction(alice_wallet.address, bob_wallet.address, 100)
tx1.sign(alice_wallet)
blockchain.add_transaction(tx1)

//Mine the block
blockchain.mine_pending_transactions(miner_wallet.address)

   // check balances
    PRINT "Alice balance:", blockchain.get_balance(alice_wallet.address)
    PRINT "Bob balance:", blockchain.get_balance(bob_wallet.address)
    PRINT "Miner balance:", blockchain.get_balance(miner_wallet.address)
    
    // Verify blockchain
    PRINT "Is blockchain valid?", blockchain.is_chain_valid()
 





