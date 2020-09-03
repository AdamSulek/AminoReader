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
                TCT|TCC|TCA|TCG|AGT|AGC|ACT|ACC|ACA|ACG|TGG|TAT|TAA)'
    result = ""
    with open(file, 'r') as stream:
        for line in stream.readlines():
            for word in line.split():
                if re.match(pattern, word):
                    result += word
    return result

if __name__ == "__main__":
    # tekst = " Alignment: C:\Users\PostDoc\Desktop\subcloning (1).txt \
    #           ....|....| ....|....| ....|....| ....|....| ....|....| ....|....| \
    #           CAAGGAGATG GCGCCCAACA GTCCCCCGGC CACGGGGCCT GCCACCATAC CCACGCCGAA"
    file = "codon_notation.txt"
    print(cutter(file))
    # pattern = '(AAA|GCT)'
    # # pattern = '[ACTG]'
    # lista = ["AAA", "GCT", "GTC", "CAA", "nic", "A", "Adam"]
    # for i in lista:
    #     if re.match(pattern, i):
    #         if re.match('[A-Z]+', i):
    #             print(i)
