#import glob module
import glob

#import random
import random

# create a method for a dynamis


class dynamics:
    def __init__(self):
        self.nObject = []
        self.d_Object = {}
        
    def addnObject(self, objct):
        self.nObject.append(objct)
        
    def addd_Object(self, key, value):
        self.d_Object[key] = value
        
    def getnObject(self):
        return self.nObject
        
    def getd_Object(self):
        return self.d_Object
        
    def shownmObjects(self):
        for o in self.nObject:
            return o

# create a dynamics          
D = dynamics()

#create a method for each object
class model:
    def __init__(self, name, dOfstate, lst):
        self.name = name
        self.dictionary = dOfstate
        self.list = lst
        
    def __str__(self):
        return self.name
        
    def getname(self):
        return self.name
        
    def getD(self):
        return self.dictionary
        
    def getL(self):
        return self.list
  
# open the file that you have the causal relationsions
#CausalFile = open('/Users/hyuga/Documents/iPS_cell_reprogramming/Text/CausalFile.txt', "w")

# open the writing file that you save the numberical data
ActionFile = open('/Users/hyuga/Documents/iPS_cell_reprogramming/Text/ActionFile.txt', "w")

# invoke every file in a folder
for filename in glob.glob('/Users/hyuga/Dropbox/Regan_Group/toy_model/Andrew_lastmodel_WT/*'):
    
    #open a file
    fIn = open(filename, "r")
    
    #number of the line you are looking at
    n_line = 0
    
    #make a dictionary of the state
    dOfstate = {}
    
    #create dictionaries of sums of output when the affecting object is off and on
    dOfSoff ={}
    dOfSon ={}
    
    #make a dictionary of the relationshiop between affecting objects and the target object
    dOfR = {}
    
    #you look at each line of the file
    for aline in fIn:
        
        #the first line
        if n_line == 0:
                
            #make a list of objects
            lstOfobjects = aline.split()
            
            #name of model
            nmOfmodel = lstOfobjects[-1]
            
            #remove the name of model from the list
            lstOfobjects.pop() 
            
            #create a list of names of affecting objects
            lstOfNofAOs = lstOfobjects
            
            #count number of objects in a file
            nOfkeys = len(lstOfNofAOs)   
            
            #make a dictionary of sum of the number of the target object when the affecting object is off
            lstOfSoff = {}
            
            #make a dictionary of sum of the number of the traget object when the affecting object is on
            lstOfSon = {}
            
            for ob in lstOfNofAOs:
                
                #add the name of the affecting object to the key of the dictionary
                dOfSoff[ob] = 0
                dOfSon[ob] = 0
        
        #the other line    
        elif n_line > 0:
            
            #make a list of states of every object
            lstOfstates = aline.split()
            
            #output from the previous condition
            value = int(lstOfstates[-1])
            
            #creates a list of states of affecting objects
            lstOfstates.pop()
            
            lst_S_AOs = lstOfstates
            
            #the previous condition
            key = ""
            
            #make the previous condition
            for s in lst_S_AOs:
                key = key + s
                
            #add the output to the dictionary
            dOfstate[key] = value
            
            #every time you see the affecting object, you check the output of the target object
            for ob in lstOfNofAOs:
                
                #the positon of the object
                pOfAOs = lstOfNofAOs.index(ob)
                
                #state of the affecting object
                SofAO = lst_S_AOs[pOfAOs]
                
                #if the affecting object is off
                if SofAO == "0":
                    dOfSoff[ob] += value
                    
                #if the affeting object is on
                elif SofAO == "1":
                    dOfSon[ob] += value
                    
            
        #add 1 to the count of the line    
        n_line += 1
        
    #each affecing object
    for ob in lstOfNofAOs:
        
        #if the Sum of the output when the affecing object is off is greater than on
        if dOfSoff[ob] > dOfSon[ob]:
            
            #the dictionary of the relation between the affecting and the target object is 0
            dOfR[ob] = 0
            
        #if the Sum of the output when the affecting object is off is smaller than on
        elif dOfSoff[ob] < dOfSon[ob]:
            
            #the dictionary of the relation between the affecting and the target object is 1
            dOfR[ob] = 1
            
        #if the Sum of the output when the affecting object is off is equal to when it's on
        elif dOfSoff[ob] == dOfSon[ob]:
             
             #the dictionary of the relation btween the affecting and the target object is 2
             dOfR[ob] = 2
             
    #    #write the relationship between the affecting objects and the target object in the file
    #    CausalFile.write(ob + "  ")
    #    CausalFile.write(str(dOfR[ob]) + "  ")
    #    CausalFile.write(nmOfmodel+ "\n")
    #CausalFile.write("" + "\n")
        
    #create a new instance   
    p = model(nmOfmodel, dOfstate, lstOfNofAOs)
    
    #add name of the model to the list of the dynamics
    D.addnObject(nmOfmodel)
    
    #add data of the model to the dictionary of the dynamics
    D.addd_Object(nmOfmodel, p)
         
    #close the file 
    fIn.close()
    
