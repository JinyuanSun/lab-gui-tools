def gen_fragment(peptide):
    frag_list = []
    for left, aa in enumerate(peptide):
        if aa in ['R', 'K']:
            frag_list.append(peptide[:left+1])
        for right, _ in enumerate(peptide):
            if right > left:
                if peptide[left:right][-1] in ['R','K'] and peptide[left-1] in ["R", "K"]:
                    if len(peptide[left:right]) > 1:
                        frag_list.append(peptide[left:right])
    return frag_list

def mw_cal(peptide, modification):
    aa_weight = {'A':89.05, 'C':121.02, 'D':133.04, 'E': 147.05, 'F':165.08, 
                 'G':75.03, 'H':155.07, 'I':131.09, 'K': 146.11, 'L':131.09, 
                 'M':149.05, 'N': 132.05, 'P': 115.06, 'Q': 146.07, 'R': 174.11, 
                 'S': 105.04, 'T': 119.06, 'V': 117.08,'W':204.09,'Y':181.07}
    w = 0
    for i, aa in enumerate(peptide):
        w += aa_weight[aa] - 18.01
    # return [round(w+18.01,1), round(w+55.04,1)]
    return [str(round(w+x,1)) for x in modification]

def peptide_fragment_mass(peptide, modification, output_path):
    frags = gen_fragment(peptide)
    with open(f"{output_path}/frags.csv", 'w+') as of:
        for frag in frags:
            result = mw_cal(frag, modification)
            of.write(",".join([frag] + result)+"\n")


if __name__ == '__main__':
    peptide = "ALSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTLTYGVLCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNFNSHNVYITADKQKNGIKAYFKIRHNVEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSVLSKDPNEKRDHMVLLEFVTAAGITHGASLFG"
    modification = [18.01, 55.04]
    output_path = './'
    peptide_fragment_mass(peptide, modification, output_path)