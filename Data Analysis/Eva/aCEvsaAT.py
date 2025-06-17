import matplotlib.pyplot as plt
import csv

# Functie om CSV in te lezen met optionele rijlimiet
def read_csv(filepath, x_col, y_col, max_rows=None):
    x_data = []
    y_data = []
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # sla header over
        
        for i, row in enumerate(reader):
            if max_rows is not None and i >= max_rows:
                break
            try:
                x = float(row[x_col])
                y = float(row[y_col])
            except (ValueError, IndexError):
                continue
            x_data.append(x)
            y_data.append(y)
    return x_data, y_data

def normalize_max1(data):
    max_val =  0.7831941247
    if max_val == 0:
        return [0 for _ in data]  # voorkom deling door nul
    return [val / max_val for val in data]

def normalize_max2(data):
    max_val =0.5816487074 
    if max_val == 0:
        return [0 for _ in data]  # voorkom deling door nul
    return [val / max_val for val in data]
# Data inlezen
wavelength1, intensity1 = read_csv('PSI/PSI LHCI Fa At.csv', 0,2 )
wavelength2, intensity2 = read_csv('PSI/Plants PSI.csv',0, 3)

# Normaliseren
intensity11 = normalize_max1(intensity1)
intensity22 = normalize_max2(intensity2)

# Controle: zorg dat de lengte gelijk is en wavelengths overeenkomen
if wavelength1 != wavelength2:
    print("Waarschuwing: golflengtes zijn niet gelijk - overweeg interpolatie")
    min_len = min(len(intensity11), len(intensity22))
    intensity_diff = [intensity11[i] - intensity22[i] for i in range(min_len)]
    wavelength_common = wavelength1[:min_len]
else:
    intensity_diff = [i1 - i2 for i1, i2 in zip(intensity11, intensity22)]
    wavelength_common = wavelength1

# Plotten
plt.figure(figsize=(10, 6))
plt.plot(wavelength1, intensity11, label='Absorption AT')
plt.plot(wavelength2, intensity22, label='Absorption CE')
plt.plot(wavelength_common, intensity_diff, label='Difference (AT - CE)', linestyle='--', color='red')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity(A.U.)')
plt.title('Absorption PSI AT/CE')
plt.xlim(left=350, right= 800)
plt.legend()
plt.show()