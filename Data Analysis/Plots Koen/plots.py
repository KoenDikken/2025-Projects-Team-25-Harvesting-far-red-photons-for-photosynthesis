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

            if regelnummer < 202:
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



regelnummer2 = 0

ab_Elist = []
ab_Jlist = []
ab_Mlist = []
ab_Klist = []
ab_Nlist = []
ab_Tlist = []

flRT_FAlist = []
flRT_ATlist = []
flRT_AFlist = []
flRT_CElist = []
flRT_HAlist = []
flRT_HPlist = []

flLT_AFlist = []
flLT_CElist = []
flLT_HAlist = []
flLT_HPlist = []
flLT_FAlist = []
flLT_ATlist = []

with open('AllPlantsData.csv', 'r') as input:
    for regel in input:
        if regelnummer2 > 0:

            data_opgeknipt = regel.split(';')
            ab1 = data_opgeknipt[0].replace(',', '.')
            ab_E = float(ab1)
            ab2 = data_opgeknipt[1].replace(',', '.')
            ab_J = float(ab2)
            ab3 = data_opgeknipt[2].replace(',', '.')
            ab_M = float(ab3)
            ab4 = data_opgeknipt[3].replace(',', '.')
            ab_K = float(ab4)
            ab5 = data_opgeknipt[4].replace(',', '.')
            ab_N = float(ab5)
            ab6 = data_opgeknipt[5].replace(',', '.')
            ab_T = float(ab6)

            ab_Elist.append(ab_E)
            ab_Jlist.append(ab_J)
            ab_Mlist.append(ab_M)
            ab_Klist.append(ab_K)
            ab_Nlist.append(ab_N)
            ab_Tlist.append(ab_T)

            if regelnummer2 < 202:
                fr1 = data_opgeknipt[14].replace(',', '.')
                flRT_AF = float(fr1)
                fr2 = data_opgeknipt[15].replace(',', '.')
                flRT_CE = float(fr2)
                fr3 = data_opgeknipt[16].replace(',', '.')
                flRT_HA = float(fr3)
                fr4 = data_opgeknipt[17].replace(',', '.')
                flRT_HP = float(fr4)

                flRT_AFlist.append(flRT_AF)
                flRT_CElist.append(flRT_CE)
                flRT_HAlist.append(flRT_HA)
                flRT_HPlist.append(flRT_HP)
            
            if regelnummer2 < 252:
                fr5 = data_opgeknipt[12].replace(',', '.')
                flRT_FA = float(fr5)
                fr6 = data_opgeknipt[13].replace(',', '.')
                flRT_AT = float(fr6)
                fl1 = data_opgeknipt[6].replace(',', '.')
                flLT_AF = float(fl1)
                fl2 = data_opgeknipt[7].replace(',', '.')
                flLT_CE = float(fl2)
                fl3 = data_opgeknipt[8].replace(',', '.')
                flLT_HA = float(fl3)
                fl4 = data_opgeknipt[9].replace(',', '.')
                flLT_HP = float(fl4)
                fl5 = data_opgeknipt[10].replace(',', '.')
                flLT_FA = float(fl5)
                fl6 = data_opgeknipt[11].replace(',', '.')
                flLT_AT = float(fl6)

                flRT_FAlist.append(flRT_FA)
                flRT_ATlist.append(flRT_AT)
                flLT_AFlist.append(flLT_AF)
                flLT_CElist.append(flLT_CE)
                flLT_HAlist.append(flLT_HA)
                flLT_HPlist.append(flLT_HP)
                flLT_FAlist.append(flLT_FA)
                flLT_ATlist.append(flLT_AT)

        regelnummer2 += 1
            

absAF_final = np.array(absorptionAFlist)
absAT_final = np.array(absorptionATlist)
flAFRT_final = np.array(fluorescenceAFRTlist)
flAFLT_final = np.array(fluorescenceAFLTlist)
ab_E_final = np.array(ab_Elist)
ab_J_final = np.array(ab_Jlist)
ab_M_final = np.array(ab_Mlist)
ab_K_final = np.array(ab_Klist)
ab_N_final = np.array(ab_Nlist)
ab_T_final = np.array(ab_Tlist)

flRT_FA_final = np.array(flRT_FAlist)
flRT_AT_final = np.array(flRT_ATlist)
flRT_AF_final = np.array(flRT_AFlist)
flRT_CE_final = np.array(flRT_CElist)
flRT_HA_final = np.array(flRT_HAlist)
flRT_HP_final = np.array(flRT_HPlist)

flLT_FA_final = np.array(flLT_FAlist)
flLT_AT_final = np.array(flLT_ATlist)
flLT_AF_final = np.array(flLT_AFlist)
flLT_CE_final = np.array(flLT_CElist)
flLT_HA_final = np.array(flLT_HAlist)
flLT_HP_final = np.array(flLT_HPlist)


norm = Normalize()
norm1 = Normalize()
norm2 = Normalize()
norm3 = Normalize()
norm4 = Normalize()
norm5 = Normalize()
norm6 = Normalize()


normAF = Normalize(vmax = 0.381760925, clip=False)
normAT = Normalize(vmax = 0.236148804, clip=False)
normAFLT = Normalize(vmax = 8157200.5)
normAFLT2 = Normalize(vmax = 6138380, clip=False)

