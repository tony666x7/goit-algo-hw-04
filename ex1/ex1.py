def total_salary(path):
    try:
        # Відкриваємо файл у режимі читання з автоматичним закриттям за допомогою контекстного менеджера
        with open(path,'r', encoding='utf-8') as file:
             # Ініціалізуємо змінні для обрахунку загальної та середньої зарплати
            total_salary = 0 
            num_developer = 0

            # Перебираємо рядки у файлі
            for line in file:
                # Розділяємо рядок за допомогою коми та видаляємо зайві пробіли
                parts = line.strip().split(',')

                 # Перевіряємо, чи отримали ми дві частини (прізвище та зарплата)
                if len(parts) == 2:
                     # Додаємо зарплату до загальної суми
                    total_salary += int(parts[1])
                    # Збільшуємо кількість розробників
                    num_developer += 1

            # Обчислюємо середню зарплату
            if num_developer > 0:
                avarage_salary = total_salary / num_developer
            else:
                # Якщо немає розробників, середня зарплата - 0
                avarage_salary = 0

             # Повертаємо кортеж із загальною та середньою зарплатою
            return total_salary, avarage_salary


    except FileNotFoundError:
        # Обробляємо випадок, коли файл не знайдено
        print(f"Помилка: Файл '{path}' не знайдено.")
        return None, None
    except Exception as e:
        # Обробляємо інші можливі винятки
        print(f'Помилка: {e}')
        return None, None 

# Приклад використання функції  
total, average = total_salary("/Users/antonstoliarchuk/Desktop/My_repo/goit-algo-hw-04/ex1/salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") 
