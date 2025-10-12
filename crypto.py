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

#transaction Class
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
    return f"{self.sender} "