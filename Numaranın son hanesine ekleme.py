# 1. ÖDEV 2.SORU

liste1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
son_uc_hane = "049"
yeni_liste = [item if isinstance(item, list) else [item] for item in liste1]
yeni_liste[2][2].append([int(son_uc_hane)])


yeni_ogeler = [60, 70, 80]
yeni_liste.extend(yeni_ogeler)

print("Yeni liste görüntüsü:")
print(yeni_liste)
