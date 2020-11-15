# Workshop 1

*Einführung in Python: Sprachelemente*

- Python Entwicklungs- und Laufzeitumgebung   
- Sprachelemente: Typen (z.B. Listen, Dicts), Bedingungen, Schlaufen etc.   
- Python-Module

***

## Was ist *Python*?

*Python* ist eine Skriptsprache. Der Quellcode (File mit Endung *.py*) wird zur Laufzeit vom Python-Interpreter übersetzt (Endung *.pyc*) und ausgeführt.

***

## Python installieren

Überprüfen, ob Python (in welcher Version) installiert ist:

`python -V`

Wir wollen mit Python 3 arbeiten. Andererseits wollen wir eine installierte Python-Version nicht überschreiben. Mit *pyenv* können wir neue Python-Versionen installieren und für jeden Verzeichnisbaum wählen, welche Python-Version gelten soll.

***

### Installation von *pyenv*

#### **Linux**

```
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"
```
Nun kann Python installiert werden:
```
pyenv install --list
pyenv install miniconda3-latest
```
**Bem:** *miniconda3* ist eine leichtgewichtige Installation einer Python-3-Version.

Python 3 für einen Verzeichnisbaum aktivieren:
```
cd path/to/dir
pyenv local miniconda3-latest
pyenv version
```
#### **Windows 10**

Voraussetzung: `git` muss auf Rechner installiert sein (Test mit `git --version`).

Powershell öffnen und folgenden Befehl aufrufen:
```
git clone https://github.com/pyenv-win/pyenv-win.git $HOME/.pyenv
```

***

### Arbeiten mit *virtualenv*

Python enthält die Basisfunktionalität, welcher für die Entwicklung von Programmen benötigt wird. Das Python-Ökosystem bietet mächtige Funktionalität für spezifische Zwecke an (z.B. Statistik, Data Science, Machine Learning etc.). Solche Funktionalität kann mit `pip install` installiert werden.

*Hinweis*: Mit `pip list` kann die Liste der Python-Module angezeigt werden, welche für in der aktuellen Python-Umgebung installiert ist.

Mit *virtualenv* können wir für jedes Python-Projekt eigene Funktionalität aus dem Ökosystem installieren. Auf diese Weise können wir sicherstellen, dass sich die installierten Module nicht gegenseitig in die Quere kommen.

*virtualenv* installieren:

`pip install virtualenv`

#### **Linux**

Nun kann in einem Verzeichnis *py4sysadmins* eine massgeschneiderte Python-Umgebung erzeugt werden:
```
virtualenv py4sysadmins
cd py4sysadmins
source bin/activate
pip list
pip install freegames
pip list
python -m freegames.guess
deactivate
cd ..
rm -rf py4sysadmins
```
Wenn das Projektverzeichnis gelöscht wird, ist das System in den Originalzustand zurück versetzt.   

#### **Windows 10**

Python-Version von https://www.python.org/downloads/ hinunterladen und installiere.

In Powershell im Zielverzeichnis aufrufen:
```
python -m venv py4sysadmins
cd py4sysadmins
.\Scripts\activate
pip list
pip install freegames
pip list
python -m freegames.pacman
deactivate
cd ..
rm py4sysadmins
```

**Bem.**: Eventuell wird beim Aktivieren der virtuellen Umgebung (`.\Scripts\activate`) ein Fehler angezeigt, welcher auf fehlende Rechte in der Powershell hinweist. Das kann korrigiert werden, indem in einer Powershell mit Administratoren-Rechten der Befehl `Set-ExecutionPolicy Remotesigned` ausgeführt wird.

***

## *Entwicklungsumgebungen für Python:*   

* Interactive Shell: Aufruf mit `python`, Beenden mit `exit()`.
* Idle: einfacher Editor mit Code-Vervollständigung
* VS Code mit Python Extensions: Entwicklung von Python-Programmen.
* Jupyter Notebooks: für Präsentationen

***

## Einführung in Python:

Jupyter Notebook *Sprachelemente* auf https://sis-jupyterhub.ethz.ch/user/guest00/notebooks/Python4SysAdmins/ws1/Sprachelemente.ipynb
