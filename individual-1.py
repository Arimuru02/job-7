import sys
if __name__ == '__main__':
    # Список .
    train = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные .
            race = input("Название пункта назначения ")
            number = input("Номер поезда ")
            time = input("время отправления ")
            # Создать словарь.
            trains = {
                'race': race,
                'number': number,
                'time': time,
            }
            # Добавить словарь в список.
            train.append(trains)
            # Отсортировать список в случае необходимости.
            if len(train) > 1:
                train.sort(key=lambda item: item.get('race', ''))
        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Пункт",
                    "Номер",
                    "Время отправления"
                )
            )
            print(line)
            # Вывести данные о всех рейсах.
            for idx, trains in enumerate(train, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        trains.get('race', ''),
                        trains.get('number', ''),
                        trains.get('time', '')
                    )
                )
            print(line)
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sel = (parts[1])
            count = 0
            for trains in train:
                if trains.get('race') == sel:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, trains.get('race', ''))
                    )
                    print('Номер рейса:', trains.get('number', ''))
                    print('Время отправления:', trains.get('type', ''))
            # Если счетчик равен 0, то рейсы не найдены.
            if count == 0:
                print("Рейс не найден.")
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список рейсов;")
            print("select <товар> - информация о рейсе;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print("Неизвестная команда {command}", file=sys.stderr)