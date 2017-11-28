import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        
c = stomp.Connection([('broker-amq-stomp', 61613)])
c.set_listener('', MyListener())

c.start()
c.connect('daikon', 'daikon', wait=True)

c.subscribe(destination='/queue/salesq', id=1, ack='auto')

c.send(body='foooooo', destination='/queue/salesq')

c.disconnect()

