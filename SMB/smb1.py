import os
from subprocess import PIPE
import subprocess


with open('text.txt', 'r') as file_data:
    for line in file_data:
        data = line.split(',')
        #print(data[0] ,data[2])
        print('-----------' + data[1]+'.txt' + '----------')
        for i in data:
            cmd = 'tree ' + data[0] + data[2]
        Info = os.system(cmd)
            #f = open(data[1]+'.txt', 'w')
            #subprocess.call(cmd, stdout= f)

        #cmd2 = f'echo {os.system(cmd)}' > str(data[1]) + '.txt'
        with open(data[1] + '.txt', 'w') as file:
            output = subprocess.run(cmd,shell = True, stdout = PIPE).stdout
            #subprocess.run(cmd, stdout = file)
            file.write(output.decode())

    print('finished')

#print(os.system(cmd))
