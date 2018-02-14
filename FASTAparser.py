import matplotlib.pyplot as plt
import re
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
import time

start = time.time()

#elements
H = {'name' : 'hydrogen', 'volume' : '5.15', 'numberofelectrons' : '1'}
C = {'name' : 'carbon', 'volume' : '16.44', 'numberofelectrons' : '6'}
N = {'name' : 'nitrogen', 'volume' : '2.49', 'numberofelectrons' : '7'}
O = {'name' : 'oxygen', 'volume' : '9.13', 'numberofelectrons' : '8'}
Na = {'name' : 'sodium', 'volume' : '4.45', 'numberofelectrons' : '11'}
Mg = {'name' : 'magnesium', 'volume' : '1.56', 'numberofelectrons' : '12'}
P = {'name' : 'phosphorus', 'volume' : '3.37', 'numberofelectrons' : '15'}
S = {'name' : 'sulfur', 'volume' : '26.09', 'numberofelectrons' : '16'}
Cl = {'name' : 'chlorine', 'volume' : '24.84', 'numberofelectrons' : '17'}
K = {'name' : 'potassium', 'volume' : '11.01', 'numberofelectrons' : '19'}
Ca = {'name' : 'calcium', 'volume' : '4.19', 'numberofelectrons' : '20'}
Fe = {'name' : 'iron', 'volume' : '7.99', 'numberofelectrons' : '26'}
Co = {'name' : 'cobalt', 'volume' : '7.99', 'numberofelectrons' : '27'}
Ni = {'name' : 'nickel', 'volume' : '8.18', 'numberofelectrons' : '28'}
Cu = {'name' : 'copper', 'volume' : '8.78', 'numberofelectrons' : '29'}
Zn = {'name' : 'zinc', 'volume' : '9.85', 'numberofelectrons' : '30'}
Br = {'name' : 'bromine', 'volume' : '31.54', 'numberofelectrons' : '35'}
I = {'name' : 'iodine', 'volume' : '44.60', 'numberofelectrons' : '53'}
elements_dic = {'H' : H,'C' : C,'N' : N,'O' : O,'Na' : Na,'Mg' : Mg,'P' : P,'S' : S,'Cl' : Cl,'K' : K,'Ca' : Ca,'Fe' : Fe,
                   'Co': Co,'Ni' : Ni,'Cu' : Cu,'Zn' : Zn,'Br' : Br,'I' : I}
#amino-acids
A = {'name' : 'alanine', 'volume' : '89.27', 'numberofelectrons' : '38'}
C = {'name' : 'cysteine', 'volume' : '112.84', 'numberofelectrons' : '54'}
D = {'name' : 'aspartic acid', 'volume' : '114.43', 'numberofelectrons' : '59'}
E = {'name' : 'glutamic acid', 'volume' : '138.81', 'numberofelectrons' : '67'}
F = {'name' : 'phenyalalanine', 'volume' : '190.84', 'numberofelectrons' : '78'}
G = {'name' : 'glycine', 'volume' : '63.76', 'numberofelectrons' : '30'}
H = {'name' : 'histidine', 'volume' : '157.46', 'numberofelectrons' : '72'}
I = {'name' : 'isoleucine', 'volume' : '163.01', 'numberofelectrons' : '62'}
K = {'name' : 'lysine', 'volume' : '165.08', 'numberofelectrons' : '71'}
L = {'name' : 'leucine', 'volume' : '163.09', 'numberofelectrons' : '62'}
M = {'name' : 'methionine', 'volume' : '165.82', 'numberofelectrons' : '70'}
N = {'name' : 'asparagine', 'volume' : '122.35', 'numberofelectrons' : '60'}
P = {'name' : 'proline', 'volume' : '121.29', 'numberofelectrons' : '52'}
Q = {'name' : 'glutamine', 'volume' : '146.91', 'numberofelectrons' : '68'}
R = {'name' : 'arginine', 'volume' : '190.33', 'numberofelectrons' : '85'}
S = {'name' : 'serine', 'volume' : '93.50', 'numberofelectrons' : '46'}
T = {'name' : 'threonine', 'volume' : '119.61', 'numberofelectrons' : '54'}
V = {'name' : 'valine', 'volume' : '138.16', 'numberofelectrons' : '54'}
W = {'name' : 'tryptophan', 'volume' : '226.38', 'numberofelectrons' : '98'}
Y = {'name' : 'tyrosine', 'volume' : '194.63', 'numberofelectrons' : '86'}
amino_acids_dic = {'A' : A,'C' : C,'D' : D,'E' : E,'F' : F,'G' : G,'H' : H,'I' : I,'K' : K,'L' : L,'M' : M,'N' : N,
                   'P': P,'Q' : Q,'R' : R,'S' : S,'T' : T,'V' : V,'W' : W,'Y' : Y,}
