import sys
from proton.handlers import MessagingHandler
from proton.reactor import Container

class ReceiveHandler(MessagingHandler):
    def __init__(self, conn_url, address, count):
        super(ReceiveHandler, self).__init__()
        self.conn_url = conn_url
        self.address = address
        self.count = count
        self.received = 0
        self.stopping = False
    def on_start(self, event):
        conn = event.container.connect(self.conn_url, user='daikon', password='daikon')
        event.container.create_receiver(conn, self.address)
    def on_link_opened(self, event):
        print("RECEIVE: Created receiver for source address '{0}'".format(self.address))
    def on_message(self, event):
        if self.stopping: return
        message = event.message
        print("RECEIVE: Received message '{0}'".format(message.body))
        self.received += 1
        if self.received == self.count:
            event.connection.close()
            self.stopping = True

conn_url = 'amqp://broker-amq-amqp:5672'
address = 'salesq'
count = 5
handler = ReceiveHandler(conn_url, address, count)
container = Container(handler)
container.run()


