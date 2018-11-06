"""
This script contains class DatabaseContainer
"""


class DatabaseContainer:
    """
    This class collects instances of database classes used in application
    """

    def __init__(self, menu, orders, items):
        self.menu = menu
        self.orders = orders
        self.items = items
