#Класс Родитель
class Item:
    """
    Class Item create composition with class Inventory. I'am learned a base to composition 
    """

    def __init__(self, name: str, weight: float):
        self.name = name.lower()
        self.weight = round(weight, 3)
    
    def use(self):
        return 'Этот предмет нельзя использовать напрямую!'
    
    def get_type_item(self):
        return 'Предмет'

# Дочерние классы
class Weapon(Item):

    def __init__(self, name: str, weight: float, damage: float):
        super().__init__(name, weight)
        self.damage = damage

    def use(self):
        return f'Вы использовали предмет: {self.name}, вы нанесли: {self.damage} урона!'
    
    def get_type_item(self):
        return 'Оружие'

class Armor(Item):
    
    def __init__(self, name: str, weight: float, endurance: float):
        super().__init__(name, weight)
        self.endurance = endurance

    def use(self):
        return f'Вы использовали предмет: {self.name}, вы снизили прочность на: {self.endurance} единицы!'
    
    def get_type_item(self):
        return 'Броня'

class Consumable(Item):
    
    def __init__(self, name: str, weight: float, health_restore: float):
        super().__init__(name, weight)
        self.health_restore = health_restore

    def use(self):
        return f'Вы использовали: {self.name}, восставновили здоровья: {self.health_restore}!'
    
    def get_type_item(self):
        return 'Материал'
        