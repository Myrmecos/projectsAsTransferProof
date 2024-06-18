file = open('/Users/entomophile/AntFJ2023/antFJ_complete.csv')
file1 = open('/Users/entomophile/AntFJ2023/antFJ_version1.csv','w')
file_lines=file.readlines()
for line in file_lines:
    print(line)
    line=line.replace('Kartidris_sp1','Monomorium_sp2')
    line=line.replace('Ectommomyrmex','Ectomomyrmex')
    line=line.replace('Kaitidris_sp1','Monomorium_sp2')
    line=line.replace('Kartidirs_sp1','Monomorium_sp2')
    line=line.replace('Hypoponera+sp2','Hypoponera_sp2')
    line = line.replace('Brachyponra', 'Brachyponera')
    line = line.replace('Dolichoderus_sp1','Paratrechina_sp1')
    file1.write(line)


