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