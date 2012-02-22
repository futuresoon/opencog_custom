from telnetlib import Telnet
import opencog.cogserver

tn = Telnet('localhost', 17001)
tn.write("scm\n")
tn.write("""(define x 
                  (cog-new-node 'ConceptNode "abc" 
                     (cog-new-av 11 21 0)))\n
""") 
tn.write(".\n")
tn.write("list\n")
tn.write("exit\n")
print tn.read_all()
