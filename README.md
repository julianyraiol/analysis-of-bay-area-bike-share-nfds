# Análise de dados da Bay Area Bike Share

A Bay Area Bike Share é uma empresa que oferece aluguel de bicicletas a clientes em São Francisco, Redwood City, Palo Alto, Mountain View e San Jose. Os usuários podem desbloquear bicicletas de diversas estações em cada cidade e devolvê-las em qualquer estação dentro da mesma cidade. O serviço é pago por meio de assinatura anual ou pela compra de passes de três dias ou 24 horas. Os usuários podem fazer um número ilimitado de viagens. Viagens com menos de trinta minutos de duração não terão custo adicional; viagens mais longas incorrerão em taxas de horas extras.

Neste projeto, você se colocará no lugar de um analista para realizar uma análise exploratória dos dados. Você analisará duas das principais partes do processo de análise de dados: limpeza de dados e análise exploratória. Mas, antes de começar a análise, pense em algumas perguntas que você pode querer fazer sobre os dados. Por exemplo, se você estivesse trabalhando para a Bay Area Bike Share, que tipo de informação gostaria de ter a fim de tomar decisões de negócios mais inteligentes? Ou você pode pensar como você fosse um usuário. Que fatores podem influenciar a maneira como você gostaria de usar o serviço?

Ao final deste projeto, você será capaz de identificar as principais etapas do processo de análise de dados. Ele é projetado para ajudá-lo a tomar uma decisão informada sobre este tipo de trabalho.

Além de praticar os conhecimentos, você também entenderá o processo de envio do projeto e o tipo de feedback que você pode esperar de seu revisor.


### Estrutura do projeto

Este projeto foi divido em 3 pastas principais:

* **data**: todos os datasets do projeto
* **libs**: todas as bibliotecas do projeto
* **notebook**: todos os notebooks do projeto

```
|-- README.md
|
|-- data
|   |-- *_trip_*.csv
|   |-- *_station_*.csv
|   |-- *_weather_*.csv
|-- libs
|   |-- babs_datacheck.py
|   |-- babs_visualizations.py
|-- notebooks
|   |-- Analise_Bay_Area_Bike_Share-NDFDSI.ipynb
|   
`-- requirements.txt
```

### Ambiente de Desenvolvimento

Esta análise foi realizada em Python 3.7.

```bash
$ git clone https://github.com/julianyraiol/analysis-of-bay-area-bike-share-nfds.git
$ cd analysis-of-bay-area-bike-share-nfds
```

Para instalar os pacotes, utilize o *pip*:

`$ pip install -r requirements.txt`

### Executar

Na linha de comando do terminal, execute seguinte comando:

```bash
$ cd analysis-of-bay-area-bike-share-nfds
$ jupyter notebook
```

* \*\_README.txt - Informações sobre o conteúdo do csv.

* \*\_station\_data.csv - Informações básicas sobre os locais de estação e capacidade.

* \*\_trip\_data.csv - Informações sobre cada viagem usando o sistema de empréstimo de bicicletas.

* \*\_weather\_data.csv - Informação meteorológica por dia para uma estação em cada cidade no programa de empréstimo de bicicletas.
