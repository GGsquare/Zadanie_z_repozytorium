print("lista_zakupów")
zakupy_dict = {"piekarnia": ["chleb", "bułki", "pączek"], "warzywniak": ["marchew", "seler", "rukola"]}
zakupy_v = []
for k, v in zakupy_dict.items():
    print("Idę do", (k.capitalize()), ", kupuję tu następujące rzeczy:", (v))
    print("Idę do {} , kupię tu następujące rzeczy:{}" .format(k, v))
    zakupy_v.append(len(v))
print("W sumie kupie", sum(zakupy_v), "produktów")
#
print()
#
lista = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
liczby_pierwsze = []

for num in lista:
  is_prime=True
  
  if num > 2:
    for i in range(2, num):
      if num%i==0:
        is_prime=False
        break
  
  if is_prime:
    liczby_pierwsze.append(num)

print(liczby_pierwsze)
#
print()
#
print("Sekwencja przed sortowaniem:")
print()
herbata = ["włącz czajnik", "znajdź opakowanie herbaty", "zalej herbatę", "nalej wody do czajnika", "wyjmij kubek", "włóż herbatę do kubka"]
for i in herbata:
    print(i)
print()
print("Sekwencja po sortowaniu:")
print()
herbata[0]="nalej wody do czajnika"
herbata[1]="włącz czajnik"
herbata[2]="wyjmij kubek"
herbata[3]="znajdź opakowanie herbaty"
herbata[4]="włóż herbatę do kubka"
herbata[5]="zalej herbatę"
for i in herbata:
    print(i)
#
print("nadal nie wiem jak zrobić te duże litery w zadaniu z zakupami")
#
print("Jak masz jakieś wskazówki, jak to wszystko przyswoić, to bardzo proszę, bo już mi głową pęka od tych komend, a wiem, że to dopiero początek")
#
print("https://www.geeksforgeeks.org/python-convert-strings-to-uppercase-in-dictionary-value-lists/?ref=gcse")
print("Probowałem kodu z linku i też nic, coś musiałem schrzanić. Poza tym, to zamienia całe wyrazy na wielkie litery, a nie tylko pierwszą literę, choć to pewnie można załatwić pisząc w kodzie [0] lub coś z tym sytulu?")