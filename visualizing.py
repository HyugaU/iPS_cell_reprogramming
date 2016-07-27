import graphics

class Object:
    
    def __init__(self, name, state, pX, pY):
        self.name = name
        self.state = state
        self.pX = pX
        self.pY = pY                     
        
    #import glob module
import glob

#create a method for a dynamis
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
    def __init__(self, name, dOfstate, lst, state, pX, pY):
        self.name = name
        self.dictionary = dOfstate
        self.list = lst
        self.state = state
        self.pX = pX
        self.pY = pY
        
    def __str__(self):
        return self.name
        
    def getname(self):
        return self.name
        
    def getD(self):
        return self.dictionary
        
    def getL(self):
        return self.list
        
    def getX(self):
        return self.pX
        
    def getY(self):
        return self.pY
        
    def getState(self):
        return self.state
        
    def updateState(self, new_state):
        self.state = new_state

#invoke every file in a folder
for filename in glob.glob('/Users/hyuga/Dropbox/Regan_Group/toy_model/Andrew_lastmodel_WT/*'):
    
    #open the data file
    DataFile = open('/Users/hyuga/Documents/iPS_cell_reprogramming/Files/datafile.txt', "r")
    
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
            lst_objects = aline.split()
            
            #name of model
            nm_model = lst_objects[-1]
            
            #remove the name of model from the list
            lst_objects.pop() 
            
            #create a list of names of affecting objects
            lst_nm_AOs = lst_objects
            
            #count number of objects in a file
            n_keys = len(lst_nm_AOs)   
            
            #make a dictionary of sum of the number of the target object when the affecting object is off
            lstOfSoff = {}
            
            #make a dictionary of sum of the number of the traget object when the affecting object is on
            lstOfSon = {}
            
            for ob in lst_nm_AOs:
                
                #add the name of the affecting object to the key of the dictionary
                dOfSoff[ob] = 0
                dOfSon[ob] = 0
        
        #the other line    
        elif n_line > 0:
            
            #make a list of states of every object
            lst_states = aline.split()
            
            #output from the previous condition
            value =  lst_states.pop() # int(lst_states[-1])
            
            lst_S_AOs = lst_states
            
            #the previous condition
            key = ""
            
            #make the previous condition
            for st in lst_S_AOs:
                key = key + st
                
            #add the output to the dictionary
            dOfstate[key] = value
            
            #every time you see the affecting object, you check the output of the target object
            for ob in lst_nm_AOs:
                
                #the positon of the object
                p_AOs = lst_nm_AOs.index(ob)
                
                #state of the affecting object
                S_AO = lst_S_AOs[p_AOs]
                
                #if the affecting object is off
                if S_AO == "0":
                    dOfSoff[ob] = dOfSoff[ob] + int(value)
                    
                #if the affeting object is on
                elif S_AO == "1":
                    dOfSon[ob] = dOfSon[ob] + int(value)
                    
        #add 1 to the count of the line    
        n_line += 1
        
    #each affecing object
    for ob in lst_nm_AOs:
        
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
              
    #each line in the data file
    for aline in DataFile:
    
        #split the line into a list
        lst_data = aline.split()
        
        #call the name 
        nm_object = lst_data[0]
              
        #if the name of the object is equal to the name just defined
        if nm_model == nm_object:
            
            #call the position x
            position_X = lst_data[1]
        
            #call the position y 
            position_Y = lst_data[2]
            
            #updata the position of x and y
            pX = float(position_X) / 3.5 + 1250
            pY = float(position_Y) / 3.5 - 150
            
    #create a new instance   
    p = model(nm_model, dOfstate, lst_nm_AOs,"0" ,pX, pY)
    
    #add name of the model to the list of the dynamics
    D.addnObject(nm_model)
    
    #add data of the model to the list of the dynamics
    D.addd_Object(nm_model, p)
         
    #close the file 
    fIn.close()

#create a list of all objects in the dynamics    
lst_all_models = D.getnObject()

#open the file that has nodes
nodes = open('/Users/hyuga/Documents/iPS_cell_reprogramming/Files/nodes.txt', "r")

nm_nodes = 0

for aline in nodes:

    alinesplit = aline.split()
    aline = alinesplit[0]
    print len(aline)
    
    #make a new window
    win = graphics.GraphWin("Graphics", 1200, 800)
    
    #create a dictionary in which keys are name of models and values are the properties of models
    d_graphics = {}
    
    #index of the object in the list of objects in the dynamics
    index_of_object_in_aline = 0
      
    #every time you have object
    for ob in lst_all_models:
        
        p = D.d_Object[ob]
        
        name = p.getname()
        
        X = p.getX() 
                
        Y = p.getY()
        
        lst_AOs = p.getL()
        
        #define the position
        pt = graphics.Point(X, Y)
        
        #draw a circle
        cir = graphics.Circle(pt, 5)
        cir.draw(win)
        
        #add the circle to the dictionary
        d_graphics[name] = cir
        
        #draw the name of model 
        pt_for_name = graphics.Point(X,Y-10)
        t = graphics.Text(pt_for_name, name)
        t.draw(win)
        
        for AO in lst_AOs:
            
            A_object = D.d_Object[AO]
            
            x2 = A_object.getX()
            y2 = A_object.getY()
            
            pt2 = graphics.Point(x2, y2)
            
            line = graphics.Line(pt, pt2)
            line.draw(win)
    
    #every state in the whole state string
    for state in aline:
        
        nm = lst_all_models[index_of_object_in_aline]
        
        #recall the model from the list in dynamics 
        model = D.d_Object[nm]
        
        name_model = model.getname()
        
        #add 1 to the index of object in the list of objects
        index_of_object_in_aline += 1
        
        if state == "0":
            
            d_graphics[name_model].setFill("blue")
            
        elif state == "1":
                
            d_graphics[name_model].setFill("red")
            
    #print the state and the number on the top
    pt_for_number = graphics.Point(40, 20)
    tx = graphics.Text(pt_for_number, "number  " + str(nm_nodes))
    tx.draw(win)
    
    pt_for_state = graphics.Point(250, 40)
    tx = graphics.Text(pt_for_state, aline)
    tx.draw(win)
    
    win.save('/Users/hyuga/Documents/images/' + nm_nodes + '.png')
    
    nm_nodes += 1    
    
    #close the window
    win.getMouse()
    win.close()


