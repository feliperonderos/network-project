"""
This program initializes a Mininet topology with 1 core, 2 aggregation and 4 edge switches with a variable number (N) of 
bandwidth limited hosts. It then starts a server program on the first host, and starts malicious denial of service clients 
on hosts 3-N. After this has taken place, the first and second hosts attempt to measure the bandwidth available to clients
using iperf with host 1 serving as the iperf Server, and host 2 serving as the iperf client. The data from this analysis is
printed to a file, and the Virtual network is then shut down. The bandwidth statistics may be gathered using either UDP or TCP
depending on the second command line argument. The program can be called using "sudo python Topo.py Num_Hosts TCP_" with the 
Num_Hosts parameter being a nonzero integer and the TCP_ parameter being null or zero for UDP and nonzero otherwise.
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.node import CPULimitedHost
from mininet.cli import CLI
import time
import sys
"""
This function provides a topology with 7 switches and N hosts. The hosts are distributed evenly through the four edge switches.
"""
class Topo(Topo):
    def build(self, n=8):
        counter = 1 
        branching_factor = 2 #switches branch out in pairs
        core = [self.addSwitch('s1')]
        aggregation = []
        edge = []
        for h in core:
            for i in range(branching_factor):
                a = self.addSwitch(('s' + str(counter + 1))) 
                counter += 1
                aggregation.append(a) 
                self.addLink(a,h) #link switch to core
        for m in aggregation:
            for i in range(branching_factor):
                a = self.addSwitch(('s' + str(counter + 1)))
                counter += 1
                edge.append(a)
                self.addLink(a,m) #link switch to aggregation
        for h in range(n):
            if h < 2: #Hosts 1 and 2 should have representative CPU usage in order to accurately measure bandwidth
                host = self.addHost('h%s' % (h + 1)) #create host
            else:
                host = self.addHost('h%s' % (h + 1), cpu=.5/n)#create cpu-limited host
            if h == 0:
                self.addLink(host, edge[h%len(edge)], bw=10, delay='5ms', loss=2,
                          max_queue_size=1000, use_htb=True ) #link h1 (server) to edge switch with a 10Mb/s link
            else:
                self.addLink(host, edge[h%len(edge)], bw=1, delay='5ms', loss=2,
                          max_queue_size=1000, use_htb=True )#link all other hosts to edge switch with a 1Mb/s link
"""
This function creates a Topology object and builds a Mininet network using this. It then starts the network and initializes 
various programs on the hosts using the command line api. For more information, see the comment at the top of this file. 
After these programs execute, the network is shut down. 
"""
def simpleTest(num_hosts, tcp=0):
    topo = Topo(n=num_hosts) #Create topology
    net = Mininet(topo,host=CPULimitedHost,link=TCLink) 
    net.start() #start network
    h = net.hosts
    IPstr = str(h[0].IP()) #get IP of first host (Server)
    for i in range(len(h)):
        if i == 0: #if Server
            h[i].cmd("python Server.py &") #Start Server program   
        elif i>1: #if DOS client
            h[i].cmd("python Client.py "+ IPstr +" &") #Start DOS client program
    time.sleep(5) #wait 5 seconds
    if tcp == 0: #if UDP analysis
        h[0].cmd("iperf -s -u -i 1 -p 5566 > results_"+str(num_hosts)+".txt &") #start iperf UDP server on h1. Print output to file.
        time.sleep(5)# wait 5 seconds
        h[1].cmd("iperf -c " + IPstr + " -u -t 15 -p 5566 -b 1M &")#start iperf UDP client on h2.
        time.sleep(60) #allow enough time for analysis to complete
    else: #if TCP analysis
        h[0].cmd("iperf -s -i 15 -p 5566 > resultsTCP_"+str(num_hosts)+".txt &")#start iperf TCP server on h1. Print output to file.
        time.sleep(5)# wait 5 seconds
        h[1].cmd("iperf -c " + IPstr + " -t 15 -p 5566 &")#start iperf TCP client on h2.
        time.sleep(60)#allow enough time for analysis to complete
    net.stop() #shutdown network

if __name__ == '__main__':
    if len(sys.argv) == 3: #if TCP command line argument included
        simpleTest(int(sys.argv[1]),int(sys.argv[2])) #build and initialize network
    else: #if TCP command line arg not included
        simpleTest(int(sys.argv[1])) #build and initialize network, use UDP