#nucleotides DNA
Adenine = {'formula' : 'C5H4N5', 'volume' : '133.9', 'NexH' : '2'}
Cytozine = {'formula' : 'C4H4ON3', 'volume' : '115.6', 'NexH' : '2'}
Guanin = {'formula' : 'C5H4ON5', 'volume' : '146.6', 'NexH' : '3'}
Thymine = {'formula' : 'C4H3O2N2', 'volume' : '133.6', 'NexH' : '1'}
Backbone = {'formula' : 'C5H7O5P', 'volume' : '168.1', 'NexH' : '0'}
#nucleotides RNA
Adenine = {'formula' : 'C5H4N5', 'volume' : '139.2', 'NexH' : '2'}
Cytozine = {'formula' : 'C4H4ON3', 'volume' : '115.0', 'NexH' : '2'}
Guanin = {'formula' : 'C5H4ON5', 'volume' : '145.9', 'NexH' : '3'}
Uracil = {'formula' : 'C4H3O2N2', 'volume' : '110.8', 'NexH' : '1'}
Backbone = {'formula' : 'C5H7O6P', 'volume' : '176.1', 'NexH' : '1'}

# File save dialog
def file_save(text):
    f = Tk.filedialog.asksaveasfile(mode='w', defaultextension=".dat")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    f.write(text)
    f.close()

# Load and add in list only amino-acids
def load_and_parse():
    file_path = Tk.filedialog.askopenfilename(initialdir = "~/test",title = "Select file",
                                              filetypes = (("amino-acid sequence file","*.fasta"),("all files","*.*")))
    amino_acids = []
    with open(file_path) as f:
        plotlist = f.read()
    for str in plotlist:
        if str not in amino_acids_dic: continue
        for s in str: amino_acids.append(s)
    return amino_acids
# File load dialog
def file_load():
    file_path = Tk.filedialog.askopenfilename(initialdir = "~/test",title = "Select file",                                             filetypes = (("chemical formula","*.txt"),("all files","*.*")))
    with open(file_path) as f:
        text = f.read()
    return text

def electron_density_protein(amino_sequence):
        el_dens = 0
        num = 0
        vol = 0
        numb = 0
        for amino in amino_sequence:
            if not isinstance(amino, str): return "Wrong format of input data!"
            a = amino_acids_dic.get(amino)
            print(a.get('name') + ' volume: ' +a.get('volume') + ' number of electrons: ' + a.get('numberofelectrons'))
            vol += (float(a.get('volume')))
            numb += (int(a.get('numberofelectrons')))
        return numb/vol


def electron_density_buffer(chemical_formula):
    print(chemical_formula)
    list = re.findall(r'([A-Z][a-z]*)(\d*)', chemical_formula)
    el_dens = 0
    num = 0
    vol = 0
    numb = 0
    for element in list:
        n = element[1]
        if n == '': n = 1
        if not isinstance(element[0], str): return "Wrong format of input data!"
        e = elements_dic.get(element[0])
        print('NAME: ' + e.get('name') + ' VOLUME: ' + e.get('volume') + ' NUMBER OF ELECTRONS: ' + \
              e.get('numberofelectrons') + ' NUMBER OF ATOMS: ' + str(n))
        vol += (float(e.get('volume')))
        numb += (int(e.get('numberofelectrons')))
    return numb / vol


#///////////////////////START PROGRAM////////////////////////////////////////////////////////////
# open and read pdb file

root = Tk.Tk()
root.withdraw()
#x = load_and_parse()
#print(electron_density_protein(x))
x = file_load()
print('mean electron density: ' + str(electron_density_buffer(x)) + ' (e/A^3)')
end = time.time()
print (" Time consumed : " + str (end - start) + " sec")

