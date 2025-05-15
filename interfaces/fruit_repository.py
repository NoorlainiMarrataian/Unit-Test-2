from typing import List, Optional
from entities.fruit import Fruit

class FruitRepositoryInterface:
    def list_all(self) -> List[Fruit]: pass
    def get_by_id(self, fruit_id: int) -> Optional[Fruit]: pass
    def add(self, fruit: Fruit) -> None: pass
    def update(self, fruit: Fruit) -> bool: pass
    def delete(self, fruit_id: int) -> bool: pass
