NTD = input ("Input NTD: ")

def printNTDname(NTD):
    if NTD == 'A':
        result = 'Adenine'
    elif NTD == 'T':
        result = 'Thymine'
    elif NTD == 'C':
        result = 'Cytosine'
    elif NTD == 'G':
        result = 'Guanine'
    elif NTD == 'U':
        result = 'Uracil'
    else:
        result = 'Please enter right NTD'
    return result


print (printNTDname(NTD))
