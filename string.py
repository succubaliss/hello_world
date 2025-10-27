#  print("GJIKNJHBdd".lower())
#  print("GJIKNJHBdd".upper())
#  print("GJIKNJHBdd".isdigit())

# Розгалудження
# Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача, то виводиться повідомлення Password accepted..
# У іншому випадку повідомлення буде Sorry, that is the wrong password..
password_user_12 = 6789
password = int(input("Enter the password: "))
if password_user_12 == password:
   print("Password accepted.")
else: 
   print("Sorry, that is the wrong password.")

#Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.
name1 = input("Please enter the 1st name: ")
name2 = input("Please enter the 2nd name: ")
if name1 <= name2:
   print(name1, name2)
   name1, name2 = name2, name1


#Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. Якщо це число або 1 або 2 або 3, то виводиться повідомлення - назва числа, відповідно, One, Two, Three. В усіх інших випадках виводиться слово Unknown.
num = int(input("Enter your number (1-3): "))
if num == 1:
   print("One.")
elif num == 2:
   print("Two.")
elif num == 3:
   print("Three.")
else:
   print("This nukber is unknown.")

#Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.
letter1 = input("Enter the 1st letter: ")
letter2 = input("Enter the 2st letter: ")
if letter1 <= letter2:
    print(letter1, letter2)
elif letter2 <= letter1:
    print(letter2, letter1)

#Середній рівень

#Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори. Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні. Непарні номери від 19 до 28 - червоні, а парні номери - чорні. Непарні номери від 29 до 36 - чорні, а парні номери - червоні. Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.
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

#Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.

#Вхідні дані:
#1
#2
#3
#2

#4
#4
#4
#4

# Вихідні дані:
# B
# The distance is the same 

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dA = x1 ** 2 + y1 ** 2
dB = x2 ** 2 + y1 ** 2

if dA > dB:
    print ("A")
elif dB > dA:
    print ("B")
else:
    print("The distance is the same.")
    
# Вводяться координати (x, y) точки A і радіус кола (r). Визначити, чи належить дана точка колу, якщо його центр знаходиться в початку координат.
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

# Напишіть програму для знаходження коренів квадратного рівняння a*x2 + b*x + c = 0. Користувач вводить значення коефіцієнтів a, b, c. У вхідних даних наведено три пари вхідних значень коефіцієнтів, а у вихідних даних - відповідні повідомлення про кількість коренів або їх відсутність.
# Вхідні дані:
# 8
# 4
# 2
# 3.6
# 10
#  -3
# 2
# 4
# 2
# Вихідні дані:
# No roots.
# 0.27 and -3.05
# -1.00

# Напишіть програму, щоб визначити, чи задане ціле число (вводиться користувачем) парне або непарне.
# Вхідні дані:
# 2
# 5
# 11
# Вихідні дані:
# True
# False
# False

for _ in range(3):
   n = int(input())
if n % 2 == 0:
     print("True")
else:
    print("False")

# Відомі рік і номер місяця народження людини, а також рік і номер місяця сьогоднішнього дня (січень - 1 і т. д.). Визначити вік людини (число повних років). У разі збігу вказаних номерів місяців вважати, що пройшов повний рік.
# Вхідні дані:
# 1998
# 3
# 2018
# 2
# Вихідні дані:
# 19

birth_year = int(input())
birth_month = int(input())
current_year = int(input())
current_month = int(input())
age = current_year - birth_year
if current_month < birth_month:
    age -= 1
print(age)

# Дано чотирицифрове число. Замінити усі парні цифри числа на символ * і вивести число.
# Вхідні дані:
# 2358
# 2227
# 1353
# Вихідні дані:
# *35*
# ***7
# 1353

for _ in range(3): 
    n = input()
    result = ""
for ch in n:
    if int(ch) % 2 == 0: 
        result += "*"
    else:
        result += ch
print(result)

# String (рядки)
# Напишіть програму, яка приймає від користувача рядок, і відображає цей рядок у верхньому і нижньому регістрах.
text = input()
print(text.upper())
print(text.lower())

# Скласти програму, яка запитує назву баскетбольної команди і повторює її на екрані зі словами: This is a champion!.
team = input()
print(team + " - This is a champion!")

# Дано натуральне число. Знайти число, що отримується при прочитанні його цифр справа наліво.
n = input()
reversed_n = n[::-1]
print(reversed_n)

# Дано рядок. Змініть регістр символів в цьому рядку так, щоб перша буква кожного слова була великою, а інші літери - малими. (метод s.title())
s = input()
print(s.title())

