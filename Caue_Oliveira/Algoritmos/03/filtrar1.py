#Codigo para agregar idade em grupos

import csv
with open('30 - Deficientes2018media5posicoesFILTRADO.csv', 'rt') as csvfile:
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('40 - Deficientes2018media5posicoesFILTRADOstring.csv', 'wt', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(header)
        for row in spamreader:
            filtrado = row[0].split(";")
            if(filtrado[55]<='430'):
                filtrado[55] = "Ruim"
            else:			
                if(filtrado[55]>='430' and filtrado[55]<'480'):
                    filtrado[55] = "Regular"
                else:
                    if(filtrado[55]>='480' and filtrado[55]<'540'):
                        filtrado[55] = "Bom"
                    else:
                        if(filtrado[55]>='540' and filtrado[55]<'620'):
                            filtrado[55] = "Otimo"
                        else:
                            if(filtrado[55]>='620' and filtrado[55]<'840'):
                                filtrado[55] = "Excelente"	
            row = filtrado
            writer.writerow(row)