abnorm_E = Normalize(vmax = 0.725952387, clip=False)
abnorm_J = Normalize(vmax = 0.499314457, clip=False)
abnorm_M = Normalize(vmax = 0.537089109, clip=False)
abnorm_K = Normalize(vmax = 0.381760925, clip=False)
abnorm_N = Normalize(vmax = 0.215625808, clip=False)
abnorm_T = Normalize(vmax = 0.236148804, clip=False)

LTnorm_FA = Normalize(vmax = 49243912, clip=False)
LTnorm_AT = Normalize(vmax = 1, clip=False)
LTnorm_AF = Normalize(vmax = 8157200.5, clip=False)
LTnorm_CE = Normalize(vmax = 37699076, clip=False)
LTnorm_HA = Normalize(vmax = 11919807, clip=False)
LTnorm_HP = Normalize(vmax = 47526864, clip=False)


absAFnorm = normAF(absAF_final)
absATnorm = normAT(absAT_final)
flAFRTnorm = norm(flAFRT_final)
flAFLTnorm = normAFLT(flAFLT_final)
flAFLTnorm2 = normAFLT2(flAFLT_final)

ab_Enorm = abnorm_E(ab_E_final)
ab_Jnorm = abnorm_J(ab_J_final)
ab_Mnorm = abnorm_M(ab_M_final)
ab_Knorm = abnorm_K(ab_K_final)
ab_Nnorm = abnorm_N(ab_N_final)
ab_Tnorm = abnorm_T(ab_T_final)

fl_RTFAnorm = norm1(flRT_FA_final)
fl_RTATnorm = norm2(flRT_AT_final)
fl_RTAFnorm = norm3(flRT_AF_final)
fl_RTCEnorm = norm4(flRT_CE_final)
fl_RTHAnorm = norm5(flRT_HA_final)
fl_RTHPnorm = norm6(flRT_HP_final)

fl_LTFAnorm = LTnorm_FA(flLT_FA_final)
fl_LTATnorm = LTnorm_AT(flLT_AT_final)
fl_LTAFnorm = LTnorm_AF(flLT_AF_final)
fl_LTCEnorm = LTnorm_CE(flLT_CE_final)
fl_LTHAnorm = LTnorm_HA(flLT_HA_final)
fl_LTHPnorm = LTnorm_HP(flLT_HP_final)


plt.figure(1)
plt.plot(wv_abslist, absAFnorm, 'b-')
plt.plot(wv_flRTlist, flAFRTnorm, 'r-')
plt.xlabel('wavelength (nm)')
plt.ylabel('absorption / fluorescence')
plt.title('Absorption vs RT fluorescence of AF')
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


plt.figure(6)
plt.plot(wv_abslist, ab_Enorm, 'b-')
plt.plot(wv_abslist, ab_Jnorm, 'r-')
plt.plot(wv_abslist, ab_Mnorm, 'g-')
plt.plot(wv_abslist, ab_Knorm, 'y-')
plt.plot(wv_abslist, ab_Nnorm, 'm-')
plt.plot(wv_abslist, ab_Tnorm, 'c-')
plt.xlabel('wavelength (nm)')
plt.ylabel('absorption')
plt.title('Absorption of all the plants')
plt.legend(['Eva (CE)', 'Jasmijn (HP)', 'Mads (HA)', 'Koen (AF)', 'Nicco (FA)', 'Model (AT)'], loc='upper right', fontsize='small')
plt.savefig('Absorptions (all)')


plt.figure(7)
plt.plot(wv_flRTlist, fl_RTCEnorm, 'b-')
plt.plot(wv_flRTlist, fl_RTHPnorm, 'r-')
plt.plot(wv_flRTlist, fl_RTHAnorm, 'g-')
plt.plot(wv_flRTlist, fl_RTAFnorm, 'y-')
plt.plot(wv_flLTlist, fl_RTFAnorm, 'm-')
plt.plot(wv_flLTlist, fl_RTATnorm, 'c-')
plt.xlabel('wavelength (nm)')
plt.ylabel('fluorescence (RT)')
plt.title('Fluorescence of all the plants in room temperature')
plt.legend(['Eva (CE)', 'Jasmijn (HP)', 'Mads (HA)', 'Koen (AF)', 'Nicco (FA)', 'Model (AT)'], fontsize='small')
plt.savefig('Fluorescence (RT) (all)')


plt.figure(8)
plt.plot(wv_flLTlist, fl_LTCEnorm, 'b-')
plt.plot(wv_flLTlist, fl_LTHPnorm, 'r-')
plt.plot(wv_flLTlist, fl_LTHAnorm, 'g-')
plt.plot(wv_flLTlist, fl_LTAFnorm, 'y-')
plt.plot(wv_flLTlist, fl_LTFAnorm, 'm-')
plt.plot(wv_flLTlist, fl_LTATnorm, 'c-')
plt.xlabel('wavelength (nm)')
plt.ylabel('fluorescence (LT)')
plt.title('Fluorescence of all the plants in low temperature (77K)')
plt.legend(['Eva (CE)', 'Jasmijn (HP)', 'Mads (HA)', 'Koen (AF)', 'Nicco (FA)', 'Model (AT)'], fontsize='small')
plt.savefig('Fluorescence (LT) (all)')
plt.show()
