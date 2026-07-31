from inventory import Inventory
from items import (
    Weapon,
    Armor,
    Consumable
)

def main() -> str:
    my_player = Inventory()
    while True:
        try:
            command = input('Введите команду: ').strip().split()
            cmd = command[0].lower()
        except IndexError:
            print('Вы не ввели никакую команду, попробуйте снова, но впредь будте внимательней!')
            continue

        if cmd == 'add_item' and len(command) == 5:
            try:
                type_item = command[3].lower()
                if type_item == 'оружие':
                    print(my_player.add_item(Weapon(command[1], float(command[2]), command[4])))
                elif type_item == 'броня':
                    print(my_player.add_item(Armor(command[1], float(command[2]), command[4])))
                elif type_item == 'материал':
                    print(my_player.add_item(Consumable(command[1], float(command[2]), command[4])))
                else:
                    print('Вы не можете взять с собой данный предмет!')

            except ValueError:
                print('Вы ввели в поле "Вес" не число, следите внимательнее!')
                continue
            except Exception as e:
                print(f'Ошибка: {e}')
                continue
        
        elif cmd == 'remove_item' and len(command) == 2:
            print(my_player.remove_item(command[1]))

        elif cmd == 'use_item' and len(command) == 2:
            print(my_player.use_item(command[1]))

        elif cmd == 'list_items' and len(command) == 1:
            print(my_player.list_items())
        
        elif cmd == 'quit':
            return 'Вы вышли из программы.'
        
        else:
            print('\nВы ввели неверную команду или совершили ошибку в синтаксисе программы, следите за условиями.\n')

if __name__ == '__main__':
    print(main())



