# RaspberryPiPicoW-IOT-PabloEspinosa
Evaluación del Primer Parcial – Internet de las Cosas (IoT)

# Descripción del Proyecto
El proyecto tiene como objetivo implementar un código para que una placa Raspberry Pi Pico W pueda medir temperatura con su sensor interno y conectarse a internet para poder imprimir y mantenerse enviando las lecturas de la temperatura cada 180 segundos a la página de ThingSpeak. El código está realizado con MicroPython y se conecta a la red para poder enviar los datos que irá recolectando constantemente.

# Instrucciones de Instalación y Uso

Para poder utilizar este proyecto se requiere de los siguientes elementos:
* Una placa Raspberry Pi Pico W.
* Conexión a internet de 2.4G, junto a su contraseña para que el dispositivo pueda acceder a ella.
* MicroPython instalado.
* Una cuenta de ThingSpeak, con un canal con Field Charts y API Key para poder realizar la conexión y poder imprimir los datos.

Una vez cumplidos los requisitos, clonar los archivos de este repositorio o copiar el código y guardarlo dentro de la Raspberry. Se puede utilizar herramientas como Thonny para subir el código.
Asegurarse de cambiar las siguientes variables a por el nombre de la red a la que se va a conectar, su contraseña, y la API Key del ThingSpeak:
- SSID = "YOUR NETWORK NAME"
- PASSWORD = "YOUR NETWORK PASSWORD"
- THINGSPEAK_API_WRITE = "YOUR API KEY"
Una vez guardado el código, correrlo y comprobar que la conexión se realice con la red. Si se conectó exitosamente, los datos deberían de empezar a reflejarse en el ThingSpeak.
Cada vez que un dato sea envíado, el LED de la placa se encenderá. El proceso se mantendrá mientras exista conexión y la placa esté conectada a corriente, de tal manera que la información se mantendrá enviándose a ThingSpeak.

Captura del código en funcionamiento:
![image](https://github.com/user-attachments/assets/68f5ac03-e3ff-4c28-a263-68aa62df4cee)

Captura de las gráficas en ThingSpeak:
![image](https://github.com/user-attachments/assets/a428b17f-c3b5-4b58-9ba9-9802e8a25ab7)

Capturas de los procesos de MathWorks:
![image](https://github.com/user-attachments/assets/463add3f-62b5-495c-9aaf-e7509d46ab95)
![image](https://github.com/user-attachments/assets/da66b413-0988-4e07-b594-77ff47ccbed8)
