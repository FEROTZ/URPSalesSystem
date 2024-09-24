## Instrucciones para ejecutar el Seeder

Para inicializar la base de datos con los permisos predeterminados, siga estos pasos:

1. Asegúrese de que la aplicación y la base de datos estén configuradas correctamente.
2. Abra una terminal en el directorio raíz del proyecto.
3. Active el entorno virtual si está utilizando uno.
4. Ejecute el siguiente comando:

   ```
   python run_seeder.py
   ```

5. Verá un mensaje indicando si el seeder se ejecutó con éxito o si hubo algún error.

Nota: Este script solo debe ejecutarse una vez para inicializar los permisos en la base de datos. Si lo ejecuta más de una vez, el script verificará si los permisos ya existen y no creará duplicados.