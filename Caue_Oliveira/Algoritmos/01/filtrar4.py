import csv
with open('3 - Deficientes2018semZERADOS.csv', 'rt') as csvfile:
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('6 - Deficientes2018mediaSTRING.csv', 'wt', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(header)
        for row in spamreader:
            filtrado = row[0].split(";")
            if(filtrado[5]<'455'):
                filtrado[5] = "Ruim"
            else:			
                if(filtrado[5]>='455' and filtrado[5]<'560'):
                    filtrado[5] = "Regular"
                else:
                    if(filtrado[5]>='560'):
                        filtrado[5] = "Bom"				
            row = filtrado
            writer.writerow(row)