---
name: linux-software-setup
description: Preparar instalaciones Linux con fuentes verificadas, alcance acotado y comprobación funcional. En IAbot.io, asígnala a un empleado técnico autorizado y aporta herramienta necesaria, objetivo, entorno de destino y permisos de instalación.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Datos, software y ordenador Linux
---

# Preparar software en el ordenador virtual

## Uso en IAbot.io

Asigna esta skill a **un empleado técnico autorizado** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta herramienta necesaria, objetivo, entorno de destino y permisos de instalación.

**Ejemplo de encargo:** «Prepara la herramienta de OCR necesaria en este ordenador y verifica una muestra sin cambiar otros servicios.»

**Resultado a revisar:** Herramienta configurada o plan concreto, con versión, prueba y cambios registrados.

## Cuándo usarla y qué necesita

Preparar instalaciones Linux con fuentes verificadas, alcance acotado y comprobación funcional

Trabaja con herramienta necesaria, objetivo, entorno de destino y permisos de instalación. Usa el ordenador virtual autorizado y comprueba sus programas antes de ejecutar. Las consultas, instalaciones y accesos respetan el alcance concedido y conservan datos y configuraciones existentes.

## Procedimiento

1. Confirma distribución, arquitectura, permisos y espacio en el ordenador de destino.
2. Comprueba si la herramienta o una alternativa compatible ya existe y consulta instrucciones oficiales.
3. Elige el método más acotado compatible con el entorno, conservando paquetes y configuraciones ajenos.
4. Instala solo dentro del alcance autorizado; evita ejecutar scripts remotos sin inspección o eludir restricciones.
5. Prueba una entrada mínima representativa y registra versión, dependencias y forma de retirar el cambio.

## Comprobación del resultado

- No se instala en el servidor central por confundirlo con el ordenador del empleado.
- Se conservan los trabajos y entornos existentes.
- Instalar un paquete no se declara equivalente a una integración funcional completa.

## Entrega

Herramienta configurada o plan concreto, con versión, prueba y cambios registrados.

Conserva la identidad y revisión de las fuentes utilizadas. Señala los datos pendientes que afecten al resultado; no los sustituyas por valores inventados.

Usa [el registro de trabajo](assets/registro.csv) cuando no exista una plantilla del usuario; adapta sus filas sin perder las referencias.

## Referencias

- [Documentación del CLI de skills](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Documentación de OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/)
- [Manual de PostgreSQL, transacciones](https://www.postgresql.org/docs/current/sql-set-transaction.html)
