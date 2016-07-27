import glob

#open files that have lists of final states
fstates1 = open('/Users/hyuga/Documents/iPS_cell_reprogramming/test1/f_states.txt', "r")
fstates2 = open('/Users/hyuga/Documents/iPS_cell_reprogramming/test2/f_states.txt', "r")

#open files that have dynamics data
dynamics1 = open('/Users/hyuga/Documents/iPS_cell_reprogramming/test1/ActionFile.txt', "r")
dynamics2 = open('/Users/hyuga/Documents/iPS_cell_reprogramming/test2/ActionFile.txt', "r")

#create a list of final states from both files
lst_fstates = []

#create a list of final states from the other file
lst_new_fstates = []

#numbering of final states from one file
nm_fstates1 = 0

#store final states from one file
for aline in fstates1:
    aline = aline.strip()
    lst_fstates.append(aline)
    nm_fstates1 += 1
    
fstates1.close()
   
#numbering of new final states 
nm_fstates2 = nm_fstates1
    
#store new final states from the other file
for aline in fstates2:
    aline = aline.strip()
    if aline not in lst_fstates:
        aline = aline.strip()
        lst_fstates.append(aline)
        lst_new_fstates.append(aline)

fstates2.close()
        
#open the file that will have all final states from both files
fstates = open('/Users/hyuga/Documents/iPS_cell_reprogramming/test3/nodes.txt', "w")

#write all final states
for fstate in lst_fstates:
    fstates.write(fstate + "\n")
    
fstates.close()

#recall a
for afile in glob.glob('/Users/hyuga/Documents/iPS_cell_reprogramming/test3/Fstates/*'):
    
    afl = open(afile, "r")
    new_fstate = ""
    
    for aline in afl:
        
        #if the file is of new final state
        if aline in lst_new_fstates:
            
            new_fstate = aline
            
            newfstate = open('/Users/hyuga/Documents/iPS_cell_reprogramming/test1/Fstates/' + str(nm_fstates2), "w")
            nm_fstates2 += 1
        
        #copy the file
        if len(new_fstate) > 0:
            newfstate.write(aline)
        
    afl.close()
    
    if len(new_fstate) > 0:
        newfstate.close()
        
#open a new dynamics file
dynamics = open('/Users/hyuga/Documents/iPS_cell_reprogramming/test3/dynamics.txt', "w")

#copy one file of dynamics
for aline in dynamics1:
    dynamics.write(aline)
    
#list of states
lst_stats = []

#write a new final state and its leading states
lst_states = []
for aline in dynamics2:
    
    aline = aline.split()
    
    print aline
    
    if len(aline) == 0:
        lst_states = []
    
    else:
        values = aline
        print values
        lst_states.append(values[0])
        lst_states.append(values[1])
        
        if values[1] in lst_new_fstates:
            
            dynamics.write(lst_states[0] + "   ")
            
            p_state = 1
            
            n = len(lst_states) - 2
            
            for i in range(n):
            
                dynamics.write(lst_states[p_state] + "\n")
                dynamics.write(lst_states[p_state] + "   ")
                
                p_state += 1
                
            dynamics.write(lst_states[-1] + "\n")
            dynamics.write("\n")
        
        
dynamics.close()

        
print len(lst_new_fstates)