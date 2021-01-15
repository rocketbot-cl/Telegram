# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""


base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Telegram" + os.sep + "libs" + os.sep
sys.path.append(cur_path)

import telegram
global bot_rb

module = GetParams("module")
if module == "connect":
    token = GetParams("token")
    option = GetParams("option")
    try:
        bot_rb = telegram.Bot(token=token)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "sendMessage":
    msg = GetParams("msg")
    chat_id_unfixed = GetParams("chat_id")
    try:
        if chat_id_unfixed.find("_") != -1:
            underscore_index = chat_id_unfixed.find("_")
            cad_without_underscore = chat_id_unfixed[:underscore_index]
            removed_prefixed_letter = cad_without_underscore[1:]
            chat_id = "-100" + removed_prefixed_letter
        if chat_id_unfixed[0] == "g":
            chat_id = chat_id_unfixed[1:]
            chat_id = "-" + chat_id
        if chat_id_unfixed.find("@") != -1:
            chat_id = chat_id_unfixed
        if chat_id_unfixed.isdigit():
            chat_id = chat_id_unfixed
        bot_rb.sendMessage(chat_id=chat_id, text=msg)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
