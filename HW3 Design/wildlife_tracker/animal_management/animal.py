from typing import Any, Optional

from wildlife_tracker.animal_management.animal import Animal

class Animal:
    def __init__(self,
                age: Optional[int] = None,
                animal_id: int,
                health_status: Optional[str] = None,):

        self.age = age
        self.animal_id = animal_id
        self.health_status = health_status

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass

    def get_animal_details(self, animal_id) -> dict[str, Any]:
        pass
    
    
    
