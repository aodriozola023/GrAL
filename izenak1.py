import os
path = 'C:/Users/Ane/Desktop/Gehitutakoak'
files = os.listdir(path)

hitza = 'Octopus_'

for file in files:
    if file[0].isdigit():
        berria = hitza+file
        os.rename(os.path.join(path, file), os.path.join(path, berria))
