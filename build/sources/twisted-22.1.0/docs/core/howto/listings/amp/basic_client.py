if __name__ == "__main__":
    import basic_client

    raise SystemExit(basic_client.main())

from sys import stdout

from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.protocol import Factory
from twisted.protocols.amp import AMP
from twisted.python.log import err, startLogging


def connect():
    endpoint = TCP4ClientEndpoint(reactor, "127.0.0.1", 8750)
    return endpoint.connect(Factory.forProtocol(AMP))


def main():
    startLogging(stdout)

    d = connect()
    d.addErrback(err, "Connection failed")

    def done(ignored):
        reactor.stop()

    d.addCallback(done)

    reactor.run()
