class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def increase_quality(self):
        self.quality = self.quality + 1

    def decrease_quality(self):
        self.quality = self.quality - 1

    def is_expired(self):
        return self.sell_in < 0

    def handle_expired_item(self):
        if self.quality > 0:
            self.decrease_quality()

    def age_item(self):
        self.sell_in = self.sell_in - 1
        if self.quality > 0:
            self.decrease_quality()

    def reduce_quality_to_upper_limit(self):
        if self.quality > 50:
            self.quality = 50

class Sulfuras(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, quality)

    def reduce_quality_to_upper_limit(self):
        return None

    def age_item(self):
        if self.quality < 50:
            self.increase_quality()


class BackstagePass(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)

    def handle_expired_item(self):
        self.quality = 0

    def age_item(self):
        self.sell_in = self.sell_in - 1
        self.increase_quality_with_age()

    def increase_quality_with_age(self):
        self.increase_quality()
        if self.sell_in < 6:
            self.increase_quality()
        if self.sell_in < 11:
            self.increase_quality()


class AgedBrie(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def handle_expired_item(self):
        if self.sell_in <= 0:
            self.quality = 0

    def age_item(self):
        self.sell_in = self.sell_in - 1
        self.increase_quality_with_age()

    def increase_quality_with_age(self):
        self.increase_quality()
        if self.sell_in < 6:
            self.increase_quality()
        if self.sell_in < 11:
            self.increase_quality()