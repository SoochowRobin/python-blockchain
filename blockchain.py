from block import Block

class Blockchain:
	"""
	Blockchain: a public ledger of transactions.
	Implemented as a list of blocks - data sets of transactions 
	"""
	def __init__(self) -> None:
		self.chain = [Block.genesis()]

	def add_block(self, data):
		last_block = self.chain[-1]
		self.chain.append(Block.mine_block(last_block, data)) # mine from last_block and add current data
		# it would be more concise if you write as this :
		# self.chain.append(mine_block(self.chain[-1], data))


	def __repr__(self) -> str:
		return f'Blockchain: {self.chain}'

def main():
	blockchain = Blockchain()
	blockchain.add_block('one')
	blockchain.add_block('two')
	blockchain.add_block('three')

	print(blockchain)
	print(f'filename: {__name__}')


if __name__ == '__main__':
	main()

