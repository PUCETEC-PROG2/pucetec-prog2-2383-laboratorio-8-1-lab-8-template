[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-ue548Ro)
# Laboratorio 8. Taller Inicial de Django: Views, Templates y Modelos

Este laboratorio está diseñado para que los participantes puedan aprender y reforzar sus conocimientos de Python, HTML y CSS mediante la creación de una lista de Pokemones y una página de datalle. Utilizando como framework de desarrollo MVC a Django. De la misma manera se hará una introduccion a Bootstrap para el uso de librerías de Interfaz de usuario en HTML.

Por otra parte se aplica el uso de Modelos en Django y uso de bases de datos relacionales en PostgreSQL

## Objetivos 
- El estudiante debe ser capaz de reconocer y aplicar conceptos básicos del Paradigma Orientado a Objetos (POO) como: Clases, Ojetos, Atributos, Métodos. Así mismo el presente proyecto introduce al desarrollo de aplicaciones Web mediante el uso de Django como marco de trabajo para el desarrollo.
- El estudiante reforzará sus conocimientos de POO y manejo de bases de datos relacionales a través del uso de modelos en Django

## Tareas a realizar
1. Generación de Modelos de Pokemon y Trainer
2. Generación de migraciones.
3. Despliegue de Pokemones en Templates lista y detalle
4. Despliegue de Entrenadores en Templates lista y detalle

## Instalación del ambiente

### Requerimientos

- Python 3.10 o superior
- PostgreSQL

### Ubuntu Linux / MacOS
Instalación de gestor de ambientes virtuales de Python
~~~
sudo apt install python3-venv
~~~
Creación del ambiente virtual
~~~
python3 -m venv .venv
~~~
Activación del ambiente virtual
~~~
source .venv/bin/activate
~~~
Instalación de dependencias de este proyecto
~~~
pip3 install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~
### Windows
Instalación de gestor de ambientes virtuales de Python
~~~
pip install virtualenv
~~~
Creación del ambiente virtual
~~~
py -m venv .venv
~~~
Activación del ambiente virtual para CMD
~~~
.venv\Scripts\activate
~~~
Activación del ambiente virtual para PowerShell
~~~
.venv\Scripts\activate.ps1
~~~
Instalación de dependencias de este proyecto
~~~
pip install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~

## Comandos útiles

### Iniciar servidor
#### Linux o MaCOS
~~~
python3 manage.py runserver
~~~
#### Windows
~~~
python manage.py runserver
~~~

Una vez inicializado el servidor se deberá dirigir al siguiente enlace: <http://localhost:8000>

### Crear nueva aplicación
#### Linux o MaCOS
~~~
python3 manage.py startapp <nombre_de_la_aplicacion>
~~~
#### Windows
~~~
python manage.py startapp <nombre_de_la_aplicacion>
~~~

### Crear Súper Usuario
#### Linux o MaCOS
~~~
python3 manage.py createsuperuser
~~~
#### Windows
~~~
python manage.py createsuperuser
~~~

### Generar archivos de migración
#### Linux o MaCOS
~~~
python3 manage.py makemigrations
~~~
#### Windows
~~~
python manage.py makemigrations
~~~

### Migrar a bases de datos
#### Linux o MaCOS
~~~
python3 manage.py migrate
~~~
#### Windows
~~~
python manage.py migrate
~~~

### Almacenar depdendencias y librerías instaladas
#### Linux o MaCOS
~~~
pip3 freeze > requirements.txt
~~~
#### Windows
~~~
pip freeze > requirements.txt
~~~

# Nota
Para los siguientes pasos se deberán seguir las instrucciones del docente en clase. No olvide que puedes contactarlo a <paperez@puce.edu.ec> o a <pablo.perez@uisek.edu.ec> dependiendo de la institución donde te encuentres