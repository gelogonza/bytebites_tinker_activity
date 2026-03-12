## UML Class Diagram

mermaid
classDiagram
    class Customer {
        +int customerId
        +String name
        +List~Order~ purchaseHistory
        +verifyUser() bool
    }

    class Item {
        +int itemId
        +String name
        +float price
        +String category
        +float popularityRating
    }

    class Menu {
        +int menuId
        +List~Item~ items
        +filterByCategory(category: String) List~Item~
        +addItem(item: Item) void
        +removeItem(itemId: int) void
    }

    class Order {
        +int orderId
        +int customerId
        +List~Item~ selectedItems
        +float totalCost
        +Date orderDate
        +computeTotal() float
        +addItem(item: Item) void
        +removeItem(itemId: int) void
    }

    Customer "1" --> "0..*" Order : places
    Order "1" --> "1..*" Item : contains
    Menu "1" --> "0..*" Item : lists

