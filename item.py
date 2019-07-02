class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.change_quality_with_age()
        self.reduce_sell_in()
        self.handle_expired_item()

    def change_quality_with_age(self):
        self.decrease_quality()

    def reduce_sell_in(self):
        self.sell_in = self.sell_in - 1

    def handle_expired_item(self):
        if self.sell_in < 0:
            self.decrease_quality()

    def decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1


class ImprovingProduct(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def change_quality_with_age(self):
        self.increase_quality_based_on_age()
        self.reduce_quality_to_max()

    def increase_quality_based_on_age(self):
        self.increase_quality()
        if self.sell_in < 11:
            self.increase_quality()
        if self.sell_in < 6:
            self.increase_quality()

    def reduce_quality_to_max(self):
        if self.quality > 50:
            self.quality = 50

    def handle_expired_item(self):
        if self.sell_in < 0:
            self.quality = 0

    def increase_quality(self):
        self.quality = self.quality + 1


class Sulfuras(Item):
    def __init__(self, sell_in, quality):
        Item.__init__(self, "Sulfuras, Hand of Ragnaros", sell_in, quality)

    def decrease_quality(self):
        pass

    def reduce_sell_in(self):
        pass
