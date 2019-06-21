MIN_QUALITY = 0
MAX_QUALITY = 50

class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def reduce_quality_to_cap(self):
        if self.quality > MAX_QUALITY:
            self.quality = MAX_QUALITY

    def change_with_time(self):
        self.reduce_quality()
        
    def reduce_quality(self):
        if self.quality > MIN_QUALITY:
            self.quality = self.quality - 1

    def reduce_sell_in(self):
        self.sell_in = self.sell_in - 1

    def handle_expired(self):
        self.reduce_quality()

    def update_quality(self):
        self.change_with_time()
        self.reduce_quality_to_cap()
        self.reduce_sell_in()
        if self.sell_in < 0:
            self.handle_expired()

class Sulfuras(Item):
    def __init__(self, *args):
        super(Sulfuras, self).__init__("Sulfuras, Hand of Ragnaros", *args)

    def reduce_quality(self):
        return None

    def reduce_quality_to_cap(self):
        return None

    def reduce_sell_in(self):
        return None


class ImprovingProduct(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def change_with_time(self):
        if self.quality < MAX_QUALITY:
            self.quality = self.quality + 1
            if self.sell_in < 6:
                self.quality = self.quality + 1
            if self.sell_in < 11:
                self.quality = self.quality + 1

    def handle_expired(self):
        self.quality = MIN_QUALITY
