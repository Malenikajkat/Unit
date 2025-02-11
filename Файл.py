file = open("text.txt","r")
str = file.read()

file.close()
print(str)

new_file = open("new_text.txt", "w")
new_file.write("Пробная запись в файл")
new_file.close()
