# 🚀 Quick Start Guide
## MSG-3 → Maximo Integration Project

**Welkom Pedro! Dit document helpt je om snel te starten met je project.**

---

## ✅ Setup Checklist (Eerst dit doen!)

### 1. Development Environment Setup

```powershell
# Navigeer naar project directory
cd "C:\Users\pmec\.cursor\worktrees\MSGConverter\jjv"

# Controleer Python versie (moet 3.11+ zijn)
python --version

# Maak virtual environment
python -m venv venv

# Activeer virtual environment
.\venv\Scripts\activate  # Windows PowerShell

# Installeer dependencies
pip install -r requirements.txt

# Verify installatie
python -c "import openpyxl, pandas, pytest; print('✓ All dependencies installed!')"
```

### 2. Git Setup

```bash
# Initialiseer git (als nog niet gedaan)
git init

# Voeg remote repository toe (vervang URL)
git remote add origin https://github.com/your-username/msg3-maximo-integration.git

# Eerste commit
git add .
git commit -m "feat: Initial project setup with complete structure"

# Push naar remote (optioneel)
# git push -u origin main
```

### 3. Environment Variables

```powershell
# .env bestand is al aangemaakt, update de waarden:
# MAXIMO_BASE_URL, MAXIMO_USERNAME, MAXIMO_PASSWORD
notepad .env
```

---

## 🎯 Je Eerste Stappen

### Week 1: Oriëntatie & Documentatie

#### Dag 1-2: Project Setup ✅
- [x] Repository structuur klaar
- [ ] Development environment setup
- [ ] Kennismaking met Babcock team
- [ ] Toegang tot Maximo test environment regelen

#### Dag 3-4: Projectdefinitie
```bash
# Start met projectdefinitie documenten
cd docs/projectdefinitie
# Lees 00-START-HIER.md
# Schrijf documenten 01 t/m 05
```

**Focus:**
- Context analyse Babcock Schiphol
- Probleemstelling formuleren
- SMART doelen definiëren
- Scope bepalen
- Stakeholders identificeren

**Cursor AI hulp:**
```
"Schrijf een context analyse voor Babcock Schiphol als luchtvaart 
maintenance organisatie. Focus op MSG-3 en IBM Maximo gebruik."
```

#### Dag 5: Plan van Aanpak
```bash
cd docs/plan-van-aanpak
# Lees 00-START-HIER.md
# Maak planning met milestones
```

---

### Week 2: Technisch Onderzoek

#### Dag 1-2: MSG-3 Excel Analyse
```python
# Analyseer de huidige MSG-3 Excel structuur
# - Welke sheets zijn er?
# - Wat zijn de kolommen?
# - Wat zijn de datatypes?
# - Zijn er formules/validaties?

# Maak notities in:
# docs/onderzoek/05-msg3-analyse.md
```

#### Dag 3-4: Maximo API Onderzoek
```python
# Test Maximo API connectie
# Maak een simpel test script:

import requests

base_url = "https://maximo-test.babcock.local"
# Test authentication
# Test GET request naar /maximo/oslc/os/mxpm
# Documenteer API endpoints

# Documenteer in:
# docs/onderzoek/02-maximo-api.md
```

#### Dag 5: Proof of Concept
```python
# POC 1: Excel Parsing
# Doel: Lees een MSG-3 Excel en print de data

import openpyxl

wb = openpyxl.load_workbook("examples/msg3_example.xlsx")
sheet = wb.active

for row in sheet.iter_rows(values_only=True):
    print(row)

# POC 2: Maximo API Call
# Doel: Maak een test PM record in Maximo

# Sla POCs op in /examples/poc/
```

---

## 📚 Belangrijkste Bestanden om te Lezen

### Voor je Start
1. `README.md` - Project overzicht
2. `docs/readme-docs.md` - Documentatie structuur
3. `.cursor/project_instructions.md` - Cursor AI instructies
4. `CONTRIBUTING.md` - Workflow & best practices

### Tijdens Development
1. `src/main.py` - Main entry point (template aanwezig)
2. `src/parser/msg3_parser.py` - Parser voorbeeld
3. `tests/unit/test_parser.py` - Test voorbeeld
4. `requirements.txt` - Dependencies

---

## 🧪 Testing Workflow

### Run je Eerste Test

```bash
# Activeer venv (als nog niet gedaan)
.\venv\Scripts\activate

# Run alle unit tests
pytest tests/unit/ -v

# Run specifieke test
pytest tests/unit/test_parser.py -v

# Run met coverage
pytest tests/unit/ --cov=src --cov-report=html

# Open coverage report
start htmlcov\index.html  # Windows
```

---

## 💻 Development Workflow

### Feature Implementeren

```bash
# 1. Kies een feature (bijv. Excel Parser)

# 2. Schrijf eerst de test (TDD)
notepad tests/unit/test_parser.py

# 3. Run test (moet falen)
pytest tests/unit/test_parser.py -v

# 4. Implementeer feature
notepad src/parser/msg3_parser.py

# 5. Run test (moet slagen)
pytest tests/unit/test_parser.py -v

# 6. Documenteer
# - Docstrings in code
# - Technical doc in docs/technisch-ontwerp/
# - Update README.md

# 7. Code quality checks
black src/parser/  # Format
flake8 src/parser/ # Lint
mypy src/parser/   # Type check

# 8. Commit
git add .
git commit -m "feat(parser): Implement Excel parsing for MSG-3"

# 9. Repeat!
```

---

## 🤖 Cursor AI Effectief Gebruiken

