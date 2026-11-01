from dataclasses import dataclass
from typing import List

@dataclass
class Postulante:
    """Modelo de datos para un postulante."""
    nombre: str
    edad: int
    estado: str  # "Elegible" o "No elegible"

    def es_elegible(self) -> bool:
        """Retorna True si el postulante es elegible (edad entre 18 y 27)."""
        return 18 <= self.edad <= 27


PostulanteList = List[Postulante]