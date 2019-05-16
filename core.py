import hashlib
from datetime import datetime
from Block import Block

blockChain: list = [] 

def main():
    #最初のブロックの作成
    genesisBlock: Block = Block(0, str(datetime.now()), [], '-')
    appendTransaction: dict = {'genesis': input('please input Transaction for genesis block:')}
    nonce: int = genesisBlock.miningCoin(appendTransaction)
    genesisBlock.nonce = nonce

    blockChain.append(genesisBlock)

    #指定回数ブロックを作成する
    num: int = int(input('How many blocks do you make?:'))

    for i in range(num):
        newBlock: Block = Block(i + 1, str(datetime.now()), [], blockChain[i].hash)
        appendTransaction: dict = {'Transaction': input('please input Transaction for block{}:'.format(i + 1))}
        nonce = newBlock.miningCoin(appendTransaction)
        newBlock.nonce = nonce
        blockChain.append(newBlock)

    #作成したブロックのindex,ブロックそのもののhash値, マイニングで求めた変数n, 最終的に得られるhash値を表示する
    for block in blockChain:
        nonceJoined: str = block.hash + str(block.nonce)
        calced: str = hashlib.sha256(nonceJoined.encode('ascii')).hexdigest()

        print("index =", block.index ,"sha256(", block.hash, "+", block.nonce, ") =", calced)

    return 0

if __name__ == "__main__":
    main()
