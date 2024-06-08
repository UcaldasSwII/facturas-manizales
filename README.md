# Facturas-Manizales

Este proyecto es una aplicación web desarrollada con FastAPI para la gestión de facturas en la ciudad de Manizales.

## Características

- Autenticación de usuarios.
- Gestión de servicios.
- Registro y manejo de pagos.
- Generación y administración de facturas.

## Tecnologías Utilizadas

- FastAPI
- SQLAlchemy
- Passlib
- JWT para autenticación

## Instalación

Para ejecutar este proyecto, asegúrate de tener Docker instalado en tu sistema.

1. Clona este repositorio:

  git clone <url-del-repositorio>

2. Navega al directorio del proyecto:
   
  cd Facturas-Manizales

3. Construye y ejecuta el contenedor Docker:
   
  docker build -t facturas-manizales .
  docker run -d --name facturas-manizales -p 8000:8000 facturas-manizales

Ahora puedes acceder a la aplicación en http://localhost:8000.

## Documentación de la API

Una vez que la aplicación esté ejecutándose, puedes acceder a la documentación de la API generada automáticamente por FastAPI en http://localhost:8000/docs.

## Contribuir
Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y envía un pull request con tus cambios.
