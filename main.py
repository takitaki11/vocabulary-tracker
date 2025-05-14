from manager import WordManager

manager = WordManager()



def menu():
    print("\n📚 Добро пожаловать в трекер слов на Python!")

    while True:
        print("\n--- Language Vocabulary Tracker ---")
        print("1. Добавить слово")
        print("2. Показать все слова")
        print("3. Обновить слово")
        print("4. Удалить слово")
        print("5. Сгенерировать отчёт")
        print("6. Экспорт в CSV")
        print("7. Импорт из CSV")
        print("8. Экспорт в JSON")
        print("9. Импорт из JSON")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            term = input("Введите слово: ").strip()
            definition = input("Значение: ").strip()
            example = input("Пример: ").strip()
            manager.add_word(term, definition, example)

        elif choice == '2':
            manager.show_words()

        elif choice == '3':
            manager.show_words()
            index = int(input("Номер слова для обновления: ")) - 1
            term = input("Новое слово: ").strip()
            definition = input("Новое значение: ").strip()
            example = input("Новый пример: ").strip()
            manager.update_word(index, term, definition, example)

        elif choice == '4':
            manager.show_words()
            index = int(input("Номер слова для удаления: ")) - 1
            manager.delete_word(index)

        elif choice == '5':
            manager.generate_report()

        elif choice == '6':
            manager.export_to_csv()
            print("Экспортировано в words.csv")

        elif choice == '7':
            manager.import_from_csv()
            print("Импортировано из words.csv")

        elif choice == '8':
            manager.export_to_json()
            print("Экспортировано в words.json")

        elif choice == '9':
            manager.import_from_json()
            print("Импортировано из words.json")

        elif choice == '0':
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()
