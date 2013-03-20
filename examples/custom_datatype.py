"""

rdflib.term.bind lets you register new mappings between literal
datatypes and python objects 

"""


from rdflib import Graph, Literal, Namespace, XSD
from rdflib.term import bind

# complex numbers are not registered by default
# on custom constructor/serializer needed since 
# complex('(2+3j)') works fine
bind(XSD.complexNumber, complex) 

ns=Namespace("urn:my:namespace:")

c=complex(2,3)

l=Literal(c)

g=Graph()
g.add((ns.mysubject, ns.myprop, l))

n3=g.serialize(format='n3')

# round-trip through n3

g2=Graph()
g2.parse(data=n3, format='n3')

l2=list(g2)[0][2]

print l2 

print l2.value == c # back to a python complex object

