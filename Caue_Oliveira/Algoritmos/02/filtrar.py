#Codigo para eliminar candidatos que não são deficientes

import csv
with open('MICRODADOS_ENEM_2018.csv', 'rt') as csvfile:
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('Deficientes2018.csv', 'wt', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(header)
        for row in spamreader:
            filtrado = row[0].split(";")
            if(filtrado[28]=='1')or(filtrado[29]=='1')or(filtrado[30]=='1')or(filtrado[31]=='1')or(filtrado[32]=='1')or(filtrado[33]=='1')or(filtrado[34]=='1')or(filtrado[35]=='1')or(filtrado[36]=='1')or(filtrado[37]=='1')or(filtrado[38]=='1')or(filtrado[39]=='1')or(filtrado[40]=='1'):
                writer.writerow(row)