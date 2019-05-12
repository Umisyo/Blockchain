from Block import Block
from datetime import datetime

class genesisBlock(Block):
    def __init__(self):
        self.index = 0
        self.data = input('please input data for genesis block.\n')
        self.timestamp = str(datetime.now())
        self.previousHash = 0
        self.hash = self.hashBlock()
