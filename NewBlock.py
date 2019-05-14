from datetime import datetime
from Block import Block

class NewBlock(Block):
    def __init__(self, lastBlock):
        self.index = int(lastBlock.index) + 1
        self.timestamp = str(datetime.now())
        self.data = list(input('please input data for new block.\n') + str(self.index))
        self.previousHash = lastBlock.hash
        self.hash = self.hashBlock()