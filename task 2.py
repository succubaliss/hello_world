#Вік через рік: Напишіть програму, яка запитує ім'я користувача та його вік. Потім виведіть повідомлення, яке повідомляє, скільки йому буде років через рік.
name = (input("What's ur name?: "))
age = int(input("What's ur age?: "))
print("In a year you'll be: ", age + 1 )

#Площа прямокутника: Напишіть програму, яка запитує довжину та ширину прямокутника, а потім обчислює та виводить його площу.
l = int(input("Enter lenght: "))
w = int(input("Enter width: "))
a = (l+w)**2
print(f"The rectangle with a lenght of {l} and width of {w} has an area pf {a}.")

#Конвертер валют: Запропонуйте користувачеві ввести суму в одній валюті (наприклад, доларах), а потім виведіть цю суму в іншій валюті (наприклад, євро), використовуючи заздалегідь визначений коефіцієнт обміну.
usd_to_eur_exchangerate = 0.86
usd = float(input("Enter your amount in USD: "))
eur = usd * usd_to_eur_exchangerate
print(f"{usd} USD = {eur:.2f}")

#Вартість покупки: Запитайте користувача назву товару, його ціну та кількість. Обчисліть загальну вартість покупки та виведіть її на екран.
name =  (input("Enter the product name: "))
price = float(input("Enter the price: "))
quantity = int(input("Enter prodyct quantity: "))
totalcost = price * quantity
print(f"Product: {name}")
print(f"Price per item: {price}")
print(f"Total cost: {totalcost:.2f}")

#Температура: Напишіть програму, яка перетворює температуру з градусів Цельсія на Фаренгейт. Запитайте користувача температуру в градусах Цельсія.
temp_c = int(input("Enter the temperature in °C: "))
temp_f = temp_c * 1.8 + 32
print(f'{temp_c}°C = {temp_f}°F') 