# Contributing Guide
## MSG-3 → Maximo Integratie Project

---

## 🎯 Voor Pedro (Projecteigenaar)

Dit project is jouw Comakership project. Deze guide helpt je om:
- Gestructureerd te werken
- Code kwaliteit hoog te houden
- Documentatie bij te houden
- Assessment voor te bereiden

---

## 📋 Workflow

### 1. Nieuwe Feature Implementeren

```bash
# 1. Maak een feature branch (optioneel, kan ook direct op main)
git checkout -b feature/excel-parser

# 2. Implementeer de feature in kleine stappen
# - Schrijf eerst tests (TDD)
# - Implementeer functionaliteit
# - Documenteer in code (docstrings)

# 3. Run tests
pytest tests/unit/test_parser.py -v

# 4. Check code kwaliteit
black src/parser/  # Format code
flake8 src/parser/  # Lint code
mypy src/parser/   # Type checking

# 5. Update documentatie
# - Update relevante docs in /docs
# - Update README.md indien nodig

# 6. Commit met duidelijke message
git add .
git commit -m "feat(parser): Add Excel to JSON conversion"

# 7. Merge naar main
git checkout main
git merge feature/excel-parser
```

### 2. Bug Fixen

```bash
# 1. Schrijf test die bug reproduceert
# 2. Fix de bug
# 3. Verify dat test slaagt
# 4. Commit
git commit -m "fix(validator): Handle empty cells correctly"
```

### 3. Documentatie Updaten

```bash
# 1. Update relevante .md bestanden in /docs
# 2. Commit
git commit -m "docs(mapping): Add PM field mapping table"
```

---

## ✅ Code Kwaliteit Checklist

### Voor elke commit
- [ ] Code is geformatteerd met `black`
- [ ] Geen linter warnings (`flake8`)
- [ ] Type hints aanwezig (`mypy` clean)
- [ ] Tests geschreven en passing
- [ ] Docstrings compleet
- [ ] Geen hardcoded credentials
- [ ] Error handling aanwezig

### Voor elke module
- [ ] `__init__.py` met module docstring
- [ ] Alle functies hebben docstrings
- [ ] Unit tests met >80% coverage
- [ ] Type hints op alle functie signatures
- [ ] Logging statements op juiste niveau

### Voor elke feature
- [ ] Technisch ontwerp gedocumenteerd in `/docs/technisch-ontwerp/`
- [ ] Mapping gedocumenteerd in `/docs/mapping/` (indien relevant)
- [ ] Tests gedocumenteerd in `/docs/testcases/`
- [ ] README.md bijgewerkt

---

## 🧪 Testing

### Unit Tests Runnen

```bash
# Alle unit tests
pytest tests/unit/ -v

# Specifieke module
pytest tests/unit/test_parser.py -v

# Met coverage
pytest tests/unit/ --cov=src --cov-report=html

# Open coverage report
open htmlcov/index.html  # macOS
start htmlcov/index.html  # Windows
```

### Integration Tests Runnen

```bash
# Alle integration tests
pytest tests/integration/ -v -m integration

# Met Maximo connectie (vereist .env configuratie)
pytest tests/integration/ -v -m maximo
```

### Test Markers Gebruiken

```python
@pytest.mark.unit
def test_parser():
    pass

@pytest.mark.integration
def test_full_pipeline():
    pass

@pytest.mark.slow
@pytest.mark.maximo
def test_maximo_upload():
    pass
```

---

## 📝 Commit Message Conventies

