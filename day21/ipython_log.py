# IPython log file

from main4 import *
directional_macros
def blarg(to_press):
    path = "A"+to_press
    for b1, b2 in zip(path[:-1], path[1:]):
        print(directional_macros[b1][b2], end="")
        
blarg("><")
def blarg(to_press):
    path = "A"+to_press
    possibilities = None
    for b1, b2 in zip(path[:-1], path[1:]):
        possibilities = append_many_to_many(possibilities, directional_macros[b1][b2])
    return possibilities
    
        
blarg("><")
from main import append_many_to_many
blarg("><")
tuple(blarg("><"))
tuple(blarg("<v"))
tuple(blarg("v<"))
tuple(blarg("v<<A"))
tuple(blarg("<v<A"))
directional_macros["A"]["<"]
arglebargle = {}
for b1 in "><v^A":
    for b2 in "><v^A":
        macros = directional_macros[b1][b2]
        for m in macros:
            for b in blarg(m):
                arglebargle[b1][b2].extend(b)
                
arglebargle = defaultdict(lambda: defaultdict(list))
from collections import defaultdict
arglebargle = defaultdict(lambda: defaultdict(list))
for b1 in "><v^A":
    for b2 in "><v^A":
        macros = directional_macros[b1][b2]
        for m in macros:
            for b in blarg(m):
                arglebargle[b1][b2].extend(b)
                
arglebargle
arglebargle["A"]["^"]
for b1 in "><v^A":
    for b2 in "><v^A":
        macros = directional_macros[b1][b2]
        for m in macros:
            for b in blarg(m):
                arglebargle[b1][b2].extend([b])
                
arglebargle
arglebargle = defaultdict(lambda: defaultdict(list))
for b1 in "><v^A":
    for b2 in "><v^A":
        macros = directional_macros[b1][b2]
        for m in macros:
            for b in blarg(m):
                arglebargle[b1][b2].extend([b])
                
arglebargle["A"]["^"]
[len(_a) for _a in _]
arglebargle
get_ipython().run_line_magic('logstart', '')
def remove_long_entries(l):
    shortest_len = len(min(l, key=len))
    return tuple(_l for _l in l if len(_l) == shortest_len)
    
arglebargle
def apply_to_values(d, f, args):
    if isinstance(d, dict):
        return {k: apply_to_values(v) for k, v in d.items()}
    if isinstance(d, (list, tuple)):
        return tuple(apply_to_values(v) for v in d)
    return f(v, *args)
    
hoobadoop = apply_to_values(arglebargle, remove_long_entries, (,))
hoobadoop = apply_to_values(arglebargle, remove_long_entries, ())
def apply_to_values(d, f, args):
    if isinstance(d, dict):
        return {k: apply_to_values(v, f, args) for k, v in d.items()}
    if isinstance(d, (list, tuple)):
        return tuple(apply_to_values(v, f, args) for v in d)
    return f(v, *args)
    
hoobadoop = apply_to_values(arglebargle, remove_long_entries, ())
def apply_to_values(d, f, args):
    if isinstance(d, dict):
        return {k: apply_to_values(v, f, args) for k, v in d.items()}
    if isinstance(d, (list, tuple)):
        return tuple(apply_to_values(v, f, args) for v in d)
    return f(d, *args)
    
hoobadoop = apply_to_values(arglebargle, remove_long_entries, ())
arglebargle
hoobadoop
arglebargle
arglebargle["A"]["<"]
hoobadoop["A"]["<"]
def apply_to_values(d, f, args):
    if isinstance(d, dict):
        return {k: apply_to_values(v) for k, v in d.items()}
    return f(v, *args)
    
hoobadoop = apply_to_values(arglebargle, remove_long_entries, ())
def apply_to_values(d, f, args):
    if isinstance(d, dict):
        return {k: apply_to_values(v, f, args) for k, v in d.items()}
    return f(v, *args)
    
def apply_to_values(d, f, args):
    if isinstance(d, dict):
        return {k: apply_to_values(v, f, args) for k, v in d.items()}
    return f(d, *args)
    
