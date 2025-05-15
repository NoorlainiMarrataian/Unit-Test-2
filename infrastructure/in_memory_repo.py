from interfaces.fruit_repository import FruitRepositoryInterface
from entities.fruit import Fruit

class InMemoryFruitRepository(FruitRepositoryInterface):
    def __init__(self):
        self.fruits = {}
        self.counter = 1

    def list_all(self):
        return list(self.fruits.values())

    def get_by_id(self, fruit_id):
        return self.fruits.get(fruit_id)

    def add(self, fruit):
        fruit.id = self.counter
        self.fruits[self.counter] = fruit
        self.counter += 1

    def update(self, fruit):
        if fruit.id in self.fruits:
            self.fruits[fruit.id] = fruit
            return True
        return False

    def delete(self, fruit_id):
        if fruit_id in self.fruits:
            del self.fruits[fruit_id]
            return True
        return False
