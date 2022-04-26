import numpy as np
with open('todas_pals.txt') as f:
    lines = f.readlines()
#print(type(lines))

cinco=[]
for x in lines:
    if len(x)==6:
        cinco.append(x)
cinco_random=np.random.permutation(cinco)

output_file = open('cinco.txt', 'w')

for palabra in cinco:
    output_file.write(palabra)

output_file.close()

output_file = open('cinco_random.txt', 'w')

for palabra in cinco_random:
    output_file.write(palabra)

output_file.close()
