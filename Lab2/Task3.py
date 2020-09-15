name, old, sex = input("Введите ваше имя : "), int(input("сколько вам лет? >> ")), input("Ваш пол М/Ж? >> ")
res = ""
if sex == "М":
    res += "Его зовут " + name + ". Ему " + str(old)
if sex == "Ж":
    res += "Её зовут " + name + ". Ей " + str(old)

# лет 5 - 20, 25-30, 35-40, 45-50, 55-60, 65-70, 75-80, 85-90, 95-100
# год 1-4,21-24, 31-34, 41-44, 51-54

if (1 <= old%10 <= 4 and (1 < old <= 4 or 15 < old)): # god
    res += " год."
if ((5 <= old%10 <= 9 or old%10 == 0) and 15 <= old) or 5 <= old <= 14:
    res += " лет."



print(res)

