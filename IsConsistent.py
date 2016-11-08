def consistOFzero(vector):
    OFzero = True
    for i in vector:
        if i != 0:
            OFzero = False
            break;
    return OFzero
def numberOFrows(V):
    return len(V)
def numberOfcolums(M):
    return len(M)
def ToReducedRowEchelonForm(M):
    Lead = 0
    rowCount = numberOFrows()