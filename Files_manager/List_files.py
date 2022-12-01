from logging import root
import os
from datetime import datetime

dt = datetime.now()
hora = str(dt.strftime('%d_%m_%y_%H_%M_%p'))
nome_arquivo = f'directories_{hora}.txt'
arquivo = open(nome_arquivo, 'w+')
arquivo.close()

for (root, dir, files) in os.walk("C:/Users/HM-admin/",topdown=True):
    for directories in dir:
        arquivo = open(nome_arquivo, 'r')
        conteudo = arquivo.readlines()
        conteudo.append(directories + '\n')
        arquivo = open(nome_arquivo, 'w+')
        arquivo.writelines(conteudo)
        arquivo.close()
        print(directories)
