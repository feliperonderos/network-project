from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.node import CPULimitedHost
from mininet.cli import CLI
import time
import sys

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
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))#, cpu=.5/n)
            if h == 0:
                self.addLink(host, edge[h%len(edge)], bw=1, delay='5ms', loss=2,
                          max_queue_size=1000, use_htb=True )
            else:
                self.addLink(host, edge[h%len(edge)], bw=1, delay='5ms', loss=2,
                          max_queue_size=1000, use_htb=True )

def simpleTest(num_hosts):
    "Create and test a simple network"
    topo = Topo(n=num_hosts)
    net = Mininet(topo,host=CPULimitedHost,link=TCLink)
    net.start()
    h = net.hosts
    IPstr = str(h[0].IP())
    for i in range(len(h)):
        if i == 0:
            h[i].cmd("python Server.py &")
        else:
            h[i].cmd("python Client.py "+ IPstr + " " + str(i)+" &")
    CLI(net)
    net.stop()

if __name__ == '__main__':

    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest(int(sys.argv[1]))





        #elif i == 1:
        #    h[i].cmd("python TestClient.py "+IPstr + " &")
      """top | awk '/Cpu/ { print "CPU utilization:" $2 }' >> lala.txt """

    """
    
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    """
    
    #net.pingAll()
