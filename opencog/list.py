from telnetlib import Telnet
import os

#os.system('/root/cogbuntu-11.10/ochack/bin/opencog/server/cogserver -c /root/cogbuntu-11.10/ochack/lib/opencog.conf &')

tn = Telnet('localhost', 17001)

tn.write("list\n")
tn.write("exit\n")
print tn.read_all()


#tn.write("loadmodule libattention.so\n")
#tn.write("agents-start-loop\n")
#tn.write("agents-start opencog::ForgettingAgent opencog::HebbianUpdatingAgent opencog::ImportanceDiffusionAgent opencog::ImportanceSpreadingAgent opencog::ImportanceUpdatingAgent opencog::STIDecayingAge$
#tn.write("scm\n")
#tn.write('(load-scm-from-file "tests/reasoning/pln/smalldemo.scm")\n')
#tn.write(".\n")
#tn.write("list\n")
#tn.write("exit\n")
#tn.write("shutdown\n")
#print tn.read_all()




