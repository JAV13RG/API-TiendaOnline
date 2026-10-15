# API de Tienda Online - Backend

Sistema centralizado para digitalizar la gestión de ventas, pedidos y mantener registros históricos consistentes. Esta API REST está construida con Django y Django REST Framework (DRF), utilizando PostgreSQL como motor de base de datos.

## Requisitos Previos
- Python 3.x
- Git
- PostgreSQL (Motor de base de datos)

## Instrucciones de Instalación y Ejecución

**1. Clonar el repositorio:**
```bash
git clone [URL_DE_TU_REPOSITORIO]
cd API-TIENDAONLINE
```

**2. Crear y activar el ambiente virtual:**
    - En windows:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```
    - En macOS/Linux:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

**3. Instalar dependencias:**
```bash
pip install -r requirements.txt
```

**4. Configurar la Base de Datos:**
- Asegúrate de que el servicio de PostgreSQL esté en ejecución.
- Ejecuta el `script scripts_db.sql` incluido en la raíz del proyecto dentro de tu gestor de base de datos (por ejemplo, DBeaver) conectado como administrador.
- Este script creará la base de datos `tienda_online_db`, el usuario `admin_tienda` y asignará los permisos necesarios.

**5. Configurar las variables de entorno:**
- Crear un archivo llamado `.env` en la raíz del proyecto.
- Añade las siguientes variables y ajusta los valores si es necesario:
```bash
SECRET_KEY=tu_secret_key_aqui
DB_NAME=tienda_online_db
DB_USER=admin_tienda
DB_PASSWORD=admin123
DB_HOST=127.0.0.1
DB_PORT=5432
```

**6. Aplicar las migraciones:**
Construye las tablas en la base de datos ejecutando:
```bash
python manage.py migrate
```

**7. Ejecutar en el servidor local:**
```bash
python manage.py runserver
```

## Endpoints Principales (API REST)
Una vez levantado el servidor, puedes acceder a la interfaz navegable de la API en las siguientes rutas:

- Categorías: `http://127.0.0.1:8000/api/categorias/`

- Productos: `http://127.0.0.1:8000/api/productos/`