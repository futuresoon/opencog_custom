from telnetlib import Telnet
import os

#os.system('/root/cogbuntu-11.10/ochack/bin/opencog/server/cogserver -c /root/cogbuntu-11.10/ochack/lib/opencog.conf &')

tn = Telnet('localhost', 17001)

tn.write("loadmodule libattention.so\n")
tn.write("loadpy mindagent\n")
tn.write("agents-start-loop\n")
tn.write("agents-start mindagent.MyMindAgent opencog::ForgettingAgent opencog::HebbianUpdatingAgent opencog::ImportanceDiffusionAgent opencog::ImportanceSpreadingAgent opencog::ImportanceUpdatingAgent opencog::STIDecayingAgent\n")
tn.write("exit\n")
#tn.write("shutdown\n")
print tn.read_all()

