from items import Item, Consumable

class Inventory:
    
    def __init__(self):
        self.max_weight = 50.0 # Interval for validate weight items 
        self.items = [] # List all items


    def add_item(self, item: Item):
        """
        Add item and validate data (weight and type) on error.
        """
        current_weight = sum(i.weight for i in self.items)
        if current_weight + item.weight > self.max_weight:
            return f'Будет тяжеловато, стоит оставить этот предмет.\nДоступно ещё {self.max_weight - current_weight}.'
    
        for i in range(len(self.items)):
            if item.name == self.items[i].name:
                return 'Вы уже брали этот предмет с собой, думаю, его можно оставить, зачем две одинаковые штуковины).'
        
        self.items.append(item)
        return f'Вы взяли с собой {item.name}, вес: {item.weight}.'


    def remove_item(self, item_name: str):
        """
        Delete item in inventory and validate, use generator list.
        """
        item_name = item_name.lower()

        if not self.items:
            return 'Инвентарь пуст.'
  
        self.items = [el for el in self.items if el.name != item_name]
        return f'\nТекущий вес: {sum(i.weight for i in self.items)}/{self.max_weight}.\n' 


    def use_item(self, item_name: str):
        """
        Use the item, up and down health and battle to the enemy.
        """
        for el in self.items:
            if el.name.lower() == item_name:
                result = el.use()
                if isinstance(el, Consumable):
                    self.remove_item(item_name)
                return result
        return 'Предмет не найден.'

    def list_items(self):
        """
        Return items lists use join().
        """
        return '\n'.join(f'[{item.weight}] {item.name} - ({item.get_type_item()})' for item in self.items) + f'\nТекущий вес: {sum(i.weight for i in self.items)}/{self.max_weight}.'