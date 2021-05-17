genetic_code = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                "TAT":"Y", "TAC":"Y", "TAA":"O", "TAG":"U",
                "TGT":"C", "TGC":"C", "TGA":"X", "TGG":"W",
                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Z",
                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                "ATT":"I", "ATC":"I", "ATA":"J", "ATG":"M",
                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                "AAT":"N", "AAC":"B", "AAA":"K", "AAG":"K",
                "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def DNA_to_protein(s):
    protein=""
    for i in range (0, len(s), 3):
        codon = s[i:i+3]
        protein += genetic_code[codon]
    return protein

import re
import os
os.chdir("/Users/jiayifan/IBI1_2020-21/Practical8")
fr=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
fw=open('oneline.fa', 'w')
line=fr.read()
r=line.replace('\n','')
s=re.sub('>','\n>',r)
fw.write(s)
fr.close()
fw.close()

seq=open('oneline.fa', 'r')
gene=''
name=[]
pro=[]
for line in seq:
    if line.startswith('>'):
        if not line.find('unknown function') == -1:
            name.append(''.join(re.findall(r'^>([^ ]+)_mRNA',line)))
            gene=''.join(re.findall(r'\[Source:[A-Z]{3};Acc:\w{10}\]([A-Z]+)',line))
            pro.append(DNA_to_protein(gene))

# Asks the user to input a filename as the new fasta file to be written to;
new=open('unknown_function_protein.fa', 'w')

for i in range (0,len(name)):
    new.write('>' + name[i] + ' ' + str(len(pro[i])) + '\n')
    new.write(pro[i] + '\n')

new.close()
os.remove('oneline.fa')
