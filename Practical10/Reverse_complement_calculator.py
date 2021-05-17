def reverse(s):
    cmpdict = {'A':'T','G':'C','C':'G','T':'A'}
    cmplmt = ''
    s = s.upper()
    for i in range (0, len(s)):
        nucleotide = s[i:i+1]
        cmplmt += cmpdict[nucleotide]
    print('complement strand:' + cmplmt)

# example
seq = 'atCGATCGATCGATCG'
reverse(seq)
