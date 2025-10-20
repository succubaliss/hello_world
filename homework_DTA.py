# Домашнє завдання:
# Задача 1. Середнє трьох чисел
# Користувач вводить три числа. Обчисли середнє арифметичне.
n1 = int(input("Enter your 1st number: "))
n2 = int(input("Enter your 2nd number: ")) 
n3 = int(input("Enter your 3rd number: ")) 
arithmetic_mean = (n1+n2+n3) / 3 
print(f"The arithmetic mean of {n1}, {n2}, and {n3} is {arithmetic_mean}.")

# Задача 2. Остача від ділення
# Користувач вводить два числа. Знайди остачу від ділення першого на друге.
n1= float(input("Enter the 1st number: "))
n2 = float(input("Enter the 2nd number: ")) 
remainder = ( n1 / n2 ) 
print(f"The remainder of your inquiry is {remainder}.")

#Задача 3. Подвоєне число
# Користувач вводить число. Виведи подвоєне значення цього числа.
n = float(input("Enter the number: "))
number_x2 = n * 2
print(f"The double of {n} is {number_x2}.")

# Задача 4. Конвертація хвилин у секунди
# Користувач вводить кількість хвилин. Обчисли, скільки це буде секунд.
min = int(input("Enter minutes : "))
min_to_sec = min * 60
print(f"The number of {min} equals {min_to_sec}.")

# Задача 5. Кількість яблук на кожного
# Є n яблук і k учнів. Скільки яблук отримає кожен учень, якщо ділити порівну, і скільки залишиться?
apples = int(input("Enter the number of apples : "))
stud = int(input("Enter the number of students : "))
apples_per_stud = apples // stud 
remaining_apples = apples % stud 
print(f"Every student will get {apples_per_stud} apples.")
print(f"The remainder will be {remaining_apples} apples.")

# Задача 6. Остання цифра числа
# Користувач вводить число. Виведи його останню цифру.
n = int(input("Please enter the number: "))
last_digit = abs(n) % 10 
print(f" The last digit of your number is:{last_digit}")

# Задача 7*. Обмін змінних
# Користувач вводить два числа. Після цього потрібно “поміняти” їх місцями і вивести результат.
a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))
a, b = b, a
print(f"After swapping: 1st number = {a}, 2nd number = {b}.")