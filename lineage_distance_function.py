def lineage_distance(lin1:str, lin2:str):
    
    progenitors = set((lin1.split(' ')[0], lin2.split(' ')[0]))
    if len(progenitors) == 1: # meaning the two cells have the same embryonic progenitor
        lin1 = lin1.replace(' ', '') # removing spaces
        lin2 = lin2.replace(' ', '')
        smaller_lin = min([lin1, lin2], key=len) # finding the smaller lineage to iterate over
        for i in range(len(smaller_lin)): # finding the index after the most recent common ancestor (MRCA)
            if lin1[i] != lin2[i]:
                break

        d1, d2 = len(lin1[i:-1]), len(lin2[i:-1]) 
        dist = d2 + d1 + 1
        return dist

    elif progenitors == {'AB', 'D'} or progenitors == {'MS', 'D'}: # 4 divisions separate both of these pairs of progenitors
        lin1_after_prog, lin2_after_prog = lin1.split(' ')[1], lin2.split(' ')[1]
        dist = len(lin1_after_prog) + len(lin2_after_prog)
        dist += 4 
        return dist

    elif progenitors == {'AB','MS'} or progenitors == {'AB', 'C'} or progenitors == {'MS', 'C'}: # 3 divisions separate them
        lin1_after_prog, lin2_after_prog = lin1.split(' ')[1], lin2.split(' ')[1]
        dist = len(lin1_after_prog) + len(lin2_after_prog)
        dist += 3 
        return dist

    elif progenitors == {'D','C'}: # 2 divisions separate them
        lin1_after_prog, lin2_after_prog = lin1.split(' ')[1], lin2.split(' ')[1]
        dist = len(lin1_after_prog) + len(lin2_after_prog)
        dist += 2 
        return dist

    