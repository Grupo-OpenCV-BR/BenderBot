# BenderBot
Um bot para ajudar a moderar e enviar informações (in)úteis para um grupo.

O projeto ainda está em desenvolvimento e você pode colaborar. Existe uma lista de features que ainda precisam ser implementadas para que o bot possa acrescentar mais ao nosso grupo (OpenCV Brasil).

## Como contribuir

Para contribuir com o projeto, siga os seguintes passos:

- <b>Crie uma issue:</b> Nesta issue você deve especificar qual problema o bot está apresentando. Caso queira resolvê-lo, manifeste este interesse na issue e atribuiremos a issue a você (caso sua issue realmente tenha algum fundamento);

- <b>Crie a seu Fork:</b> Depois que sua issue for aceita e atribuida a você, crie seu fork, trabalhe nela e envie suas alterações para seu fork;

- <b>Faça testes localmente: </b>
  - você precisa de um token. procure pelo usuário BotFather no telegram, envie /start e siga as instruções para criar um bot. 
  - Altere a valor de TELEGRAM_TOKEN em config/settings.py. por uma string com seu token. 
  - Em core.py, você deve comentar as linhas updater.start_webhook e updater.bot.setwbhook e adicionar updater.start_polling().
  - O bot que você acabou de criar agora é um clone do bender, faça os teste nele. 
  - Lembre-se de desfazer ou ignorar as alterações mencionada aqui no seu commit;

- <b>Faça uma Pull Request:</b> Terminado o trabalho com todas as suas modificações estando na sua branch do nosso repositório remoto, é hora de fazer a pull request e aguardar a revisão por parte dos membros da organização.
