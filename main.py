from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

message = client.messages \
                .create(
                     body="Olá meu nome é Jonas Moreira Barbosa e estou participando do PROGRAMA DE ESTÁGIO TALENT LAB ITACOATIARA.",
                     from_='+12052739236',
                     to='+5592994041016'
                 )
print(f"Mensagem Enviada com Sucesso!\nID:{message.sid}")