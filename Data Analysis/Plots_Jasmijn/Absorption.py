# Import packages
import csv
import matplotlib.pyplot as plt

# Lists
rownumber = 0
wv = []
wv_ac = []
abs = []
absac = []

with open('PSI/Absorption.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Slaat de kopregel over

    for row in reader:
        rownumber += 1
        if rownumber >0:
            wv_corrected = float(row[2].replace(',', '.'))
            abs_corrected = float(row[3].replace(',', '.'))   
            wv_ac_corrected = float(row[0].replace(',', '.'))
            absac_corrected = float(row[1].replace(',', '.'))
        
        # Add values to lists
        wv.append(wv_corrected)
        wv_ac.append(wv_ac_corrected)
        abs.append(abs_corrected)
        absac.append(absac_corrected - 0.06)

# # Normalise values on second maximum
max = 0.364663601 + 0.11
max_ac = 0.25467518
norm = [(x / max) for x in abs]
ac_norm = [(x / max_ac) for x in absac]

# Plot graph
plt.figure()

plt.plot(wv, norm, color = 'blue', label = 'Absorption no aceton')
plt.plot(wv_ac, ac_norm, color = 'red', label = 'Absorption aceton')

# plt.plot(wv_AT, verschil, color = 'grey', label = 'AT - HP')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorption (a.u.)')
plt.title('Absorption HP aceton vs. no aceton')
plt.legend()
plt.xlim(350, 750)
plt.savefig('Absorption aceton vs. no aceton.jpg')
plt.show()