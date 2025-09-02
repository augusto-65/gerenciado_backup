#janela para selecionar a pasta de origem
import os
import tkinter
import shutil

from tkinter.filedialog import askdirectory

nome_pasta_selecionada = askdirectory()
print(nome_pasta_selecionada)

lista_arquivos = os.listdir(nome_pasta_selecionada)
print(lista_arquivos)

#criar pasta para backup
nome_pasta_backup = "backup"
nome_completo_pasta_backup = f"{nome_pasta_selecionada}/{nome_pasta_backup}"
if not os.path.exists(nome_completo_pasta_backup):
    os.mkdir(nome_completo_pasta_backup)

#fazer o backup dos arquivos que estão na pasta
for arquivo in lista_arquivos:
    print(arquivo)
    nome_completo_arquivo = f"{nome_pasta_selecionada}/{arquivo}"
    nome_final_arquivo = f"{nome_completo_pasta_backup}/{arquivo}"
    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
    elif "backup" != arquivo:
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)