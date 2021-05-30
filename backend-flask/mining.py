from hashlib import sha256
from PIL import Image
import imagehash
import dynamic

MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(prev_hash, item, difficulty):
    prefix_str = '0'*difficulty
    for nonce in range(MAX_NONCE):
        text = str(prev_hash) + str(item.sender_id) + str(item.reciver_id) + str(item.transaction_amt) + str(nonce)
        new_hash = SHA256(text)
        print(new_hash)
        if new_hash.startswith(prefix_str):
            return new_hash, nonce

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")


def wallet_tx(prev_hash, sender_id, reciver_id, transaction_amt):
    difficulty = 2
    prefix_str = '0'*difficulty
    
    for nonce in range(MAX_NONCE):
        text = str(prev_hash) + str(sender_id) + str(reciver_id) + str(transaction_amt) + str(nonce)
        new_hash = SHA256(text)
        print(new_hash)
        if new_hash.startswith(prefix_str):
            return new_hash, nonce
    
    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")
    
    
def set_mine(prev_hash, item):
    difficulty = 5
    new_hash, nonce = mine(prev_hash, item, difficulty)
    mine_reward = float(nonce) * 0.00005
    return new_hash, mine_reward, nonce


def img_Hash(item):
    return imagehash.average_hash(Image.open(item))


def checkchain(item):
    text = str(item.prev_hash) + str(item.sender_id) + str(item.reciver_id) + str(item.transaction_amt) + str(item.nonce)
    new_hash = SHA256(text)
    return item.prev_hash, new_hash, item.nonce


def set_train_testing(x, y):
    return True