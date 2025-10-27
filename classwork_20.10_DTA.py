# Розгалудження
# 1 Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача, то виводиться повідомлення Password accepted.. У іншому випадку повідомлення буде Sorry, that is the wrong password..
password_user_12 = 6789
password = int(input("Enter the password: "))
if password_user_12 == password:
   print("Password accepted.")
else: 
   print("Sorry, that is the wrong password.")

# 2 Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.
name1 = input("Please enter the 1st name: ")
name2 = input("Please enter the 2nd name: ")
if name1 <= name2:
   print(name1, name2)
   name1, name2 = name2, name1

# 3 Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. Якщо це число або 1 або 2 або 3, то виводиться повідомлення - назва числа, відповідно, One, Two, Three. В усіх інших випадках виводиться слово Unknown.
number = int(input("Enter the number: "))
if number == 1:
   name_of_number = "One"
elif number == 2:
   name_of_number = "Two"
elif number == 3:
   name_of_number = "Three"
else: 
   print("Unknown")
   name_of_number = "Unknown"

# 4 Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.
letter1 = input("Please enter the 1st letter: ").lower()
letter2 = input("Please enter the 2nd letter: ").lower()
if letter1 <= letter2:
   print("First letter:", letter1, "Second letter:", letter2)
else:
   print("First letter:", letter2, "Second letter:", letter1)

#Якщо важливий реєстр
letter1 = input("Please enter the 1st letter: ")
letter2 = input("Please enter the 2nd letter: ")
if letter1.lower() <= letter2.lower():
   if letter1 <= letter2:
   print("First letter:", letter1, "Second letter:", letter2)
else:
   print("First letter:", letter2, "Second letter:", letter1)

# 5 Напишіть програму, в якій користувач вводить значення температури, і, 
# якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення 
# A cold, isn’t it?. 
# Якщо ж температура становить більше 0 і менше 10 градусів Цельсія
#  повідомлення буде Cool., 
# у інших випадках Nice weather we’re having..
temp = int(input("Enter the temperature in °C:"))
if temp <= 0:
    print("Quite cold, isn't it? ")
elif 1 <= temp < 10:
    print("Cool... ")
else:
    print("Nice weather we're having... ")

# Середній рівень
# 1. Визначте назву геометричної фігури за введеною кількістю її сторін. 
# Програма повинна підтримувати фігури від 3 до 6 сторін.
# Якщо введена кількість сторін поза межами цього діапазону, програма повинна відображати відповідне повідомлення.
sides = int(input("Enter the number of sides (3-6): "))
if sides == 3:
   print("That's a triangle")
elif sides == 4:
   print("That's a square")
elif sides == 5:
   print("That's a pentagon")
elif sides == 6:
   print("That's a hexagon")
else: 
   print("A figure with this number of sides doesn't exist in this program.")

# 2 Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори.
#  Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні.
#  Непарні номери від 19 до 28 - червоні, а парні номери - чорні. Непарні номери від 29 до 36 - чорні, а парні номери - червоні.
#  Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. 
# Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.
number = int(input("Enter a number (0-36: "))
if number < 0 or number > 36:
    print("Invalid number! Please enter a number between 0 and 36,")
elif number == 0:
    print("Green")
elif 1 <= number <= 10:
    if number % 2 == 0:
        print("Black")
    else:
        print("Red")
elif 11 <= number <= 18:
    if number % 2 == 0:
        print("Red")
    else: 
        print("Black")
elif 19 <= number <= 28:
    if number % 2 == 0:
        print("Black")
    else:
        print ("Red")
elif 29 <= number <= 36:
    if number % 2 == 0:
       print("Red")
    else:
        print("Black")

# Дано дві точки: 
# A (x1, y1) і B (x2, y2).
#  Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.
#  Вхідні дані: 
#  1 
#  2 
#  3 
#  2 
#  4 
#  4 
#  4 
#  4 
#  Вихідні дані: 
#  B 
#  The distance is the same 
nums = [int(input()) for _ in range(8)]
for i in range(0, len(nums), 4):
    x1, y1, x2, y2 = nums[i:i+4]
    
    dA = x1**2 + y1**2
    dB = x2**2 + y2**2
    
    if dA > dB:
        print("A")
    elif dA < dB:
        print("B")
    else:
        print("The distance is the same")

# Вводяться координати (x, y) точки A і радіус кола (r). 
# Визначити, чи належить дана точка колу, якщо його центр знаходиться в початку координат.

# Вхідні дані:
# 3
# 4
# 5
# -2
# 5
# 3
# Вихідні дані:
# The point belongs to the circle
# The point is outside the circle

for _ in range(2):
    x = int(input())
    y = int(input())
    r = int(input())

    distance_squared = x**2 + y**2
    radius_squared = r**2

if distance_squared == radius_squared:
        print("The point belongs to the circle")
elif distance_squared < radius_squared:
        print("The point is inside the circle")
else:
        print("The point is outside the circle")

# Дано натуральное число. Визначити, чи закінчується число парною цифрою.
# Вхідні дані:
# 1234
# 35
# Вихідні дані:
# True
# False

for _ in range(2):
    n = int(input())
if n % 10 % 2 == 0:
    print("True")
else:
    print("False")