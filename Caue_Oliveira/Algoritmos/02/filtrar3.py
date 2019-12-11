#Codigo para calcular as médias finais

import csv
with open('10 - Deficientes2018realizaramDUASprovas.csv', 'rt') as csvfile:
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('20 - Deficientes2018comMEDIAfinal.csv', 'wt', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(header)
        for row in spamreader:
            filtrado = row[0].split(";")
            media = (float(filtrado[90])+float(filtrado[91])+float(filtrado[92])+float(filtrado[93])+float(filtrado[109]))/5.0
            media = (round(media,1))		
            filtrado[137] = media
            row = filtrado
            writer.writerow(row)