# Напишіть програму, яка по введеному числу n від 1 до 9 виводить на екран n пінгвінів з відповідним номером - число від 1 до n. 
# Зображення одного пінгвіна має розмір 5 x 9 символів, між двома сусідніми пінгвінами також є порожній (з пропусків) стовпець.
# Дозволяється вивести порожній стовпець після останнього пінгвіна. 
# Для спрощення малювання скопіюйте пінгвіна із вихідних даних.
# Врахуйте, що виведення на екран виконується порядково, а не «попінгвінно».

# Вхідні дані: 
# 4 
# Вихідні дані: 
#     _~_        _~_        _~_        _~_ 
#    (o o)      (o o)      (o o)      (o o) 
#   /  V  \    /  V  \    /  V  \    /  V  \ 
#  /(  1  )\  /(  2  )\  /(  3  )\  /(  4  )\ 
#    ^^ ^^      ^^ ^^      ^^ ^^      ^^ ^^



n = int(input())
for i in range(n):
    print("    _~_    ", end="")
print()
for i in range(n):
    print("   (o o)   ", end="")
print()
for i in range(n):
    print("  /  V  \\  ", end="")
print()
for i in range(n):
    print(f" /(  {i+1}  )\\ ", end="")
print()
for i in range(n):
    print("   ^^ ^^   ", end="")
print()

# У рядку є кілька слів, розділених одним або декількома пропусками. Потрібно прибрати з тексту зайві пропуски: два і більше пропусків поспіль, а також всі пропуски на початку і в кінці рядка. На вхід програмі подається рядок, що складається не більше ніж з 255 символів. Надрукувати новий рядок.
# Вхідні дані:
# Beyond the green     swelling hills of the     Mittel Land rose mighty slopes of forest    up    to the lofty steeps of the Carpathians    themselves
# Вихідні дані:
# Beyond the green swelling hills of the Mittel Land rose mighty slopes of forest up to the lofty steeps of the Carpathians themselves

s = input()  
words = s.split()
result = " ".join(words)
print(result)            

# Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими стоїть n-1 знаків операцій, кожна з яких може бути або +, або -. Обчисліть значення цього виразу. Програма має надрукувати результат обчислення цього виразу.
# Вхідні дані:
# 5-3+1
# 6+3-2
# Вихідні дані:
# 3
# 7

for _ in range(2):
 expr = input() 
result = eval(expr)
print(result)

# Напишіть програму, на вхід якої даються чотири числа a, b, c і d, кожне у своєму рядку. Програма повинна вивести фрагмент таблиці множення для всіх чисел відрізка [a; b] на всі числа відрізка [c; d]. Числа a, b, c і d є натуральними і не перевищують 10, a ≤ b, c ≤ d. Дотримуйтесь формату виведення як у вихідних даних. Для поділу елементів всередині рядка використовуйте \t - символ табуляції. Зауважте, що лівим стовпчиком і верхнім рядком виводяться самі числа із заданих відрізків.
# Вхідні дані:
# 1
# 4
# 2
# 5
# Вихідні дані:
# 	2	3	4	5
# 1	2	3	4	5
# 2	4	6	8	10
# 3	6	9	12	15
# 4	8	12	16	20

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print("\t", end="")
for j in range(c, d + 1):
    print(j, end="\t")
print()
for i in range(a, b + 1):
    print(i, end="\t") 
    for j in range(c, d + 1):
        print(i * j, end="\t")
    print()

# Напишіть програму для друку літери A за допомогою введеного користувачем символа.
#  Вхідні дані: 
#  * 
#  Вихідні дані: 
#    *** 
#   *   * 
#   *   * 
#   ***** 
#   *   * 
#   *   * 
#   *   * 

ch = input()
print("  " + ch*3)
print(" " + ch + "   " + ch)
print(" " + ch + "   " + ch)
print(" " + ch*5)
print(" " + ch + "   " + ch)
print(" " + ch + "   " + ch)
print(" " + ch + "   " + ch)

# Напишіть програму, яка визначає, чи є у введеному рядку десяткові цифри, і виводить найбільше число, яке можна скласти з цих цифр. Провідних нулів у числі бути не повинно (за винятком числа 0, запис якого містить рівно одну цифру). Гарантовано, що у рядку є принаймні одна цифра. Вхідний рядок містить довільні символи. Програма повинна вивести найбільше число, яке можна скласти з присутніх в рядку десяткових цифр.
# Вхідні дані:
# Release Date: July 27, 2008
# Last Updated: February 22, 2018
# Вихідні дані:
# 872200
# 822210

for _ in range(2): 
    s = input()   
    digits = [ch for ch in s if ch.isdigit()]  
    digits.sort(reverse=True)
    number = "".join(digits)
    print(number)