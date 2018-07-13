from twisted.internet import reactor, protocol


# a client protocol

class GPSdClient(protocol.Protocol):


    def connectionMade(self):
        # self.transport.write(b"hello, world!")
        print("[*] Connection made with GPSd.")

    def dataReceived(self, data):
        # print("Server said:", data)

        print(data)

        # Close connection if required.
        self.transport.loseConnection()

    def connectionLost(self, reason):
        print("[*] Connection lost")
        print(reason)


class GPSdFactory(protocol.ClientFactory):
    protocol = GPSdClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    f = GPSdFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()