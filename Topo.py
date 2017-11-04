"""top | awk '/Cpu/ { print "CPU utilization:" $2 }' 
"""


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class Topo(Topo):
    def build(self, n=8):
        counter = 1
        branching_factor = 2
        core = [self.addSwitch('s1')]
        aggregation = []
        edge = []
        for h in core:
            for i in range(branching_factor):
                a = self.addSwitch(('s' + str(counter + 1)))
                counter += 1
                aggregation.append(a)
                self.addLink(a,h)
        for m in aggregation:
            for i in range(branching_factor):
                a = self.addSwitch(('s' + str(counter + 1)))
                counter += 1
                edge.append(a)
                self.addLink(a,m)
        self.hostList = []
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            print h
            self.addLink(host, edge[h%len(edge)])
            self.hostList.append(host)

def simpleTest():
    "Create and test a simple network"
    topo = Topo(n=64)
    net = Mininet(topo)
    net.start()
    """
    h = net.hosts
    for i in range(len(h)):
        if i == 0:
            h[i].cmd("top | awk '/Cpu/ { print "CPU utilization:" $2 }' > lala.txt ")

    """
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()