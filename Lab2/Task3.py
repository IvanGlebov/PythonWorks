name, old, sex = input("Введите ваше имя : "), int(input("сколько вам лет? >> ")), input("Ваш пол М/Ж? >> ")
res = ""
if sex == "М":
    res += "Его зовут " + name + ". Ему " + str(old)
if sex == "Ж":
    res += "Её зовут " + name + ". Ей " + str(old)

# лет 5 - 20, 25-30, 35-40, 45-50, 55-60, 65-70, 75-80, 85-90, 95-100
# год 1-4,21-24, 31-34, 41-44, 51-54

if 1 <= old <= 4 or 21 <= old <= 24 or 31 <= old <= 34 or 41 <= old <= 44 or 51 <= old <= 54 or 61 <= old <= 64 or 71 <= old <= 74 or 81 <= old <= 84 or 91 <= old <= 94:
    res += " года."
if 5 <= old <= 20 or 25 <= old <= 30 or 35 <= old <= 40 or 45 <= old <= 50 or 55 <= old <= 60 or 65 <= old <= 70 or 75 <= old <= 80 or 85 <= old <= 90 or 95 <= old <= 100:
    res += " лет."

print(res)

