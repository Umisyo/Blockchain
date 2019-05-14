import hashlib
from datetime import datetime
from Block import Block

blockChain: list = [] 

def main():
    genesisBlock: Block = Block(0, str(datetime.now()), [], '-')
    appendData: dict = {'genesis': input('please input data for genesis block:')}
    nonce: int = genesisBlock.miningCoin(appendData)
    genesisBlock.nonce = nonce

    blockChain.append(genesisBlock)

    num: int = int(input('How many blocks do you make?:'))

    for i in range(num):
        newBlock: Block = Block(i + 1, str(datetime.now()), [], blockChain[i].hash)
        appendData: dict = {'data': input('please input data for block{}:'.format(i + 1))}
        nonce = newBlock.miningCoin(appendData)
        newBlock.nonce = nonce
        blockChain.append(newBlock)

    for block in blockChain:
        nonceJoined: str = block.hash + str(block.nonce)
        calced: str = hashlib.sha256(nonceJoined.encode('ascii')).hexdigest()

        print("index =", block.index ,"sha256(", block.hash, "+", block.nonce, ") =", calced)

    return 0

if __name__ == "__main__":
    main()
