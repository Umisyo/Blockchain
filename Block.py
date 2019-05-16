import hashlib
import json
from typing import Optional, Union

class Block:
    def __init__(self, index: int, timestamp: str, transaction: list, previousHash: str):
        self.index: int = index 
        self.timestamp: Optional[str] = timestamp
        self.transaction: Optional[list] = transaction
        self.previousHash: Optional[str] = previousHash
        self.diff: int = 4
        self.nonce: Optional[int] = None 
        self.hash: str = self.hashBlock()

    #ブロックのハッシュ値を計算する関数
    def hashBlock(self) -> str:
        joinedBlock: dict = {
            'index': self.index,
            'timestamp': self.timestamp,
            'transaction': self.transaction,
            'previousHash': self.previousHash,
            'diff': self.diff 
        }

        jsonBlock: str = json.dumps(joinedBlock, sort_keys=True)

        return hashlib.sha256(jsonBlock.encode('ascii')).hexdigest()

    #変数nの真偽をチェックする
    def checkNonce(self, nonce: int) -> bool:
        nonceJoined: str = self.hash + str(nonce)
        calced: str = hashlib.sha256(nonceJoined.encode('ascii')).hexdigest()

        if calced[:self.diff:].count('0') == self.diff:
            return True
        else:
            return False

    #hash値の先頭diff桁が0になるまでnonceを総当たりで求める
    def miningCoin(self, appendtransaction: dict) -> int:
        nonce: int = 0

        self.transaction.append(appendtransaction)
        self.hash = self.hashBlock()

        while True:
            nonceJoined: str = self.hash + str(nonce)
            calced: str = hashlib.sha256(nonceJoined.encode('ascii')).hexdigest()

            if calced[:self.diff:].count('0') == self.diff:
                break
            
            nonce += 1

        return nonce

