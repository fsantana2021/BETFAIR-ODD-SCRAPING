
from datetime import datetime
import pytz

hora_data_local = datetime.now()
fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
formato_desejado = "%d-%m-%Y %H-%M-%S"
data_hora_formatada = hora_data_local.strftime(formato_desejado)
print(data_hora_formatada)