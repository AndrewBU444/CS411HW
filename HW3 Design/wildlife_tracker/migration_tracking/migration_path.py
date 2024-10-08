from typing import Any, Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:

    def __init__ (self, 
                  path_id: int,
                  size: int, 
                  species: str,
                  start_dates: str
                  start_location: Habitat) -> None:
        self.path_id = path_id
        self.size = size
        self.species = species
        self.start_dates = start_dates
        self.start_location = start_location

        def update_migration_path_details(path_id: int, **kwargs) -> None:
            pass    

        def get_migration_path_details(path_id) -> dict:
            pass