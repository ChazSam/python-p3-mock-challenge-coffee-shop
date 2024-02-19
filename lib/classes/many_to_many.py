class Coffee:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        print(f"coffee name: {self.name}")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name

    def orders(self):
        return [x for x in Order.all if self == x.coffee]
    
    def customers(self):
        return list(set([x.customer for x in Order.all if self == x.coffee]))
    
    def num_orders(self):
        orders = [x for x in Order.all if self == x.coffee]

        if len(orders) > 0:
            return len(orders)
        else:
            return 0
    
    def average_price(self):
        orders = [x.price for x in Order.all if self == x.coffee]

        if len(orders) > 0:
            return (sum(orders) / len(orders))
        else:
            return 0


class Customer:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        print(f"Customer name: {self.name}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15 :
            self._name = name

    def orders(self):
        return [x for x in Order.all if self == x.customer] 
    
    def coffees(self):
        return list(set([x.coffee for x in Order.all if self == x.customer]))
    
    def create_order(self, coffee, price):       
        return Order(self, coffee, price)
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def __repr__(self):
        print(f"Order: Customer- {self.customer} Coffee - {self.coffee} Price: {self.price}")
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0 and not hasattr(self, "price"):
            self._price = price
