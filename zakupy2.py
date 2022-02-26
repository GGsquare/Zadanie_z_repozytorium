print("lista_zakupów")
zakupy_dict = {"piekarnia": ["chleb", "bułki", "pączek"], "warzywniak": ["marchew", "seler", "rukola"]}
zakupy_v = []
for k, v in zakupy_dict.items():
    print("Idę do", (k.capitalize()), ", kupuję tu następujące rzeczy:", (v))
    print("Idę do {} , kupię tu następujące rzeczy:{}" .format(k, v))
    zakupy_v.append(len(v))
print("W sumie kupie", sum(zakupy_v), "produktów")