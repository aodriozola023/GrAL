import csv

klasea = 'rainbow'
izena = 'C:/Users/Ane/Desktop/Gehitutakoak2/%s/labels_%s.csv'%(klasea, klasea)

with open('C:/Users/Ane/Desktop/Gehitutakoak2/%s/via_export_csv.csv'%(klasea),'r') as f:
    with open(izena,'w',newline='') as f_out:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)
        
        zerrenda = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
        writer = csv.writer(f_out, delimiter=',')
        writer.writerow(zerrenda)
        writer.writerow([])
        
        for row in reader:
            fitx = row[0]
            #print(fitx)
            fitx_iz = klasea+'_'+fitx
            datuak = row[5]
            zab_i = datuak.find('"width":')
            luz_i = datuak.find(',"height":')
            zab = datuak[zab_i+len('"width":') : luz_i]
            luz = datuak[luz_i+len(',"height":'):-1]
            if(int(zab)>245):
                zab = 254
            if(int(luz)>245):
                luz = 254
            writer.writerow([fitx_iz, '255', '255', klasea, '0', '0', zab, luz])
    
    
