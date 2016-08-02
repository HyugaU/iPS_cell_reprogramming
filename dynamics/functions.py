import glob


#function that returns the list of models from toymodel
def get_lst_models():
    lst_models = []
    
    for filename in glob.glob('data/AndrewModel_After_SBHD_Aug1_2016/*'):

        file = open(filename, "r")
        n_lines = 0
    
        for aline in file:
    
            if n_lines == 0:
        
                lst = aline.split()
                nm = lst[-1]
                lst_models.append(nm) 
    
                n_lines += 1
    
        file.close()
    
    return lst_models

#lst of models
lst_models = get_lst_models()

#function that checks the state of the model
def check_model(m, s):
    p_model = lst_models.index(m)
    s_model = s[p_model]
    return s_model

#function that checks which phase the model stucks in
def check_phase(cdh1, cycA, cycB):
    if cdh1 == '1' and cycA == '0' and cycB =='0':
        return 'G0/1'
    elif cycA =='1' and cycB =='1':
        return 'G2'
    else:
        return 'anything else'

#function that checks the state stucks in senescence
def check_sene(sene, p16):
    if sene =='0' and p16 =='0':
        return 1
    elif sene =='1' and p16 =='1':
        return 0
    else:
        return 'anything else'

#function that checks the cycle is CC or not
def check_cc(lst):
    sum_ras = 0
    sum_dna = 0
    len_cycle = len(lst)
    cc=1
    for st in lst:
        ras = int(check_model('Ras', st))
        dna = int(check_model('4N_DNA', st))
        sum_ras += ras
        sum_dna += dna
    summ = sum_ras + sum_dna
    if summ ==0 or summ == len_cycle or summ == 2*len_cycle:
        cc=0
    else:
        cc=1
    return cc





	