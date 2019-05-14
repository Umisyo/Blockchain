from genesis import genesisBlock
from NewBlock import NewBlock 

def main():
    genesisblock = genesisBlock()
    BlockChain = []

    BlockChain.append(genesisblock)

    previousBlock = BlockChain[0]

    num: int = int(input('How many block do you add?'))

    for _ in range(num):
        newblock = NewBlock(previousBlock)
        BlocksToAdd = newblock
        BlockChain.append(BlocksToAdd)
        previousBlock = BlocksToAdd
        print('Block {} has been added to the chain\n'.format(BlocksToAdd.index) + 'Hash: {}'.format(BlocksToAdd.previousHash))

if __name__ == "__main__":
    main()
