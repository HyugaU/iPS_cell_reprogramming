import glob
import random
import dynamics

# create a dynamics
D = dynamics.Dynamics()

# open the file that you have the causal relationsions
dyn = open('data/andrew_dynamics.txt', "w")

# open the writing file that you save the numberical data
#network = open('data/network.txt', "w")

# invoke every file in a folder
for filename in glob.glob('data/AndrewModel_After_SBHD_Aug1_2016/*.csv'):

    # open a file
    modelfile = open(filename, "r")

    # number of the line you are looking at
    n_line = 0

    # make a dictionary of the relationship between the target model and affecting modesl
    d_rl = {}

    # create dictionaries of sums of output when affecting models is off and on
    d_outp_off = {}
    d_outp_on = {}

    # make a dictionary of the relationshiop between affecting objects and the target object
    d_rls = {}

    # you look at each line of the file
    for aline in modelfile:

        # the first line
        if n_line == 0:

            # make a list of names on first line
            lst_nm_1line = aline.split()

            # name of model
            nm_model_file = lst_nm_1line[-1]

            # remove the name of model from the list
            lst_nm_1line.pop()

            # create a list of names of affecting models
            lstOfNofAOs = lst_nm_1line

            # count number of objects in a file
            nOfkeys = len(lstOfNofAOs)

            # make a dictionary of sum of the number of the target object when the affecting object is off
            lstOfSoff = {}

            # make a dictionary of sum of the number of the traget object when the affecting object is on
            lstOfSon = {}

            for ob in lstOfNofAOs:
                # add the name of the affecting object to the key of the dictionary
                d_outp_off[ob] = 0
                d_outp_on[ob] = 0

        # the other line
        elif n_line > 0:

            # make a list of states of every object
            lstOfstates = aline.split()

            # output from the previous condition
            value = int(lstOfstates[-1])

            # creates a list of states of affecting objects
            lstOfstates.pop()

            lst_S_AOs = lstOfstates

            # the previous condition
            key = ""

            # make the previous condition
            for s in lst_S_AOs:
                key = key + s

            # add the output to the dictionary
            d_rls[key] = value

            # every time you see the affecting object, you check the output of the target object
            for ob in lstOfNofAOs:

                # the positon of the object
                pOfAOs = lstOfNofAOs.index(ob)

                # state of the affecting object
                SofAO = lst_S_AOs[pOfAOs]

                # if the affecting object is off
                if SofAO == "0":
                    d_outp_off[ob] += value

                # if the affeting object is on
                elif SofAO == "1":
                    d_outp_on[ob] += value

        # add 1 to the count of the line
        n_line += 1

    # each affecing object
    for ob in lstOfNofAOs:

        # if the Sum of the output when the affecing object is off is greater than on
        if d_outp_off[ob] > d_outp_on[ob]:

            # the dictionary of the relation between the affecting and the target object is 0
            d_rl[ob] = 0

        # if the Sum of the output when the affecting object is off is smaller than on
        elif d_outp_off[ob] < d_outp_on[ob]:

            # the dictionary of the relation between the affecting and the target object is 1
            d_rl[ob] = 1

        # if the Sum of the output when the affecting object is off is equal to when it's on
        elif d_outp_off[ob] == d_outp_on[ob]:

            # the dictionary of the relation btween the affecting and the target object is 2
            d_rl[ob] = 2

    # #write the relationship between the affecting objects and the target object in the file
        dyn.write(ob + "  ")
        dyn.write(str(d_rl[ob]) + "  ")
        dyn.write(nm_model_file+ "\n")
    dyn.write("\n")

    # create a new instance
    p = dynamics.Model(nm_model_file, d_rls, lstOfNofAOs)

    # add name of the model to the list of the dynamics
    D.add_nm_model(nm_model_file)

    # add data of the model to the dictionary of the dynamics
    D.add_model(nm_model_file, p)

    # close the file
    modelfile.close()

##close the file that you have the causal relations 
dyn.close()

# create a list of all objects in the dynamics
lst_all_models = D.get_lst_nm_models()

# dictionary in which keys are ends and values lists of leading states
d_ends = {}

lst_ends = []

# list of dead
lst_dead = []

# list of roops
lst_loops = []

# make a list of all sequence
lst_all_seq = []