##close the file that you have the causal relations 
#CausalFile.close()

#create a list of all objects in the dynamics    
lst_all_models = D.getnObject()

# dictionary in which keys are nodes and values lists of leading states
D_nodes = {}

# list of nodes
L_nodes = []

#make a list of all sequence
lst_all_seq = []

nOFinput = 5

for i in range(nOFinput):
    
    #create a dictionary of the state of each object at the time
    dOfs = {}
    
    #create the initial 
    Istate = ""
    
    #create a list of existed states
    lst_Exs = []
    
    #input the initial state of each object by random chance
    for m in lst_all_models:
        #take input by the module
        i = random.randint(0, 1)
        
        #add the intial state to the dictionary
        dOfs[m] = i
        
        #conjugate the initial state of each
        Istate = Istate + str(i)
    
    while Istate in lst_all_seq:
        
        for m in lst_all_models:
            #take input by the module
            i = random.randint(0, 1)
            
            #add the intial state to the dictionary
            dOfs[m] = i
            
            #conjugate the initial state of each
            Istate = Istate + str(i)
        
    #add the initial state to the list of all sequences
    lst_all_seq.append(Istate)
    
    #create the whole state of the time
    WholeS = ""
    
    Wholes = Istate
    
    #the value of the node
    node = ""
     
    while WholeS not in lst_Exs:
        
        #add a new whole state to the memory
        lst_Exs.append(WholeS)
        
        WholeS = ""
    
        #find new states of every object
        for m in lst_all_models:    
            
            #create a string of previous state of affecting objects
            pS_AOs = ""
            
            #create a list of names of affecting objects
            lst_nm_AOs = D.d_Object[m].getL()
            
            #create a dictionary of the relationship between previous and new state of the object
            d_pn = D.d_Object[m].getD()
                
            #looking at the state of each affecting object
            for ao in lst_nm_AOs:
                
                #the previous state of each affecting object
                pS_AO = dOfs[ao]
                
                #conjugate the state of the previous stage
                pS_AOs += str(pS_AO)
                    
            #create the new state of the object
            nS_O = d_pn[pS_AOs]
                    
            #update the dictionary of the states of all
            dOfs[m] = nS_O
            
            #create a new whole state
            WholeS = WholeS + str(nS_O)
            
        #add the state to the list of all sequence
        lst_all_seq.append(WholeS)
    
    #define the final state
    node = WholeS    
    
    #write the inital state on the top-left of the file
    ActionFile.write(Istate + " ")
    
    #find the existed state except initial and final states
    lst_track = lst_Exs[1:-2]
    
    #every time you have the leading state
    for state in lst_track:
       ActionFile.write(state + "\n")
       ActionFile.write(state + " ")
        
    #write the final state on the lower-right of the file
    ActionFile.write(node + "\n")
    ActionFile.write("\n")
    
    # add the new final state to the list of final states and the dictionary
    if node not in L_nodes:
        L_nodes.append(node)
        
        D_nodes[node] = lst_Exs
        
    #if the final state is already in the list, the leading states are to be stored in the dictionary
    elif node in L_nodes:
        
        for s in lst_Exs:
            
            if s not in D_nodes[node]:
            
                D_nodes[node].append(s)
                
#close the file that you have the list of numerical states
ActionFile.close()

#open the file that has all final states
f_states = open('/Users/hyuga/Documents/iPS_cell_reprogramming/Text/f_states.txt', "w")

i = 0

for node in L_nodes:
    
    #open the file in which you write the numbering of final states
    tr_states = open('/Users/hyuga/Documents/iPS_cell_reprogramming/Text/nodes/' + str(i) + ".txt", "w")
    
    tr_states.write(node + "\n")
    tr_states.write("\n")
    
    f_states.write(node + "\n")
    
    for Ls in D_nodes[node]:
        
        tr_states.write(Ls + "\n")
        
    tr_states.write("\n")
    
    i += 1
    
    tr_states.close()
    
f_states.close()

print len(L_nodes)
