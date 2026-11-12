from dataclasses import dataclass
from abc import ABC, abstractmethod
from excecoes.erros import HorarioIndisponivelError, PacienteJaAgendadoError


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
        if self.retorno:
            return 15  
        return 30


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
    def __init__(self, limite_minutos: int = 240) -> None:
        self._limite_minutos = limite_minutos
        self._atendimentos: list[Atendimento] = []
        self._minutos_ocupados = 0

    @property
    def atendimentos(self) -> tuple[Atendimento, ...]:
        return tuple(self._atendimentos)

    @property
    def minutos_ocupados(self) -> int:
        return self._minutos_ocupados

    def agendar(self, atendimento: Atendimento) -> None:
        for item in self._atendimentos:
            if item.paciente == atendimento.paciente:
                raise PacienteJaAgendadoError(
                    f"O paciente {atendimento.paciente.nome} já tem atendimento na agenda."
                )

        minutos_restantes = self._limite_minutos - self._minutos_ocupados
        if atendimento.duracao_minutos() > minutos_restantes:
            raise HorarioIndisponivelError(
                f"O tempo de atendimento ({atendimento.duracao_minutos()} min) "
                f"ultrapassa o tempo disponível ({minutos_restantes} min)."
            )

        self._atendimentos.append(atendimento)
        self._minutos_ocupados += atendimento.duracao_minutos()