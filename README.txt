Topo.py simulates a distributed denial of service (DDoS) attack using Mininet and Python’s socket library by created a virtualized network and runnning programs on its hosts. In order to start this program, call:

	sudo python Topo.py Num_Hosts TCP_

Where Num_Hosts is an integer parameter representing the total number of hosts desired and TCP_ is an optional parameter which will run a TCP instead of UDP analysis on the virtual network if the parameter is non zero.

The analysis will output files named results_N.txt or resultsTCP_N.txt where N is the number of hosts depending on if a TCP or UDP analysis was performed.


If you would like to try out the component Server and DOS clients ran on the hosts, you can call:
	
	python Server.py
	
then:
	
	python Client.py localhost

Feel free to modify these programs to print output.

All source files can be found at: https://github.com/feliperonderos/network-project
