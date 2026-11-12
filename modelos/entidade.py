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


class Atendimento(ABC,):
    def __init__(self, nome: str, cartao_sus: str, tipo_atendimento: str,paciente:Paciente) -> None:
        self._nome = nome
        self._cartao_sus = cartao_sus
        self._tipo_atendimento = tipo_atendimento
        self.paciente = paciente
   
    @abstractmethod
    def duracao_minutos(self) -> int: 
        pass

    def __str__(self) -> str:
        return f"Tipo do atendimento: {self._tipo_atendimento}, Nome do paciente: {self._nome}, Duração: {self.duracao_minutos()} minutos"


class Consulta(Atendimento):
    def __init__(self, especialidade: str, retorno: bool = False) -> None:
        super().__init__(nome="", cartao_sus="", tipo_atendimento="Consulta")
        self._especialidade = especialidade
        self._retorno = retorno
    
    def duracao_minutos(self) -> int: 
        if self._retorno:
            return 15
        return 30

class Exame(Atendimento):
    def __init__(self, tipo: str, jejum: bool = False) -> None:
        super().__init__(nome="", cartao_sus="", tipo_atendimento="Exame")
        self._tipo = tipo
        self._jejum = jejum
        self._duracao_minutos = 20

    def duracao_minutos(self) -> int: 
        if self._jejum:
            return 30
        return 20

class Vacinacao(Atendimento):
    def __init__(self, vacina: str, doses: int = 1) -> None:
        super().__init__(nome="", cartao_sus="", tipo_atendimento="Vacinação")
        self._vacina = vacina
        self._doses = doses
        self._duracao_minutos = 10

    def duracao_minutos(self) -> int: 
        return 10 * self._doses


class Agenda():
    def __init__(self) -> None:
        self.limites_minutos = 240
        self.__atendimentos : list[Atendimento] = []


    def agendar(self, atendimento:Atendimento) -> None:
        if not isinstance(atendimento, Atendimento):
            raise TypeError("Atendimento informado é inválido")

        for i in self.__atendimentos:
            if i.paciente == atendimento.paciente:
                raise PacienteJaAgendadoError("o paciente já tem atendimento na agenda")

        if (atendimento.duracao_minutos > self.limites_minutos):
            raise HorarioIndisponivelError("O tempo de atendimento ultrapassa o tempo disponivel.")

        self.__atendimentos.append(atendimento)
        print("Atendimento adicionado com sucesso")
            
        # pacientejaagendado se já tiver na lista
        # horarioindisponivel se nao couber no minutos


   