hoobadoop = apply_to_values(arglebargle, remove_long_entries, ())
arglebargle["A"]["<"]
hoobadoop["A"]["<"]
test = "<A^A>^^AvvvA"
test = "<A^A>^^AvvvA"; path = "A"+test
all_from_A = ("A", "<A", "vA", "<vA", "v<A", "<v<A", "v<<A")
subcommands = ("A", "<A", "vA", "<vA", "v<A", "<v<A", "v<<A")
blarg(subcommands[0])
tuple(blarg(subcommands[0]))
tuple(blarg(subcommands[1]))
tuple(blarg(subcommands[-1]))
tuple(blarg(subcommands[1]))
tuple(blarg(subcommands[-1]))
tuple(blarg(subcommands[-2]))
get_ipython().run_line_magic('pinfo', 'blarg')
get_ipython().run_line_magic('pinfo2', 'blarg')
hoobadoop["A"]["<"]
blarg(hoobadoop["A"]["<"][0])
tuple(blarg(hoobadoop["A"]["<"][0]))
tuple(blarg(hoobadoop["A"]["<"][1]))
hoobadoop["A"]["<"]
tuple(blarg(hoobadoop["A"]["<"][2]))
tuple(blarg(hoobadoop["A"]["<"][3]))
hoobadoop["A"]["<"]
blumpadork = apply_to_values(hoobadoop, remove_long_entries, (lambda v: len(blarg(v)[0])))
blumpadork = apply_to_values(hoobadoop, remove_long_entries, (lambda v: len(blarg(v)[0]),))
get_ipython().run_line_magic('pinfo2', 'remove_long_entries')
def apply_to_values(d, f, *args, **kwargs):
    if isinstance(d, dict):
        return {k: apply_to_values(v, f, args) for k, v in d.items()}
    return f(d, *args, **kwargs)
    
blumpadork = apply_to_values(hoobadoop, remove_long_entries, key=lambda v: len(blarg(v)[0]))
def remove_long_entries(l, key=len):
    shortest_len = len(min(l, key=key))
    return tuple(_l for _l in l if key(_l) == shortest_len)
    
blumpadork = apply_to_values(hoobadoop, remove_long_entries, key=lambda v: len(blarg(v)[0]))
def remove_long_entries(l, key=len):
    shortest_len = key(min(l, key=key))
    return tuple(_l for _l in l if key(_l) == shortest_len)
    
blumpadork = apply_to_values(hoobadoop, remove_long_entries, key=lambda v: len(blarg(v)[0]))
get_ipython().run_line_magic('pdb', 'blumpadork = apply_to_values(hoobadoop, remove_long_entries, key=lambda v: len(blarg(v)[0]))')
get_ipython().run_line_magic('pinfo', 'apply_to_values')
def apply_to_values(d, f, *args, **kwargs):
    if isinstance(d, dict):
        return {k: apply_to_values(v, f, *args, **kwargs) for k, v in d.items()}
    return f(d, *args, **kwargs)
    
blumpadork = apply_to_values(hoobadoop, remove_long_entries, key=lambda v: len(blarg(v)[0]))
def blarg(to_press):
    path = "A"+to_press
    possibilities = None
    for b1, b2 in zip(path[:-1], path[1:]):
        possibilities = append_many_to_many(possibilities, directional_macros[b1][b2])
    return tuple(possibilities)
    
        
blumpadork = apply_to_values(hoobadoop, remove_long_entries, key=lambda v: len(blarg(v)[0]))
blumpadork
hoobadoop["A"]["<"]
blumpadork["A"]["<"]
test
test = "<A^A>^^AvvvA"; path = "A"+test
list(test.split("A"))
for b1, b2 in zip(path[:-1], path[1:]):
    print(blumpadork[b1][b2])
    
for b1, b2 in zip(path[:-1], path[1:]):
    print(blumpadork[b1][b2][0], end="")
    
len(_)
for b1, b2 in zip(path[:-1], path[1:]):
    print(blumpadork[b1][b2][0], end="")
    
len("<vA<AA>>^AvAA<^A>Av<<A>>^AvA^A<vA^>Av<<A>^A>AAvA^Av<<A>A^>AAA<A>vA^A")
blumpadork
blumpadork["v"]
hoobadoop["v"]
