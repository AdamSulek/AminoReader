import os

def str_checker(inscription):
    '''
        The function recognize the float and integer value and than
            return True

        otherwise
            return False
    '''
    if inscription:
        as_list = list(inscription)
        if as_list and as_list.count('.') <= 1:
            for char in range(len(as_list)):
                if not as_list[char].isdigit() and as_list[char] != '.'\
                                           or as_list[0] == '.' \
                                           or as_list[len(as_list)-1] == '.':
                    return False
            return True

def amino_dict(filepath):
    '''
        This function return dictionary of three character aminoacids notation
        with appropriate codons.
    '''
    amino_di = {}
    with open(str(filepath)) as file:
        lines = file.readlines()
        for line in lines:
            three = ""
            amino = ""
            codons = []
            for char in range(len(line)):
                if char == len(line) - 1:
                    amino_di[amino] = codons
                else:
                    if char % 4 != 3:
                        three += line[char]
                    if len(three) == 3:
                        if char == 2:
                            amino = three
                        if char > 3:
                            codons.append(three)
                        three = ""
    return amino_di

def mass_dict(filepath):
    '''
        This function return dictionary of three character aminoacids notation
        with appropriate mass.
    '''
    mass = {}
    with open(str(filepath)) as file:
        lines = file.readlines()
        for line in lines:
            three = ""
            digit = ""
            number = False
            for char in range(len(line)):
                if number:
                    digit += line[char]
                if char < 3:
                    three += line[char]
                if line[char].isdigit() and not number:
                    digit += line[char]
                    number = True
            mass[three] = float(digit)
    return mass

def acronyms(filepath):
    '''
        This function return dictionary of three character aminoacids notation
        and corrsponding aminoacids in one character notation.
    '''
    acronym = {}
    with open(str(filepath)) as file:
        lines = file.readlines()
        for line in lines:
            three = ""
            for char in range(len(line)):
                if char < 3:
                    three += line[char]
                if char == len(line)-1:
                    letter = line[len(line)-2]
            acronym[three] = letter
    return acronym

if __name__ == '__main__':

    mass_path = os.path.join(os.getcwd(), "docs/baseMass.def")
    print(mass_path)
    massdict = mass_dict(mass_path)
    print(massdict)
