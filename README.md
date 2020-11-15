# Estructuras_Datos_Investigacion1
Demo de la investigacion 1

Instalación:
***Instalar python***
Una vez python está instalado en una ventana de comandos CMD ejecutar la siguiente linea:
"python get-pip.py" (sin las comillas)

Luego ejecutar la siguiente línea cuando pip está instalado de manera correcta:
"pip install bcrypt==3.2.0" (sin las comillas)

***Configurar Visual Code para correr programas en python Windows:***
https://code.visualstudio.com/docs/python/python-tutorial

***Configurar IntelliJ para correr programas en python Windows:***
https://www.jetbrains.com/help/idea/plugin-overview.html

***Instalar Postman para poder correr servicios***
https://www.postman.com/

Descargue los archivos que se encuentran en este repositorio y ubíquelos en una ruta local.

***Pasos para ejecutar el demo:***
En una ventana de CMD navegar hasta la carpeta que contiene los archivos Login_service.py y Login_logic.py
Ejectuar el siguiente comando en la ventana de CMD: "python Login_service.py 8080" (sin las comillas)

Crear una ventana en postman con un método GET
En la caja de texto, ingresar el siguiente comando: localhost:8080

Click en Send. En la parte inferior de la ventana donde se despliegan los mensajes, verificar si se muestra el siguiente mensaje:
"Service running successfully"

Una vez que el servicio está corriendo de manera correcta, crear una segunda ventana en Postman con un método POST.
En la caja de texto, ingresar el siguiente comando: localhost:8080/createbcrypt

En la ventana, click en Body, seleccionar "raw" como valor de entrada e ingresar en la caja de texto el siguiente JSON:
{
    "username":"Diego",
    "password":"12345"
}

El siguiente JSON simula el login en una aplicación web donde ingresamos nuestro usuario y contraseña.
El usuario y contraseña ingresados se hashean utilizando bcrypt y se almacena en una base de datos (en este caso una base de datos temporal en memoria)

Al terminar de ejecutarse el servicio, nos mostrará el resultado de nuestro usuario y password hasheado utilizando bcrypt.

Test para login:
Crear una segunda ventana en Postman con un método POST.
En la caja de texto, ingresar el siguiente comando: localhost:8080/login

En la ventana, click en Body, seleccionar "raw" como valor de entrada e ingresar en la caja de texto el siguiente JSON:
{
    "username":"Diego",
    "password":"12345"
}

El siguiente JSON simula el login en una aplicación web donde ingresamos nuestro usuario y contraseña.
El servicio "autentica" el usuario y contraseña ingresados buscando dichos valores en el registro de contraseñas que creamos temporalmente, utilizando las funciones de bcrypt para decodificar el password previamente registrado contra el password ingresado al servicio.




