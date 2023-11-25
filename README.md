# Verificador de dados com Python

Projeto em Python de um verificador de dados em um buffer de armazenagem.

## Resumo/Apresentação do Projeto

Uma aplicação feita em Python, para obter dados de 2 fontes distintas e comparar a equidade das mesmas, sendo capaz de gerar um resumo apontando onde estão as diferenças e os valores registrados. Esses dados são os números de produção de produtos armazenados em um buffer industrial de peças.

## Objetivo final do projeto

Possibilitar aos interessados, encontrar em quais posições do buffer, possam existir divergências entre os dados salvos na camada de T.I. e os dados salvos na camada de T.A., auxiliando e diminuindo o tempo necessário para possíveis correções e qual método de correção será necessário para sanar as divergências caso encontradas.

## Requisitos básicos importantes

O app Python:

- Deverá ser executável sem necessidade de ser instalado
- Precisará funcionar no modo “janela” utilizando biblioteca de janelas `Tkinter`
- Ter interface o mais simples possível e estável. Seguindo ideia de “_Click and Go. If it fails, show me why_.”

## Informações adicionais

- Serão duas fontes de dados. Um CLP _Siemens_ _319F_ e uma página web no seguinte endereço (`url dos mapas sem necessidade de autenticação`)
- Na página web será necessário fazer `web scraping` com a biblioteca `BeautifulSoup` para obter os números de produto armazenado nas respectivas posições (andar / coluna / lado 1 ou 2)
- Para obter os dados do CLP, será necessário utilizar a biblioteca Python-snap7 e apontar para cada uma das posições do buffer de maneira individual e obter os dados. É recomendável criar um laço de repetição porém não “bombardear” o CLP com requisições, criando um tempo de espera entre uma e outra
- Com ambos os dados obtidos, será necessário fazer um verificação em cada posição do buffer e identificar se os dados que foram obtidos da camada de tecnologia da informação estão iguais com os dados obtidos do CLP na camada de tecnologia da automação. Conforme forem encontradas divergências, gerar um resumo simples e direto ao ponto mostrando qual posição e os valores em ambas fontes. Dessa maneira, torna mais simples e direta a tarefa de verificar qual dado está correto e então buscar pela melhor forma de correção.
