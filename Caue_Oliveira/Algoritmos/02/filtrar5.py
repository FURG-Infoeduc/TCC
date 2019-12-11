#Codigo para agregar idade em grupos

import csv
with open('30 - Deficientes2018mediaSTRING.csv', 'rt') as csvfile:
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('40 - Deficientes2018idadeSTRING.csv', 'wt', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(header)
        for row in spamreader:
            filtrado = row[0].split(";")
            print(filtrado[1])
            if(filtrado[6]>='13' and filtrado[6]<='17'):
                filtrado[6] = "Grupo 1"
            else:			
                if(filtrado[6]>'17' and filtrado[6]<='18'):
                    filtrado[6] = "Grupo 2"
                else:
                    if(filtrado[6]>'18' and filtrado[6]<='19'):
                        filtrado[6] = "Grupo 3"
                    else:
                        if(filtrado[6]>'19' and filtrado[6]<='21'):
                            filtrado[6] = "Grupo 4"
                        else:
                            if(filtrado[6]>'21' and filtrado[6]<='25'):
                                filtrado[6] = "Grupo 5"	
                            else:
                                if(filtrado[6]>'25' and filtrado[6]<='35'):
                                    filtrado[6] = "Grupo 6"	
                                else:
                                    if(filtrado[6]>'35' and filtrado[6]<='87'):
                                        filtrado[6] = "Grupo 7"	
            row = filtrado
            writer.writerow(row)