import os
import pandas as pd
import json
from src.core.metrics import analyze

def open_csv(): 
    file_csv = 'C:/Users/55219/Downloads/pós/python 2/trab final/data/vendas.csv'
    df = pd.read_csv(file_csv, sep=";", encoding="utf-8")
    df['valor_total'] = df['quantidade'] * df['valor_unitario']
    stats = analyze(df)
    caminho = os.path.join('C:/Users/55219/Downloads/pós/python 2/trab final', 'stats.json')
    with open(caminho, 'w', encoding='utf-8') as f:
       return json.dump(stats, f, indent=4, ensure_ascii=False)

    

    
if __name__ == '__main__':
    open_csv()