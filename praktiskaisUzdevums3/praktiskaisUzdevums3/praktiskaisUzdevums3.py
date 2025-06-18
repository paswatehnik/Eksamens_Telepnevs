# Lietotājs ievada skaitli
skaitlis = int(input("Ievadiet veselu skaitli: "))

# Inicializē mainīgos
summa = 0
i = 1

# Pārbauda, vai skaitlis ir negatīvs
if skaitlis < 0:
    print("Nepareiza ievade!")
else:
    # While cikls, kas summē skaitļus no 1 līdz ievadītajam skaitlim
    while i <= skaitlis:
        summa += i  # Pieskaita i vērtību summai
        i += 1      # Palielina skaitītāju
    print(f"Summa no 1 līdz {skaitlis} ir: {summa}")