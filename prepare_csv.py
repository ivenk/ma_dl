import os
import shutil

inp_dir_name = '../input/lfw.out'
out_dir_name = '../output/lfw.list.out'

csv = open('../input/labels.csv', 'w')
csv.write('name;tags\n')

os.makedirs(out_dir_name)

directories = os.listdir(inp_dir_name)

fileCounter = 0

label_range = 128

def buildLabelText(code):
    bin = f'{int(code):0128b}'
    reverse_bin = bin[::-1]
    text = ""
    
    for i in range(128):
        if reverse_bin[i] == "1":
            text = text + str(i) + " "
    
    return text

for d in directories:
    if d.startswith('.'):
        continue

    img_dir_name = inp_dir_name + '/' + d
    files = os.listdir(img_dir_name)
    for f in files:
        file_name = 'i' + str(fileCounter)
        shutil.copyfile(img_dir_name + '/'+  f, out_dir_name + '/' + file_name + '.png')

        # file csv
        print(d)
        csv.write(file_name + ';' + buildLabelText(d) + '\n')

        fileCounter = fileCounter + 1

csv.close()
