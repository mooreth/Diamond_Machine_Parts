import math
import os

out_dir='D:/Diamond_Machine_Parts//Diamond_Machine_Parts/Classic Hydrocarbon Bearing/' #CHANGE THIS
data_file_out='temp.txt' #this is a file that holds all the atoms before the header info is written to the final file which is another name down below
output_data=os.path.join(out_dir,data_file_out)

atoms = {}
group_list = []
atom_count = 0
num_atom_types = 0 
num_atom_types_and_mass = []
Xs =  []
Ys = []
Zs = []

####get hi/lo xyz
def get_hi_and_low(x,y,z):    
    all_dim = []   
    Xs.append(x)
    Ys.append(y)
    Zs.append(z) 
    padding = 10
    
    X_low =  min(Xs)
    X_high = max(Xs)
    all_dim.append(X_high)
    
    Y_low =  min(Ys)
    Y_high = max(Ys)
    all_dim.append(Y_high)
    
    Z_low =  min(Zs)
    Z_high = max(Zs)
    all_dim.append(Z_high)
    
    #print("highest value", max(all_dim))
    highest_value = max(all_dim)
    
    if X_low < 0:
        X_low_pad = math.floor(X_low - padding)
    else:
        X_low_pad = math.floor(X_low + padding)
        
    if X_high < 0:
        X_high_pad = math.floor(X_high - padding)
    else:
        X_high_pad = math.floor(X_high + padding)
    
    if Y_low < 0:
        Y_low_pad = math.floor(Y_low - padding)
    else:
        Y_low_pad = math.floor(Y_low + padding)
        
    if Y_high < 0:
        Y_high_pad = math.floor(Y_high - padding)
    else:
        Y_high_pad = math.floor(Y_high + padding)   
        
    if Z_low < 0:
        Z_low_pad = math.floor(Z_low - padding)
    else:
        Z_low_pad = math.floor(Z_low + padding)
        
    if Z_high < 0:
        Z_high_pad = math.floor(Z_high - padding)
    else:
        Z_high_pad = math.floor(Z_high + padding)        
    return X_low_pad, X_high_pad, Y_low_pad, Y_high_pad, Z_low_pad, Z_high_pad 

# find groups 
# getNodes returns an indexer that contains all nodes corresponding to a NSL string
# (e.g., all nodes called "anchor"), and [0] returns the first element of that indexer
anchor = SAMSON.getNodes('"anchor"')[0] # the anchor node in the document
roty = SAMSON.getNodes('"roty"')[0] # the rotz node in the document


anchorNodes = anchor.getGroupNodes() # the nodes in the anchor group
rotyNodes = roty.getGroupNodes() # the nodes in the rotz group
# find all atoms

atomIndexer = SAMSON.getNodes('node.type atom')
for atom in atomIndexer:
    atom_count = atom_count + 1
    
    symbol = atom.elementSymbol
    if symbol == "C":
        atom_mass = 12.0109997
        atom_type = 1
        if atom_type not in num_atom_types_and_mass:
            num_atom_types_and_mass.append(atom_type)
            num_atom_types_and_mass.append(str(atom_mass)) 
    else:
        atom_mass = 1.00796998
        atom_type = 2
        if atom_type not in num_atom_types_and_mass:
            num_atom_types_and_mass.append(atom_type)
            num_atom_types_and_mass.append(str(atom_mass))        
        

    x = SBQuantity.angstrom(atom.getX()).value
    y = SBQuantity.angstrom(atom.getY()).value
    z = SBQuantity.angstrom(atom.getZ()).value
    get_hi_and_low(x,y,z)
    
    group = 'free'
    #Jig one, an anchor jig
    if anchorNodes.hasNode(atom):
        group = 'anchor'
        if symbol == "C":
            atom_type = 3
            if atom_type not in num_atom_types_and_mass:
                num_atom_types_and_mass.append(atom_type)
                num_atom_types_and_mass.append(str(atom_mass))            
        else:
            atom_type = 4
            if atom_type not in num_atom_types_and_mass:
                num_atom_types_and_mass.append(atom_type)
                num_atom_types_and_mass.append(str(atom_mass))            

   #Jig two, a rotational group   
    elif rotyNodes.hasNode(atom):
        group = 'roty'    
        if symbol == "C":
            atom_type = 5
            if atom_type not in num_atom_types_and_mass:
                num_atom_types_and_mass.append(atom_type)
                num_atom_types_and_mass.append(str(atom_mass))            
        else:
            atom_type = 6
            if atom_type not in num_atom_types_and_mass:
                num_atom_types_and_mass.append(atom_type)
                num_atom_types_and_mass.append(str(atom_mass))            
    
    atoms[atom] = {'atom_count':atom_count,'part_num':"1", 'atom_type':atom_type, 'symbol':symbol, 'x_position':x, 'y_position':y, 'z_position':z, 'group':group }   #this creates a nested dictionary for each atom so we can calculate the centroid of each group
    #print(f"{symbol} {atom_type} {x:.4f} {y:.4f} {z:.4f} {group}")
    
    
