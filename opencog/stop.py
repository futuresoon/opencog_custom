from telnetlib import Telnet
import os

#os.system('/root/cogbuntu-11.10/ochack/bin/opencog/server/cogserver -c /root/cogbuntu-11.10/ochack/lib/opencog.conf &')

tn = Telnet('localhost', 17001)

tn.write("shutdown\n")
print tn.read_all()

