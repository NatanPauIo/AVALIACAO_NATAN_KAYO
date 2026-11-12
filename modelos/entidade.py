from dataclasses import dataclass, field, FrozenInstanceError
from abc import ABC, abstractmethod
from excecoes.erros import *


@dataclass
class Paciente:
    nome: str
    cartao_sus: str

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Paciente):
            return NotImplemented
        
        return (self.nome == outro.nome
        and self.cartao_sus == outro.cartao_sus)


class Atendimento(ABC, Paciente):
    def __init__(self, nome: str, cartao_sus: str, tipo_atendimento: str) -> None:
        self._nome = nome
        self._cartao_sus = cartao_sus
        self._tipo_atendimento = tipo_atendimento

class Consulta(Atendimento):
    def __init__(self, especialidade: str, retorno: bool = False) -> None:
        super().__init__(nome="", cartao_sus="", tipo_atendimento="Consulta")
        self._especialidade = especialidade
        self._retorno = retorno

class Exame(Atendimento):
    def __init__(self, tipo: str, jejum: bool = False) -> None:
        super().__init__(nome="", cartao_sus="", tipo_atendimento="Exame")
        self._tipo = tipo
        self._jejum = jejum
        self._duracao_minutos = 20

class Vacinacao(Atendimento):
    def __init__(self, vacina: str, doses: int = 1) -> None:
        super().__init__(nome="", cartao_sus="", tipo_atendimento="Vacinação")
        self._vacina = vacina
        self._doses = doses
        self._duracao_minutos = 10
        

    @abstractmethod
    def duracao_minutos(self) -> int: ...

    def __str__(self) -> str:
        return f"Atendimento de {self._nome} com cartão SUS {self._cartao_sus} e tipo {self._tipo_atendimento}"
@abstractmethod
def duracao_minutos(self) -> int: ...


class Agenda():
    def __init__(self) -> None:
        self.limites_minutos = 240
        self.__atendimentos : list[Atendimento] = []


    def agendar(self, atendimento:Atendimento) -> None:
        if not isinstance(atendimento, Atendimento):
            raise TypeError("Atendimento informado é inválido")

        for i in self.__atendimentos:
            if i._cartao_sus == atendimento._cartao_sus:
                raise PacienteJaAgendadoError("o paciente já tematendimento na agenda")

        if (atendimento.)
            
        # pacientejaagendado se já tiver na lista
        # horarioindisponivel se nao couber no minutos


   
