names = {
    "masha": {"city": "Moscow", "temperature": 20, "wind": "east"},
    "vasya": {"city": "Rostov", "temperature": 12, "wind": "north"},
    "igor": {"city": "London", "temperature": 40, "wind": "west"}
}
name = input('Введите имя:\n')
#print(names[name])
print('Город: ' + names[name]["city"] + 
      '\nТемпература: ' + str(names[name]["temperature"]) + 
      '\nВетер: ' + names[name]["wind"])

