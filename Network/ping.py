import platform
import subprocess
from datetime import datetime
import time

# Função que pinga o servidor da google e retorna um bool se estiver on ou não
def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False


dt = datetime.now() 
nome_arquivo = "pings"
hora = str(dt.strftime('%d_%m_%y_%H_%M_%p'))
extensao = ".txt"
completo = nome_arquivo + hora + extensao
arquivo = open(completo, 'w+')
arquivo.close()

while True:
    dt = datetime.now()
    arquivo = open(completo, 'r')
    conteudo = arquivo.readlines()
    conteudo.append(f'{myping("8.8.8.8")}_{dt.strftime("%d/%m/%y %H:%M:%S %p")}\n')
    arquivo = open(completo, 'w+')
    arquivo.writelines(conteudo)
    arquivo.close()
    time.sleep(1)
