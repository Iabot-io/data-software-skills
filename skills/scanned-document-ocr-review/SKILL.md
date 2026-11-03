---
name: scanned-document-ocr-review
description: Preparar OCR y revisar texto reconocido conservando originales y localización por página. En IAbot.io, asígnala a un empleado de gestión documental y aporta el PDF o imágenes originales, idiomas y requisitos de conservación.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Datos, software y ordenador Linux
---

# OCR revisable de documentos escaneados

## Uso en IAbot.io

Asigna esta skill a **un empleado de gestión documental** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta el PDF o imágenes originales, idiomas y requisitos de conservación.

**Ejemplo de encargo:** «Genera una copia buscable de este escaneo y señala las páginas con reconocimiento dudoso.»

**Resultado a revisar:** Copia con OCR, texto extraído y registro de incidencias por página.

## Cuándo usarla y qué necesita

Preparar OCR y revisar texto reconocido conservando originales y localización por página

Trabaja con el PDF o imágenes originales, idiomas y requisitos de conservación. Usa el ordenador virtual autorizado y comprueba sus programas antes de ejecutar. Las consultas, instalaciones y accesos respetan el alcance concedido y conservan datos y configuraciones existentes.

## Procedimiento

1. Identifica páginas, orientación, resolución y capas de texto existentes sin alterar el original.
2. Comprueba las herramientas e idiomas de OCR disponibles y el efecto de firmas o restricciones del PDF.
3. Genera una copia con las opciones adecuadas, sin forzar OCR sobre texto válido innecesariamente.
4. Compara una muestra y todas las páginas problemáticas con su imagen, especialmente cifras, tablas y nombres.
5. Entrega texto y PDF identificados como derivados y conserva las incertidumbres de reconocimiento.

## Comprobación del resultado

- El número y orden de páginas se conservan.
- No se presenta texto OCR dudoso como transcripción fiel.
- Las firmas digitales o propiedades relevantes no se dan por preservadas sin verificar.

## Entrega

Copia con OCR, texto extraído y registro de incidencias por página.

Conserva la identidad y revisión de las fuentes utilizadas. Señala los datos pendientes que afecten al resultado; no los sustituyas por valores inventados.

Usa [el registro de trabajo](assets/registro.csv) cuando no exista una plantilla del usuario; adapta sus filas sin perder las referencias.

## Referencias

- [Documentación del CLI de skills](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Documentación de OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/)
- [Manual de PostgreSQL, transacciones](https://www.postgresql.org/docs/current/sql-set-transaction.html)
