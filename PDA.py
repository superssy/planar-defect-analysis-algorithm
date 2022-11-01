############################################################
#    pda value      0      1     2     3     4     5    6  #
# structure type   other  fcc   ISF   HCP   ESF   TB   BCC #
############################################################
from ovito.data import *
import numpy as np
def modify(frame, data):
    pda = data.particles_.create_property('planar defect', dtype=int, components=1)
    N = 12
    finder = NearestNeighborFinder(N, data)
    def ESF_TWIN(k, neighbor):
        for i in neighbor:
            index = i
            fcc, hcp = 0, 0
            if data.particles['Structure Type'][index] == 1:               
                for neigh in finder.find(index):
                    if data.particles['Structure Type'][neigh.index] == 1:
                        fcc += 1
                    elif data.particles['Structure Type'][neigh.index] == 2:
                        hcp += 1
                if (5<= fcc <= 6) and (5<= hcp <= 6):
                    pda[k] = 4
                    break
            else:
                pass  
        if pda[k] != 4:
            pda[k] = 5             
    def HCP(index):
        fcc, hcp =0, 0
        pb = []
        neighbor = []
        for neigh in finder.find(index):
            neighbor.append(neigh.index)
            if data.particles['Structure Type'][neigh.index] == 1:
                fcc += 1
            elif data.particles['Structure Type'][neigh.index] == 2:
                hcp += 1
                pb.append(neigh.index)
        if hcp >= 11:
            pda[index] = 3
            for i in pb:
                pda[i] = 3
        elif (2<= fcc <= 3) and ( 8<= hcp <= 9):
            if pda[index] != 3:
                pda[index] = 2
            else:
                pass      
        elif (5<= fcc <= 6) and ( 5<= hcp <= 6):
            ESF_TWIN(index, neighbor)
        else:
            pass
    for index in range(data.particles.count):
        yield(index / data.particles.count)
        if data.particles['Structure Type'][index] == 2:
            HCP(index)
        elif data.particles['Structure Type'][index] == 1:
            pda[index] = 1
        elif data.particles['Structure Type'][index] == 3:
            pda[index] = 6
        else:
            pda[index] = 0
