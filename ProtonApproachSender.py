import sys
from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container

class SendHandler(MessagingHandler):
    def __init__(self, conn_url, address, message_body):
        super(SendHandler, self).__init__()
        self.conn_url = conn_url
        self.address = address
        self.message_body = message_body
        self.stopping = False
    def on_start(self, event):
        conn = event.container.connect(self.conn_url, user='daikon', password='daikon')
        event.container.create_sender(conn, self.address)
    def on_link_opened(self, event):
        print("SEND: Opened sender for target address '{0}'".format(self.address))
    def on_sendable(self, event):
        if self.stopping: return
        message = Message(self.message_body)
        event.sender.send(message)
        print("SEND: Sent message '{0}'".format(self.message_body))
        event.connection.close()
        self.stopping = True

conn_url = 'amqp://broker-amq-amqp:5672'
address = 'salesq'
message_body = 'foooooo'
handler = SendHandler(conn_url, address, message_body)
container = Container(handler)
container.run()


