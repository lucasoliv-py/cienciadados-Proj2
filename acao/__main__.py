"""
Módulo Principal
Descrição: Este é o módulo principal do Aplicativo de Modelagem do Mercado de Ações na B3.
Autores: Lucas Oliveira e Sheila Avila
Versão: 0.0.1
Data: 04/12/2023

"""



# Importação dos módulos

import es
from proc import Acao


# Definindo as funções

def main():
    # Leitura de dados
    dados = es.leitora()
    
    # Instanciamento do objeto
    acao = Acao(dados[0], dados[1])
    
    # Saída de dados
    es.impressora(acao)
    
    

if __name__ == "__main__":
    main()
    