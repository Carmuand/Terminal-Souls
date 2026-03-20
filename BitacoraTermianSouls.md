# 📓 Bitácora del Proyecto — Terminal Souls

> *Estudiante:* [Tu nombre aquí]
> *Curso / Materia:* [Nombre del curso]
> *Fecha de inicio:* [DD/MM/AAAA]
> *Lenguaje:* Python

-----

## 📌 Descripción del Proyecto

Terminal Souls es un simulador de combate por turnos que se ejecuta en la terminal. El jugador controla un Héroe que debe derrotar a un Enemigo eligiendo acciones cada turno: atacar, curar o usar una habilidad especial.

-----

## 🎯 Objetivos del Reto

- [ ] Implementar la función generar_daño(minimo, maximo)
- [ ] Implementar la función mostrar_estado(...)
- [ ] Implementar la función turno_jugador()
- [ ] Implementar la función turno_enemigo()
- [ ] Implementar la función verificar_ganador(hp_h, hp_e)
- [ ] Bucle principal con while
- [ ] Validación de pociones
- [ ] Mensajes de consola para cada acción

### Desafíos extra

- [ ] Sistema de críticos (10% de probabilidad, doble daño)
- [ ] IA básica del enemigo (se cura si HP < 20%)

-----

## 🗂️ Estructura del Archivo


terminal_souls.py
│
├── generar_daño()        → Genera daño aleatorio
├── mostrar_estado()      → Muestra HP de ambos personajes
├── turno_jugador()       → Maneja las acciones del jugador
├── turno_enemigo()       → Lógica automática del enemigo
├── verificar_ganador()   → Revisa si alguien llegó a 0 HP
└── Bucle principal       → Ciclo while que corre el juego


-----

## 📋 Atributos del Juego

|Personaje|HP Inicial|Especial              |
|---------|----------|----------------------|
|Héroe    |100       |3 pociones de curación|
|Enemigo  |120       |Ataca automáticamente |

### Acciones del jugador

|Acción            |Efecto                                        |
|------------------|----------------------------------------------|
|Atacar            |Daño aleatorio entre 10 y 25                  |
|Curar             |Recupera 20 HP (requiere poción)              |
|Habilidad Especial|Daño 30-50, pero 50% de probabilidad de fallar|

-----

## 📅 Registro de Avances

### Entrada 1 — [DD/MM/AAAA]

*¿Qué se hizo?*

> Describe qué parte del código trabajaste hoy. Ejemplo: “Creé la función generar_daño y la función mostrar_estado”.

*¿Cómo se hizo?*

> Explica brevemente cómo lo resolviste. Ejemplo: “Usé random.randint() para generar el número aleatorio dentro del rango.”

*¿Qué aprendiste?*

> Escribe algo nuevo que hayas entendido hoy.

-----

### Entrada 2 — [DD/MM/AAAA]

*¿Qué se hizo?*

*¿Cómo se hizo?*

*¿Qué aprendiste?*

-----

### Entrada 3 — [DD/MM/AAAA]

*¿Qué se hizo?*

*¿Cómo se hizo?*

*¿Qué aprendiste?*

-----

## 🐛 Registro de Errores

### Error 1

- *Fecha:* [DD/MM/AAAA]
- *Descripción:* ¿Qué error apareció? Copia el mensaje de error si puedes.
- *Causa:* ¿Por qué ocurrió?
- *Solución:* ¿Cómo lo corregiste?

-----

### Error 2

- *Fecha:* [DD/MM/AAAA]
- *Descripción:*
- *Causa:*
- *Solución:*

-----

### Error 3

- *Fecha:* [DD/MM/AAAA]
- *Descripción:*
- *Causa:*
- *Solución:*

-----

## ✏️ Registro de Modificaciones

### Modificación 1

- *Fecha:* [DD/MM/AAAA]
- *¿Qué se cambió?* Describe qué parte del código fue modificada.
- *¿Por qué se cambió?* ¿Era un error, una mejora o un requisito nuevo?
- *Antes:*

python
# Código original


- *Después:*

python
# Código modificado


-----

### Modificación 2

- *Fecha:* [DD/MM/AAAA]
- *¿Qué se cambió?*
- *¿Por qué se cambió?*
- *Antes:*

python



- *Después:*

python



-----

## 💡 Conceptos Aprendidos

|Concepto          |¿Para qué sirve?                                |
|------------------|------------------------------------------------|
|def             |Definir una función                             |
|random.randint()|Generar número aleatorio                        |
|while           |Repetir código mientras se cumpla una condición |
|global          |Usar una variable de fuera dentro de una función|
|input()         |Pedir datos al usuario                          |
|[Agrega más aquí] |                                                |

-----

## 🔍 Preguntas y Dudas

> Anota aquí las preguntas que te surgieron durante el desarrollo, aunque ya las hayas resuelto.

1. [Pregunta 1]
1. [Pregunta 2]
1. [Pregunta 3]

-----

## ✅ Estado Final del Proyecto

- *Fecha de entrega:* [DD/MM/AAAA]
- *¿Funciona correctamente?* Sí / No / Parcialmente
- *Observaciones finales:*

> Escribe una reflexión corta sobre el proceso: qué fue lo más difícil, qué aprendiste, qué harías diferente.

-----

Bitácora generada para el proyecto Terminal Souls — Reto de Programación