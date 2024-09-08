# Reflex App

Este proyecto es una aplicación web construida con Reflex. La aplicación utiliza Supabase para gestionar la base de datos y está diseñada para ser desplegada en Google Cloud Run.

## Requisitos

- Python 3.11
- Docker
- Google Cloud SDK

## Instalación

### Clonar el Repositorio

```sh
git clone https://github.com/frealexandro/RandIA.git
cd RandIA

```

# Crear y Activar un Entorno Virtual

```py
python -m venv .env
source .env/bin/activate
```

# Instalar Depenedencias

Asegúrate de que el archivo requirements.txt incluya las siguientes dependencias:

```txt
reflex==0.5.10
supabase
python-dotenv
```
Luego, instala las dependencias:

```sh
pip install --upgrade pip
pip install -r requirements.txt
```

# Configurar Variables de Entorno

Crea un archivo .env en la raíz del proyecto y agrega las siguientes variables de entorno:

```sh
SUPABASE_URL=tu_supabase_url
SUPABASE_KEY=tu_supabase_key
```

# Desplegar en tu entorno

```sh
reflex init
reflex run
```