for key, value in atoms.items():
    atom_index_write = str(atoms[key].get('atom_count'))
    molecule_tag_write = atoms[key].get('part_num')
    atom_type_write = str(atoms[key].get('atom_type'))
    x_cor_write = str(round(   atoms[key].get('x_position'),3)    )
    y_cor_write = str(round(   atoms[key].get('y_position'),3)    )
    z_cor_write = str(round(   atoms[key].get('z_position'),3)    )
                      
    atom_data_line = atom_index_write + "   " + molecule_tag_write + "   "  + atom_type_write + "   " + x_cor_write + "000"+  "   " + y_cor_write + "000"+ "  " + z_cor_write + "000" + "\n" #the "000" were added for a quick test, needs to be formated correctly
    with open(output_data,'a') as new_data:
        new_data.write(atom_data_line)


num_atom_types = len(num_atom_types_and_mass)/2

print("number of atoms in structure is : ", atom_count)
print("number of atoms types in structure is : ", num_atom_types)
dimensions =  get_hi_and_low(0,0,0)
#get the centroid of all the groups. Might really only be necessary for rotational fixes, but could have other uses. 
for key, value in atoms.items():       
    this_atoms_group = atoms[key].get('group')
    if this_atoms_group not in group_list:
                group_list.append(this_atoms_group)
print("Jig List", group_list)
for jigs in group_list:
    X_SUM = 0
    Y_SUM = 0
    Z_SUM = 0
    ATOM_NUM = 0    
    for key2, value2 in atoms.items(): 
        if jigs == atoms[key2].get('group'):
            ATOM_NUM = ATOM_NUM + 1
            X_SUM = X_SUM + atoms[key2].get('x_position')
            Y_SUM = Y_SUM + atoms[key2].get('y_position')
            Z_SUM = Z_SUM + atoms[key2].get('z_position')  
    x_centroid = round(X_SUM/ATOM_NUM, 3)
    y_centroid = round(Y_SUM/ATOM_NUM, 3)
    z_centroid = round(Z_SUM/ATOM_NUM, 3)
    print(jigs, "centroid", x_centroid, y_centroid, z_centroid)    
    
comment = "hydrocarbon bearing" + "\n" #CHANGE THIS
num_atoms = " " + str(atom_count) + " atoms" + "\n"
atom_type_header = " " + str(int(num_atom_types)) + " atom types" + "\n"
xhilo = "   "+ str(dimensions[0]) + "          "+ str(dimensions[1]) + "      "+ "xlo xhi"+  "\n"
yhilo = "   "+ str(dimensions[2]) + "          "+ str(dimensions[3]) + "      "+ "ylo yhi"+  "\n"
zhilo = "   "+ str(dimensions[4]) + "          "+ str(dimensions[5]) + "      "+ "zlo zhi"+  "\n"
masses_header = " Masses" + "\n"
atoms_header = " Atoms " + "#molecular"+ "\n"

f = open('D:/Diamond_Machine_Parts//Diamond_Machine_Parts/Classic Hydrocarbon Bearing/Hydrocarbon_Bearing.data', "a") #CHANGE THIS
#f = open(output_data, "a")
f.write(comment)
f.write("\n")
f.write(num_atoms)
f.write("\n")
f.write(atom_type_header)
f.write("\n")
f.write(xhilo)
f.write(yhilo)
f.write(zhilo)
f.write("\n")
f.write(masses_header)
f.write("\n")

for items in range(0, len(num_atom_types_and_mass), 2):
    f.write(" " + str(num_atom_types_and_mass[items]) + " " +  str(num_atom_types_and_mass[items+1]) + "\n")
f.write("\n")
f.write(atoms_header)
f.write("\n")    
    
with open(output_data,'r') as atom_data:
    igot = atom_data.readlines()
    for line_raw in igot:
        f.write(line_raw)
f.close()
os.remove(output_data)
