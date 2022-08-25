import csv

from .track_orders import TrackOrders


def read_file(path_to_file):
    if "csv" not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
    try:
        orders_list = []

        with open(path_to_file, encoding="utf-8") as file:
            logs = csv.reader(file)
            for log in logs:
                orders_list.append(log)

        return orders_list

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    track_orders = TrackOrders()

    for customer, order, day in orders:
        track_orders.add_new_order(customer, order, day)

    most_ordered_dish_by_maria = (
        track_orders.get_most_ordered_dish_per_customer("maria")
    )
    times_arnaldo_ordered_burger = track_orders.get_customer_meal_count(
        "arnaldo", "hamburguer"
    )
    never_ordered_by_joao = track_orders.get_never_ordered_per_customer("joao")
    days_whithout_joao_order = (
        track_orders.get_days_never_visited_per_customer("joao")
    )

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{most_ordered_dish_by_maria}\n"
            f"{times_arnaldo_ordered_burger}\n"
            f"{never_ordered_by_joao}\n"
            f"{days_whithout_joao_order}\n"
        )
