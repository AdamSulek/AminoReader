import re

def cutter(file):
    '''
        This function delete non-coding fragment from sequence
        e.g. white signs, numbers, non-coding character.
    '''
    pattern = '(AAA|GCT|GCC|GCA|GCG|CGT|CGC|CGA|CGG|AGA|TAC|GTT|GTC| \
                AGG|AAT|AAC|GAT|GAC|TGT|TGC|CAA|CAG|GAA|GAG|GAA|GTA| \
                GAG|GGT|GGC|GGA|GGG|CAT|CAC|ATT|ATC|ATA|CTT|CTC|GTG| \
                CTA|CTG|TTA|TTG|AAG|ATG|TTT|TTC|CCT|CCC|CCA|CCG| \
                TCT|TCC|TCA|TCG|AGT|AGC|ACT|ACC|ACA|ACG|TGG|TAT|)'

    result = ""
    codon = ""
    # for letter in seq:
    with open(file, 'r') as stream:
        for index, line_val in enumerate(stream.readlines()):
            print("index: {}".format(index))
            print("line_val: {}".format(line_val))
            # if re.match(pattern, line_val):
            #     print(line_val)
        # codon += letter
        # if len(codon) == 3:
        #     for letter in combination:
        #         if codon == letter:
        #             self.result += codon
        #     codon = ""
    return result



if __name__ == "__main__":
    # tekst = " Alignment: C:\Users\PostDoc\Desktop\subcloning (1).txt \
    #           ....|....| ....|....| ....|....| ....|....| ....|....| ....|....| \
    #           CAAGGAGATG GCGCCCAACA GTCCCCCGGC CACGGGGCCT GCCACCATAC CCACGCCGAA"
    file = "codon_notation.txt"
    print(cutter(file))
    pattern = '(AAA|GCT)'
    lista = ["AAA", "GCT", "GTC", "CAA"]
    for i in lista:
        if re.match(pattern, i):
            print("chuj")
