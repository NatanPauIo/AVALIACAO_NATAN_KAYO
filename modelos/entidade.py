from dataclasses import dataclass
from abc import ABC, abstractmethod
from excecoes.erros import *


@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str


class Atendimento(ABC):
    def __init__(self, paciente: Paciente) -> None:
       
        self._paciente = paciente

    @property
    def paciente(self) -> Paciente:
        return self._paciente
   
    @abstractmethod
    def duracao_minutos(self) -> int: 
        pass

    def __str__(self) -> str:
        
        return f"{type(self).__name__} - Paciente: {self._paciente.nome} ({self.duracao_minutos()} min)"


class Consulta(Atendimento):
    def __init__(self, paciente: Paciente, especialidade: str, retorno: bool = False) -> None:
        super().__init__(paciente=paciente)
        self.especialidade = especialidade
        self.retorno = retorno
    
    def duracao_minutos(self) -> int: 
        return 15 if self.retorno else 30


class Exame(Atendimento):
    def __init__(self, paciente: Paciente, tipo: str, jejum: bool = False) -> None:
        super().__init__(paciente=paciente)
        self.tipo = tipo
        self.jejum = jejum

    def duracao_minutos(self) -> int: 
        return 30 if self.jejum else 20


class Vacinacao(Atendimento):
    def __init__(self, paciente: Paciente, vacina: str, doses: int = 1) -> None:
        super().__init__(paciente=paciente)
        self.vacina = vacina
        self.doses = doses

    def duracao_minutos(self) -> int: 
        return 10 * self.doses


class Agenda:
    def __init__(self) -> None:
        self.minutos_ocupados = 240
        self._atendimentos: list[Atendimento] = []
        self.minutos_ocupados = 0

    @property
    def atendimentos(self) -> list[Atendimento]:
        return self._atendimentos

    def agendar(self, atendimento: Atendimento) -> None:
        if not isinstance(atendimento, Atendimento):
            raise TypeError("Atendimento informado é inválido")

        for item in self._atendimentos:
            if item.paciente == atendimento.paciente:
                raise PacienteJaAgendadoError("O paciente já tem atendimento na agenda")

        tempo_ocupado = sum(item.duracao_minutos() for item in self._atendimentos)
        if tempo_ocupado + atendimento.duracao_minutos() > self.minutos_ocupados:
            raise HorarioIndisponivelError("O tempo de atendimento ultrapassa o tempo disponível.")

        
        self.__atendimentos.append(atendimento)
        self.minutos_ocupados += atendimento.duracao_minutos()
