**Código para monitorar ações na bolsa de valores**

Esse código em Python permite monitorar ações na bolsa de valores e salvar seus dados em arquivos de texto.

Instalação
Para executar o código, é necessário ter o Python instalado no seu computador. Caso não o tenha, pode fazer o download em https://www.python.org/downloads/.

Também é necessário instalar as seguintes bibliotecas:

requests
bs4 (beautifulsoup4)
Para instalar as bibliotecas, basta executar o seguinte comando no terminal:
pip install -r requirements.txt

**Como usar**

Para utilizar o código, basta executar o arquivo "monitorar_acoes.py" no terminal: python monitorar_acoes.py

O código irá fazer uma requisição no site "https://br.investing.com/equities/" e buscará as informações das ações presentes na tabela "cross_rate_markets_stocks_1".

Em seguida, para cada ação encontrada, o código criará um arquivo de texto com o nome da ação e seus dados, como nome, último valor, valor máximo, variação e valor de mercado.

Os arquivos de texto serão salvos no mesmo diretório onde o código está sendo executado.

**Observações**

O código utiliza a biblioteca "locale" para formatar os números no padrão brasileiro. É necessário ter o pacote de idioma "pt_BR.UTF-8" instalado no seu sistema para que o código funcione corretamente.