Gebruik [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: Nieuwe feature
- `fix`: Bug fix
- `docs`: Documentatie wijziging
- `style`: Code formatting (geen functionaliteit wijziging)
- `refactor`: Code refactoring
- `test`: Tests toevoegen/wijzigen
- `chore`: Build, dependencies, tooling

### Voorbeelden

```bash
feat(parser): Add support for redesign Excel format

Implemented parsing logic for the new redesign format with
standardized headers and validation fields.

Closes #12

---

fix(validator): Handle None values in optional fields

Previously crashed when optional fields were None.
Now correctly skips validation for None values.

---

docs(mapping): Add complete PM field mapping table

Added comprehensive table showing all MSG-3 to Maximo PM
field mappings with transformation rules.

---

test(change-detection): Add tests for field-level changes

Added unit tests covering:
- Added tasks
- Deleted tasks  
- Modified fields
```

---

## 🏗️ Architectuur Principes

### SOLID Principes
- **S**ingle Responsibility: Elke class heeft één verantwoordelijkheid
- **O**pen/Closed: Open voor extensie, closed voor modificatie
- **L**iskov Substitution: Subclasses kunnen parent vervangen
- **I**nterface Segregation: Kleine, specifieke interfaces
- **D**ependency Inversion: Depend on abstractions, not concretions

### Code Organizatie
```
src/
├── parser/           # Excel → JSON conversie
│   ├── __init__.py
│   ├── msg3_parser.py      # High-level parser
│   └── excel_reader.py     # Low-level Excel utilities
│
├── validator/        # Data validatie
│   ├── __init__.py
│   ├── msg3_validator.py   # Main validator
│   ├── schema_validator.py # Schema checks
│   └── business_rules.py   # Business logic checks
│
└── ... (andere modules)
```

### Naming Conventions
- **Classes**: PascalCase (`MSG3Parser`, `PMMapper`)
- **Functions**: snake_case (`parse_excel`, `validate_data`)
- **Constants**: UPPER_SNAKE_CASE (`MAX_ROWS`, `DEFAULT_TIMEOUT`)
- **Private**: prefix met underscore (`_internal_method`)

---

## 📚 Documentatie Schrijven

### Docstring Format (Google Style)

```python
def map_task(self, msg3_task: Dict[str, Any]) -> Dict[str, Any]:
    """
    Map een MSG-3 taak naar een Maximo PM object.
    
    Deze functie converteert alle MSG-3 velden naar de corresponderende
    Maximo PM velden volgens de mapping specificatie in /docs/mapping/.
    
    Args:
        msg3_task: Dictionary met MSG-3 taak data. Moet minimaal
            de velden 'task_code' en 'description' bevatten.
            
    Returns:
        Dictionary met Maximo PM object. Bevat alle verplichte
        Maximo velden (PMNUM, DESCRIPTION, etc.)
        
    Raises:
        ValueError: Als verplichte velden ontbreken
        MappingError: Als mapping faalt
        
    Example:
        >>> mapper = PMMapper()
        >>> msg3_task = {"task_code": "32-11-01-001", "description": "Check"}
        >>> pm_record = mapper.map_task(msg3_task)
        >>> print(pm_record['PMNUM'])
        32-11-01-001
        
    Note:
        Interval units worden automatisch geconverteerd (FH → HOURS).
        Zie _map_interval_unit() voor details.
    """
    pass
```

### Markdown Documentatie

```markdown
# Titel (H1 - één per document)

Korte introductie wat dit document beschrijft.

## Sectie (H2)

Content met:
- Bullet lists voor opsommingen
- **Bold** voor belangrijke termen
- `code` voor code references
- [Links](url) voor referenties

### Subsectie (H3)

Code voorbeelden:

\`\`\`python
# Code met syntax highlighting
def example():
    return "Hello"
\`\`\`

Diagrammen:

\`\`\`mermaid
graph LR
    A --> B
\`\`\`

Tabellen:

| Kolom 1 | Kolom 2 |
|---------|---------|
| Data 1  | Data 2  |
```

---

## 🎓 Assessment Voorbereiding

### Competentie: Analyseren
**Wat laat je zien:**
- Requirements analyse in `/docs/projectdefinitie/`
- Onderzoek naar technologieën in `/docs/onderzoek/`
- Problem decomposition in architectuur

**Demo voorbeelden:**
- "Hier zie je mijn analyse van de MSG-3 structuur..."
- "Ik heb verschillende Excel parsing libraries onderzocht..."

### Competentie: Adviseren
**Wat laat je zien:**
- Technische keuzes in `/docs/onderzoek/`
- Alternatieven evaluatie met pros/cons
- Risico analyse in `/docs/plan-van-aanpak/`

**Demo voorbeelden:**
- "Ik heb gekozen voor openpyxl omdat..."
- "De alternatieve aanpak zou zijn... maar..."

### Competentie: Ontwerpen
**Wat laat je zien:**
- Architectuur diagrammen in `/docs/technisch-ontwerp/`
- Class diagrammen, sequence diagrammen
- Datamodellen en API specs

**Demo voorbeelden:**
- "Dit is mijn high-level architectuur..."
- "Hier zie je de class structuur met design patterns..."

### Competentie: Realiseren
**Wat laat je zien:**
- Werkende code in `/src`
- Test coverage >80%
- Clean code principes

**Demo voorbeelden:**
- "Laat ik de parser live demonstreren..."
- "Hier zie je de test coverage..."

### Competentie: Manage & Control
**Wat laat je zien:**
- Planning in `/docs/plan-van-aanpak/`
- Git commit history
- Test rapportage

**Demo voorbeelden:**
- "Hier is mijn planning met milestones..."
- "Deze commit messages laten mijn voortgang zien..."

---

## 🤝 Hulp Vragen

### Aan Cursor AI
Cursor is jouw technische assistent. Gebruik hem voor:
- Code generatie en refactoring
- Documentatie generatie
- Test schrijven
- Uitleg van complexe concepten

**Goede prompts:**
```
"Implementeer de Excel parsing logica in msg3_parser.py"
"Genereer unit tests voor de PMMapper class"
"Schrijf technisch ontwerp voor change detection in /docs"
"Leg uit hoe Maximo REST API authenticatie werkt"
```

### Aan Begeleiders
Voor strategische vragen en feedback:
- Architectuur beslissingen
- Project scope
- Assessment voorbereiding
- Stakeholder management

---

## 📦 Release Checklist

### Voor oplevering
- [ ] Alle modules geïmplementeerd
- [ ] Test coverage >80%
- [ ] Alle documentatie compleet
- [ ] Code review uitgevoerd
- [ ] Integration tests passing
- [ ] Gebruikershandleiding geschreven
- [ ] Installatie instructies getest
- [ ] Demo scenario's voorbereid
- [ ] Reflectie geschreven

---

**Succes met je Comakership, Pedro! 🚀**

*Voor vragen: gebruik Cursor AI of neem contact op met je begeleiders.*
