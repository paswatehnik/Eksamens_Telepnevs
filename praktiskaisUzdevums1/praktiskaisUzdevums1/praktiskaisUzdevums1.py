# Inicializē skaitītāju
i = 2

# While cikls, kas strādā, kamēr i <= 20
while i <= 20:
    if i % 2 != 0:  # Pārbauda, vai skaitlis ir nepāra
        i += 1      # Palielina skaitītāju
        continue     # Izlaiž iterāciju, ja skaitlis ir nepāra
    print(i)        # Izvada pāra skaitli
    i += 1          # Palielina skaitītāju