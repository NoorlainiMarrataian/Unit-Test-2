from use_cases.fruit_usecase import FruitUseCases
from infrastructure.in_memory_repo import InMemoryFruitRepository

repo = InMemoryFruitRepository()
usecase = FruitUseCases(repo)

usecase.add("Apple", 2.5)
usecase.add("Banana", 1.5)

print("All Fruits:", usecase.browse())
print("Get Fruit ID 1:", usecase.read(1))
usecase.edit(1, "Green Apple", 3.0)
print("Edited Fruit:", usecase.read(1))
usecase.delete(2)
print("All Fruits After Delete:", usecase.browse())
