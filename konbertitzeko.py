import re

with open('Marrazkiak_COCO.json','r') as f_in:
    with open('Marrazkiak_COCO_azkena.json','w') as f_out:
        data = f_in.read()
        bilatu = re.findall('"id":[0-9]*,"name":"[a-z\_]*","supercategory":"[a-z\_]*"', data)
        klaseak = set()
        for i in range(len(bilatu)):
            elem = bilatu[i]
            buk = elem.find('"',15,)
            klase = elem[15:buk]
            klaseak.add(klase)
        print(klaseak)
        

    
