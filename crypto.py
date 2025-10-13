from datetime import datetime
import hashlib
import time
import json
import hmac

# hashing functions
def calculate_hash(data):
    '''calculatesthe SHA-256 hash of the given data'''
    #converts the data to a JSON string and encods it to bytes
    data_string = json.dumps(data, sort_keys = True) 
    data_bytes = data_string.encodes('utf-8') #converts the string to bytes
    hash_object = hashlib.sha256(data_bytes)#creates a SHA-256 hash object
    return hash_object.hexdigest()#returns the hexadecimal representation of the hash

#2 transaction Class
class Transaction:
    """ 
      Represents money moving to one person to another person
        """
    def __init__(self,sender, receiver,amount):
        self.sender = sender #the sender of the transaction
        self.receiver = receiver #the reciver of the transaction
        self.amount = amount #the amount of the transaction
        self.timestamp = time.time() #the timestamp of the transaction

    def to_dict(self):
        """converts transaction to a dictionary"""
        return{
            'sender': self.sender, 
            'receiver': self.receiver, 
            'amount':self.amount,
            'timestamp': self.timestamp
        } #returns a dictionary representation of the transaction

# --- IGNORE ---
def __str__(self):
    return f"{self.sender} ->{self.reciver}:{self.amount} at {datetime.fromtimestamp(self.timestamp)}"


#3 block class

class Block:
    """ a block is container data for transaction
    each block is linked to the previous block in the chain by including the previous block's hash
    """
    def __init__(self,transactions,previous_hash =''):
        self.timestamp = time.time() #the timestamp of the block
        self.transactions = transactions #the list of transactions in the block
        self.previous_hash = previous_hash #the hash of the previous block in the chain
        self.nonce = 0 #the nonce is a number that is used to vary the hash of the block
        self.hash = self.calculate_hash()#the hash of the block

    def calculate_hash(self):
        """calculates the SHA-256 hash of the world state of the block
        """
        block_data ={
            'timestamp':self.timestamp,
            'transactions':[tx.to_dict() for tx in self.transactions],
            'previous_hash':self.previous_hash,
            'nonce':self.nonce
        }
        return calculate_hash(block_data)
    
    def mine_block(self, difficulty):
        """mining: Find a nonce that makes hash start with 'difficulty' zeros
        Example : difficulty = 4 -> hash starts with '0000'
        """
        target = 'o' * difficulty #the target hash prefix
        print(f"mining block....(need hash starting with '{target}'")

        while not self.hash.startswith(target): #keep trying until we find a hash that starts with the target prefix
            self.nonce += 1 #increment the nonce
            self.hash = self.calculate_hash() #recalculate the hash

            #show progress every 10000 attempts
            if self.nonce%10000 == 0:
                print(f"Tried{self.nonce} times... Current hash:{self.hash[:20]}...")
        print(f"Block mined! Nonce:{self.nonce}, Hash:{self.hash}")
# --- IGNORE ---
    def __str__(self):
        tx_list = "\n  ".join([str(tx) for tx in self.transactions])
        return f"""
Block hash:{self.hash}
Previous hash:{self.previous_hash}
Timestamp:{datetime.fromtimestamp(self.timestamp)}
Transactions:
  {tx_list}
Nonce:{self.nonce}
        """
