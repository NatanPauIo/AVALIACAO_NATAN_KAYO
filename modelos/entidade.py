from dataclasses import dataclass, field, FrozenInstanceError
from abc import ABC, abstractmethod


@dataclass
class Paciente:
    nome: str
    cartao_sus: str


class Atendimento(ABC, Paciente):
    def __init__(self, nome: str, salario: float) -> None:
        self._nome = nome
        self._cartao_sus = salario

@abstractmethod
def duracao_minutos(self) -> int: ...
