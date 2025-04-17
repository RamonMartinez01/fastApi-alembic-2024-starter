#  fastapi-alembic-2024-starter

Este es un proyecto base (starter) para crear aplicaciones backend modernas usando **Python**, **FastAPI**, **SQLAlchemy** y **Alembic**, con conexión a bases de datos **PostgreSQL** mediante variables de entorno.

> Ideal para desarrolladores que buscan aprender o trabajar con FastAPI de forma estructurada, clara y escalable.  
> También útil para proyectos personales, pruebas técnicas o como punto de partida para backends profesionales.

---

##  ¿Qué incluye este proyecto?

-  **FastAPI** como framework backend rápido y moderno.
-  **SQLAlchemy** como ORM para manejar la base de datos.
-  **Alembic** para gestionar migraciones de esquema.
-  **PostgreSQL** como sistema gestor de base de datos.
-  **dotenv** para cargar variables de entorno desde archivos `.env`.
-  Estructura modular: separa controladores, modelos y rutas.
-  Listo para agregar pruebas y documentación en el futuro.

---

## Estructura del Proyecto

fastapi-alembic-2024-starter/ 

├── app/ 

│ ├── controllers/  # Tu lógica de negocio (vacía por ahora) 

│ ├── models/       # Modelos SQLAlchemy (vacío) 

│ ├── routes/       # Rutas de la API (vacío) 

│ ├── config.py     # Configuración basada en variables de entorno 

│ ├── database.py   # Conexión a la base de datos 

│ └── init.py 

│

├── .env.example     # Archivo de ejemplo con variables de entorno 

├── .gitignore 

├── alembic.ini      # Configuración de Alembic 

├── main.py          # Archivo principal de entrada de la aplicación 

└── requirements.txt # Lista de dependencias

##  Cómo usar este proyecto como base para tus propios desarrollos

¿Quieres comenzar tu propio backend con esta misma estructura? Aquí te explico cómo hacerlo:

---

### Opción A: Usar como plantilla (recomendado si quieres empezar desde cero)

1. Ve al repositorio original en GitHub (este repositorio 😄)

2. Haz clic en el botón verde **"Use this template" / "Create a new repository"**  
   Esto te permitirá crear una copia nueva del repositorio en tu cuenta, **sin el historial de cambios (commits)** del original.  
   Ideal para empezar limpio y personalizado.

3. Ponle un nuevo nombre a tu proyecto  
   Por ejemplo: `mi-api-fastapi`, `backend-tareas-2024`, `api-python-starter`, etc.

4. Clona tu nuevo repositorio a tu computadora:  
   Desde tu cuenta de GitHub, copia el enlace (URL) del nuevo repositorio y en tu terminal:

```git clone https://github.com/tu-usuario/mi-api-fastapi.git```

```cd mi-api-fastapi```

##### Después de esto puedes continuar con la sección "Cómo Empezar" (de este mismo README)

### Opción B: Fork (recomendado si quieres colaborar con este proyecto o mantenerlo sincronizado)

1. Haz clic en el botón "Fork" en la esquina superior derecha del repositorio.

Esto crea una copia completa del repositorio en tu cuenta, con el historial de cambios incluido (commits, ramas, etc.).

2. Clona el Fork a tu computadora:

```git clone https://github.com/tu-usuario/fastapi-alembic-2024-starter.git```

```cd fastapi-alembic-2024-starter```

##### Después de hacer esto, puedes seguir con la sección "Cómo Empezar" (justo a continuación)

## Cómo Empezar 

>Tanto si copiaste este repositorio como Template, como si lo hiciste con un Fork, y ya lo has clonado a tu entorno local, lo que sigue es terminar de configurar tu proyecto para que puedas comenzar a crear tu API.
>
--- 

### 1. Crear entorno virtual (solo una vez)
```python -m venv env```

#### Activar entorno virtual:

##### En Windows:
```env\Scripts\activate```

##### En macOS/Linux:
```source env/bin/activate```

### 2. Instala las dependencias del proyecto

```pip install -r requirements.txt```

Esto instalará todos los paquetes necesarios para que el proyecto funcione: FastAPI, Alembic, SQLAlchemy, Uvicorn, etc.

### 3. Configura tus variables de entorno

Copia el archivo .env.example a un nuevo archivo llamado .env:

```cp .env.example .env```

Edita el archivo .env y reemplaza <nombre_DB> por el nombre de tu base de datos PostgreSQL:

```DATABASE_URL=postgresql://postgres:tu_contraseña@127.0.0.1:5432/nombre_real_de_tu_db```

Asegúrate de que tu base de datos esté creada y en funcionamiento antes de ejecutar el servidor.

### 4. Ejecuta el servidor de desarrollo

```uvicorn main:app --reload```

Esto levantará tu servidor en modo desarrollo, con recarga automática al guardar cambios.

#### Abre tu navegador y visita:

```http://localhost:8000```

#### Deberías ver:

```{"message": "Bienvenido a tu nueva API!"}```

### También puedes visitar la documentación automática generada por FastAPI:

Documentación Swagger UI: http://localhost:8000/docs

Documentación Redoc: http://localhost:8000/redoc


## ¿Y para producción?

Cuando estés listo para desplegar tu proyecto en la nube (Render, Railway, GCP, AWS, etc.), asegúrate de usar el siguiente comando como comando de inicio:

```uvicorn main:app --host 0.0.0.0 --port 8000```

Este comando inicia el servidor en modo estándar de producción, y es el que puedes especificar como "start command" en plataformas como Render o Railway.

En la próxima sección te mostraré cómo configurar Alembic para crear migraciones de tu base de datos. También puedes empezar a construir tus modelos, rutas y controladores desde la carpeta app/.
