Rand_number = input("Write year of your birth:")
a3 = int(Rand_number)
a2 = 5
a1 = len(str(abs(a3)))
if a1 < a2:
    print(*str(a3), sep='\n')
else:
    print("Not correct date")