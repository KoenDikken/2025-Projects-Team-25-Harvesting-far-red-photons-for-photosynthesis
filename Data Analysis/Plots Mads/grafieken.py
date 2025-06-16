import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV-bestand inlezen
df = pd.read_csv('grafiek2.csv', sep=';', decimal=',')

# Namen van alle kolommen opvragen
print(df.columns)



golflengte1 = df['Wavelength (nm)'].tolist()
laagtemp = df['THYLTHA'].tolist()
hoogtemp = df['THYRTHA'].tolist()
absorptie = df['Abs'].tolist()
golflengte2 = df['Wavelength (nm)2'].tolist()
absorptie2 = df['Abs2'].tolist()
athoogtemp =  df['THYRTAT'].tolist()
atlaagtemp =  df['THYLTAT'].tolist()


laagtemp = laagtemp[:-875]
golflengte1 = golflengte1[:-875]
hoogtemp = hoogtemp[:-925]
athoogtemp = athoogtemp[:-875]
atlaagtemp = atlaagtemp[:-875]


golflengte2 = sorted(golflengte2)
absorptie.reverse()
absorptie2.reverse()




golflengte2 = [float(x) for x in golflengte2]

golflengte1 = [float(x) for x in golflengte1 ]
laagtemp = [float(x) for x in laagtemp]
hoogtemp = [float(x) for x in hoogtemp]
absorptie =[float(x) for x in absorptie ]
absorptie2 = [float(x) for x in absorptie2 ]
atlaagtemp = [float(x) for x in atlaagtemp]
athoogtemp = [float(x) for x in athoogtemp]

golflengte3 = golflengte1[:-50]


def normalize(lst):
    arr = np.array(lst)
    return (arr - arr.min()) / (arr.max() - arr.min())

laagnorm = normalize(laagtemp)
hoognorm = normalize(hoogtemp)



absorptie_grafiek2 = normalize(absorptie)
absorptie2_grafiek2 = normalize(absorptie2)

verschil_absorptie = []
for i in range (len(absorptie_grafiek2)):
    verschil_absorptie.append(absorptie2_grafiek2[i] - absorptie_grafiek2[i] )

absorptie = np.array(absorptie)
index_max_hoognorm = np.argmax(hoognorm)  # Index waar hoognorm 1 is (na normalisatie)

# Referentiewaarde in absorptie op die index
ref_abs = absorptie[index_max_hoognorm]

# Deel hele absorptie door deze referentiewaarde
absorptie_scaled = absorptie / ref_abs







# Normaliseren rond tweede piek (~700 nm) voor grafiek 2
# Bepaal indexen waar golflengte rond 680-720 nm ligt
start_idx = next(i for i, x in enumerate(golflengte2) if x > 600)
end_idx = next(i for i, x in enumerate(golflengte2) if x > 700)

# Zoek maxima in dit bereik
max_ha = max(absorptie_grafiek2[start_idx:end_idx])
max_at = max(absorptie2_grafiek2[start_idx:end_idx])

# Normaliseer volledige curves op basis van deze maxima
absorptie_grafiek2 = absorptie_grafiek2 / max_ha
absorptie2_grafiek2 = absorptie2_grafiek2 / max_at

# Verschil opnieuw berekenen na normalisatie
verschil_absorptie = absorptie2_grafiek2 - absorptie_grafiek2















# Zoek index van eerste piek in hoognorm (bv. tussen 600 en 700 nm)
start_idx = next((i for i, x in enumerate(golflengte3) if x >= 600), 0)
end_idx = next((i for i, x in enumerate(golflengte3) if x >= 700), len(golflengte3))

if end_idx <= start_idx:
    raise ValueError("Geen geldige piek gevonden tussen 600 en 700 nm")

# Index van lokale piek in hoognorm
local_max_idx = start_idx + np.argmax(hoognorm[start_idx:end_idx])

# Waarden bij deze piek
waarde_emissie_piek = hoognorm[local_max_idx]
waarde_absorptie_op_die_piek = absorptie_scaled[local_max_idx]

# Schaal absorptie zodat piek gelijk wordt aan emissie
schaalfactor_grafiek1 = waarde_emissie_piek / waarde_absorptie_op_die_piek
absorptie_scaled = absorptie_scaled * schaalfactor_grafiek1












plt.figure

plt.plot(golflengte3, hoognorm, label='Emission Room Temperature', color='red')
plt.plot(golflengte2, absorptie_scaled, label='Absorption Room Temperature', color='blue')

plt.xlabel('Golflengte (nm)')
plt.ylabel('Waarde')
plt.title('Emission vs Absorption')
plt.legend()
plt.show


plt.savefig('grafiek1')




plt.figure()

plt.plot(golflengte2, absorptie_grafiek2 , label='Absorption HA', color='red')
plt.plot(golflengte2, absorptie2_grafiek2 , label='Absorption AT', color='blue')
plt.plot(golflengte2, verschil_absorptie, label ='Difference in absorption', color = 'green' )

plt.xlabel('Golflengte (nm)')
plt.ylabel('Waarde')
plt.title('Absorption of HA vs AT')
plt.legend()
plt.show

plt.savefig('grafiek2')




plt.figure()

plt.plot(golflengte1, laagnorm, label='Emission 77K ', color='blue')

plt.plot(golflengte1, atlaagtemp, label='Emission AT 77K', color='green')





plt.xlabel('Golflengte (nm)')
plt.ylabel('Waarde')
plt.title('Absorption of HA vs AT cold temp')
plt.legend()
plt.show
plt.savefig('grafiek3')


plt.figure()

plt.plot(golflengte3, hoognorm, label='Emission Room Temperature', color='red')

plt.plot(golflengte1, athoogtemp, label='Emission AT Room Temperature', color='yellow')






plt.xlabel('Golflengte (nm)')
plt.ylabel('Waarde')
plt.title('Absorption of HA vs AT room temp')
plt.legend()
plt.show
plt.savefig('grafiek4')








# Zoek index van eerste piek in laagtemp (bv. tussen 400 en 500 nm)
start_idx = next((i for i, x in enumerate(golflengte1) if x >= 600), 0)
end_idx = next((i for i, x in enumerate(golflengte1) if x >= 700), len(golflengte1))

# Controleer op geldig bereik
if end_idx <= start_idx:
    raise ValueError("Geen geldige piek gevonden tussen 400 en 500 nm")

# Zoek index van maximale waarde in dat bereik voor laagtemp
local_max_idx = start_idx + np.argmax(laagtemp[start_idx:end_idx])

# Waarden bij de piekpositie
waarde_laag_piek = laagtemp[local_max_idx]
waarde_hoog_op_die_piek = hoogtemp[local_max_idx]

# Schaalfactor zodat hoogtemp daar dezelfde waarde heeft als laagtemp
schaalfactor = waarde_laag_piek / waarde_hoog_op_die_piek

# Pas de schaal toe op hoogtemp
hoogtemp_gestandaardiseerd = [x * schaalfactor for x in hoogtemp]
laagtemp_gestandaardiseerd = laagtemp  # ongewijzigd





plt.figure()

plt.plot(golflengte3, hoogtemp_gestandaardiseerd, label='Emission Room Temperature', color='red')

plt.plot(golflengte1, laagtemp_gestandaardiseerd, label='Emission 77K ', color='blue')


plt.xlabel('Golflengte (nm)')
plt.ylabel('Waarde')
plt.title('Room temperature vs 77K HA')
plt.legend()

plt.show
plt.savefig('grafiek5')