#if the end is dead or not
che_loop = True

nOFinput = 300000

count = 0

for i in range(nOFinput):

    # create a dictionary of the state of each object at the time
    dOfs = {}

    # create the initial
    Istate = ""

    # create a list of existed states
    lst_Exs = []

    #a loop
    loop = []

    # input the initial state of each object by random chance
    for m in lst_all_models:
        # take input by the module
        i = random.randint(0, 1)

        # add the intial state to the dictionary
        dOfs[m] = i

        # conjugate the initial state of each
        Istate = Istate + str(i)

    while Istate in lst_all_seq:
        for m in lst_all_models:
            # take input by the module
            i = random.randint(0, 1)

            # add the intial state to the dictionary
            dOfs[m] = i

            # conjugate the initial state of each
            Istate = Istate + str(i)

    # add the initial state to the list of all sequences
    lst_all_seq.append(Istate)

    # create the whole state of the time
    WholeS = ""

    Wholes = Istate

    # the value of the node
    end = ""

    while WholeS not in lst_Exs:

        # add a new whole state to the memory
        lst_Exs.append(WholeS)

        WholeS = ""

        # find new states of every object
        for m in lst_all_models:

            # create a string of previous state of affecting objects
            pS_AOs = ""

            # create a list of names of affecting objects
            lst_nm_AOs = D.get_models()[m].getL()

            # create a dictionary of the relationship between previous and new state of the object
            d_pn = D.get_models()[m].getD()

            # looking at the state of each affecting object
            for ao in lst_nm_AOs:
                # the previous state of each affecting object
                pS_AO = dOfs[ao]

                # conjugate the state of the previous stage
                pS_AOs += str(pS_AO)

            # create the new state of the node
            ns_n = d_pn[pS_AOs]

            # update the dictionary of the states of all
            dOfs[m] = ns_n

            # create a new whole state
            WholeS = WholeS + str(ns_n)

        # add the state to the list of all sequence
        lst_all_seq.append(WholeS)

    # define the final state
    end = WholeS

    #check the end associate with a loop or dead
    if end == lst_Exs[-1]:
        che_loop = False

    else:
        che_loop = True

        #position of starting point
        p_star = lst_Exs.index(end)

        for l in lst_Exs[p_star:]:
            loop.append(l)

    # write the inital state on the top-left of the file
    #network.write(Istate + " ")

    # find the existed state except initial and final states
    lst_track = lst_Exs[1:-2]

    # every time you have the leading state
    #for state in lst_track:
    #    network.write(state + "\n")
    #   network.write(state + " ")

    # write the final state on the lower-right of the file
    #network.write(end + "\n")
    #network.write("\n")

    # add the new final state to the list of final states and the dictionary
    if end not in lst_ends:
        if che_loop == False:
            lst_dead.append(end)
        elif che_loop == True:
            lst_loops.append(loop)

        d_ends[end] = lst_Exs
        lst_ends.append(end)

    # if the final state is already in the list, the leading states are to be stored in the dictionary
    elif end in lst_ends:

        for s in lst_Exs:

            if s not in d_ends[end]:
                d_ends[end].append(s)

    count += 1
    print (count)

# close the file that you have the list of numerical states
#network.close()

# open the file that has dead states and loops
deadfile = open('data/deadfile.txt', "w")
loopfile = open('data/loopfile.txt', "w")


# number of end
i = 0

for dead in lst_dead:

    # open the file in which you write the numbering of final states
    tr_states = open('data/ends/' + str(i) + ".txt", "w")

    tr_states.write(dead + "\n")
    #tr_states.write("\n")

    deadfile.write(dead + "\n")

    for Ls in d_ends[dead]:
        tr_states.write(Ls + "\n")

    tr_states.write("\n")

    i += 1

    tr_states.close()

deadfile.close()

for loop in lst_loops:

    tr_states = open('data/ends/' + str(i) + ".txt", "w")

    for state in loop:

        tr_states.write(state + "\n")
        loopfile.write(state + "\n")

    tr_states.write("\n")

    for state in d_ends[loop[0]]:
        tr_states.write(state + "\n")

    tr_states.write("\n")

    loopfile.write("\n")

    tr_states.close()

    i += 1

loopfile.close()

print (len(lst_ends))

