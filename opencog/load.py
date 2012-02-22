from telnetlib import Telnet
import os

#os.system('/root/cogbuntu-11.10/ochack/bin/opencog/server/cogserver -c /root/cogbuntu-11.10/ochack/lib/opencog.conf &')

tn = Telnet('localhost', 17001)

tn.write("scm\n")
#tn.write('(load-scm-from-file "tests/reasoning/pln/smalldemo.scm")\n')
tn.write('(load-scm-from-file "/root/custom/opencog/demodata/truck.scm")\n')
tn.write(".\n")
tn.write("list\n")
tn.write("exit\n")
#tn.write("shutdown\n")
print tn.read_all()

