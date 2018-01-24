# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def filter_data(data, condition):
    """
    Remove os elementos que não correspondem a condicao fornecida.
    Pega uma lista de dados como entrada e retorna uma lista filtrada.
    As condicoes devem ser uma lista de cadeias do seguinte formato:
      '<field> <op> <value>'
    onde as seguintes operacoes sao validas: >, <, >=, <=, ==, !=
    
    Exemplo: ["duration < 15", "start_city == 'San Francisco'"]
    """

    # Separa nos primeiros dois espaços separando o campo e a operação e operação do valor.
    # operator from value: spaces within value should be retained.
    field, op, value = condition.split(" ", 2)
    
    # verifica se o campo é válido
    if field not in data.columns.values :
        raise Exception(u"'{}' não é uma coluna do DataFrame. Por acaso você escreveu de maneira errada?".format(field))

    # converte o numero em float e tira aspas adicionais
    try:
        value = float(value)
    except:
        value = value.strip("\'\"")

    # cria o vetor de booleans para filtrar as linhas
    if op == ">":
        matches = data[field] > value
    elif op == "<":
        matches = data[field] < value
    elif op == ">=":
        matches = data[field] >= value
    elif op == "<=":
        matches = data[field] <= value
    elif op == "==":
        matches = data[field] == value
    elif op == "!=":
        matches = data[field] != value
    else: # pega códigos inválidos
        raise Exception("Invalid comparison operator. Only >, <, >=, <=, ==, != allowed.")
    
    # filtra os dados e retorna
    data = data[matches].reset_index(drop = True)
    return data

def usage_stats(data, filters = [], verbose = True):
    """
    Relata o numero de viagens e a duração media da viagem para pontos de dados que se encontram
    nos criterios de filtragem especificados.
    """

    n_data_all = data.shape[0]

    # aplica o filtro aos dados
    for condition in filters:
        data = filter_data(data, condition)

    # Calcula o número de linhas que corresponde ao filtro
    n_data = data.shape[0]

    # Calcula estatísticas para o campo duração
    duration_mean = data['duration'].mean()
    duration_qtiles = data['duration'].quantile([.25, .5, .75]).as_matrix()
    
    # Reporta as estatísticas computadas se o parâmetro verbosity está definido como True
    if verbose:
        if filters:
            print(
                u'Existem {:d} pontos ({:.2f}%) se enquadram nos critérios de filtros'.format(n_data, 100. * n_data / n_data_all))
        else:
            print('Existem {:d} pontos no conjunto de dados'.format(n_data))

        print(u'A duração média das viagens foi de {:.2f} minutos'.format(duration_mean))
        print(u'A mediana das durações das viagens foi de {:.2f} minutos'.format(duration_qtiles[1]))
        print(u'25% das viagens foram mais curtas do que {:.2f} minutos'.format(duration_qtiles[0]))
        print(u'25% das viagens foram mais compridas do que {:.2f} minutos'.format(duration_qtiles[2]))
        
    # retorna o resumo com três números
    return duration_qtiles


def usage_plot(data, key = '', filters = [], **kwargs):
    """
    Plota numero de viagens, dada uma caracteristica de interesse e qualquer numero 
    de filtros (incluindo sem filtros). A funcao aceita uma serie de argumentos opcionais 
    para desenhar o grafico dos dados em variaveis continuas:
      - n_bins: numero de barras (padrao = 10)
      - bin_width: largura de cada barra (por padrao dividira o total de dados pelo numero de barras). 
      "n_bins" e "bin_width" nao podem ser usados em conjunto.
      - boundary: especifica onde as bordas do grafico serao colocadas; outras bordas
      serao colocados em volta deste valor (pode causar em uma barra adicional). Pode ser usada com
      "n_bins" e "bin_width".
    """
    
    # Check that the key exists
    if not key:
        raise Exception(u"Nenhuma chave foi dada. Tenha certeza que você passou uma variavel que sera usada para fazer o grafico.")
    if key not in data.columns.values :
        raise Exception(u"'{}' nao e uma caracteristica do dataframe. Você digitou alguma coisa errada?".format(key))

    # Apply filters to data
    for condition in filters:
        data = filter_data(data, condition)

    # Create plotting figure
    plt.figure(figsize=(8,6))

    if isinstance(data[key][0] , str): # Categorical features
        # For strings, collect unique strings and then count number of
        # outcomes for survival and non-survival.
        
        # Summarize dataframe to get counts in each group
        data['count'] = 1
        data = data.groupby(key, as_index = False).count()
        
        levels = data[key].unique()
        n_levels = len(levels)
        bar_width = 0.8
        
        for i in range(n_levels):
            trips_bar = plt.bar(i - bar_width/2, data.loc[i]['count'], width = bar_width)
        
        # add labels to ticks for each group of bars.
        plt.xticks(range(n_levels), levels)
        
    else: # Numeric features
        # For numbers, divide the range of data into bins and count
        # number of outcomes for survival and non-survival in each bin.
        
        # Set up bin boundaries for plotting
        if kwargs and 'n_bins' in kwargs and 'bin_width' in kwargs:
            raise Exception(u"Argumentos 'n_bins' e 'bin_width' não podem ser usados juntos.")

        min_value = data[key].min()
        max_value = data[key].max()
        value_range = max_value - min_value
        n_bins = 10
        bin_width = float(value_range) / n_bins

        if kwargs and 'n_bins' in kwargs:
            n_bins = int(kwargs['n_bins'])
            bin_width = float(value_range) / n_bins
        elif kwargs and 'bin_width' in kwargs:
            bin_width = kwargs['bin_width']
            n_bins = int(np.ceil(float(value_range) / bin_width))
        
        if kwargs and 'boundary' in kwargs:
            bound_factor = np.floor(( min_value - kwargs['boundary'] ) / bin_width)
            min_value = kwargs['boundary'] + bound_factor * bin_width
            if min_value + n_bins * bin_width <= max_value:
                n_bins += 1

        bins = [i*bin_width + min_value for i in range(n_bins+1)]
        
        # plot the data
        plt.hist(data[key], bins = bins)

    # Common attributes for plot formatting
    key_name = ' '.join([x.capitalize() for x in key.split('_')])
    plt.xlabel(key_name)
    plt.ylabel(u"Número de Viagens")
    plt.title(u"Número de Viagens por {:s}".format(key_name))
    plt.show()