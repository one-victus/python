from collections import defaultdict
from .enums import SettingChipsType

class Player():
    def __init__(self, name: str, age: int, id: str, casino: object):
        self.name = name
        self.age = age
        self._id = id
        self.casino = casino
        self._chips = defaultdict(int)

        self._set_default_chips()

    def __str__(self) -> str:
        return f"Player: {self.name}, Age: {self.age}, ID: {self._id}, Chips: {self._chips}, Casino: {self.casino.name}, Casino ID: {self.casino.id}"
    
    def __repr__(self) -> str:
        return f"Player(name={self.name}, age={self.age}, id={self._id}, chips={self._chips}, casino={self.casino.name}, casino_id={self.casino.id})"
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def chips(self) -> dict[str, int]:
        return self._chips
    
    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @chips.setter
    def chips(self, values: dict[str, int]) -> None:
        self.set_chips(values)

    def set_chips(self, chips: dict[str, int] | int, set_type: SettingChipsType = SettingChipsType.SET) -> None:
        if set_type == SettingChipsType.SUM:
            ranges = sorted([chip[1] for chip in self.casino.default_chips], reverse=True)
            acc = 0
            
            if isinstance(chips, int):
                while acc < chips:
                    for range in ranges:
                        if acc + range <= chips:
                            acc += range
                            key = next(chip[0] for chip in self.casino.default_chips if chip[1] == range)
                            self._chips[key] += 1
                            break
        else:
            if set_type == SettingChipsType.SUB and not self._validate_chips_amount(chips):
                return

            for key, value in chips.items():
                if not self._validate_chips(key, value):
                    continue
                
                if set_type == SettingChipsType.SUB:
                    self._chips[key] -= value
                elif set_type == SettingChipsType.SET:
                    self._chips[key] = value

    def calculate_chips(self, chips: dict[str, int] | None = None) -> int:
        acc = 0

        if chips is None:
            chips = self._chips

        for key, value in chips.items():
            acc += value * next(chip[1] for chip in self.casino.default_chips if chip[0] == key)

        return acc
    
    def _validate_chips_amount(self, chips: dict[str, int] | int) -> bool:
        for key, value in chips.items():
            if self._validate_chips(key, value):
                if self._chips[key] - value < 0:
                    return False
        
        return True
    
    def _validate_chips(self, key: str, value: int) -> bool:
        if not isinstance(key, str) or not isinstance(value, int):
            raise ValueError("Las fichas deben ser un diccionario con string como keys y enteros como values")
        
        key = key.lower().strip()

        if len(key) == 0:
            raise ValueError("El nombre de la ficha no puede ser vacio")
        
        if value < 0:
            raise ValueError("El valor de la ficha no puede ser negativo")
        
        if key not in self._chips.keys():
            raise ValueError("La ficha no existe")
        
        return True

    def _set_default_chips(self) -> None:
        for chip in self.casino.default_chips:
            self._chips[chip[0]] = 0