from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
	# It should create the same hash with arguments of different data since we sort the encoded data 
	# types in any order 
	assert crypto_hash(1, [2], 'three') == crypto_hash(1, 'three', [2])
	