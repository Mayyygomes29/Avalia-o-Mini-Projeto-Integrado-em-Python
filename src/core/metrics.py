import pandas as pd 
from functools import reduce

def analyze(df: pd.DataFrame, limite= 10) -> dict:
    even_numbers = list(filter(lambda x: x % 2 == 0 and x > limite, df['quantidade']))
    squared = list(map(lambda x: x**2, df['quantidade']))
    sum, count = list(reduce(lambda a, b: (a[0]+b, a[1]+1) , squared, (0,0)))
    media = sum // count 
    resumo = df.describe().to_dict()
        

    return {'números pares de qtd': even_numbers,
            'números elevado ao quadrado de qtd': squared,
            "media_inteira": media,
            'soma_quadrados': sum,
            'contagem': count, 
            'RESUMO': resumo }
   


