import time 

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-d11103b7-02c3-4649-94f4-0cca627d6e20"
pnconfig.publish_key = "pub-c-25bbfe7f-15e4-417c-9b4c-a636e8def02f"


CHANNELS = {
	'TEST': 'TEST',
	'BLOCK': 'BLOCK'
}

class Listener(SubscribeCallback):
	def message(self, pubnub, message_object):
		print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')


class PubSub():
	"""
	Handles the publish/subscribe layer of the application.
	Provides communication between the nodes of the blockchain network.
	"""
	def __init__(self):
		self.pubnub = PubNub(pnconfig)
		self.pubnub.subscribe().channels(CHANNELS.values()).execute()
		self.pubnub.add_listener(Listener())

	def publish(self, channel, message):
		"""
		Publish the message object to the channel.
		"""
		self.pubnub.publish().channel(channel).message(message).sync()

	def broadcast_block(self, block):
		"""
		Broadcast a block object to all nodes.
		"""
		self.publish(CHANNELS['BLOCK'], block.to_json())

def main():
	pubsub = PubSub()
	time.sleep(1)

	pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})


if __name__ == '__main__':
	main()







