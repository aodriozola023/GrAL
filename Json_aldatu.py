import re

with open('Marrazkiak_aldatuta.json') as f:
    data = f.read()
    bilatu = re.findall('"name"\:\ "[a-z]*",\n[ ]* "type":\ "unknown"', data)
    print(bilatu[:5])
    print()
    klaseak = set()
    for i in range(len(bilatu)):
        elem = bilatu[i]
        klase = elem[9:-30]
        klaseak.add(klase)

    print(klaseak)
    for elem in klaseak:
        data = data.replace('"name": "%s",\n          "type": "unknown"'%(elem),
                            '"name": "%s",\n          "type": "%s"'%(elem,elem))
    with open('Marrazkiak.json','w') as f_out:
        f_out.write(data)
    print()
    print(len(klaseak))
        
