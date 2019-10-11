from random import randint 
from time import localtime 

"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Order inherit from"""

    def __init__ (self, species, qty, country_code, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type 
        self.tax = tax
        self.country_code = country_code


    def get_base_price(self):
        random_price = randint(5, 9)
        print(random_price)
        base_price = random_price * 1.5 if self.species == 'Christmas' else random_price
        # psuedocode for rush hour prices:
        # if the local time is between 8am and 11am M-F
        # then we add an extra $4 PER MELON
        # M = tm_wday 0 and F = tm_wday 4
        # 8am = tm_hour 8 and 11am = tm_hour 11
        return base_price         


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()         
        total = (1 + self.tax) * self.qty * base_price
        if self.country_code != 'USA' and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, country_code='USA', order_type='domestic', tax=0.08)
        
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, country_code, order_type='international', tax=0.17)


class GovernmentMelonOrder(AbstractMelonOrder):

    passed_inspection = False

    def __init__(self, species, qty):
        super().__init__(species, qty, country_code='USA', order_type='domestic', tax=0.00)

    def mark_inspection(self, passed):
        """Record the fact than an order has been inspected."""

        self.passed_inspection = passed 