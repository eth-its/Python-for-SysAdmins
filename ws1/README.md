# Workshop 1

*Einführung in Python: Sprachelemente*

- Python Entwicklungs- und Laufzeitumgebung   
- Sprachelemente: Typen (z.B. Listen, Dicts), Bedingungen, Schlaufen etc.   
- Python-Module

***

Überprüfen, ob Python (in welcher Version) installiert ist:

`python -V`

Wir wollen mit Python 3 arbeiten. Andererseits wollen wir eine installierte Python-Version nicht überschreiben. Mit *pyenv* können wir neue Python-Versionen installieren und für jeden Verzeichnisbaum wählen, welche Python-Version gelten soll.

## Installation von *pyenv*

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
## Arbeiten mit *virtualenv*

Python enthält die Basisfunktionalität, welcher für die Entwicklung von Programmen benötigt wird. Das Python-Ökosystem bietet mächtige Funktionalität für spezifische Zwecke an (z.B. Statistik, Data Science, Machine Learning etc.). Solche Funktionalität kann mit `pip install` installiert werden.

Mit *virtualenv* können wir für jedes Python-Projekt eigene Funktionalität aus dem Ökosystem installieren. Auf diese Weise können wir sicherstellen, dass sich die installierten Module nicht gegenseitig in die Quere kommen.

*virtualenv* installieren:

`pip install virtualenv`

Nun kann in einem Verzeichnis *py4sysadmins* eine massgeschneiderte Python-Umgebung erzeugt werden:
```
virtualenv py4sysadmins
cd py4sysadmins
source bin/activate
pip install boas-game
boas
deactivate
cd ..
rm -rf py4sysadmins
```
Wenn das Projektverzeichnis gelöscht wird, ist das System in den Originalzustand zurück versetzt.
