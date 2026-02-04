# MSG-3 → IBM Maximo Integratie

Dit project is ontwikkeld tijdens het Comakership ADSD voor Babcock Schiphol.  
Het doel is een automatische koppeling bouwen tussen een MSG-3 Excel-document en IBM Maximo.

## 🎯 Doelen
1. MSG-3 Excel automatisch inlezen, valideren en structureren.
2. Wijzigingen detecteren (change detection).
3. Mapping uitvoeren naar Maximo PM/JobPlan objecten.
4. Data automatisch naar Maximo sturen via REST API of MIF.
5. MSG-3 Excel herontwerpen zodat het geschikt is voor automatische verwerking.

## 📁 Projectstructuur

```
msg3-maximo-integration/
├── docs/
│   ├── projectdefinitie/      # Projectdefinitie volgens Windesheim format
│   ├── plan-van-aanpak/        # PvA met planning en scope
│   ├── onderzoek/              # Onderzoeksdocumenten (technisch & functioneel)
│   ├── technisch-ontwerp/      # Architectuur, class diagrammen, API specs
│   ├── mapping/                # MSG-3 → Maximo field mappings
│   ├── testcases/              # Testplannen en testresultaten
│   ├── overdracht/             # Overdracht documentatie
│   └── readme-docs.md          # Overzicht documentatie
│
├── src/
│   ├── parser/                 # Excel → JSON conversie
│   ├── validator/              # Structuur + datatypes validatie
│   ├── change_detection/       # Wijzigingsdetectie logica
│   ├── mapping/                # MSG-3 → Maximo objecten mapping
│   ├── maximo_connector/       # Maximo REST API / MIF interface
│   └── main.py                 # Hoofdapplicatie entry point
│
├── examples/
│   ├── msg3_original.xlsx      # Huidige MSG-3 formaat
│   └── msg3_redesign.xlsx      # Herontworpen MSG-3 formaat
│
├── tests/
│   ├── unit/                   # Unit tests per module
│   └── integration/            # End-to-end integratietests
│
├── .cursor/                    # Cursor AI project configuratie
├── .gitignore
└── README.md
```

## 🚀 Technologie Stack

### Taal & Framework
- **Python 3.11+** (primaire keuze voor Excel parsing en data processing)
- Alternatief: Node.js / C# (afhankelijk van Maximo omgeving)

### Libraries
- **openpyxl** / **pandas**: Excel parsing
- **pydantic**: Data validatie en schema's
- **requests**: Maximo REST API communicatie
- **pytest**: Testing framework
- **python-dotenv**: Environment configuratie

### Maximo Integratie
- Maximo REST API (Object Structure)
- Alternatief: MIF (Maximo Integration Framework) XML

## 🏗️ Architectuur

### Verwerkingspipeline
```
MSG-3 Excel
    ↓
[Parser] → Gestructureerde JSON
    ↓
[Validator] → Validatie + Error Reporting
    ↓
[Change Detection] → Delta's identificeren
    ↓
[Mapping Engine] → Maximo objecten
    ↓
[Maximo Connector] → API Calls → IBM Maximo
```

### Kerncomponenten
1. **Parser**: Leest MSG-3 Excel en converteert naar gestandaardiseerd JSON formaat
2. **Validator**: Controleert data integriteit, verplichte velden, datatypes
3. **Change Detection**: Vergelijkt met vorige versie, genereert changelog
4. **Mapping Engine**: Vertaalt MSG-3 structuur naar Maximo PM/JobPlan objecten
5. **Maximo Connector**: Communiceert met Maximo API, error handling, retry logica

## 📚 Documentatie

Alle projectdocumenten staan in `/docs` en zijn georganiseerd per Windesheim deliverable:

- **Projectdefinitie**: Context, probleemstelling, doelstellingen
- **Plan van Aanpak**: Planning, risicoanalyse, scope
- **Onderzoek**: Technisch onderzoek naar Excel parsing, Maximo API, change detection
- **Technisch Ontwerp**: Architectuur, datamodellen, API specificaties
- **Mapping**: Veldmapping MSG-3 ↔ Maximo
- **Testcases**: Testplannen, testscripts, resultaten
- **Overdracht**: Gebruikershandleiding, installatie instructies

Zie `/docs/readme-docs.md` voor een volledig overzicht.

## 🧪 Testen

### Unit Tests
```bash
pytest tests/unit/ -v
```

### Integratietests
```bash
pytest tests/integration/ -v
```

### Coverage
```bash
pytest --cov=src tests/
```

## 🔧 Installatie & Setup

```bash
# Clone repository
git clone <repository-url>
cd msg3-maximo-integration

# Virtuele omgeving aanmaken
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Dependencies installeren
pip install -r requirements.txt

# Environment variabelen configureren
cp .env.example .env
# Bewerk .env met Maximo credentials

# Applicatie draaien
python src/main.py
```

## 🎓 Comakership Context

### Organisatie
**Babcock Schiphol** - Maintenance Excellence voor luchtvaarttechniek

### Opleiding
**Windesheim** - Associate Degree Software Development (ADSD)

### Competenties
- ✅ **Analyseren**: Requirements analyse MSG-3 en Maximo
- ✅ **Adviseren**: Technische keuzes en architectuur beslissingen
- ✅ **Ontwerpen**: Systeem architectuur en datamodellen
- ✅ **Realiseren**: Implementatie van de integratie
- ✅ **Manage & Control**: Projectmanagement en kwaliteitsborging

### Student
**Pedro** - ADSD Student

### Periode
Februari - Juni 2026

## 📋 Status & Roadmap

### Phase 1: Analyse & Ontwerp ✅
- [x] Projectdefinitie
- [x] Plan van Aanpak
- [x] Repository structuur
- [ ] Technisch onderzoek
- [ ] Architectuur ontwerp

### Phase 2: MSG-3 Parser (Week 1-2)
- [ ] Excel parsing implementeren
- [ ] JSON schema definitie
- [ ] Validator bouwen
- [ ] Unit tests

### Phase 3: Change Detection (Week 3)
- [ ] Versie vergelijking logica
- [ ] Changelog generatie
- [ ] Delta rapportage

### Phase 4: Maximo Mapping (Week 4-5)
- [ ] Field mapping configuratie
- [ ] PM object generatie
- [ ] JobPlan object generatie
- [ ] Validatie regels

### Phase 5: Maximo Connector (Week 6-7)
- [ ] REST API client
- [ ] Authentication & authorization
- [ ] CRUD operaties
- [ ] Error handling & retry logica

### Phase 6: Testing & Documentatie (Week 8-9)
- [ ] Integratietests
- [ ] Gebruikershandleiding
- [ ] Overdracht documentatie

### Phase 7: MSG-3 Redesign (Week 10-11)
- [ ] Analyse huidige structuur
- [ ] Ontwerp nieuwe template
- [ ] Implementatie nieuwe parser
- [ ] Migratie strategie

### Phase 8: Afronding (Week 12)
- [ ] Code review
- [ ] Documentatie finalisatie
- [ ] Oplevering & presentatie
- [ ] Reflectie

## 🤝 Contributing

Dit is een Comakership project. Voor vragen of suggesties, neem contact op met Pedro.

## 📄 License

Dit project is ontwikkeld in opdracht van Babcock Schiphol voor educatieve doeleinden.

## 🔗 Links

- [Maximo REST API Documentation](https://www.ibm.com/docs/en/mam/7.6.1?topic=api-maximo-rest)
- [MSG-3 Specification (ATA)](https://www.ata.org/)
- [Windesheim ADSD](https://www.windesheim.nl/)

---

*Laatste update: 4 februari 2026*
