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

def sort_contacts(contacts, sort_by='name', reverse=False):
    if sort_by == 'name':
        contacts.sort(key=lambda x: x['name'], reverse=reverse)
    elif sort_by == 'phone':
        contacts.sort(key=lambda x: x['phone'], reverse=reverse)
    return contacts

def main_menu(stdscr):
    curses.curs_set(0)  
    stdscr.nodelay(0)  
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
        stdscr.addstr(10, 4, "7. Сортировать контакты")
        stdscr.addstr(11, 4, "8. О программе")
        stdscr.addstr(12, 4, "9. Выход из программы")

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
            sort_contacts_ui(stdscr)
        elif choice == ord('8'):
            about_program_ui(stdscr)
        elif choice == ord('9'):
            break

def sort_contacts_ui(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(2, 2, "Сортировать контакты", curses.A_BOLD)
    stdscr.addstr(4, 4, "1. По имени")
    stdscr.addstr(5, 4, "2. По номеру телефона")
    stdscr.addstr(6, 4, "Выберите критерий сортировки: ")
    criterion = stdscr.getch()
    
    stdscr.addstr(8, 4, "3. Возрастание")
    stdscr.addstr(9, 4, "4. Убывание")
    stdscr.addstr(10, 4, "Выберите направление сортировки: ")
    direction = stdscr.getch()

    sort_by = 'name' if criterion == ord('1') else 'phone'
    reverse = True if direction == ord('4') else False

    sort_contacts(contacts, sort_by, reverse)
    display_contacts_ui(stdscr)  

def display_contacts_ui(stdscr):
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(2, 2, "Телефонная книга", curses.A_BOLD)
    display_contacts(stdscr, contacts)
    stdscr.refresh()
    stdscr.getch()


def display_contacts(stdscr, contacts):
    if contacts:
        for i, contact in enumerate(contacts):
            stdscr.addstr(4 + i, 4, f"Имя: {contact['name']}, Телефон: {contact['phone']}")
    else:
        stdscr.addstr(4, 4, "Телефонная книга пуста.")

filename = "contacts.txt"
contacts = load_contacts(filename)
curses.wrapper(main_menu)
