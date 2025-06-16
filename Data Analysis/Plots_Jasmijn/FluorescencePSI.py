# Import packages
import csv
import matplotlib.pyplot as plt

# Lists
rownumber = 0
wv = []
wv_AT = []
emAF = []
emCE = []
emHA = []
emHP = []
emAT = []
emFA = []

with open('PSI/FluorescencePSI.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Slaat de kopregel over

    for row in reader:
        rownumber += 1
        if rownumber >0:
            wv_AT_corrected = float(row[0].replace(',', '.'))
            emAT_corrected = float(row[5].replace(',', '.'))
            emFA_corrected = float(row[6].replace(',', '.'))
        if rownumber < 201:   
            wv_corrected = float(row[0].replace(',', '.'))
            emAF_corrected = float(row[1].replace(',', '.'))
            emCE_corrected = float(row[2].replace(',', '.'))
            emHA_corrected = float(row[3].replace(',', '.'))
            emHP_corrected = float(row[4].replace(',', '.'))
        
        # Add values to lists
        wv_AT.append(wv_AT_corrected)
        wv.append(wv_corrected)
        emAT.append(emAT_corrected)
        emFA.append(emFA_corrected)
        emAF.append(emAF_corrected)
        emCE.append(emCE_corrected)
        emHA.append(emHA_corrected)
        emHP.append(emHP_corrected)

# Normalise values on second maximum
max_AT = 1
max_FA = 1
max_AF = 14626193
max_CE = 286762.7188
max_HA = 6533169
AT_norm = [x / max_AT for x in emAT]
FA_norm = [x / max_FA for x in emFA]
AF_norm = [x / max_AF for x in emAF]
CE_norm = [x / max_CE for x in emCE]
HA_norm = [x / max_HA for x in emHA]

# Plot graph
plt.figure()

plt.plot(wv_AT, AT_norm, color = 'magenta', label = 'AT')
plt.plot(wv_AT, FA_norm, color = 'blue', label = 'FA')

plt.plot(wv, AF_norm, color = 'red', label = 'AF')
plt.plot(wv, CE_norm, color = 'black', label = 'CE')
plt.plot(wv, HA_norm, color = 'green', label = 'HA')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Fluorescence (a.u.)')
plt.title('Fluorescence PSI')
plt.legend()
plt.xlim(600, 850)
plt.savefig('Fluorescence PSI')
plt.show()
