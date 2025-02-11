file = open("text.txt","r")
k = 1
print("Построчное считывание")
for L in file:
    print("["+str(k)+"]", L, end="")
    k+=1

file.close()
print("\nФайл закрыт")
