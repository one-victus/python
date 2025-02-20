class Casino():    
    def __init__(self, name: str, address: str, id: str, default_chips: tuple[str, int]):
        self.name = name
        self.address = address
        self._id = id
        self.default_chips = default_chips

    def __str__(self) -> str:
        return f"Casino: {self.name}, Address: {self.address}, ID: {self._id}"
    
    def __repr__(self) -> str:
        return f"Casino(name={self.name}, address={self.address}, id={self._id})"
    
    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, value: str) -> None:
        self._id = value