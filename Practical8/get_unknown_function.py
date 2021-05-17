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
sequence=[]
name=[]
for line in seq:
    if line.startswith('>'):
        if not line.find('unknown function') == -1:
            name.append(''.join(re.findall(r'^>([^ ]+)_mRNA',line)))
            sequence.append(''.join(re.findall(r'\[Source:[A-Z]{3};Acc:\w{10}\]([A-Z]+)',line)))

new=open('unknown_function.fa', 'w')
for i in range (0,len(name)):
    new.write('>' + name[i] + ' ' + str(len(sequence[i])) + '\n')
    new.write(sequence[i] + '\n')

new.close()
os.remove('oneline.fa')
