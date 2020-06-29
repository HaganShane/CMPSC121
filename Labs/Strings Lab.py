# We will enter the paragraph stores as "Pgraph"
Pgraph = '''CMPSC 121 - Introduction to Programming Techniques
This course will feature the following information:
Design and implementation of algorithms.
Structured Programming.
Problem solving techniques.
Introduction to a high-level language, including arrays, procedures, and recursion.'''
print(Pgraph)

# Now we will enter the adjusted paragraph as "APgraph"
APgraph = '''\nCMPSC 121 - Introduction to Programming Techniques\n
This course will feature the following information:
\tDesign and implementation of algorithms.\n
\tStructured Programming.\n
\tProblem solving techniques.\n
\tIntroduction to a \'high-level\' language, including arrays, procedures, and recursion.\n'''
print(APgraph)

# Storing Hello 10 times
Store1 = 'Hello ' * 10 + '\n'
print(Store1)

# Variable to store the first line of part 2
Store2 = APgraph[1:53]
print(Store2)

# Store the length of variable from part 2
Store3 = len(Store2)
print(Store3)

# Replacing periods
APgraphReplace = APgraph.replace('.','_PERIOD_')
print(APgraphReplace)