### Goede Prompts voor Verschillende Taken

#### Code Generatie
```
"Implementeer de parse() method in src/parser/msg3_parser.py.
De method moet een Excel bestand inlezen met openpyxl,
de headers detecteren op rij 1, en elke rij converteren naar
een MSG3Task object. Return een dictionary met metadata en tasks."
```

#### Test Generatie
```
"Schrijf pytest unit tests voor de MSG3Parser class in 
tests/unit/test_parser.py. Test scenarios:
1. Succesvol parsen van geldig bestand
2. FileNotFoundError voor niet-bestaand bestand
3. ValueError voor corrupt bestand
4. Empty file handling"
```

#### Documentatie
```
"Genereer een technisch ontwerp document voor de Parser module
in docs/technisch-ontwerp/01-parser-design.md. Inclusief:
- Class diagram
- Sequence diagram voor parsing flow
- Error handling strategie
- Performance overwegingen"
```

#### Debugging
```
"Ik krijg deze error: [plak error]. Dit gebeurt in deze code: 
[plak code]. Wat is de oorzaak en hoe fix ik het?"
```

#### Refactoring
```
"Refactor deze functie om SOLID principes te volgen:
[plak code]"
```

---

## 📊 Progress Tracking

### Wekelijkse Review Vragen
- **Wat heb ik deze week bereikt?**
- **Welke problemen kwam ik tegen?**
- **Wat heb ik geleerd?**
- **Wat ga ik volgende week doen?**
- **Heb ik hulp nodig?**

### Documenteer in
```
docs/plan-van-aanpak/progress-log.md
```

---

## 🆘 Als je Vast Zit

### 1. Check de Documentatie
- Lees `docs/readme-docs.md` voor documentatie structuur
- Check `CONTRIBUTING.md` voor workflows
- Bekijk voorbeelden in `tests/` en `src/`

### 2. Gebruik Cursor AI
```
"Ik zit vast met [beschrijf probleem]. Ik heb geprobeerd [wat je probeerde].
Wat kan ik doen?"
```

### 3. Google & Documentation
- [Python openpyxl docs](https://openpyxl.readthedocs.io/)
- [Pandas docs](https://pandas.pydata.org/)
- [pytest docs](https://docs.pytest.org/)
- [IBM Maximo REST API docs](https://www.ibm.com/docs/en/mam)

### 4. Vraag Begeleiders
- Babcock team: Functionele vragen, requirements
- Windesheim begeleider: Procesmatige vragen, competenties

---

## 🎯 Sprint 1 Goals (Week 3-4)

**Doel:** Basis parser implementeren

### Must Have (Week 3-4)
- [ ] Excel bestand kan worden ingelezen
- [ ] Headers worden gedetecteerd
- [ ] Data wordt naar JSON geconverteerd
- [ ] Basis validatie (file exists, correct format)
- [ ] Unit tests geschreven
- [ ] Documentatie in `/docs/technisch-ontwerp/`

### Nice to Have
- [ ] Support voor meerdere Excel formaten
- [ ] Performance optimalisatie
- [ ] Uitgebreide error messages

### Demo
**Aan eind week 4:** Demo aan Babcock team:
- Toon Excel parsing
- Toon JSON output
- Toon error handling

---

## 📈 Success Metrics

### Code Quality
- ✅ Test coverage >80%
- ✅ Zero linter warnings
- ✅ Type hints everywhere
- ✅ All functions documented

### Documentation
- ✅ All deliverables complete
- ✅ README up to date
- ✅ Code comments clear

### Progress
- ✅ Weekly demos to stakeholders
- ✅ Regular commits (min. 3x/week)
- ✅ Milestones on track

---

## 🎓 Learning Resources

### Python
- [Real Python](https://realpython.com/)
- [Python official docs](https://docs.python.org/3/)

### Excel Parsing
- [openpyxl tutorial](https://openpyxl.readthedocs.io/en/stable/tutorial.html)
- [pandas Excel tutorial](https://pandas.pydata.org/docs/user_guide/io.html#excel-files)

### Testing
- [pytest tutorial](https://docs.pytest.org/en/stable/getting-started.html)
- [Test-Driven Development](https://www.obeythetestinggoat.com/)

### API Development
- [requests library](https://requests.readthedocs.io/)
- [REST API best practices](https://restfulapi.net/)

---

## ✨ Motivatie

**Je hebt dit! 💪**

Dit project is:
- ✅ **Haalbaar**: Gestructureerd opgezet, duidelijke stappen
- ✅ **Leerzaam**: Je leert Python, APIs, testing, documentatie
- ✅ **Relevant**: Echte business value voor Babcock
- ✅ **Portfolio**: Mooi project voor je CV

**Tips:**
- 🎯 Focus op één ding tegelijk
- 🧪 Test vroeg en vaak
- 📝 Documenteer terwijl je werkt (niet achteraf!)
- 🤝 Vraag hulp als je vast zit
- 🎉 Vier kleine successen

---

## 📞 Contact & Support

### Cursor AI
- Altijd beschikbaar
- Best voor: code, tests, documentatie, technical vragen

### Begeleiders
- Beschikbaar: volgens afspraak
- Best voor: strategie, proces, competenties

---

**Veel succes met je Comakership! 🚀**

**Next Steps:**
1. ✅ Setup development environment
2. 📝 Start met projectdefinitie (`docs/projectdefinitie/00-START-HIER.md`)
3. 🔬 Begin met technisch onderzoek (week 2)
4. 💻 Start coding (week 3)

*Happy coding!*
