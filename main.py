import curses
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

def export_contacts_to_file(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")
    print(f"Контакты успешно выгружены в файл {filename}")

def main_menu(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(0)  # Set blocking mode
    while True:
        stdscr.clear()
        stdscr.border(0)
        stdscr.addstr(2, 2, "Телефонный справочник", curses.A_BOLD)
        stdscr.addstr(4, 4, "1. Добавить контакт")
        stdscr.addstr(5, 4, "2. Удалить контакт")
        stdscr.addstr(6, 4, "3. Поиск контакта")
        stdscr.addstr(7, 4, "4. Отобразить телефонную книгу")
        stdscr.addstr(8, 4, "5. Изменить номер контакта")
        stdscr.addstr(9, 4, "6. Выгрузить контакты в файл")
        stdscr.addstr(10, 4, "7. О программе")
        stdscr.addstr(11, 4, "8. Выход из программы")

        stdscr.refresh()
        choice = stdscr.getch()

        if choice == ord('1'):
            add_contact_ui(stdscr)
        elif choice == ord('2'):
            remove_contact_ui(stdscr)
        elif choice == ord('3'):
            search_contact_ui(stdscr)
        elif choice == ord('4'):
            display_contacts_ui(stdscr)
        elif choice == ord('5'):
            update_contact_ui(stdscr)
        elif choice == ord('6'):
            export_contacts_ui(stdscr)
        elif choice == ord('7'):
            about_program_ui(stdscr)
        elif choice == ord('8'):
            break

def add_contact_ui(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(2, 2, "Добавить контакт", curses.A_BOLD)
    stdscr.addstr(4, 4, "Введите имя: ")
    name = stdscr.getstr(4, 18, 20).decode('utf-8')
    stdscr.addstr(5, 4, "Введите телефон: ")
    phone = stdscr.getstr(5, 20, 20).decode('utf-8')
    add_contact(contacts, name, phone)
    stdscr.addstr(7, 4, f"Контакт {name} успешно добавлен!")
    stdscr.refresh()
    stdscr.getch()

def remove_contact_ui(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.border(0)
    print_contacts(stdscr, contacts)
    stdscr.addstr(10, 4, "Введите имя контакта для удаления: ")
    name = stdscr.getstr(10, 38, 20).decode('utf-8')
    remove_contact(contacts, name)
    stdscr.refresh()
    stdscr.getch()

def search_contact_ui(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(2, 2, "Поиск контакта", curses.A_BOLD)
    stdscr.addstr(4, 4, "Введите имя контакта для поиска: ")
    name = stdscr.getstr(4, 36, 20).decode('utf-8')
    contact = find_contact(contacts, name)
    if contact:
        stdscr.addstr(6, 4, f"Найден контакт: Имя: {contact['name']}, Телефон: {contact['phone']}")
    else:
        stdscr.addstr(6, 4, "Контакт не найден.")
    stdscr.refresh()
    stdscr.getch()

def display_contacts_ui(stdscr):
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(2, 2, "Телефонная книга", curses.A_BOLD)
    display_contacts(stdscr, contacts)
    stdscr.refresh()
    stdscr.getch()

def update_contact_ui(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(2, 2, "Изменить номер контакта", curses.A_BOLD)
    stdscr.addstr(4, 4, "Введите имя контакта: ")
    name = stdscr.getstr(4, 28, 20).decode('utf-8')
    stdscr.addstr(5, 4, "Введите новый номер: ")
    new_phone = stdscr.getstr(5, 28, 20).decode('utf-8')
    update_contact(contacts, name, new_phone)
    stdscr.refresh()
    stdscr.getch()

def export_contacts_ui(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(2, 2, "Выгрузить контакты в файл", curses.A_BOLD)
    stdscr.addstr(4, 4, "Введите имя файла: ")
    export_filename = stdscr.getstr(4, 22, 20).decode('utf-8')
    export_contacts_to_file(export_filename, contacts)
    stdscr.addstr(6, 4, f"Контакты успешно выгружены в файл {export_filename}")
    stdscr.refresh()
    stdscr.getch()

def about_program_ui(stdscr):
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(2, 2, "О программе", curses.A_BOLD)
    stdscr.addstr(4, 4, "Программа телефонный справочник, версия 1.0")
    stdscr.addstr(5, 4, "Написал студент GeekBrains: Павел О.")
    stdscr.addstr(6, 4, "Преподаватель: Сердюк С.С.")
    stdscr.refresh()
    stdscr.getch()

def add_contact(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})
    save_contacts(filename, contacts)

def remove_contact(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            save_contacts(filename, contacts)
            return

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
            return

def display_contacts(stdscr, contacts):
    if contacts:
        for i, contact in enumerate(contacts):
            stdscr.addstr(4 + i, 4, f"Имя: {contact['name']}, Телефон: {contact['phone']}")
    else:
        stdscr.addstr(4, 4, "Телефонная книга пуста.")

def print_contacts(stdscr, contacts):
    if contacts:
        stdscr.addstr(4, 4, "Список контактов:")
        for i, contact in enumerate(contacts):
            stdscr.addstr(6 + i, 4, f"{i+1}. Имя: {contact['name']}, Телефон: {contact['phone']}")
    else:
        stdscr.addstr(4, 4, "Телефонная книга пуста.")

filename = "contacts.txt"
contacts = load_contacts(filename)
curses.wrapper(main_menu)
