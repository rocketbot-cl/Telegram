



# Telegram
  
Conecte seu bot do Telegram com o Rocketbot  

*Read this in other languages: [English](Manual_Telegram.md), [Português](Manual_Telegram.pr.md), [Español](Manual_Telegram.es.md)*
  
![banner](imgs/Banner_Telegram.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Como usar este modulo

Antes de usar este modulo, e necessario criar um bot do Telegram e obter o identificador do chat onde o bot enviara as mensagens.

1. Abra o Telegram e procure por **BotFather**.
2. Inicie uma conversa com o BotFather e envie o comando **/newbot**.
3. Informe o nome do bot e depois o usuario do bot. O usuario deve terminar em **bot**.
4. O BotFather retornara um token semelhante a: **1520225275:AAELRsagaahsrp0M_LtehaS4eheaadpUOfsLjhw**. Copie esse valor.
5. Adicione o bot ao chat, grupo ou canal onde deseja enviar mensagens. Se for um grupo ou canal, verifique se o bot tem permissao para enviar mensagens.
6. Para obter o chat_id, envie uma mensagem ao bot ou ao grupo onde o bot foi adicionado e depois abra esta URL em um navegador:
https://api.telegram.org/bot{token}/getUpdates
Substitua **{token}** pelo token gerado pelo BotFather.
7. Na resposta, encontre o valor **chat.id** e copie-o. Para canais ou grupos publicos, tambem e possivel usar o usuario com 
**@**, por exemplo **@meu_canal**.
8. No Rocketbot, use o comando **Connect** e informe o token do bot no campo **Token**.
9. Depois de conectar, use o comando **Send Message**. Informe o texto em **Message** e o destino em **chat_id**.
10. Para enviar um arquivo, selecione o caminho em **File**. Se o arquivo for uma imagem e voce quiser envia-lo como foto, marque **Is Image?**. Se nao estiver marcado, o arquivo sera enviado como documento.

Nota: O comando **Connect** deve ser executado antes de **Send Message** no mesmo fluxo de execucao do Rocketbot.
## Descrição do comando

### Conectar
  
Conecte seu bot do Telegram com o Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Token|Token do seu bot do Telegram|1520225275:AAELRsagaahsrp0M_LtehaS4eheaadpUOfsLjhw|

### Enviar mensagem
  
Envie uma mensagem para um chat
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Mensagem|A mensagem que você quer enviar|El mensaje va aca...|
|chat_id|O chat_id do chat para o qual você deseja enviar a mensagem|chat_id|
|Arquivo|Caminho opcional do arquivo para enviar. Se for uma imagem, será enviada como foto, caso contrário, como documento.|C:\ruta\archivo.pdf|
|É uma imagem?|Marque esta caixa se o arquivo a enviar for uma imagem. Se não marcada, será enviado como documento.||
