# Ejercicio 1
class Evento:
    def __init__(self, codigo_evento: str, 
                nombre: str,
                fecha: str,         #formato YYYY-MM-DD
                hora: str,          #formato HH:MM
                capacidad: int) -> None:
        self.codigo_evento = codigo_evento
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.capacidad = capacidad

    def __str__(self) -> str:
        return 'Codigo del evento: ' + self.codigo_evento + ' \n Nombre: ' + self.nombre + '\n Fecha: ' + self.fecha + '\n Hora: ' + self.hora + '\n Capacidad del evento: ' + str(self.capacidad)

evento1 = Evento(
    "E001",
    "Concierto de Rock",
    "2026-10-20",
    "19:00",
    100)

# print(evento1)

# Ejercicio 2

class ReservaEvento:
    def __init__(self, dni_cliente: str,
                nombre_cliente: str,
                evento: Evento,
                numero_asistentes: int) -> None:
        self.dni_cliente = dni_cliente
        self.nombre_cliente = nombre_cliente
        self.evento = evento
        self.numero_asistentes = numero_asistentes

    def __str__(self) -> str:
        return "  DNI: " + self.dni_cliente + "\n Nombre: " + self.nombre_cliente + "\n Evento:" + str(self.evento) + '\n Numero de asistentes: ' + str(self.numero_asistentes)


reserva1 = ReservaEvento(
    "12345678",
    "Juan Perez",
    evento1,
    4
)

# print(reserva1)

# Ejercicio 3

class SistemaEventos:
    def __init__(self) -> None:
        self.eventos = {}
        self.reservas = {}      # Ejercicio 5
        
    def agregarEvento(self, ev: Evento) -> None:
        if ev.codigo_evento in self.eventos:
            print("Ya existe un evento con este codigo")
        else:
            self.eventos[ev.codigo_evento] = ev
            print("Evento agregado correctamente")

    def mostrarEventos(self) -> None:
        for ev in self.eventos:
            print(ev)
#ejercicio 4
    def eliminarEvento(self, cod: str) -> None:
        if cod in self.eventos:
            self.eventos.pop(cod)
        else:
            print("No existe el evento con ese codigo", cod)
#ejercicio 6
    def devolver_capacidad_restante(self, cod: str) -> int:
        if cod in self.eventos:
            capacidad_total = self.eventos[cod].capacidad
            asistentes = 0
            if cod in self.reservas:
                for reserva in self.reservas[cod]:
                    asistentes = reserva.numero_asistentes
            return capacidad_total - asistentes
#ejercicio 7
    def crear_reserva(self, dni: str, nombre: str, cod: str, cant: int) -> None:
        if cod in self.eventos:
            if cant <= self.devolver_capacidad_restante(cod):
                r = ReservaEvento(dni, nombre, self.eventos[cod], cant)
                if cod in self.reservas:
                    self.reservas[cod].append(r)
                else:
                    self.reservas[cod] = [r]