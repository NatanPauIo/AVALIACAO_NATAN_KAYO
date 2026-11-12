class AgendaError(Exception):
    pass
class HorarioIndisponivelError(AgendaError):
    pass
class PacienteError(AgendaError):
    pass
class PacienteJaAgendadoError(PacienteError):
    pass