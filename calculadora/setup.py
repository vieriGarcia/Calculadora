from setuptools import setup,  find_packages


setup(name="Calculadora",  # Nombre
    version="0.1",  # Versión de desarrollo
    description="Paquete de prueba",  # Descripción del funcionamiento
    author="Vieri Garcia",  # Nombre del autor
    author_email='vieri.garcia@unmsm.edu.pe',  # Email del autor
    license="GPL",  # Licencia: MIT, GPL, GPL 2.0...
    url="http://ejemplo.com",  # Página oficial (si la hay)
    packages=find_packages(),
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    test_suite="tests"
)