nfa={}
transitions = []
with open('fisierintrare.txt') as file:
    stare_initiala = file.readline().replace('\n', '')
    stari_finale = file.readline().replace('\n', '').split()
    for line in file:
        line = line.replace('\n', '').split(' ')
        sursa, litera, destinatie = line
        if litera == 'lambda':
            litera = ''
        if litera not in transitions:
            if litera != '':
                transitions.append(litera)
        if sursa not in nfa:
            nfa[sursa]={}
        if litera not in nfa[sursa]:
            nfa[sursa][litera] = [destinatie]
        else:
            nfa[sursa][litera] += [destinatie]
transitions=tuple(transitions)

def lambda_closure(stari, nfa):
    l_closure = stari.copy()
    queue = list(stari)
    while queue:
        state = queue.pop(0)
        for next_state in nfa.get(state, {}).get('', []):
            if next_state not in l_closure:
                l_closure.append(next_state)
                queue.append(next_state)
    return sorted(l_closure)

# Convert the NFA to a DFA
start_state = sorted(lambda_closure(['q0'], nfa))
dfa_states = [start_state]
dfa_transition = {}
queue = [start_state]
while queue:
    current_state = queue.pop(0)
    for transition in transitions:
        next_state = sorted(list(set(state for nfa_state in current_state for state in nfa.get(nfa_state, {}).get(transition, []))))
        lambda_states = lambda_closure(next_state, nfa)
        if tuple(lambda_states) not in [tuple(s) for s in dfa_states]:
            dfa_states.append(lambda_states)
            queue.append(lambda_states)
        dfa_transition.setdefault(tuple(current_state), {})[transition] = tuple(lambda_states)

# Print the resulting DFA
print('DFA Transition Table:')
print(' '.center(len(max(dfa_states))*4),end='|')
for x in transitions:
    print(str(x).center(len(max(dfa_states))*4), end = '|')
print()
for i in range(len(max(dfa_states))):
    print('-------------', end='')
print()
for state in dfa_states:
    print('{:2s} | {:2s} | {:2s} | {:2s}'.format(','.join(state), ','.join(dfa_transition.get(tuple(state), {}).get('0', [])), ','.join(dfa_transition.get(tuple(state), {}).get('1', [])), ','.join(dfa_transition.get(tuple(state), {}).get('2', []))))

