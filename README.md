The blockchain is a list of blocks where each block represents a unit of storage for data. The list is called a chain because each block references the block before it, creating (chain) links between blocks.

Some basic python concepts:
A python module is a file that contains various Python definitions and statements. 

Mininig blocks refers to the process of running a computationally expensive algorithm in order to create new blocks for the blockchain. 
The <b>genesis block</b> is the first block in the blockchain. Since all blocks must reference the block that came before it, the genesis block serves as a hardcoded starter block for the chain. 

Encoding is the process of converting data into a particular format (such as the utf-8 format). For example, encoding a string in utf-8, would produce the equivalent byte string in utf-8 characters. Decoding converts the encoded data back into its original form.


The entire project could be divided into several sections:

Section 2: Test the application
Listed required python package for this project, and other developers could jusr run 'pip3 install -r requirements.txt'. Continuous update requirements.txt file to make future collaboration as easy as possible. 


**Activate the vitural environment**
'''
source blockchain-env/bin/activate
'''

**Install all package**
'''
pip3 install -r requirements.txt 
'''

**Run the tests**
Make sure to activate the vitural environment.

'''
python3 -m pytest backend/tests
'''

**Run the application and API**

Make sure to activate the virtual environment

'''
python3 -m backend.app
'''


**Run a peer instance**

Make sure to activate the virtual environment.

'''
export PEER=True && python3 -m backend.app
'''

**Run the frontend**
In the frontend directory:
'''
npm run start 
'''