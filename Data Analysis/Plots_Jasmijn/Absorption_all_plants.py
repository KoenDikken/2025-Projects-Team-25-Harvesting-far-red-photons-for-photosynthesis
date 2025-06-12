# import packages
import csv
import matplotlib.pyplot as plt

### LISTS
rownumber = 0
wv = []
absEva = []
absJasmijn = []
absMads = []
absKoen = []
absNicco = []
absModel = []

# Verkrijg data uit excel bestand
with open('Absorption_all_plants.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Slaat de kopregel over

    for row in reader:
        rownumber += 1
        if rownumber >0:
            # Verander elke komma in punt en string --> float
            wv_corrected = float(row[0].replace(',', '.'))
            absEva_corrected = float(row[1].replace(',', '.')) 
            absJasmijn_corrected = float(row[2].replace(',', '.'))
            absMads_corrected = float(row[3].replace(',', '.'))
            absKoen_corrected = float(row[4].replace(',', '.'))
            absNicco_corrected = float(row[5].replace(',', '.'))
            absModel_corrected = float(row[6].replace(',', '.'))
        
        wv.append(wv_corrected)
        absEva.append(absEva_corrected)
        absJasmijn.append(absJasmijn_corrected)
        absMads.append(absMads_corrected)
        absKoen.append(absKoen_corrected)
        absNicco.append(absNicco_corrected)
        absModel.append(absModel_corrected)

# Normaliseer de waarden op het tweede maximum
max_Eva = 0.725952387
max_Jasmijn = 0.499314457
max_Mads = 0.537089109
max_Koen = 0.381760925
max_Nicco = 0.215625808
max_Model = 0.236148804
absEva_norm = [x / max_Eva for x in absEva]
absJasmijn_norm = [x / max_Jasmijn for x in absJasmijn]
absMads_norm = [x / max_Mads for x in absMads]
absKoen_norm = [x / max_Koen for x in absKoen]
absNicco_norm = [x / max_Nicco for x in absNicco]
absModel_norm = [x / max_Model for x in absModel]

# Plot grafiek
plt.figure()
plt.plot(wv, absEva_norm, alpha = 0.8, color = 'blue', label = 'Eva')
plt.plot(wv, absJasmijn_norm, alpha = 0.8, color = 'red', label = 'Jasmijn')
plt.plot(wv, absMads_norm, alpha = 0.8, color = 'green', label = 'Mads')
plt.plot(wv, absKoen_norm, alpha = 0.8, color = 'purple', label = 'Koen')
plt.plot(wv, absNicco_norm, alpha = 0.8, color = 'pink', label = 'Nicco')
plt.plot(wv, absModel_norm, alpha = 0.8, color = 'orange', label = 'Model')

plt.xlabel('Wavelength (nm)')
plt.ylabel('a.u.')
plt.title('Absorption all plants')
plt.legend()
plt.savefig('Absorption_all_plants.png')