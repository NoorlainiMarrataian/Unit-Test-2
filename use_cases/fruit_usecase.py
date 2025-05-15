from interfaces.fruit_repository import FruitRepositoryInterface
from entities.fruit import Fruit

class FruitUseCases:
    def __init__(self, repo: FruitRepositoryInterface):
        self.repo = repo

    def browse(self):
        return self.repo.list_all()

    def read(self, fruit_id):
        return self.repo.get_by_id(fruit_id)

    def add(self, name, price):
        new_fruit = Fruit(id=0, name=name, price=price)
        self.repo.add(new_fruit)
        return new_fruit

    def edit(self, fruit_id, name, price):
        fruit = Fruit(id=fruit_id, name=name, price=price)
        return self.repo.update(fruit)

    def delete(self, fruit_id):
        return self.repo.delete(fruit_id)
