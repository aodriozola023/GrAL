import re
import csv
#import pandas as pd

with open('Marrazkiak_COCO.json','r') as f_coco:
    with open('Marrazkiak_proba_2.json','r') as f_json:
        with open('Marrazkiak.csv','w', newline='') as f_out:
            #zerrenda = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
            writer = csv.writer(f_out, delimiter=',')
            writer.writerow(['filename', 'width', 'height'])
            
            data_coco = f_coco.read()
            bilatu = re.findall('"width":[0-9]*,"height":[0-9]*,"file_name":"[^\"]*"', data_coco)
            for elem in bilatu:
                buk_w = elem.find(',"height"')
                w = elem[8:buk_w]
                buk_h = elem.find(',"file')
                h = elem[buk_w+10:buk_h]
                file = elem[buk_h+14:-1]
                writer.writerow([file, w, h])
                
            data_json = f_json.read()
            
                
