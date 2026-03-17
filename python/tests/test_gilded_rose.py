import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # 🔴 Test 1: Conjured item degrades twice as fast
    def test_conjured_item_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(8, items[0].quality)  # should drop by 2

    # 🔴 Test 2: Conjured item degrades 4 after sell date
    def test_conjured_item_degrades_four_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(6, items[0].quality)  # should drop by 4

    # 🔴 Test 3: Conjured item quality never negative
    def test_conjured_item_quality_never_negative(self):
        items = [Item("Conjured Mana Cake", 5, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertGreaterEqual(items[0].quality, 0)

    # 🔴 Test 4: Conjured item sell_in decreases
    def test_conjured_item_sell_in_decreases(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(4, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()