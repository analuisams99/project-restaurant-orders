class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.inventory, self.orders = dict(self.MINIMUM_INVENTORY), []

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] == 0:
                return False
            self.inventory[ingredient] -= 1

        self.orders.append({customer, order, day})

    def get_quantities_to_buy(self):
        quantities_to_buy = dict()

        for ingredient in self.MINIMUM_INVENTORY:
            total = (
                self.MINIMUM_INVENTORY[ingredient] - self.inventory[ingredient]
            )
            quantities_to_buy[ingredient] = total

        return quantities_to_buy

    def get_available_dishes(self):
        available_dishes = set()

        for dish in self.INGREDIENTS:
            if self.inventory[self.INGREDIENTS[dish][0]] > 1:
                available_dishes.add(dish)

        return available_dishes
