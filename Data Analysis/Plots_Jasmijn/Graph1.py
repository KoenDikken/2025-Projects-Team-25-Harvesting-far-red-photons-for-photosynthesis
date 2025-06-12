# paketten importeren
import csv
import matplotlib.pyplot as plt

### LIJSTEN
rownumber = 0
wv_abs = []
wv_flu = []
absHPrt = []
emHPrt = []

# Verkrijg data uit excel bestand
with open('Graph1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Slaat de kopregel over

    for row in reader:
        rownumber += 1
        if rownumber >0:
            # Verander elke komma in punt en string --> float
            wv_abs_corrected = float(row[2].replace(',', '.'))
            absHPrt_corrected = float(row[3].replace(',', '.'))
        if rownumber < 202:   
            wv_flu_corrected = float(row[0].replace(',', '.'))
            emHPrt_corrected = float(row[1].replace(',', '.'))
        
        wv_abs.append(wv_abs_corrected)
        wv_flu.append(wv_flu_corrected)
        absHPrt.append(absHPrt_corrected)
        emHPrt.append(emHPrt_corrected)

# Normaliseer de waarden op het tweede maximum
max_em = 2748197.25
max_abs = 0.499314457
abs_norm = [x / max_abs for x in absHPrt]
em_norm = [x / max_em for x in emHPrt]


# Plot grafiek
plt.figure()
plt.plot(wv_abs, abs_norm, color = 'blue', label = 'Absorption')
plt.plot(wv_flu, em_norm, color = 'red', label = 'Emission')
plt.xlabel('Wavelength (nm)')
plt.ylabel('a.u.')
plt.title('Absorption vs. Emission of HP in room temperature')
plt.legend()
plt.savefig('Graph1.png')