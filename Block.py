from datetime import datetime
import hashlib

class Block:
    def __init__(self):
        self.index: int = 0
        self.timestamp: str = str(datetime.now())
        self.data = None
        self.previousHash = 0
        self.hash = self.hashBlock()

    def hashBlock(self):
        sha = hashlib.sha256()
        
        sha.update(
            (
                str(self.index) + 
                self.timestamp + 
                str(self.data) + 
                str(self.previousHash)
            ).encode('utf-8')
        )
        
        return sha.hexdigest()