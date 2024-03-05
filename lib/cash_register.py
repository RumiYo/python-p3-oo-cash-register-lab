#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = list()
    
    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.price = price
        self.quantity = quantity
        for i in range(quantity):
            self.items.append(title)

    def apply_discount(self, discount=20):
        if self.total == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total * discount / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        self.total -= (self.price * self.quantity) 


