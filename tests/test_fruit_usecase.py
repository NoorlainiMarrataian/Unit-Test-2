import unittest
from use_cases.fruit_usecase import FruitUseCases
from infrastructure.in_memory_repo import InMemoryFruitRepository

class TestFruitUseCase(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryFruitRepository()
        self.usecase = FruitUseCases(self.repo)

    # === TEST ADD ===
    def test_add_fruit(self):
        fruit = self.usecase.add("Apple", 2.5)
        self.assertEqual(fruit.name, "Apple")
        self.assertEqual(fruit.price, 2.5)

    def test_add_empty_name(self):
        fruit = self.usecase.add("", 3.0)
        self.assertEqual(fruit.name, "")

    def test_add_negative_price(self):
        fruit = self.usecase.add("Weird Fruit", -5.0)
        self.assertEqual(fruit.price, -5.0)

    # === TEST EDIT ===
    def test_edit_fruit(self):
        fruit = self.usecase.add("Apple", 2.5)
        self.usecase.edit(fruit.id, "Banana", 3.0)
        updated = self.usecase.read(fruit.id)
        self.assertEqual(updated.name, "Banana")

    def test_edit_non_existing(self):
        result = self.usecase.edit(999, "Durian", 5.0)
        self.assertFalse(result)

    def test_edit_price_only(self):
        fruit = self.usecase.add("Lemon", 0.5)
        self.usecase.edit(fruit.id, "Lemon", 1.0)
        self.assertEqual(self.usecase.read(fruit.id).price, 1.0)

    # === TEST DELETE ===
    def test_delete_fruit(self):
        fruit = self.usecase.add("Apple", 2.5)
        deleted = self.usecase.delete(fruit.id)
        self.assertTrue(deleted)

    def test_delete_invalid_id(self):
        result = self.usecase.delete(999)
        self.assertFalse(result)

    def test_delete_twice(self):
        fruit = self.usecase.add("Watermelon", 5.0)
        self.usecase.delete(fruit.id)
        result = self.usecase.delete(fruit.id)
        self.assertFalse(result)

    # === TEST READ ===
    def test_read_existing(self):
        fruit = self.usecase.add("Pear", 2.0)
        result = self.usecase.read(fruit.id)
        self.assertIsNotNone(result)

    def test_read_invalid_id(self):
        result = self.usecase.read(999)
        self.assertIsNone(result)

    # === TEST BROWSE ===
    def test_browse_multiple_fruits(self):
        self.usecase.add("Apple", 2.5)
        self.usecase.add("Banana", 1.0)
        self.usecase.add("Cherry", 3.0)
        fruits = self.usecase.browse()
        self.assertEqual(len(fruits), 3)

    def test_browse_after_delete(self):
        f1 = self.usecase.add("Fig", 1.2)
        f2 = self.usecase.add("Grape", 1.8)
        self.usecase.delete(f1.id)
        self.usecase.delete(f2.id)
        self.assertEqual(self.usecase.browse(), [])

    def test_browse_return_type(self):
        self.usecase.add("Golden Apple", 9.99)
        result = self.usecase.browse()
        self.assertIsInstance(result, list)
