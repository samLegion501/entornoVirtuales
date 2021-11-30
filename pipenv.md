# GUIA ENTORNOS VIRTUALES PYTHON CON PIPENV

Administrar dependencias y creación entornos virtuales de Python

> *pip:* Administrador de paquetes
>
> *pipenv:* Administrador de paquetes en entornos virtuales para python
>
> *Link:* [pipenv](https://pipenv-es.readthedocs.io/es/latest/)

Controlar módulos y dependencias de nuestro proyecto

1. Validar instalación en terminal

```
py --version
python --version
pipthon3 --version
```

2. Configurar terminal embebida en VSC


```json
{"Cmder λ": {
			"path": [
				"${env:windir}\\Sysnative\\cmd.exe",
				"${env:windir}\\System32\\cmd.exe"
			],
			"args": ["/K","C:\\Users\\3073662\\Cmder\\vendor\\bin\\vscode_init.cmd"]
	}
}
```



3. Actualizar pip en nuestro sistema

```bat
python -m pip install --upgrade pip
py -m ensurepip --upgrade
rem Reload enviroment
pip --version
```

 <!-- ![Upgrade or update pip](./1_update_pip.png) -->

4. Instalar *pipenv* con *pip*

```
pip install pipenv
```
<!-- ![Install pipenv](./2_install_pipenv.png) -->

5. Crear o inicializar un entorno virtual

```
pipenv shell
```

<!-- ![Create virtual enviroment per project](./3_pipenv_shell.png) -->

- Crea archivo Pipfile (archivo metainformación, describe requerimientos del proyecto)
- Guarda virtual enviroment en una nueva ruta: `C:\Users\3073662\.virtualenvs\website_one-NBidnG23`
- Va a instalar los módulos en un entorno aislado. Cada proyecto tendrá sus propios módulos.
- Crea un subshell para los comandos
- Guide to install cmder in vsc: [Click here](https://github.com/cmderdev/cmder/wiki/Seamless-VS-Code-Integration)

6. Instalar modulos o paquetes en nuestro entorno virtual

```
pipenv install colorama
pipenv install art
pipenv install django
```

- Created Pipfile.lock file that contains all dependencies of our virtual enviroment. This file tells to VE which modules and packages to use in the project.
- Crear archivo main.py para crear un programa de ejemplo que utilice colorama y art.

<!-- ![Install colorama](./4_install_colorama_pipenv.png) -->

7. Listar dependencias del entorno virtual

```
pipenv lock -r
```

8. Instalar-desinstalar paquete en entorno virtual

```
pipenv uninstall colorama
```

9. Paquetes que solo se usan en desarrollo

```
pipenv install colorama --dev
```

10. Instalando desde un archivo

```
pipenv install -r requirements.txt
```

11. Ejemplo de django:

```
django-admin startproject hello
cd hello
py manage.py runserver
```

12.  Listar dependencias:
```
pipenv graph
```

13. Checa por vulnerabilidades en dependencias:
```
pipenv check
```

14. Actualizar y/o instalar dependencias:
```
pipenv install
```

15. Crear, actualizar archivo Pipfile.lock:
```
pipenv lock
```

16. Instalar dependencias ignorando el archivo pipfile:
```
pipenv install --ignore-pipfile
```

17. Eliminar entorno virtual:
```
pipenv --rm
```

## Links interesting:

- [Pipenv](https://pipenv-es.readthedocs.io/es/latest/) for humans.
- Example to work: [Art](https://pypi.org/project/art/) in Pypi.
- [pip](https://pip.pypa.io/en/stable/getting-started/) documentation.
- [pipenv](https://buildmedia.readthedocs.org/media/pdf/pipenv/latest/pipenv.pdf) pdf doc.
- [pipenv](https://github.com/pypa/pipenv) documentation.
- [pep](https://pep8.org/) documentation
- W3C [python](https://www.w3schools.com/python/) tutorial.
- Article initial commit [here](https://initialcommit.com/blog/What-Is-The-Most-Popular-Initial-Commit-Message-In-Git).
- CSEstack.org python tutorial [here](https://www.csestack.org/python/).
- Hide __pycache__ article [here](https://www.it-swarm-es.com/es/python/que-es-pycache/1073619916/).