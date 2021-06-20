from dataclasses import dataclass


@dataclass
class Product:
    id: int
    title: str
    description: str
    amount: int
    is_gift: bool
