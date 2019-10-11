"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Order inherit from"""

    def __init__ (self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5 * 1.5 if self.species == 'Christmas' else 5         
        total = (1 + self.tax) * self.qty * base_price
        if self.country_code != 'USA' and self.qty <10:
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
    order_type = "domestic"
    tax = 0.08
    country_code = 'USA'


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    order_type = 'domestic'
    tax = 0
    country_code = 'USA' # We're assuming its our own government
    passed_inspection = False

    def mark_inspection(self, passed):
        """Record the fact than an order has been inspected."""
        
        self.passed_inspection = passed 