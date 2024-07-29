import re

path = 'C:/Users/aviad/OneDrive/Documents/DataSets/people_ir/CAMEL_GT/Seq13'

with open(path + '/Seq13-IR.txt', 'r') as file:
    line = file.readline()
    # out = line.split('\t|\n')

    # Regex pattern splits on substrings "; " and ", "
    out = re.split('\t|\n', line)
    file_name = out[0]
    while len(file_name) < 6:
        file_name = '0' + file_name
    file_name = file_name + '.jpg'

    with open(path+'/labels/'+file_name, 'w') as out_file:
        out_file.write(out[1] + '\t' + out[2] + '\t' + out[3] + '\t' + out[4] + '\t' + out[5] + '\n')
    a=1