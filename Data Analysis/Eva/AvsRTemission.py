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

# Data inlezen uit beide bestanden zonder limiet
wavelength1, intensity1 = read_csv('normaliseers/FLUOROLOGDATA-Sheet1.csv', 0, 8)
wavelength2, intensity2 = read_csv('normaliseers/Plantsthylakoids.csv', 0, 5)
# Normaliseren van de intensiteiten (tussen 0 en 1)

def normalize_max(data):
    max_val = max(data)
    if max_val == 0:
        return [0 for _ in data]  # voorkom deling door nul
    return [val / max_val for val in data]

def normalize_max2(data):
    max_val = 0.725428045
    if max_val == 0:
        return [0 for _ in data]  # voorkom deling door nul
    return [val / max_val for val in data]

# Data normaliseren vóór plotten
intensity11 = normalize_max(intensity1)
intensity22 = normalize_max2(intensity2)


# Plotten
plt.plot(wavelength1, intensity11, label=' RT Emission CE')
plt.plot(wavelength2, intensity22, label='Absorption CE')
plt.xlabel('Wavelength (nm)')
plt.ylabel(' Intensity(A.U.)')
plt.title('Absorption vs Room Temperature emission CE')
plt.xlim(left=350, right= 800)
plt.legend()

plt.show()
