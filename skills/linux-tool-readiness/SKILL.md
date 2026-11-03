---
name: linux-tool-readiness
description: Comprobar qué herramientas están disponibles antes de prometer un flujo de trabajo. En IAbot.io, asígnala a un empleado técnico del ordenador virtual y aporta el encargo, formatos requeridos y acceso autorizado al ordenador Linux.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Datos, software y ordenador Linux
---

# Inventario de herramientas Linux del empleado

## Uso en IAbot.io

Asigna esta skill a **un empleado técnico del ordenador virtual** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta el encargo, formatos requeridos y acceso autorizado al ordenador Linux.

**Ejemplo de encargo:** «Comprueba si este ordenador dispone de las herramientas para documentos, CAD y vídeo sin instalar nada.»

**Resultado a revisar:** Inventario de ejecutables y versiones con capacidades pendientes de probar.

## Cuándo usarla y qué necesita

Comprobar qué herramientas están disponibles antes de prometer un flujo de trabajo

Trabaja con el encargo, formatos requeridos y acceso autorizado al ordenador Linux. Usa el ordenador virtual autorizado y comprueba sus programas antes de ejecutar. Las consultas, instalaciones y accesos respetan el alcance concedido y conservan datos y configuraciones existentes.

## Procedimiento

1. Identifica el ordenador y su alcance autorizado; no confundas el servidor de la plataforma con el ordenador de la organización.
2. Localiza ejecutables necesarios y consulta versiones con comandos de lectura. Si falta el archivo local, abre [el ayudante](scripts/inventory_tools.py) de la revisión elegida, inspecciónalo y guárdalo en scripts/inventory_tools.py dentro del ordenador autorizado. Ejecuta python3 scripts/inventory_tools.py --out inventario.json desde su carpeta superior; el informe solo describe el entorno en que se ejecuta.
3. Relaciona cada herramienta con el formato o etapa que debe resolver, distinguiendo presencia de funcionamiento verificado.
4. Comprueba espacio y requisitos del encargo sin leer secretos ni datos ajenos.
5. Entrega carencias y siguiente comprobación concreta antes de proponer instalaciones.

## Comprobación del resultado

- Un ejecutable presente no se da por probado con un documento real.
- No se imprimen variables ni archivos de credenciales.
- El informe identifica el entorno comprobado.

## Entrega

Inventario de ejecutables y versiones con capacidades pendientes de probar.

Conserva la identidad y revisión de las fuentes utilizadas. Señala los datos pendientes que afecten al resultado; no los sustituyas por valores inventados.

Usa [el registro de trabajo](assets/registro.csv) cuando no exista una plantilla del usuario; adapta sus filas sin perder las referencias.

## Referencias

- [Documentación del CLI de skills](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Documentación de OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/)
- [Manual de PostgreSQL, transacciones](https://www.postgresql.org/docs/current/sql-set-transaction.html)
