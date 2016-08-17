#open the file
OpenFile = open("data/andrewmodel_data/andrew_view.xgmml", "r")
OutFile = open("data/andrewmodel_data/andrew_view.txt", "w")

#looking at every line
for aline in OpenFile:
    
    #make a list of values of the line 
    lstOfvalues = aline.split()
    
    #if the line starts at node
    if lstOfvalues[0] == "<node":
        
        #recall the label in the list
        label = lstOfvalues[2]
        
        #print the name of the label
        OutFile.write(label[7:-2]+ "   ")
        
        
    #if the line has the values of x and y
    elif lstOfvalues[0] == "<graphics" and len(lstOfvalues) > 3 :
        
        for i in lstOfvalues:
            
            #recall x
            if i[0] == "x":
                x = i[3:-2]
                
            elif i[0] == "y":
                y = i[3:-1]
        
        #print the value of x
        OutFile.write(x + "   ")
        
        #print the value of y
        OutFile.write(y + "  " + "\n")
        
        
    
    
    
    
#close the file
OpenFile.close()
OutFile.close()