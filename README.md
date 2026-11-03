# Datos, software y ordenador Linux · Skills para empleados IA de IAbot.io

Calidad de datos, consultas de lectura, OCR y preparación de herramientas y skills en el ordenador virtual.

Procedimientos abiertos y concretos para agentes IA, con entradas, criterios de revisión y entregables. Publicados por [IAbot.io](https://iabot.io), plataforma de empleados IA con memoria, aplicaciones y ordenador virtual Linux.

## Habilidades y uso

| Skill | Empleado en IAbot.io | Entrega que revisar |
| --- | --- | --- |
| [Revisar calidad de CSV y hojas de datos](skills/tabular-data-quality-review/SKILL.md) | un empleado de análisis de datos | Informe de calidad, registros problemáticos y propuesta de correcciones. |
| [Análisis SQL de solo lectura](skills/read-only-sql-analysis/SKILL.md) | un empleado de análisis con acceso a datos | Consulta, resultado agregado y explicación reproducible de su alcance. |
| [OCR revisable de documentos escaneados](skills/scanned-document-ocr-review/SKILL.md) | un empleado de gestión documental | Copia con OCR, texto extraído y registro de incidencias por página. |
| [Inventario de herramientas Linux del empleado](skills/linux-tool-readiness/SKILL.md) | un empleado técnico del ordenador virtual | Inventario de ejecutables y versiones con capacidades pendientes de probar. |
| [Preparar software en el ordenador virtual](skills/linux-software-setup/SKILL.md) | un empleado técnico autorizado | Herramienta configurada o plan concreto, con versión, prueba y cambios registrados. |
| [Buscar y elegir skills para un empleado](skills/iabot-skill-discovery/SKILL.md) | un empleado organizador o técnico | Selección razonada con fuentes, versiones, requisitos y propuesta de incorporación. |

## Instalación y uso en IAbot.io

```sh
npx skills add Iabot-io/data-software-skills --list
npx skills add Iabot-io/data-software-skills
```

En la plataforma, abre **Skills**, revisa la habilidad e impórtala con el ámbito adecuado. Adjunta sus entradas y da el encargo al empleado. Consulta [la guía de uso en IAbot.io](USO-EN-IABOT.md) para el recorrido completo.

## Ejemplos

- **Revisar calidad de CSV y hojas de datos:** «Audita este CSV y entrega incidencias por fila y columna sin modificar el original.»
- **Análisis SQL de solo lectura:** «Obtén el resumen de ventas solicitado con una consulta de lectura y explica filtros y limitaciones.»
- **OCR revisable de documentos escaneados:** «Genera una copia buscable de este escaneo y señala las páginas con reconocimiento dudoso.»

## Herramientas y límites

Usa el ordenador virtual autorizado y comprueba sus programas antes de ejecutar. Las consultas, instalaciones y accesos respetan el alcance concedido y conservan datos y configuraciones existentes.

La colección no instala aplicaciones ni concede accesos. Las referencias se comprueban según la fecha, jurisdicción y alcance del encargo. Los resultados profesionales o administrativos conservan sus responsables y revisiones.

## Fuentes de referencia

- [Documentación del CLI de skills](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Documentación de OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/)
- [Manual de PostgreSQL, transacciones](https://www.postgresql.org/docs/current/sql-set-transaction.html)

Las fuentes orientan el método; su enlace no significa que una institución certifique o avale estas skills.

## Comprobación y licencia

```sh
python3 -m pip install -r scripts/requirements-validation.txt
python3 scripts/validate_skills.py
```

Se comprueban formato, recursos y referencias locales. Esa validación no acredita por sí sola un recorrido con un empleado real ni resultados en datos de producción. [Licencia MIT](LICENSE).

Agent Skills for AI employees and agents. Each skill includes an IAbot.io usage example and remains usable in compatible agents outside the platform.
