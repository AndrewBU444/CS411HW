from typing import Any, Optional, List
from wildlife_tracker.animal_management.animal import Animal
from wildlife_tracker.habitat_management.habitat import Habitat
#any

class HabitatManager:
    def __init__(self) -> None:
        animals: List[int] = {}

    def create_habitat(self, habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass

    def get_animals_in_habitat(self, habitat_id: int) -> List[Animal]:
        pass

    def get_habitat_by_id(self, habitat_id: int) -> Habitat:
        pass

    def get_habitat_details(self, habitat_id: int) -> dict:
        pass

    def get_habitats_by_size(self, size: int) -> List[Habitat]:
        pass

    def get_habitats_by_type(self, environment_type: str) -> List[Habitat]:
        pass

    def update_habitat_details(self, habitat_id: int, **kwargs: dict[str, Any]) -> None:
        pass

    def remove_habitat(self, habitat_id: int) -> None:
        pass

    pass
