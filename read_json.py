# Adicione ao repositório um script em Python (read_json.py) que receba o caminho para um ficheiro JSON e depois imprima os resultados com base na tabela abaixo - e com a prioridade definida na tabela.
# Tem que se dar o path DIRETO para o Python em si para funcionar... (Python\Python313\python.exe) :/
import json
import sys
import os

filepath = sys.argv[1] if len(sys.argv) > 1 else None

def end(msg):
    print(msg)
    print("Processo Concluído!")
    exit()

if not filepath or not os.path.exists(filepath):
    end("Erro: Ficheiro Não Encontrado!")

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read().strip()

if content == "":
    end("Erro: Ficheiro Vazio!")

try:
    data = json.loads(content)
except:
    end("Erro: Ficheiro Não Contém JSON Válido!")

required = ["nome", "idade", "localização"]
if not all(k in data for k in required):
    end("Erro: Campos Obrigatórios em Falta!")

print(data)
print("Processo Concluído!")
