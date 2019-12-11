#Codigo para agregar idade em grupos

import csv
with open('media_final_3.csv', 'rt') as csvfile:
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('media_final_3_NOVOOOOOOOO.csv', 'wt', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(header)
        for row in spamreader:
            filtrado = row[0].split(";")
            if(filtrado[55]<'465'):
                filtrado[55] = "Ruim"
            else:			
                if(filtrado[55]>='465' and filtrado[55]<'565'):
                    filtrado[55] = "Regular"
                else:
                    if(filtrado[55]>='565'):
                        filtrado[55] = "Bom"
            row = filtrado
            writer.writerow(row)