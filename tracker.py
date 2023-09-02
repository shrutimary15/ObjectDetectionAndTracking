def update_counters(last_positions1, last_positions2, counter1, counter2, people_enter, people_exit):
    remove_keys1 = []
    for t, (x, y) in last_positions1.items():
        if t in last_positions2:
            remove_keys1.append(t)
    
    for t in remove_keys1:
        del last_positions1[t]

    for t in remove_keys1:
        people_enter[t] = (x, y)
        counter2.add(t)

    remove_keys2 = []
    for t, (x, y) in last_positions2.items():
        if t in last_positions1:
            remove_keys2.append(t)
    
    for t in remove_keys2:
        del last_positions2[t]

    for t in remove_keys2:
        people_exit[t] = (x, y)
        counter1.add(t)


    return counter1, counter2, people_enter, people_exit
