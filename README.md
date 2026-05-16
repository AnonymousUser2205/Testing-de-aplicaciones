# TPO2: Automatización de pruebas y pipeline CI/CD

Este proyecto implementa una calculadora básica en Python con pruebas automatizadas utilizando `pytest` y un pipeline de CI/CD mediante GitHub Actions.

## Estructura del Proyecto

- `app/calculator.py`: Lógica principal de la aplicación.
- `tests/test_calculator.py`: Pruebas unitarias (Éxito, Error y Borde).
- `.github/workflows/pipeline.yml`: Configuración del pipeline de GitHub Actions.
- `requirements.txt`: Dependencias del proyecto.

## Cómo ejecutar localmente

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar pruebas y generar reporte:
   ```bash
   python -m pytest --html=report.html --self-contained-html
   ```

## Pipeline CI/CD

El pipeline se ejecuta automáticamente con cada `push` a las ramas `main` o `master`.
Realiza las siguientes tareas:
1. Configura el entorno Python.
2. Instala las dependencias.
3. Ejecuta los tests.
4. Genera y sube el reporte HTML como un artefacto de la ejecución.
