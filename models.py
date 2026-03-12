# ByteBites Data Models
#
# Customer    - Represents a registered user with a purchase history; supports user verification.
# Item        - Represents a single menu item with a price, category, and popularity rating.
# Menu        - Represents a named collection of Items; supports filtering and adding items.
# Transaction - Represents a customer purchase containing selected Items; computes total cost.


class Customer:
    def __init__(self, customer_id: int, name: str):
        self.customer_id = customer_id
        self.name = name
        self.purchase_history: list = []  # List[Transaction]

    def verify_user(self) -> bool:
        pass


class Item:
    def __init__(self, item_id: int, name: str, price: float, category: str, popularity_rating: float):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, menu_id: int, name: str):
        self.menu_id = menu_id
        self.name = name
        self.items: list = []  # List[Item]

    def filter_by_category(self, category: str) -> list:  # List[Item]
        pass

    def add_item(self, item: Item) -> None:
        pass


class Transaction:
    def __init__(self, transaction_id: int, transaction_date):
        self.transaction_id = transaction_id
        self.transaction_date = transaction_date
        self.items: list = []  # List[Item]
        self.total_cost: float = 0.0

    def compute_total(self) -> float:
        pass