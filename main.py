import time

def load_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, phone = line.strip().split(',')
                contacts.append({"name": name, "phone": phone})
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")
    print("Контакты успешно сохранены в файл.")

def main_menu():
    while True:
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Поиск контакта")
        print("4. Отобразить телефонную книгу")
        print("5. Изменить номер контакта")
        print("6. О программе")
        print("7. Выход из программы")

        choice = input("Выберите опцию: ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            phone = input("Введите телефонный номер: ")
            add_contact(contacts, name, phone)
            print(f"Контакт {name} успешно добавлен!")
        elif choice == "2":
            print_contacts(contacts)
            name = input("Введите имя контакта для удаления: ")
            remove_contact(contacts, name)
        elif choice == "3":
            name = input("Введите имя контакта для поиска: ")
            contact = find_contact(contacts, name)
            if contact:
                print(f"Найден контакт: Имя: {contact['name']}, Телефон: {contact['phone']}")
            else:
                print("Контакт не найден.")
        elif choice == "4":
            display_contacts(contacts)
        elif choice == "5":
            name = input("Введите имя контакта для изменения номера: ")
            new_phone = input("Введите новый телефонный номер: ")
            update_contact(contacts, name, new_phone)
        elif choice == "6":
            print("Программа телефонный справочник, версия 1.0")
            print("Написал студент GeekBrains: Павел О.")
            print("Преподаватель: Сердюк С.С.")
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

        time.sleep(1)

def add_contact(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})
    save_contacts(filename, contacts)

def remove_contact(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            save_contacts(filename, contacts)
            print(f"Контакт {name} успешно удален")
            return
    print("Контакт не найден.")

def find_contact(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None

def update_contact(contacts, name, new_phone):
    for contact in contacts:
        if contact["name"] == name:
            contact["phone"] = new_phone
            save_contacts(filename, contacts)
            print(f"Номер телефона контакта {name} успешно обновлен")
            return
    print("Контакт не найден.")

def display_contacts(contacts):
    if contacts:
        for contact in contacts:
            print(f"Имя: {contact['name']}, Телефон: {contact['phone']}")
    else:
        print("Телефонная книга пуста.")

def print_contacts(contacts):
    if contacts:
        print("Список контактов:")
        for i, contact in enumerate(contacts):
            print(f"{i+1}. Имя: {contact['name']}, Телефон: {contact['phone']}")
    else:
        print("Телефонная книга пуста.")

if __name__ == "__main__":
    filename = "contacts.txt"
    contacts = load_contacts(filename)
    print("Контакты загружены из файла.")
    main_menu()
