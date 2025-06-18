# Lietotājs ievada skaitli
skaitlis = int(input("Ievadiet veselu skaitli: "))

# Inicializē skaitītāju
i = 1

# While cikls, kas izvada skaitļus no 1 līdz ievadītajam skaitlim
while i <= skaitlis:
    print(i)
    i += 1  # Palielina skaitītāju par 1
else:
    # Izvada paziņojumu, ja cikls nav pārtraukts ar 'break'
    print("Skaitīšana pabeigta!")