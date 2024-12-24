import graphviz

import input
#import test2 as input

dot = graphviz.Digraph()

for init in input.initial.split("\n"):
    init = init[:-3]
    dot.node(init)

swaps = (
    ("rjm", "wsv"),
    ("z07", "swt"),
    ("z13", "pqc"),
    ("z31", "bgs"),
)
rewirings = {}
for w1, w2 in swaps:
    rewirings[w1], rewirings[w2] = w2, w1

for wiring in input.wires.split("\n"):
    gate, output = wiring.split(" -> ")
    l, gate, r = gate.split()
    output_gate = output+"gate"
    dot.node(output_gate, label=gate)
    dot.edge(l, output_gate)#, label=l)
    dot.edge(r, output_gate)#, label=r)
    #dot.edge(rewirings.get(l,l), output_gate)#, label=l)
    #dot.edge(rewirings.get(r,r), output_gate)#, label=r)
    dot.node(output)
    dot.edge(output_gate, rewirings.get(output,output))

dot.render()

swaps = sorted(swaps[0] + swaps[1] + swaps[2] + swaps[3])
print("Part 2:", ",".join(swaps))
