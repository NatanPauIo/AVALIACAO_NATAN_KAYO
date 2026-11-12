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


class Agenda():
    def __init__(self) -> None:
        self.limites_minutos = 240
        self.__atendimentos : list[Atendimento] = []


    def agendar(self, atendimento:Atendimento) -> None:
        if not isinstance(atendimento, Atendimento):
            raise TypeError("Atendimento informado é inválido")
        pass
        # pacientejaagendado se já tiver na lista
        # horarioindisponivel se nao couber no minutos


   
