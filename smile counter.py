import re
#valid symbols: eyes: : ;  
#nose: - ~
#smiling: ) D
def is_smile(smile:str):
    if len(smile)==2:
        if smile in [":)",":D",";D",";)"]:
            return True
    elif len(smile)==3:
        if smile in [":-)",":-D",";-D",";-)",":~)",":~D",";~D",";~)"]:
            return True
    return False

#через регулярные выражения
def find_smiles(smiles):
    valid_smiles=re.findall(r"[:;][-~]?[)D]"," ".join(smiles))
    print(valid_smiles)

find_smiles([';]', ':[', ';*', ':$', ';-D'])