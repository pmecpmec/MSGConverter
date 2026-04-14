# Architectuuroverzicht – MSG-3 to Maximo Converter

Dit document beschrijft het architectuuroverzicht van het systeem volgens SDD sectie 3. Het sluit aan op het [SDD-TEMPLATE](SDD-TEMPLATE.md). Gedetailleerde dataflow en mapping staan in [MAPPING-FLOW-VISUAL.md](MAPPING-FLOW-VISUAL.md) en [MAXIMO-INTEGRATIE-UPDATE.md](MAXIMO-INTEGRATIE-UPDATE.md).

## 3.1 Technische eisen

**Performance.** Verwerking van een MSG-3 Excel-bestand moet binnen enkele seconden plaatsvinden. API-calls naar Maximo moeten met retry en timeouts robuust zijn; per record wordt een acceptabele responstijd nagestreefd (orde van honderden milliseconden).

**Betrouwbaarheid.** Geen automatische delete in Maximo. Foutafhandeling bij parsing, validatie en API: duidelijke foutmeldingen en logging. Bij API-fouten: retry-logic en graceful failure zodat geen onvolledige data wordt weggeschreven.

**Onderhoudbaarheid.** Modulaire opzet: parser, validator, mapping en Maximo-client zijn gescheiden. Business rules staan centraal in `business_rules.py` en worden in alle stappen toegepast. Code voldoet aan PEP 8; type hints en docstrings voor alle publieke functies.

**Beveiliging.** Credentials voor de Maximo API worden niet in code opgenomen; configuratie via omgevingsvariabelen of configbestand. Geen gevoelige data in logs.

**Compatibiliteit.** Ondersteuning voor het bestaande MSG-3 Excel-formaat en het herontworpen template. Python 3.11+; dependencies vastgelegd in requirements.txt.

## 3.2 Algemene architectuur

Het systeem is een pipeline: MSG-3 Excel wordt ingelezen, gevalideerd, optioneel vergeleken met een vorige versie, gemapped naar Maximo-objecten en naar de Maximo REST API gestuurd. De gebruiker bedient het systeem via een command-line interface (CLI).

**Hoofdstappen:**

1. **Parse.** Excel wordt ingelezen (excel_reader, msg3_parser). Output: gestructureerde data (Python-dict).
2. **Validate.** Structuur- en schemavalidatie (schema_validator, msg3_validator) en business rules (business_rules.py). Output: gevalideerde data plus eventuele waarschuwingen.
3. **Change detection (optioneel).** Vergelijking met een vorige versie (change_detector, diff_engine). Output: change report (toegevoegd, gewijzigd, verwijderd).
4. **Mapping.** MSG3MaximoMapper zet MSG-3 taken om naar Maximo-objecten. Volgorde is vast: eerst Commodities, dan Items, dan Item/Org, dan PM, dan JobPlan. Zie MAPPING-FLOW-VISUAL.md voor het volledige overzicht.
5. **Send to Maximo.** maximo_client en rest_client sturen de objecten via de Maximo REST API (create/read/update; geen delete).

**Componenten:**

- **parser:** excel_reader.py, msg3_parser.py – inlezen en structureren van MSG-3 Excel.
- **validator:** schema_validator.py, msg3_validator.py, business_rules.py – validatie van structuur en bedrijfsregels.
- **change_detection:** change_detector.py, diff_engine.py – diff tussen versies.
- **mapping:** item_mapper.py, pm_mapper.py, jobplan_mapper.py, msg3_maximo_mapper.py – transformatie naar Maximo Item, PM, JobPlan (en commodities, item_org).
- **maximo_connector:** rest_client.py, maximo_client.py – HTTP-calls naar de Maximo API.
- **main:** main.py – orkestratie en CLI-entrypoint.

Er is geen eigen database; alle status zit in de Excel-input en in Maximo. Configuratie (API-URL, credentials) is extern (config of omgeving).

## 3.3 Technologieën en frameworks

**Programmeertaal.** Python 3.11+.

**Excel en data.** openpyxl voor het lezen van MSG-3 Excel (.xlsx/.xlsm). pandas waar nuttig voor tabulaire verwerking. Geen aparte database; data stroomt als dict/objecten door de pipeline.

**Validatie.** pydantic voor datamodellen en type-validatie waar van toepassing. Business rules in eigen code (validator/business_rules.py).

**Maximo-integratie.** requests voor HTTP. REST API van IBM Maximo; authenticatie volgens Maximo-documentatie (bijv. Basic of token). Alleen create, read en update; geen delete.

**Testing.** pytest voor unit- en integratietests. Test coverage doel minimaal 80%.

**Overig.** CLI via argparse of vergelijkbaar (in main.py). Logging via de standaard logging-module. Type hints (typing) in de hele codebase.

**Referenties.** Zie maximo-specificaties.md voor Maximo-velden en -regels; business-rules.md voor de volledige set van 80 business rules.

Datum: februari 2026  
Auteur: Pedro Eduardo Cardoso  
Project: MSG-3 to Maximo Converter
