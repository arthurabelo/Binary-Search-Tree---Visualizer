# Binary Search Tree Application

- Esta aplicação é uma interface gráfica para manipulação de uma Árvore Binária de Busca (BST). Através dela, é possível inserir, deletar, carregar e exportar dados, além de visualizar informações e travessias da árvore.

## Arquivos Principais

- **main.py**: Contém a lógica da interface gráfica e as funcionalidades principais da aplicação.
- **src/BST.py**: Implementa a estrutura de dados da Árvore Binária de Busca (BST).

## Funcionalidades

### Inserir Nome
Adiciona um novo nome à BST.

### Apagar Nome
Remove um nome existente da BST.

### Carregar entrada.txt
Carrega os nomes do arquivo entrada.txt e insere-os na BST.

### Exportar
Exporta os nomes da BST para o arquivo entrada.txt.

### Mostrar Informações
Exibe informações detalhadas sobre a BST, como tamanho, altura, valor mínimo e máximo, nós folhas, comprimento interno e se a árvore está balanceada.

### Mostrar Travessias
Exibe as travessias da BST.

### Resetar Zoom
Reseta o zoom da visualização da árvore.

## Como Usar

### Requisitos

- Python 3.x
- Tkinter
- MatPlotLib

### Estrutura de Código
#### main.py
##### Classe App
- **create_widgets**: Cria os widgets da interface.
- **abrir_entrada**: Carrega os dados do arquivo entrada.txt.
- **exportar_entrada**: Exporta os dados da BST para o arquivo entrada.txt.
- **zoom**: Controla o zoom da visualização da árvore.
- **start_drag e dragging**: Permitem arrastar a visualização da árvore.
- **insert_name e delete_name**: Inserem e deletam nomes na BST.
- **show_info**: Exibe informações detalhadas sobre a BST.
- **show_traversals**: Exibe as travessias da BST.
- **reset_zoom**: Reseta o zoom da visualização.
- **draw_tree**: Desenha a árvore no canvas.
### Exemplos de Uso
#### Inserir Nome:

- Digite um nome no campo de entrada e clique em "Inserir".
#### Apagar Nome:

- Digite um nome no campo de entrada e clique em "Apagar".
#### Carregar entrada.txt:

- Clique em "Carregar entrada.txt" para carregar os nomes do arquivo.
#### Exportar:

- Clique em "Exportar" para salvar os nomes da BST no arquivo entrada.txt.
#### Mostrar Informações:

- Clique em "Mostrar informações" para visualizar detalhes da BST.
#### Mostrar Travessias:

- Clique em "Mostrar travessias" para visualizar as travessias da BST.