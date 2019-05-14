from datetime import datetime
import hashlib
import json
from typing import Optional

class Block:
    def __init__(self):
        self.index: int = 0 
        self.timestamp: Optional[str] = None
        self.data: Optional[list] = None
        self.previousHash: Optional[str] = None
        self.hash: str = self.hashBlock()
        self.nonce: Optional[int] = None
        self.diff: int = 0

    def hashBlock(self) -> str:
        joinedBlock: dict = {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previousHash': self.previousHash,
            'diff': self.diff
        }

        jsonBlock = json.dumps(joinedBlock, sort_keys=True)

        return hashlib.sha256(jsonBlock.encode('ascii')).hexdigest()

    def toJson(self) -> bool or str:
        if self.nonce == None:
            return False

        joinedBlock: dict = {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previousHash': self.previousHash,
            'diff': self.diff,
            'hash': self.hash,
            'nonce': self.nonce
        }

        jsonBlock = json.dumps(joinedBlock, sort_keys=True)

        return jsonBlock

    def checkNonce(self, nonce: int) -> bool:
        nonceJoined = self.hash + str(nonce)
        calced = hashlib.sha256(nonceJoined.encode('ascii')).hexdigest()

        if calced[:self.diff:].count('0') == self.diff:
            return True
        else:
            return False

    def miningCoin(self, appendData: dict) -> int:
        nonce: int = 0

        self.data.append(appendData)
        self.hash = self.hashBlock()

        while True:
            nonceJoined: str = self.hash + str(nonce)
            calced: str = hashlib.sha256(nonceJoined.encode('ascii')).hexdigest()

            if calced[:self.diff:].count('0') == self.diff:
                break
            
            nonce += 1

        return nonce

