import os
path = 'C:/Users/Ane/Desktop/Gehitutakoak3'

for direkt in os.listdir(path):
    bidea = os.path.join(path,direkt)
    if os.path.isdir(bidea):
        files = os.listdir(bidea)

        #hitza = 'Octopus_'
        hitza = direkt

        for file in files:
            if file[0].isdigit():
                berria = hitza+'_'+file
                os.rename(os.path.join(bidea, file), os.path.join(bidea, berria))
