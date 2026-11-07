
import json
from pathlib import Path

# Find the project data folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "orders.json"


def load_orders():

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            orders = json.load(file)

        return orders

    except FileNotFoundError:
        print("Error: orders.json not found.")
        return {}

    except json.JSONDecodeError:
        print("Error: Invalid JSON data.")
        return {}


def get_all_products(orders):

    products = set()

    for customer_products in orders.values():

        for product in customer_products:
            products.add(product)

    return sorted(products)
