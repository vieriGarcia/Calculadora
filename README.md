# Calculadora
Proyecto de ejemplo para hacer pruebas unitarias y de desarrollador


#Creación del entorno virtual (Omitir si ya se tiene creado)

 1. Instalar virtualenv
     pip install virtualenv #Windows
     sudo apt install python3-virtualenv #Linux
 2. Crear el entorno virtual
     virtualenv env
 3. Activar el entorno virtual
     source env/bin/activate #Linux
     source env/Scripts/activate #Gitbatch
     env\Scripts\activate.bat #Windows

#Desactivar entorno virtual
 deactivate

#Crear o actualizar fichero requirements
 pip freeze > requirements.txt

#Instalar las dependencias
 pip install -r requirements.txt

#Instalar proyecto
 python setup.py develop

# Ejecutar proyecto
 cd src/entrypoint
 python flask_app.py