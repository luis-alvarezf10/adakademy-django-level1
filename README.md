## INSTALACIÓN DE PROYECTO CON DJANGO (PARA MI)


1. Abrir terminal
2. Instalar el entorno virtual 
    ```bash
    python -m venv .venv
3. Activar el entorno virtual
    ```bash
    .venv\Scripts\activate.ps1
4. Inicializar un proyecto django
    ```Bash
    # es necesario poner un punto al final ya que esto crea el archivo manage.py (main de pagina web creada)
    django-admin startproject django_project .
5. Correr servidor django
    ```bash
    `# deberia salir una linea en la terminal parecido a esto `
    `# Starting development server at http://127.0.0.1:8000/`
    `# copia y pega en el navegador deberia salir una pagina con un mensaje de que la instalacion fue exitosa`
    `python manage.py runserver`

6. Se puso una linea de codigo en el archivo settings.py del proyecto `'DIRS': [BASE_DIR / 'templates'],` y creado una carpeta llamada "templates"
- ojo: django deberia trabajarse de la siguiente manera `MTVUU = models templates views urls urls` el cual se utilizara con las ultimas cuatro 

7. Se creo un archivo llamado "views.py" en la carpeta django_projects
- nota: puedo revisar la pagina para estructuracion django // https://ccbv.co.uk