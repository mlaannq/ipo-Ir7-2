import json
kvalif = str(input("Введите номер квалификации: "))#запрос на номер квалификации
found = False
kvalif2 = kvalif[:-3]
with open("dump.json", encoding="utf-8") as file:
    soderjim = file.read()
    text = json.loads(soderjim)#загружаем данные json
    for skill in text:
        if skill["model"] == "data.skill" and skill["fields"]["code"] == kvalif:
            skill_code = skill["fields"]["code"]
            skill_title = skill["fields"]["title"]
            found = True
            for spec in text:#поиск спициальности
                if spec["model"] == "data.specialty":
                    if spec["fields"]["code"] == kvalif2 and skill["fields"]["specialty"] == spec["pk"]:
                        spec_code = spec["fields"]["code"]
                        spec_title = spec["fields"]["title"]
                        spec_type = spec["fields"]["c_type"]
            break
if found:
    print("=============== Найдено ===============")
    print(f"{spec_code} >> Специальность '{spec_title}', {spec_type}")
    print(f"{skill_code} >> Квалификация '{skill_title}'")
else:
    print("=============== Не найдено ===============")