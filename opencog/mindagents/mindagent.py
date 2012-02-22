from telnetlib import Telnet
import opencog.cogserver

from opencog.atomspace import types
class MyMindAgent(opencog.cogserver.MindAgent):
    def run(self,atomspace):
        atomspace.add_node(types.ConceptNode, "test")
class MyRequest(opencog.cogserver.Request):
    def run(self,args,atomspace):
        # args is a list of strings
#        atomspace.add_node(types.ConceptNode, args[0])
#        tn = Telnet('localhost', 17001)
#        tn.write("scm\n")
#        tn.write("(define x\n") 
#        tn.write("(cog-new-node 'ConceptNode '" + args[0] + "'\n") 
#        tn.write("(cog-new-av 11 21 0)))\n")
#        tn.write(".\n")
#        tn.write("exit\n")
        tn = Telnet('localhost', 17001)
        tn.write("scm\n")
        tn.write("""(define x
                          (cog-new-node 'ConceptNode \"""")
        tn.write(args[0])
        tn.write(""""
        """)
        tn.write("""
                             (cog-new-av 11 21 0)))\n
        """)
        tn.write(".\n")
        tn.write("list\n")
        tn.write("exit\n")

