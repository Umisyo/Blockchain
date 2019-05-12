from genesis import genesisBlock
from NewBlock import NewBlock 

genesisblock = genesisBlock()
BlockChain = []

BlockChain.append(genesisblock)

previousBlock = BlockChain[0]

num: int = int(input('How many block do you add?'))

for i in range(num):
    newblock = NewBlock(previousBlock)
    BlocksToAdd = newblock
    BlockChain.append(BlocksToAdd)
    previousBlock = BlocksToAdd
    print('Block {} has been added to the chain\n'.format(BlocksToAdd.index) + 'Hash: {}'.format(BlocksToAdd.previousHash))

