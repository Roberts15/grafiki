import matplotlib.pyplot as plt
x_abcisa=[2016, 2017, 2018, 2019, 2020, 2021]
y_ordinata_riga=[639357, 641192, 637777, 632998, 621120, 614618]
y_ordinata_talina=[423420, 426530, 431896, 438155, 441967, 450078]
#plt.style.use("Stacked-bar-chart")
plt.xlabel("Gadi")
plt.ylabel("Iedzīvotāju skaits")
plt.title("Iedzīvotāju skaita izmaiņas Rīgā un Tallinā")
plt.barh(x_abcisa, y_ordinata_riga, label="Rīga", color="red") 
plt.barh(x_abcisa, y_ordinata_talina, label="Tallina", color="yellow")
plt.legend(loc="lower right") #novieto leģendu
plt.show()