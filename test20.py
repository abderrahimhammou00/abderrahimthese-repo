import matplotlib.pyplot as plt
import numpy as np

# Chargement des données
data1 = np.loadtxt('Int.txt')
#Colonnes : Z, SED NR, SED NR+WC, SED SR, SED SR+WC
Z = data1[:, 0]
SED1 = data1[:, 1]


# Tracé
plt.plot(Z, SED1, color='red', label=r'$\frac{d\sigma}{d\Omega}|_{NR}$')

# Axes et légendes
plt.xlabel(r'$Z$', fontsize=12)
plt.ylabel(r'$\frac{d\sigma}{d\Omega} \, (a.u.)$', fontsize=12)
plt.legend(loc='best')
plt.grid(True)
#plt.yscale('log') # décommente si nécessaire

# Sauvegarde en PDF
plt.savefig("SED.pdf", format="pdf", bbox_inches="tight")

# Affichage
plt.show()
    
