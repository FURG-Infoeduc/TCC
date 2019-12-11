#Codigo para agregar medias finais em grupos

import csv
with open('20 - Deficientes2018comMEDIAfinal.csv', 'rt') as csvfile:
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('30 - Deficientes2018mediaSTRING.csv', 'wt', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(header)
        for row in spamreader:
            filtrado = row[0].split(";")
            if(filtrado[137]<'465'):
                filtrado[137] = "Ruim"
            else:			
                if(filtrado[137]>='465' and filtrado[137]<'565'):
                    filtrado[137] = "Regular"
                else:
                    if(filtrado[137]>='565'):
                        filtrado[137] = "Bom"				
            row = filtrado
            writer.writerow(row)