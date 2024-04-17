import logging

from slimta.edge.smtp import SmtpEdge
from slimta.queue import Queue
from slimta.queue.dict import DictStorage
from slimta.policy.headers import *
from slimta.policy.split import RecipientDomainSplit
from relay import MessageRelay


logging.basicConfig(level=logging.DEBUG)
# Set up outbound delivery by MX lookup.

# Set up local queue storage to in-memory dictionaries.

store = DictStorage({}, {})
relay = MessageRelay()
queue = Queue(store, relay)
queue.start()

# Ensure necessary headers are added.
queue.add_policy(AddDateHeader())
queue.add_policy(AddMessageIdHeader())
queue.add_policy(AddReceivedHeader())
queue.add_policy(RecipientDomainSplit())

# Listen for messages on port 25.
edge = SmtpEdge(('0.0.0.0', 25), queue)
edge.start()
try:
    # for k, v in queue_storage.env_db.items():
    #     print(k, vars(v))
    print("Before starting greenlet")
    edge.get()
except KeyboardInterrupt:
    pass
    # for k, v in queue_storage.env_db.items():
    #     print(k, vars(v))