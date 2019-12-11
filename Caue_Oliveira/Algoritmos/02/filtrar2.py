#Codigo para eliminar candidatos que não realizaram as duas provas

import csv
with open('0 - Deficientes2018.csv', 'rt') as csvfile:
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('10 - Deficientes2018realizaramDUASprovas.csv', 'wt', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(header)
        for row in spamreader:
            filtrado = row[0].split(";")
            if ( (filtrado[82]=='1') and (filtrado[83]=='1') and (filtrado[84]=='1') and (filtrado[85]=='1') ):
                writer.writerow(row)