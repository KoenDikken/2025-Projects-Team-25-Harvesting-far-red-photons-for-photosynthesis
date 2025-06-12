# import packages
import csv
import matplotlib.pyplot as plt

### LISTS
rownumber = 0
wv_0 = []
wv_203 = []
emAF = []
emCE = []
emHA = []
emHP = []
emAT = []
emFA = []

# Verkrijg data uit excel bestand
with open('Emission_all_plants_lt.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Slaat de kopregel over

    for row in reader:
        rownumber += 1
        if rownumber >0:
            # Verander elke komma in punt en string --> float
            wv_0_corrected = float(row[0].replace(',', '.'))
            emAT_corrected = float(row[5].replace(',', '.'))
            emFA_corrected = float(row[6].replace(',', '.'))
            wv_203_corrected = float(row[0].replace(',', '.'))
            emAF_corrected = float(row[1].replace(',', '.')) 
            emCE_corrected = float(row[2].replace(',', '.'))
            emHA_corrected = float(row[3].replace(',', '.'))
            emHP_corrected = float(row[4].replace(',', '.'))
        
        wv_0.append(wv_0_corrected)
        wv_203.append(wv_203_corrected)
        emAF.append(emAF_corrected)
        emCE.append(emCE_corrected)
        emHA.append(emHA_corrected)
        emHP.append(emHP_corrected)
        emAT.append(emAT_corrected)
        emFA.append(emFA_corrected)

# Normaliseer de waarden op het tweede maximum
max_AF = 8157200.5
max_CE = 37553496
max_HA = 11919807
max_HP = 46786868
max_AT = 1
max_FA = 49243912
emAF_norm = [x / max_AF for x in emAF]
emCE_norm = [x / max_CE for x in emCE]
emHA_norm = [x / max_HA for x in emHA]
emHP_norm = [x / max_HP for x in emHP]
emAT_norm = [x / max_AT for x in emAT]
emFA_norm = [x / max_FA for x in emFA]

# Plot grafiek
plt.figure()
plt.plot(wv_203, emAF_norm, alpha = 0.7, color = 'blue', label = 'AF')
plt.plot(wv_203, emCE_norm, alpha = 0.7, color = 'red', label = 'CE')
plt.plot(wv_203, emHA_norm, alpha = 0.7, color = 'green', label = 'HA')
plt.plot(wv_203, emHP_norm, alpha = 0.7, color = 'purple', label = 'HP')
plt.plot(wv_0, emAT_norm, alpha = 0.7, color = 'pink', label = 'AT')
plt.plot(wv_0, emFA_norm, alpha = 0.7, color = 'orange', label = 'FA')

plt.xlabel('Wavelength (nm)')
plt.ylabel('a.u.')
plt.title('Emission all plants low temperature')
plt.legend()
plt.savefig('Emission_all_plants_lt.png')
