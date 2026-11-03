---
name: tabular-data-quality-review
description: Detectar errores de estructura, claves, tipos y consistencia en datos tabulares. En IAbot.io, asígnala a un empleado de análisis de datos y aporta los archivos tabulares, definición de columnas y reglas de calidad.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Datos, software y ordenador Linux
---

# Revisar calidad de CSV y hojas de datos

## Uso en IAbot.io

Asigna esta skill a **un empleado de análisis de datos** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta los archivos tabulares, definición de columnas y reglas de calidad.

**Ejemplo de encargo:** «Audita este CSV y entrega incidencias por fila y columna sin modificar el original.»

**Resultado a revisar:** Informe de calidad, registros problemáticos y propuesta de correcciones.

## Cuándo usarla y qué necesita

Detectar errores de estructura, claves, tipos y consistencia en datos tabulares

Trabaja con los archivos tabulares, definición de columnas y reglas de calidad. Usa el ordenador virtual autorizado y comprueba sus programas antes de ejecutar. Las consultas, instalaciones y accesos respetan el alcance concedido y conservan datos y configuraciones existentes.

## Procedimiento

1. Identifica codificación, separador, cabeceras, hoja y volumen antes de interpretar valores.
2. Contrasta tipos, claves, valores obligatorios y rangos con las reglas aportadas.
3. Separa ausencia de dato, cero y valor no válido; conserva números con identificadores o ceros iniciales.
4. Detecta duplicados y relaciones inconsistentes sin fusionar filas ambiguas.
5. Entrega resultados reproducibles y un fichero de correcciones propuestas con localizador de origen.

## Comprobación del resultado

- Los identificadores no se convierten accidentalmente en números.
- Las fechas ambiguas conservan formato y supuesto.
- El original permanece intacto y las incidencias son localizables.

## Entrega

Informe de calidad, registros problemáticos y propuesta de correcciones.

Conserva la identidad y revisión de las fuentes utilizadas. Señala los datos pendientes que afecten al resultado; no los sustituyas por valores inventados.

Usa [el registro de trabajo](assets/registro.csv) cuando no exista una plantilla del usuario; adapta sus filas sin perder las referencias.

## Referencias

- [Documentación del CLI de skills](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Documentación de OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/)
- [Manual de PostgreSQL, transacciones](https://www.postgresql.org/docs/current/sql-set-transaction.html)
