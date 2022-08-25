from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = [
            order[1] for order in self.orders if order[0] == customer
        ]
        result = Counter(customer_orders).most_common()[0][0]

        return result

    def get_never_ordered_per_customer(self, customer):
        customer_orders = set()
        all_orders = set()

        for customer_name, order, _ in self.orders:
            all_orders.add(order)
            if customer_name == customer:
                customer_orders.add(order)

        return all_orders.difference(customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        customer_days = set()
        all_days = set()

        for customer_name, _, day in self.orders:
            all_days.add(day)
            if customer_name == customer:
                customer_days.add(day)

        return all_days.difference(customer_days)

    def get_busiest_day(self):
        busiest_day = []

        for _, _, day in self.orders:
            busiest_day.append(day)

        return Counter(busiest_day).most_common(1)[0][0]

    def get_least_busy_day(self):
        least_busy_day = []

        for _, _, day in self.orders:
            least_busy_day.append(day)

        return Counter(least_busy_day).most_common()[-1][0]

    def get_customer_meal_count(self, customer, meal):
        customer_orders = [
            order[1] for order in self.orders if order[0] == customer
        ]
        meal_counter = [order for order in customer_orders if order == meal]
        return len(meal_counter)
