# Marinoteca

Marinoteca es una aplicación de gestión de bibliotecas escrita en Python. Permite registrar y administrar usuarios y libros, así como realizar reservas. Este README proporciona una descripción general de las funcionalidades y cómo usar la aplicación.

## Tabla de Contenidos

1. [Requisitos](#requisitos)
2. [Funcionalidades](#funcionalidades)
   - [Administración de Usuarios](#administración-de-usuarios)
     - [Registrar Usuario](#registrar-usuario)
     - [Eliminar Usuario](#eliminar-usuario)
   - [Administración de Libros](#administración-de-libros)
     - [Agregar Libro](#agregar-libro)
     - [Eliminar Libro](#eliminar-libro)
     - [Agregar Copias](#agregar-copias)
     - [Mostrar Todos los Libros](#mostrar-todos-los-libros)
     - [Mostrar Libros por Categoría](#mostrar-libros-por-categoría)
     - [Mostrar Libros por Autor](#mostrar-libros-por-autor)
   - [Funcionalidades Generales](#funcionalidades-generales)
     - [Iniciar Sesión (Admin y Cliente)](#iniciar-sesión-admin-y-cliente)
     - [Generador de ID](#generador-de-id)
     - [Guardar y Leer Datos](#guardar-y-leer-datos)
     - [Limpiar Pantalla](#limpiar-pantalla)
3. [Uso](#uso)
   - [Ejecución del Programa](#ejecución-del-programa)
   - [Navegación en el Menú Principal](#navegación-en-el-menú-principal)
4. [Ejemplo de Uso](#ejemplo-de-uso)
5. [Notas](#notas)
6. [Contribuciones](#contribuciones)

## Requisitos

- Python
- Módulos estándar de Python: `json`, `time`, `os`, `datetime`

## Funcionalidades

### Administración de Usuarios

1. **Registrar Usuario**

   - Permite registrar nuevos usuarios con datos como nombres, apellidos, número de documento, dirección y teléfono móvil.

2. **Eliminar Usuario**
   - Permite eliminar usuarios existentes mediante su número de documento.

### Administración de Libros

1. **Agregar Libro**

   - Permite agregar nuevos libros a la biblioteca con detalles como título, autor, categoría, fecha de publicación y cantidad.

2. **Eliminar Libro**

   - Permite eliminar libros mediante su ID, ya sea eliminando todas las unidades o una cantidad específica.

3. **Agregar Copias**

   - Permite agregar copias adicionales a un libro existente mediante su ID.

4. **Mostrar Todos los Libros**

   - Muestra una lista de todos los libros en la biblioteca.

5. **Mostrar Libros por Categoría**

   - Muestra una lista de libros filtrados por categoría.

6. **Mostrar Libros por Autor**
   - Muestra una lista de libros filtrados por autor.

### Funcionalidades Generales

1. **Iniciar Sesión (Admin y Cliente)**

   - Permite a los administradores y clientes iniciar sesión en el sistema mediante credenciales.

2. **Generador de ID**

   - Genera un nuevo ID para cada libro añadido a la biblioteca.

3. **Guardar y Leer Datos**

   - Guarda y lee los datos de la biblioteca en un archivo `data.json`.

4. **Limpiar Pantalla**
   - Limpia la pantalla de la consola dependiendo del sistema operativo.

## Uso

### Navegación en el Menú Principal

- **Ingresar como Cliente**
  Permite a los clientes registrados iniciar sesión y acceder a las funcionalidades de reserva de libros.

- **Registrarse como Nuevo Cliente**
  Permite a nuevos usuarios registrarse en el sistema.

- **Ingresar como Administrador**
  Permite a los administradores iniciar sesión y acceder a las funcionalidades de administración de la biblioteca.

- **Salir**
  Sale del programa.

### Ejemplo de Uso

- **Registrar un Nuevo Usuario**
  1. Selecciona la opción "Incríbete para reservar" en el menú principal.
  2. Ingresa los datos solicitados.
  3. Los datos se guardarán en `data.json`.

- **Agregar un Nuevo Libro**
  1. Inicia sesión como administrador.
  2. Selecciona la opción "Agregar libro".
  3. Ingresa los datos del libro.

- **Eliminar un Libro**
  1. Inicia sesión como administrador.
  2. Selecciona la opción "Eliminar libro".
  3. Ingresa el ID del libro a eliminar.

- ** Mostrar Libros **
  1. Mostrar libros por categorias
  2. Mostrar libros por autores
  3. Mostrar libros por nombre
  4. Mostrar usuarios con libros
 
## Capturas de Pantalla

A continuación se muestran ejemplos de la interfaz de la consola para la aplicación Marinoteca. Estas capturas ilustran cómo se visualizan las distintas funcionalidades del programa.

### Pantalla de Inicio

![Pantalla de Inicio](/imgs/1.png)

### Ingreso de usuario

![Ingreso de usuario](/imgs/2.png)

### Pagina de registro

![Registro de usuarios](/imgs/3.png)

### Menu de navegacion del administrador

![Menu administrador](/imgs/4.png)

### Ejecución del Programa

Para iniciar el programa, ejecuta el script `marinoteca.py` en la consola:

## Notas

- Asegúrate de que el archivo data.json esté en el mismo directorio que marinoteca.py. Si no existe, el programa lo creará automáticamente al iniciar. 

- La aplicación utiliza la biblioteca estándar de Python, por lo que no es necesario instalar dependencias adicionales.

