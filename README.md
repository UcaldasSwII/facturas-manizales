# Facturas-Manizales

Este proyecto es una aplicación web desarrollada con FastAPI para la gestión de facturas en la ciudad de Manizales.

## Características

- Creacion y Autenticación de usuarios.
- Registro de servicios publicos.
- Generación y pago de facturas.

## Tecnologías Utilizadas

- FastAPI
- SQLAlchemy

## Instalación

Para ejecutar este proyecto, asegúrate de tener Docker instalado en tu sistema.

1. **Clona este repositorio:**
 ```shell
 git clone <url-del-repositorio>
 ```

3. **Navega al directorio del proyecto:**
  ```shell
  cd Facturas-Manizales
  ```
## Configuración del entorno

Antes de instalar las dependencias y ejecutar el proyecto, es recomendable crear un entorno virtual para aislar las dependencias del proyecto. Sigue estos pasos para configurar tu entorno virtual:

3. **Crear el entorno virtual**:
   - En Windows:
     ```shell
     python -m venv .env
     ```
   - En macOS/Linux:
     ```shell
     python3 -m venv .env
     ```

4. **Activar el entorno virtual**:
   - En Windows:
     ```shell
     .\.env\Scripts\activate
     ```
   - En macOS/Linux:
     ```shell
     source .env/bin/activate
     ```

5. **Instala las dependencias**
  ```shell
  pip install -r requirements.txt
  ```

6. **Ejecuta la aplicacion con uvicorn**
  ```shell
  uvicorn main:app --reload
  ```
Ahora puedes acceder a la aplicación en http://localhost:8000.

## Documentación de la API

Una vez que la aplicación esté ejecutándose, puedes acceder a la documentación de la API generada automáticamente por FastAPI en http://localhost:8000/docs.

## Contribuir
Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y envía un pull request con tus cambios.
