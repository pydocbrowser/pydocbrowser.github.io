# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


"""Server for PB benchmark."""

from zope.interface import implementer

from twisted.cred.portal import IRealm
from twisted.internet import reactor
from twisted.spread import pb


class PBBenchPerspective(pb.Avatar):
    callsPerSec = 0

    def __init__(self):
        pass

    def perspective_simple(self):
        self.callsPerSec = self.callsPerSec + 1
        return None

    def printCallsPerSec(self):
        print("(s) cps:", self.callsPerSec)
        self.callsPerSec = 0
        reactor.callLater(1, self.printCallsPerSec)

    def perspective_complexTypes(self):
        return ["a", 1, 1, 1.0, [], ()]


@implementer(IRealm)
class SimpleRealm:
    def requestAvatar(self, avatarId, mind, *interfaces):
        if pb.IPerspective in interfaces:
            p = PBBenchPerspective()
            p.printCallsPerSec()
            return pb.IPerspective, p, lambda: None
        else:
            raise NotImplementedError("no interface")


def main():
    from twisted.cred.checkers import InMemoryUsernamePasswordDatabaseDontUse
    from twisted.cred.portal import Portal

    portal = Portal(SimpleRealm())
    checker = InMemoryUsernamePasswordDatabaseDontUse()
    checker.addUser(b"benchmark", b"benchmark")
    portal.registerChecker(checker)
    reactor.listenTCP(8787, pb.PBServerFactory(portal))
    reactor.run()


if __name__ == "__main__":
    main()
