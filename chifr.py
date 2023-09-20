ALPHABET_RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_EN = "abcdefghijklmnopqrstuvwxyz"
answer = input("какой язык выберите EN/RU: ")
if answer == "RU":
    lang = ALPHABET_RU
elif answer == "EN":
    lang = ALPHABET_EN
else:
    print("Язык поумолчанию Русский")
    lang = ALPHABET_RU
message = input("здрастувте нам нужно чтобы вы вили сообщение ")
chipher = []
step = int(input("укажите сдвиг: "))
for leter in message:
    index = lang.find(leter)+step
    chipher.append(index)
print(chipher)
rizunt = ""
for index in chipher:
    rizunt += lang[index-step]
print(rizunt)