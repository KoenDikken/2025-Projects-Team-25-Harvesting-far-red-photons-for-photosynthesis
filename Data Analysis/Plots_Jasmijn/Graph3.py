# paketten importeren
import csv
import matplotlib.pyplot as plt

### LIJSTEN
rownumber = 0
wv_AT = []
wv_HP = []
emHPrt = []
emATrt = []

# Verkrijg data uit excel bestand
with open('Graph3.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Slaat de kopregel over

    for row in reader:
        rownumber += 1
        if rownumber < 202:
            # Verander elke komma in punt en string --> float
            wv_AT_corrected = float(row[0].replace(',', '.'))
            emATrt_corrected = float(row[2].replace(',', '.'))
        if rownumber < 202:
            wv_HP_corrected = float(row[0].replace(',', '.'))
            emHPrt_corrected = float(row[1].replace(',', '.'))

        wv_HP.append(wv_HP_corrected)
        wv_AT.append(wv_AT_corrected)
        emHPrt.append(emHPrt_corrected)
        emATrt.append(emATrt_corrected)

# Normaliseer de waarden op het tweede maximum
max_emHPrt = 2748197.25
max_emATrt = 1
emHPrt_norm = [x / max_emHPrt for x in emHPrt]
emATrt_norm = [x / max_emATrt for x in emATrt]

verschil = [abs(a - b) for a, b in zip(emATrt_norm, emHPrt_norm)]

# Plot grafiek
plt.figure()
plt.plot(wv_HP, emHPrt_norm, alpha = 0.7, label = 'Emission HP')
plt.plot(wv_AT, emATrt_norm, alpha = 0.7, label = 'Emission AT')
plt.plot(wv_HP, verschil, color = 'grey', label = 'Difference AT - HP')
plt.xlabel('Wavelength (nm)')
plt.ylabel('a.u.')
plt.title('Emission HP vs. Emission AT room temperature')
plt.legend()
plt.savefig('Graph3.png')