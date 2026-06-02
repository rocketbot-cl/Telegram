



# Telegram
  
Conecta tu bot de Telegram con Rocketbot  

*Read this in other languages: [English](Manual_Telegram.md), [Português](Manual_Telegram.pr.md), [Español](Manual_Telegram.es.md)*
  
![banner](imgs/Banner_Telegram.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Como usar este modulo

Antes de usar este modulo, es necesario crear un bot de Telegram y obtener el identificador del chat donde el bot enviara los mensajes.

1. Abra Telegram y busque **BotFather**.
2. Inicie una conversacion con BotFather y envie el comando **/newbot**.
3. Ingrese el nombre del bot y luego el usuario del bot. El usuario debe terminar en **bot**.
4. BotFather devolvera un token similar a: **1520225275:AAELRsagaahsrp0M_LtehaS4eheaadpUOfsLjhw**. Copie este valor.
5. Agregue el bot al chat, grupo o canal donde desea enviar mensajes. Si es un grupo o canal, asegurese de que el bot tenga permisos para enviar mensajes.
6. Para obtener el chat_id, envie un mensaje al bot o al grupo donde fue agregado y luego abra esta URL en un navegador:
https://api.telegram.org/bot{token}/getUpdates
Reemplace **{token}** por el token generado por BotFather.
7. En la respuesta, busque el valor **chat.id** y copielo. Para canales o grupos publicos tambien puede usar el usuario con 
**@**, por ejemplo **@mi_canal**.
8. En Rocketbot, use el comando **Conectar** e ingrese el token del bot en el campo **Token**.
9. Despues de conectar, use el comando **Enviar mensaje**. Ingrese el texto en **Mensaje** y el destino en **chat_id**.
10. Para enviar un archivo, seleccione la ruta en **Archivo**. Si el archivo es una imagen y desea enviarlo como foto, marque **Es imagen?**. Si no se marca, el archivo se enviara como documento.

Nota: El comando **Conectar** debe ejecutarse antes de **Enviar mensaje** dentro del mismo flujo de ejecucion de Rocketbot.

## Descripción de los comandos

### Conectar
  
Conecta tu bot telegram con Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Token|Token de tu bot de telegram|1520225275:AAELRsagaahsrp0M_LtehaS4eheaadpUOfsLjhw|

### Enviar mensaje
  
Envia un mensaje a un chat
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Mensaje|El mensaje que quieres enviar|El mensaje va aca...|
|chat_id|El chat_id del chat al que quieres enviar el mensaje|chat_id|
|Archivo|Ruta opcional del archivo a enviar. Si es imagen se enviara como foto, si no como documento.|C:\ruta\archivo.pdf|
|¿Es imagen?|Marca esta casilla si el archivo a enviar es una imagen. Si no se marcó, se enviará como documento.||
