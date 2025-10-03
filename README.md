# Gestión de Calificaciones NUAM

## Descripción

Este proyecto corresponde a una evaluación de Michelle Villalobos y Christian Águila utilizando **Django** como framework back-end.  
El sistema gestiona **Empresas, Instrumentos Financieros y Calificaciones Tributarias** en el contexto de **NUAM (Núcleo Andino de Mercados)**.

Incluye:

- Modelo de datos (M.E.R).
- CRUD de Empresas y Calificaciones.
- Panel de administración con Django Admin.
- Front-end con HTML, CSS y JavaScript.
- API JSON para consumo con JS.
- Archivos `.gitignore` y `README`.

---

## Tecnologías

- Python 3
- Django
- SQLite (base de datos local)
- HTML, CSS y JavaScript

---

## Modelo de Datos (M.E.R) en Mermaid

```
erDiagram
    USUARIO {
        int id
        string nombre
        string correo
        string contraseña
        string rol
    }

    EMPRESA {
        int id
        string nombre
        string pais
        string identificador
    }

    INSTRUMENTO {
        int id
        string nombre
        string tipo
    }

    CALIFICACION_TRIBUTARIA {
        int id
        int año
        string nota
        string comentario
        datetime fecha_creacion
    }

    USUARIO ||--o{ EMPRESA : "gestiona"
    EMPRESA ||--o{ INSTRUMENTO : "posee"
    EMPRESA ||--o{ CALIFICACION_TRIBUTARIA : "recibe"
```
