from time import perf_counter_ns
from linked_list import LinkedList

def time_it(whois, fn, *args):
    start = perf_counter_ns()
    for _ in range(0, 100000):
        fn(*args)
    print(f"[{whois}] Time: {perf_counter_ns() - start} ns")

ll = LinkedList(0)
for i in range(1, 101):
    ll.append(i)

l = [ x for x in range(0, 101) ]

print('\n(LL vs LIST) search')
time_it('LL', ll.search, 50)
time_it('LS', l.index, 50)

print('\n(LL vs LIST) insert at head')
time_it('LL', ll.insert_at_head, 101)
time_it('LS', l.insert, 0, 101)

print('\n(LL vs LIST) delete at head')
time_it('LL', ll.delete_at_head)
time_it('LS', l.pop, 0)
