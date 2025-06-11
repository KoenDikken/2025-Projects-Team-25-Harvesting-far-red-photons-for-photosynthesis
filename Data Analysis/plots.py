import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np

regelnummer = 0
wv_abslist = []
wv_flRTlist = []
wv_flLTlist = []
absorptionAFlist = []
absorptionATlist = []
fluorescenceAFRTlist = []
fluorescenceATRTlist = []
fluorescenceAFLTlist = []
fluorescenceATLTlist = []


with open('ValuesSimplifiedAbsorption.csv', 'r') as input:
    for regel in input:
        if regelnummer > 0:

            data_opgeknipt = regel.split(';')
            waves = data_opgeknipt[0].replace(',', '.')
            wv_abs = float(waves)
            abs = data_opgeknipt[1].replace(',', '.')
            absorptionAF = float(abs)
            abs2 = data_opgeknipt[2].replace(',', '.')
            absorptionAT = float(abs2)

            if regelnummer < 201:
                waves2 = data_opgeknipt[6].replace(',', '.')
                wv_flRT = float(waves2)
                flrt = data_opgeknipt[7].replace(',', '.')
                fluorescenceAFRT = float(flrt)
                flrt2 = data_opgeknipt[8].replace(',', '.')
                fluorescenceATRT = float(flrt2)

                wv_flRTlist.append(wv_flRT)
                fluorescenceAFRTlist.append(fluorescenceAFRT)
                fluorescenceATRTlist.append(fluorescenceATRT)
            
            if regelnummer < 252:
                waves3 = data_opgeknipt[3].replace(',', '.')
                wv_flLT = float(waves3)
                fllt = data_opgeknipt[4].replace(',', '.')
                fluorescenceAFLT = float(fllt)
                fllt2 = data_opgeknipt[5].replace(',', '.')
                fluorescenceATLT = float(fllt2)
                wv_flLTlist.append(wv_flLT)
                fluorescenceAFLTlist.append(fluorescenceAFLT)
                fluorescenceATLTlist.append(fluorescenceATLT)

            wv_abslist.append(wv_abs)
            absorptionAFlist.append(absorptionAF)
            absorptionATlist.append(absorptionAT)
        
        regelnummer += 1


absAF_final = np.array(absorptionAFlist)
absAT_final = np.array(absorptionATlist)
flAFRT_final = np.array(fluorescenceAFRTlist)
flAFLT_final = np.array(fluorescenceAFLTlist)

norm = Normalize()
normAF = Normalize(vmax = 0.381760925, clip=False)
normAT = Normalize(vmax = 0.236148804, clip=False)
normAFLT = Normalize(vmax = 8157200.5)
normAFLT2 = Normalize(vmax = 6138380, clip=False)
absAFnorm = normAF(absAF_final)
absATnorm = normAT(absAT_final)
flAFRTnorm = norm(flAFRT_final)
flAFLTnorm = normAFLT(flAFLT_final)
flAFLTnorm2 = normAFLT2(flAFLT_final)




plt.figure(1)
plt.plot(wv_abslist, absAFnorm, 'b-')
plt.plot(wv_flRTlist, flAFRTnorm, 'r-')
plt.xlabel('wavelength (nm)')
plt.ylabel('absorption / fluorescence')
plt.title('Absorption vs RT fluorescence')
plt.legend(['absorption', 'fluorescence (RT)'])
plt.savefig('absorption vs RT fluorescence')


diffAT_AF_abslist = absATnorm - absAFnorm

plt.figure(2)
plt.plot(wv_abslist, absAFnorm, 'b-')
plt.plot(wv_abslist, absATnorm, 'r-' )
plt.plot(wv_abslist, diffAT_AF_abslist, 'k-')
plt.xlabel('wavelength (nm)')
plt.ylabel('absorption')
plt.title('Absorption of AF vs AT')
plt.legend(['absorption AF', 'absorption AT', 'difference (AT - AF)'])
plt.savefig('absorption AF vs AT')


diffAT_AF_fllist = fluorescenceATRTlist - flAFRTnorm

plt.figure(3)
plt.plot(wv_flRTlist, flAFRTnorm, 'b-')
plt.plot(wv_flRTlist, fluorescenceATRTlist, 'r-')
plt.plot(wv_flRTlist, diffAT_AF_fllist, 'k-')
plt.xlabel('wavelength (nm)')
plt.ylabel('fluorescence')
plt.title('Fluorescence of AF vs AT (RT)')
plt.legend(['fluorescence AF', 'fluorescence AT', 'difference (AT - AF)'])
plt.savefig('fluorescenceRT AFvAT')

diffLT_AT_AF_fllist = fluorescenceATLTlist - flAFLTnorm

plt.figure(4)
plt.plot(wv_flLTlist, flAFLTnorm, 'b-')
plt.plot(wv_flLTlist, fluorescenceATLTlist, 'r-')
plt.plot(wv_flLTlist, diffLT_AT_AF_fllist, 'k-')
plt.xlabel('wavelength (nm)')
plt.ylabel('fluorescence')
plt.title('Fluorescence of AF vs AT (LT)')
plt.legend(['fluorescence AF', 'fluorescence AT', 'difference (AT - AF)'])
plt.savefig('fluorescenceLT AFvAT')

plt.figure(5)
plt.plot(wv_flLTlist, flAFLTnorm2, 'b-')
plt.plot(wv_flRTlist, flAFRTnorm, 'r-')
plt.xlabel('wavelength (nm)')
plt.ylabel('fluorescence')
plt.title('Fluorescense of AF in RT vs LT')
plt.legend(['fluorescence AF (LT)', 'fluorescence AF (RT)'])
plt.savefig('fluorescenceAF LTvRT')
plt.show()