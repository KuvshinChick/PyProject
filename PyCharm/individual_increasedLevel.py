y = float(input("Введите угол 0<y<2П без PI: "))
print ("Вы ввели:" , y , "PI")
# Умножение на Pi (3.14)
y = y*3.14
# Вычисление угла часовой стрелки в градусах (из радиан)
y=y*180.0/3.14
print ("Угол часовой стрелки: ", y)
# Вычисление угла минутной стрелки (%30 - отделить целые часы, *12 - угол минутной стрелки)
# Тк угловая скорость минутной стрелки в 12 раз больше, чем часовой
x = y%30*12;
print("Угол минутной стрелки: ", x)
# Кол-во полных часов = угол часовой /30
# Тк одному полному часу соответствуют 30 градусов
hour = y/30
print("Полных часов: ", hour)
# 1градус часовой соответствует двум  минутам
# Тк одному полному часу соответствуют 30 градусов
min = y%30*2
print("Полных минут: ", min)