class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.potential_discount_threshold = 300
        self.discount_threshold = 500
        self.priority_threshold = 800
        self.vip_threshold = 1000

    def add_customer(self, name, purchases):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)

    def generate_report(self):
        for customers, purchases in self.customers.items():
            total_price = 0
            for purchase in purchases:
                if purchase['price'] > self.tax_threshold:
                    taxed_price = purchase['price'] * (1 + self.tax_rate)
                    total_price += taxed_price
                else:
                    total_price += purchase['price']
            print(customers)
            self.check_discount_eligibility(total_price)

    def check_discount_eligibility(self, total_price):
        if total_price > self.vip_threshold:
            print("VIP Customer!")
        elif total_price > self.priority_threshold:
            print("Priority Customer")
        elif total_price > self.discount_threshold:
            print("Eligible for discount")
        elif total_price > self.potential_discount_threshold:
            print("Potential future discount customer")
        else:
            print("No discount")

    def has_heavy_items(self, purchases):
        return any(purchase.get('weight', 0) > 20 for purchase in purchases)

    def has_fragile_items(self, purchases):
        return any(purchase.get('fragile', False) for purchase in purchases)

    def calculate_shipping_fee(self, purchases):
        if self.has_heavy_items(purchases):
            return 50
        else:
            return 20

    def calculate_shipping_fee_for_heavy_items(self, purchases):
        if self.has_heavy_items(purchases):
            return 50
        return 20

    def calculate_shipping_fee_for_fragile_items(self, purchases):
        if self.has_fragile_items(purchases):
            return 60
        return 25

flat_tax = 0.2