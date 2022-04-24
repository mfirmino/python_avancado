from datetime import date

data_atual = date.today()
print(data_atual)

#formatando modo rústico
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)
print(data_em_texto)

#método nativo próprio
data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)

#para datas e horários
from datetime import datetime, timezone, timedelta
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_em_texto)

data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')
print(data_e_hora)

#timezone
diferenca = timedelta(hours=-3)
print(diferenca)
fuso_horario = timezone(diferenca)
print(fuso_horario)

#Padronizando datas com timezone:
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)