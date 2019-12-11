#Codigo para agregar idade em grupos

import csv
with open('50 - Deficientes2018media2posicoesFILTRADO.csv', 'rt') as csvfile:
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('60 - Deficientes2018media2posicoes.csv', 'wt', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(header)
        for row in spamreader:
            filtrado = row[0].split(";")
            if(filtrado[55]<='510'):
                filtrado[55] = "Ruim"
            else:			
                if(filtrado[55]>'510' and filtrado[55]<'840'):
                    filtrado[55] = "Bom"
            row = filtrado
            writer.writerow(row)