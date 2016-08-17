import glob
import numpy as np
import matplotlib.pyplot as plt
import dynamics.functions
import csv

# import files
loops = open('data/andrewmodel_data/loopfile.txt', "r")
dead = open('data/andrewmodel_data/deadfile.txt', "r")

# create a list of name of models in order
lst_model_nm = dynamics.functions.get_lst_models()
print (lst_model_nm)
   
# radius
r = 40

# number of node
n_dead = 0

#list of lists of csv data
lst_lst_output = []

# every time you look at a node in the file
for aline1 in dead:    
    aline1 = aline1.strip()
    lst_output = []
    
    plt.figure()
    for p_state, st in enumerate(aline1):
        
        nm_model = lst_model_nm[p_state]
        
        if st == '0':
            color = 'blue'
            
        elif st == '1':
            color = 'red'
        
        datafile = open('data/andrewmodel_data/andrew_view.txt', "r")
        
        # read andrew_view.txt line by line until it finds 
        # the same name in the line. 
        x = 0
        y = 0
        for aline2 in datafile:

            data_line = aline2.split()
            
            nm = data_line[0]
            px = data_line[1]
            py = data_line[2]

                   
            if nm == nm_model:

                x = float(px) * 1.5
                y = float(py) * (-1) * 1.5

                break
            
        datafile.close()
        
        if x == 0 and y == 0:
            print(p_state,st,nm_model)
        #draw a circle  
        plt.scatter(x, y, s=r, c=color, alpha=0.5)

        #draw the name of the circle
        plt.text(x, y+50, nm_model, fontsize=5)
                

    #draw the number of the node as title
    plt.title(n_dead, fontsize=6)

    gf = dynamics.functions.check_model('GF', aline1)
    gfh = dynamics.functions.check_model('GF_High', aline1)
    trail = dynamics.functions.check_model('Trail', aline1)
    uv = dynamics.functions.check_model('UV', aline1)
    cdh1 = dynamics.functions.check_model('Cdh1', aline1)
    cycA = dynamics.functions.check_model('CyclinA', aline1)
    cycB = dynamics.functions.check_model('CyclinB', aline1)
    sene = dynamics.functions.check_model('Senescence', aline1)
    p16 = dynamics.functions.check_model('p16', aline1)

    phase = dynamics.functions.check_phase(cdh1, cycA, cycB)
    senescence = dynamics.functions.check_sene(sene, p16)

    #draw the node as subtitle
    plt.xlabel('GF='+gf+','+ 'GFh='+gfh+',' +'Trail='+trail+',' + 'UV='+uv+','
        +'Dead='+'1'+',' 'Senescence='+str(senescence)+',' + 'CC='+'0'+',' 
        +'Phase='+phase+',' + 'Other cycle='+'/', fontsize=10)

    lst_output.append(gf), lst_output.append(gfh), lst_output.append(trail), lst_output.append(uv), lst_output.append('1'),
    lst_output.append(senescence), lst_output.append('0'), lst_output.append(phase), lst_output.append('/')

    lst_lst_output.append(lst_output)

    # plt.show()
    plt.savefig('../../images/dead_andrew/' + str(n_dead), dpi=300)
       
    n_dead += 1

dead.close()

n_loop = 0
p_loop = 0

lst_cc = []

for aline in loops:
    aline = aline.strip()
    lst_cyle = []
    if aline == '':
        cc = dynamics.functions.check_cc(lst_cyle)
        lst_cc.append(cc)
        lst_cyle = []
    else:
        lst_cyle.append(aline)
loops.close()

loops = open('data/andrewmodel_data/loopfile.txt', "r")
p_cc = 0

for aline1 in loops: 

    plt.figure() 
    aline1 = aline1.strip()
    cc = lst_cc[p_cc]
    lst_output = []

    if cc == 1:
        occ = 0
    else:
        occ = 1

    if aline1 == '':

        n_loop += 1
        p_loop = 0
        p_cc += 1

        lst_output.append(gf), lst_output.append(gfh), lst_output.append(trail), lst_output.append(uv), lst_output.append('0'),
        lst_output.append('/'), lst_output.append(cc), lst_output.append('/'), lst_output.append(occ)

        lst_lst_output.append(lst_output)

    else: 
        p_state = 0
        for st in aline1:
            nm_model = lst_model_nm[p_state]

            if st == '0':
                color = 'blue'
                
            elif st == '1':
                color = 'red'
            
            datafile = open('data/andrewmodel_data/andrew_view.txt', "r")
            
            for aline2 in datafile:

                data_line = aline2.split()               
                nm = data_line[0]
 
                if nm == nm_model:
                    px = data_line[1]
                    py = data_line[2]
                    x = float(px) * 1.5
                    y = float(py) * (-1) * 1.5
                    
            datafile.close()

               
            #draw a circle  
            plt.scatter(x, y, s=r, c=color, alpha=0.5)

            #draw the name of the circle
            plt.text(x, y+50, nm_model, fontsize=5)
                    
            p_state += 1

        #draw the number of the node as title
        plt.title(str(n_loop)+ '/' +str(p_loop), fontsize=10)

        gf = dynamics.functions.check_model('GF', aline1)
        gfh = dynamics.functions.check_model('GF_High', aline1)
        trial = dynamics.functions.check_model('Trail', aline1)
        uv = dynamics.functions.check_model('UV', aline1)

        #draw the node as subtitle
        plt.xlabel('GF='+gf+','+ 'GFh='+gfh+',' +'Trail='+trail+',' + 'UV='+uv+','
        +'Dead='+'0'+',' 'Senescence='+'/'+',' + 'CC='+str(cc)+',' 
        +'Phase='+'/'+',' + 'Other cycle='+str(occ) 
        ,fontsize=10)

        # plt.show()
        plt.savefig('../../images/loop_andrew/' + str(n_loop)+ ':' + str(p_loop), dpi=300)
           
        p_loop += 1

#write a csv file
label = ["GF", "GFh", "Trail", "UV", "Dead", "Senescence", "Cell Cycle", "Phase", "Other Cycle"]

filen = "output.csv"
with open(filen, "w") as f:
    writer = csv.writer(f)
    writer.writerow(label)
    for output in lst_lst_output:
        writer.writerow(output)

loops.close()
    
    
