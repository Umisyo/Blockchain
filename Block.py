from datetime import datetime
import hashlib
import json
from typing import Optional

class Block:
    def __init__(self):
        self.index: int = 0 
        self.timestamp: Optional[str] = None
        self.data: Optional[str] = None
        self.previousHash: Optional[str] = None
        self.hash: str = self.hashBlock()
        self.nonce: Optional[int] = None
        self.diff: int = 4

    def hashBlock(self):
        joinedBlock: dict = {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previousHash': self.previousHash,
            'diff': self.diff
        }

        jsonBlock = json.dumps(joinedBlock, sort_keys=True)

        return hashlib.sha256(jsonBlock.encode('ascii')).hexdigest()

    def toJson(self):
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

