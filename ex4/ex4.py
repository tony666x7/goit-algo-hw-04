contacts = {}  # Словник для зберігання контактів (ім'я: номер телефону)

def parse_input(user_input):
     # Функція для розбору введеного користувачем рядка на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
     # Додає контакт у словник
    try:
        name, phone = args
        contacts[name] = phone
        return f"Контакт {name} додано\n"
    except:
        return "Помилка. Введіть Им'я та номер\n"
    
def change_contact(args, contacts):
    # Змінює номер телефону для існуючого контакту
    try:
        name, phone = args
        contacts[name] = phone
        return f"Контакт {name} змінено\n"
    except:
        return "Нічого не змінено. Введіть Им'я та новий номер\n"

def show_contact():
     # Виводить усі збережені контакти
    if contacts:
        result = "Всі збережені контакти: \n"
        for name, phone in contacts.items():     
            result += f"{name}: {phone}\n"
        return result
    else:
        return "Немає збережених контактів\n"
    
def delete_contact(args, contacts):
    # Видаляє вказанний контакт
    try:
        name, = args
        phone = contacts.pop(name)
        return f"Контакт {name} видалено\n"
    except:
        return f"Контакт {name} не існує\n"


def main():
    
    # Основний цикл функції
    print("Вітаю! Я віртуальний помічник\n\
          \n\t\t Меню\
          \nКоманда \t\t-> \tДія\n\
          \nHello \t\t\t-> \tПривітання\
          \nadd 'name', 'phone' \t-> \tДодати контакт до списку\
          \nchange 'name', 'pnone' \t-> \tЗамінити контакту зі списку\
          \ndelete 'name' \t\t-> \tВидалити контакт зі списку\
          \nexit/close \t\t-> \tЗавершення роботи помічника\n")
    
    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До зустрічі!\n")
            break
        elif command == "hello":
            print("Як я можу допомогти?\n")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_contact())
        elif command == "delete" and args:
            print(delete_contact(args, contacts))
        else:
            print("Невірна команда.\n")

if __name__ == "__main__":
    main()