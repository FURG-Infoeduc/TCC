import csv
with open('1 - Deficientes2018comMEDIAfinalINT.csv', 'rt') as csvfile:
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('5 - Deficientes2018semZERADOScomMEDIAfinalSTRING.csv', 'wt', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(header)
        for row in spamreader:
            filtrado = row[0].split(";")
            if(filtrado[0]!='0'):
                writer.writerow(row)