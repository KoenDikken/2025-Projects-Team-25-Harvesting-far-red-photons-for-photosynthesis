# paketten importeren
import csv
import matplotlib.pyplot as plt

### LIJSTEN
rownumber = 0
wv = []
emHPlt = []
emATlt = []

# Verkrijg data uit excel bestand
with open('Graph4.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Slaat de kopregel over

    for row in reader:
        rownumber += 1
        if rownumber > 0:
            # Verander elke komma in punt en string --> float
            wv_corrected = float(row[0].replace(',', '.'))
            emHPlt_corrected = float(row[1].replace(',', '.'))
            emATlt_corrected = float(row[2].replace(',', '.'))

        wv.append(wv_corrected)
        emHPlt.append(emHPlt_corrected)
        emATlt.append(emATlt_corrected)

# Normaliseer de waarden op het tweede maximum
max_emHPlt = 47526864
max_emATlt = 1
emHPlt_norm = [x / max_emHPlt for x in emHPlt]
emATlt_norm = [x / max_emATlt for x in emATlt]

verschil = [abs(a - b) for a, b in zip(emATlt_norm, emHPlt_norm)]

# Plot grafiek
plt.figure()
plt.plot(wv, emHPlt_norm, alpha = 0.7, label = 'Emission HP')
plt.plot(wv, emATlt_norm, alpha = 0.7, label = 'Emission AT')
plt.plot(wv, verschil, color = 'grey', label = 'Difference AT - HP')
plt.xlabel('Wavelength (nm)')
plt.ylabel('a.u.')
plt.title('Emission HP vs. Emission AT low temperature')
plt.legend()
plt.savefig('Graph4.png')

