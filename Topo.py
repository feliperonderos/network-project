"""top | awk '/Cpu/ { print "CPU utilization:" $2 }' 
"""


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost
import time

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
            host = self.addHost('h%s' % (h + 1), cpu=.5/n)
            self.addLink(host, edge[h%len(edge)])
            self.hostList.append(host)

def simpleTest():
    "Create and test a simple network"
    topo = Topo(n=16)
    net = Mininet(topo,host=CPULimitedHost)
    net.start()
    h = net.hosts
    f = open("cl.txt","w+")
    f.close()
    IPstr = str(h[0].IP())
    for i in range(len(h)):
        if i == 0:
            h[i].cmd("python Server.py &")
            #h[i].cmd("""top | awk '/Cpu/ { print "CPU utilization:" $2 }' >> lala.txt &""")
        else:
            h[i].cmd("python Client.py "+ IPstr)
        

    """top | awk '/Cpu/ { print "CPU utilization:" $2 }' >> lala.txt """

    """
    
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    """
    #time.sleep(2)
    #net.pingAll()
    #net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()