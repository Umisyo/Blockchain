from datetime import datetime
import hashlib
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
        sha = hashlib.sha256()
        
        sha.update(
            (
                str(self.index) + 
                self.timestamp + 
                self.data + 
                self.previousHash
            ).encode('utf-8')
        )
        
        return sha.hexdigest()