# paketten importeren
import csv
import matplotlib.pyplot as plt

### LIJSTEN
rownumber = 0
wv_abs = []
absHP = []
absAT = []

# Verkrijg data uit excel bestand
with open('Graph2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Slaat de kopregel over

    for row in reader:
        rownumber += 1
        if rownumber > 0:
            # Verander elke komma in punt en string --> float
            wv_abs_corrected = float(row[0].replace(',', '.'))
            absHP_corrected = float(row[1].replace(',', '.'))
            absAT_corrected = float(row[2].replace(',', '.'))
        
        wv_abs.append(wv_abs_corrected)
        absHP.append(absHP_corrected)
        absAT.append(absAT_corrected)

# Normaliseer de waarden op het tweede maximum
max_absHP = 0.499314457
max_absAT = 0.236148804
absHP_norm = [x / max_absHP for x in absHP]
absAT_norm = [x / max_absAT for x in absAT]

verschil = [abs(a - b) for a, b in zip(absAT_norm, absHP_norm)]

# Plot grafiek
plt.figure()
plt.plot(wv_abs, absHP_norm, label = 'Absorption HP')
plt.plot(wv_abs, absAT_norm, label = 'Absorption AT')
plt.plot(wv_abs, verschil, color = 'grey', label = 'Difference AT - HP')
plt.xlabel('Wavelength (nm)')
plt.ylabel('a.u.')
plt.title('Absorption HP vs. Absorption AT')
plt.legend()
plt.savefig('Graph2.png')
plt.show()