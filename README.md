# Alura - Imersão Dados 3ª Edição

Repositório para conter os códigos criados durante a terceira edição 
da #imersaodados da #Alura.

## Aula 01: Análise de dados, python, pandas e novos fármacos

Nesta aula foi aprendido a se utilizar a biblioteca pandas para analisar dados 
a partir de uma fonte na internet.

Por meio da biblioteca foi possível analisar as colunas de dados, apresentando 
estes de forma visual ao se gerar gráficos de barras e/ou pizza.

Nesta análise inicial, descobrimos que os dados se referem a um estudo de novos 
fármacos, em que foram testados grupos com drogas e grupos de controle, que não 
receberam nenhuma droga.

:link: [Acesse o notebook da Aula 01](https://github.com/claudineipereira/alura-imersaodados3/blob/main/aula1.ipynb)

## Aula 02: Estatísticas, visualização de dados e distribuições

Nesta aula aprendemos a utilizar a biblioteca Seaborn para apresentar gráficos 
mais elaborados. Com ele conseguimos deixar nossos gráficos mais legíveis, 
manipulando configurações que impactam no tamanho do gráfico e das fontes 
das legendas

Aprendemos, também, a descrever nosso dataframe com o método describe, que 
retorna informações úteis como médias de valores, valores mínimos e máximos, etc.

Explorando um pouco mais o dataframe, aprendemos que as colunas nomeadas como *g* 
se referem à expressões genéticas e as nomeadas com *c* se referem a linhagens 
celulares nos quais foram testados os fármacos.

:link: [Acesse o notebook da aula 02](https://github.com/claudineipereira/alura-imersaodados3/blob/main/aula2.ipynb)

## Aula 3: Correlações, causalidade e relações entre genes

Nesta aula aprendemos a gerar tabelas de frequência utilizando tanto as 
funções *crosstab* quando *groupby*. Aprendemos, também a plotar gráficos de 
dispersão e de regressão linear com as funções do Seaborn *scatterplot* e 
*lmplot*, respectivamente.

Além disso, pudemos demonstrar a correlação entre expressões gênicas e 
tipos celulares por meio de um mapa de calor, fornecido pela função 
*heatmap* do Seaborn, que mostra correlações diretamente e inversamente 
proporcionais.

:link: [Acesse o notebook da aula 03](https://github.com/claudineipereira/alura-imersaodados3/blob/main/aula3.ipynb)

:link: [Visualização aprimorada do notebook da aula 03](https://nbviewer.jupyter.org/github/claudineipereira/alura-imersaodados3/blob/3518d5142ff6fec5708dbf67bb2e68abf9062193/aula3.ipynb)

## Aula 4: Merge e análise de resultados

Nesta aula passamos a trabalhar com dois dataframes. Além do dados dos 
experimentos, utilizado nas aulas anteriores, também utilizamos um 
dataframe com os dados dos resultados do estudo.

Aprendemos sobre os vários métodos de combinação de dados utilizando um 
específico, o *merge*, para criar um novo dataframe combinando os dados 
dos experimentos com o dos resultados.

A partir da combinação destes dados, descobrimos como os compostos 
utilizados nos experimentos se comportaram nas amostras, verificando 
se ativaram ou não algum mecanismo de ação.

Pudemos confirmar que os compostos de controle, sem princípio ativo, 
não ativaram nenhum mecanismo de ação, conforme esperado. Pudemos, 
também, verificar a proporção de ativação dos mecanismos de ação de 
compostos com princípio ativo.

:link: [Acesse o notebook da aula 04](https://github.com/claudineipereira/alura-imersaodados3/blob/main/aula4.ipynb)

:link: [Visualização aprimorada do notebook da aula 04](http://nbviewer.ipython.org/github/claudineipereira/alura-imersaodados3/blob/e44da65a90947e9e61720b07da6cd4c0a7242b39/aula4.ipynb)
