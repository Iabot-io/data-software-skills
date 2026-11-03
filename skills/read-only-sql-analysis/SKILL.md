---
name: read-only-sql-analysis
description: Preparar y ejecutar consultas de lectura acotadas con resultados verificables. En IAbot.io, asígnala a un empleado de análisis con acceso a datos y aporta la pregunta, esquema disponible, conexión autorizada y límites de consulta.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Datos, software y ordenador Linux
---

# Análisis SQL de solo lectura

## Uso en IAbot.io

Asigna esta skill a **un empleado de análisis con acceso a datos** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta la pregunta, esquema disponible, conexión autorizada y límites de consulta.

**Ejemplo de encargo:** «Obtén el resumen de ventas solicitado con una consulta de lectura y explica filtros y limitaciones.»

**Resultado a revisar:** Consulta, resultado agregado y explicación reproducible de su alcance.

## Cuándo usarla y qué necesita

Preparar y ejecutar consultas de lectura acotadas con resultados verificables

Trabaja con la pregunta, esquema disponible, conexión autorizada y límites de consulta. Usa el ordenador virtual autorizado y comprueba sus programas antes de ejecutar. Las consultas, instalaciones y accesos respetan el alcance concedido y conservan datos y configuraciones existentes.

## Procedimiento

1. Confirma la conexión y permisos de lectura y consulta el esquema real antes de escribir SQL.
2. Define granularidad, filtros y uniones evitando duplicar registros por relaciones uno a muchos.
3. Usa transacción de solo lectura cuando el motor la soporte, límites y tiempos máximos adecuados.
4. Comprueba nulos, conteos y totales con consultas de control acotadas.
5. Entrega consulta y resultado minimizando datos personales, sin ejecutar escrituras ni cambios de esquema.

## Comprobación del resultado

- No se interpolan entradas no confiables como SQL ejecutable.
- Las uniones no multiplican indebidamente medidas.
- Se distinguen filas devueltas y población total si hay límite.

## Entrega

Consulta, resultado agregado y explicación reproducible de su alcance.

Conserva la identidad y revisión de las fuentes utilizadas. Señala los datos pendientes que afecten al resultado; no los sustituyas por valores inventados.

Usa [el registro de trabajo](assets/registro.csv) cuando no exista una plantilla del usuario; adapta sus filas sin perder las referencias.

## Referencias

- [Documentación del CLI de skills](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Documentación de OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/)
- [Manual de PostgreSQL, transacciones](https://www.postgresql.org/docs/current/sql-set-transaction.html)
