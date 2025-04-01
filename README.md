
# Projeto Prático de Conectivos Lógicos em Python

## Descrição

Este projeto tem como objetivo reforçar o entendimento dos conectivos lógicos (AND, OR, NOT) em Python através de exercícios práticos e interativos. Cada exercício utiliza uma biblioteca diferente para tornar o aprendizado mais dinâmico e explorar as possibilidades da linguagem.

## Instruções

Siga as instruções abaixo para configurar o ambiente, completar os exercícios e submeter suas soluções.

### 1. Clonar o Repositório

Primeiro, clone este repositório para o seu ambiente local utilizando o seguinte comando no terminal:

```bash
git clone https://github.com/renan-dias/md0104.git
```



### 2. Criar um Ambiente Virtual (Recomendado)

É altamente recomendado criar um ambiente virtual para isolar as dependências do projeto do seu ambiente Python global. Siga os passos abaixo:

*   **Linux/macOS:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

*   **Windows:**

    ```bash
    python -m venv venv
    venv\Scripts\activate.bat
    ```

*Após a ativação, você verá `(venv)` no início da linha de comando, indicando que o ambiente virtual está ativo.*

### 3. Instalar as Dependências

Utilize o arquivo `requirements.txt` para instalar as bibliotecas necessárias para o projeto. Certifique-se de que o ambiente virtual está ativo e execute o seguinte comando:

```bash
pip install -r requirements.txt
```

*Este comando instalará automaticamente as bibliotecas `Pillow` e `pygame`.*

### 4. Executar e Modificar os Exercícios

Cada exercício possui um arquivo Python individual com um nome descritivo. Execute cada arquivo e siga as instruções no código para implementar o conectivo lógico faltante. Os comentários no código indicam claramente onde a modificação deve ser feita.

Exemplo de execução (substitua `nome_do_exercicio.py` pelo nome do arquivo do exercício):

```bash
python nome_do_exercicio.py
```

### 5. Testar e Validar

Após implementar o conectivo lógico, teste o código com diferentes entradas para garantir que a lógica esteja correta e que o programa se comporta conforme o esperado.

### 6. Criar uma Nova Ramificação (Branch)

Antes de fazer qualquer alteração, crie uma nova ramificação (branch) para trabalhar nas suas soluções. Isso evita conflitos com o código principal e facilita o processo de revisão.

```bash
git checkout -b sua-ramificacao
```

*Substitua `sua-ramificacao` por um nome descritivo ou seu nome, para sua ramificação (por exemplo, `resolução-renan`).*

### 7. Commit e Push das Alterações

Depois de completar um exercício e testar a sua solução, adicione as mudanças ao Git, faça o commit e envie para o repositório remoto.

```bash
git add .
git commit -m "Solução para o Exercício [Número do Exercício]"
git push origin sua-ramificacao
```

*Substitua `[Número do Exercício]` pelo número do exercício que você resolveu e `sua-ramificacao` pelo nome da ramificação que você criou.*

### 8. Criar um Pull Request

Após enviar suas alterações para o repositório remoto, crie um Pull Request (PR) para que seus códigos sejam revisados e integrados ao código principal.

1.  Acesse o repositório no GitHub.
2.  Você deverá ver um botão para criar um Pull Request relacionado à sua ramificação.
3.  Clique no botão e siga as instruções para criar o PR.
4.  Adicione uma descrição detalhada das suas mudanças e envie o PR.

## Exercícios

Abaixo estão os enunciados de cada exercício para sua referência:

### Exercício 1: Validação de Senha com Tkinter

Crie uma interface gráfica simples com Tkinter que solicita ao usuário uma senha e verifica se ela atende a dois critérios: ter pelo menos 8 caracteres e conter pelo menos um número. Use os conectivos lógicos para combinar as condições.

*   Arquivo: `senha.py`

### Exercício 2: Jogo de Adivinhação com Pygame

Crie um jogo simples com Pygame onde o jogador deve adivinhar um número entre 1 e 100. Forneça dicas ao jogador se o palpite for muito alto OU muito baixo.

*   Arquivo: `adivinhacao.py`

### Exercício 3: Verificação de Desconto com Condicionais

Uma loja oferece desconto se o cliente for um membro do clube OU se a compra for acima de R$100. Implemente a lógica para verificar se o cliente tem direito ao desconto.

*   Arquivo: `desconto.py`

### Exercício 4: Validação de Entrada com Negação

Crie uma função que valida se uma entrada do usuário é um número inteiro positivo. Use a negação para simplificar a lógica.

*   Arquivo: `validacao.py`

### Exercício 5: Combinação de Condições com AND e NOT

Uma pessoa pode dirigir se tiver 18 anos ou mais E não estiver com a CNH suspensa. Implemente a lógica para verificar se a pessoa pode dirigir.

*   Arquivo: `dirigir.py`

## Observações

*   Cada exercício foi projetado para ser simples e focado no uso dos conectivos lógicos.
*   Os comentários no código indicam onde você deve adicionar o conectivo lógico correto.
*   Sinta-se à vontade para modificar e expandir os exercícios como desejar.
*   Lembre-se de testar os códigos com diferentes entradas para garantir a correção da lógica implementada.
*   Divirta-se e bom aprendizado!


**Observações:**

*   Substitua `[URL_DO_REPOSITÓRIO]` pela URL real do seu repositório no GitHub.
*   Certifique-se de que o arquivo `requirements.txt` está presente no seu repositório.
*   Adapte os nomes das ramificações e as mensagens de commit de acordo com suas necessidades.
*   Incentive seus alunos a fazer commits frequentes com mensagens descritivas.
*   Revise os Pull Requests com atenção, fornecendo feedback construtivo e dicas de melhoria.

Este formato é equivalente ao Markdown, mas apresentado como texto, o que pode facilitar a cópia e colagem em um arquivo README.md.  Se você colar isso em um arquivo README.md, ele se formatará corretamente.
