from typing import Any, Optional

from wildlife_tracker.animal_management.animal import Animal
class AnimalManager:

    def __init__(self) -> None:
        animals: dict[int, Animal] = {}


    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass

    def remove_animal(self, animal_id: int) -> None:
        pass

    def get_animal_details(self, animal_id) -> dict[str, Any]:
        pass
    
    def register_animal(self, Animal) -> None:
        pass

    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        pass

    def remove_animal(self, animal_id: int) -> None:
        pass

    

        

    
