# paketten importeren
import csv
import matplotlib.pyplot as plt

### LIJSTEN
rownumber = 0
wv_lt = []
wv_rt = []
emHPrt = []
emHPlt = []

# Verkrijg data uit excel bestand
with open('Graph5.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Slaat de kopregel over

    for row in reader:
        rownumber += 1
        if rownumber < 202:
            # Verander elke komma in punt en string --> float
            wv_lt_corrected = float(row[0].replace(',', '.'))
            emHPlt_corrected = float(row[2].replace(',', '.'))
        if rownumber < 202:
            wv_rt_corrected = float(row[0].replace(',', '.'))
            emHPrt_corrected = float(row[1].replace(',', '.'))

        wv_lt.append(wv_lt_corrected)
        wv_rt.append(wv_rt_corrected)
        emHPlt.append(emHPlt_corrected)
        emHPrt.append(emHPrt_corrected)

# Normaliseer de waarden op het tweede maximum
max_emHPrt = 2748197.25
max_emHPlt = 53282184
emHPrt_norm = [x / max_emHPrt for x in emHPrt]
emHPlt_norm = [x / max_emHPlt for x in emHPlt]

# Plot grafiek
plt.figure()
plt.plot(wv_rt, emHPrt_norm, color = 'orange', label = 'Emission room temperature')
plt.plot(wv_lt, emHPlt_norm, color = 'blue', label = 'Emission low temperature')
# plt.plot(wv, verschil, color = 'grey', label = 'Difference AT - HP')
plt.xlabel('Wavelength (nm)')
plt.ylabel('a.u.')
plt.title('Emission HP room temperature vs. low temperature')
plt.legend()
plt.savefig('Graph5.png')