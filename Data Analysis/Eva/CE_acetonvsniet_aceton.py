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

# Normaliseer op maximum
# def normalize_max(data):
#     max_val = max(data)
#     if max_val == 0:
#         return [0 for _ in data]
#     return [val / max_val for val in data]

def normalize_max1(data):
    max_val =  1.074201107
    if max_val == 0:
        return [0 for _ in data]  # voorkom deling door nul
    return [val / max_val for val in data]
# 0.29639712
def normalize_max2(data):
    max_val =0.5816487074
    if max_val == 0:
        return [0 for _ in data]  # voorkom deling door nul
    return [val / max_val for val in data]
# Normalisatie functie
def normalize_max(data):
    max_val = max(data)
    if max_val == 0:
        return data  # of [0]*len(data) als je wilt forceren naar nullen
    return [x / max_val for x in data]

# Data inlezen
wavelength_acetone, intensity_acetone = read_csv(r'PSI/Plants PSI acetone.csv', 0, 7)
wavelength_no_acetone, intensity_no_acetone =  read_csv(r'PSI/Plants PSI acetone.csv', 0, 7)

# Nog een keer lezen met andere kolom, en corrigeren van golflengte
wavelength_shifted, _ = read_csv(r'PSI/Plants PSI.csv', 0, 7)
wavelength_shifted = [w - 0.0024 for w in wavelength_shifted]

# Normaliseren
intensity_acetone_norm = normalize_max(intensity_acetone)
intensity_no_acetone_norm = normalize_max(intensity_no_acetone)

# Laatste punt naar nul
intensity_acetone_norm[-1] = 0
intensity_no_acetone_norm[-1] = 0


# Plotten
plt.plot(wavelength_acetone, intensity_acetone_norm, label='Acetone')
plt.plot(wavelength_no_acetone, intensity_no_acetone_norm, label='No Acetone')
plt.plot(wavelength_shifted, intensity_no_acetone_norm, label='No Acetone (Shifted)')
plt.xlabel('Wavelength')
plt.ylabel('Normalized Intensity')
plt.title('Comparison of PSI with and without Acetone')
plt.legend()
plt.show()