import glob
import numpy as np
import matplotlib.pyplot as plt

# import files
datafile = open('/Users/hyuga/Documents/iPS/Files/datafile.txt', "r")
nodes = open('/Users/hyuga/Documents/iPS/Files/nodes.txt', "r")

# create a list of name of models in order
lst_model_nm = []
for filename in glob.glob('/Users/hyuga/Dropbox/Regan_Group/toy_model/Andrew_lastmodel_WT/*'):
    
    fIn = open(filename, "r")
    
    n_lines = 0
    
    for aline in fIn:
        
        if n_lines == 0:
            lst = aline.split()
            nm = lst[-1]
            lst_model_nm.append(nm)
            
            n_lines += 1
            
    fIn.close()
   
# radius
r = 40

# number of node
n_node = 0

# every time you look at a node in the file
for aline1 in nodes:    
    aline1 = aline1.split()[0]
    
    p_state = 0
    
    for st in aline1:
        
        nm_model = lst_model_nm[p_state]
        
        if st == '0':
            color = 'blue'
            
        elif st == '1':
            color = 'red'
        
        datafile = open('/Users/hyuga/Documents/iPS/Files/datafile.txt', "r")
        
        for aline2 in datafile:

            data_line = aline2.split()
            
            nm = data_line[0]
            px = data_line[1]
            py = data_line[2]
            
            if nm == nm_model:
                
                x = float(px) * 1.5
                y = float(py) * (-1) * 1.5
                
        datafile.close()
           
        #draw a circle  
        plt.scatter(x, y, s=r, c=color, alpha=0.5)

        #draw the name of the circle
        plt.text(x, y+50, nm_model, fontsize=5)
                
        p_state += 1

    #draw the number of the node as title
    plt.title(n_node, fontsize=10)

    #draw the node as subtitle
    plt.xlabel(aline1, fontsize=10)

    # plt.show()
    plt.savefig('/Users/hyuga/Documents/iPS/graphics/image_node/' + str(n_node), dpi=300)
       
    n_node += 1

nodes.close()
    
    
