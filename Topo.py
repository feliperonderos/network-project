"""top | awk '/Cpu/ { print "CPU utilization:" $2 }' 
"""


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class Topo(Topo):
    def build(self, n=8):
        counter = 0
        branching_factor = 2
        core = [self.addSwitch('s' + str(counter + 1))]
        aggregation = []
        edge = []
        for h in core:
          for i in range(branching_factor):
            a = self.addSwitch(('s' + str(counter + 1)))
			aggregation.append(a)
            self.addLink(a,h)
		for h in aggregation:
          for i in range(branching_factor):
            a = self.addSwitch(('s' + str(counter + 1)))
    		edge.append(a)
    		self.addLink(a,h)
    		self.hosts = []
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, host%len(edge))
            self.hosts.append(host)

def simpleTest():
    "Create and test a simple network"
    topo = Topo(n=8)
    net = Mininet(topo)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()