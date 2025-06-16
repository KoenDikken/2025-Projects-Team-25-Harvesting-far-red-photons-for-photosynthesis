# Import packages
import csv
import matplotlib.pyplot as plt

# Lists
rownumber = 0
wv = []
wv_AT = []
absHP = []
absAT = []

with open('PSI/Absorptionvsmodel.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Slaat de kopregel over

    for row in reader:
        rownumber += 1
        if rownumber <1002:
            wv_corrected = float(row[0].replace(',', '.'))
            absHP_corrected = float(row[1].replace(',', '.')) 

        if rownumber >0:      
            wv_AT_corrected = float(row[2].replace(',', '.'))
            absAT_corrected = float(row[3].replace(',', '.'))
        
        # Add values to lists
        wv.append(wv_corrected)
        wv_AT.append(wv_AT_corrected)
        absHP.append(absHP_corrected)
        absAT.append(absAT_corrected)

 # Normalise values on second maximum
max_absHP = 0.364870429
max_absAT = 0.783194125
HP_norm = [x / max_absHP for x in absHP]
AT_norm = [x / max_absAT for x in absAT]

# Calculate difference
verschil = [(a - b) for a, b in zip(AT_norm, HP_norm)]

# Plot graph
plt.figure()
plt.plot(wv, HP_norm, color = 'blue', label = 'HP')
plt.plot(wv_AT, AT_norm, color = 'red', label = 'AT')
plt.plot(wv_AT, verschil, color = 'grey', label = 'AT - HP')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorption (a.u.)')
plt.title('Absorption HP vs. AT')
plt.legend()
plt.xlim(350, 750)
plt.savefig('Absorption HP vs AT.jpg')
plt.show()