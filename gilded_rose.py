class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            item.age_item()
            item.reduce_quality_to_upper_limit()
            if item.is_expired():
                item.handle_expired_item()
        return items

