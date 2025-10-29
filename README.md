# Gerador de Senhas Seguras em Python

Um gerador de senhas simples e interativo feito em **Python**, desenvolvido para criar senhas seguras de forma rápida e personalizada. O programa permite escolher o tamanho, a quantidade e os tipos de caracteres usados nas senhas.

---

## Funcionalidades

*  Gera múltiplas senhas de uma só vez.
*  Permite definir o tamanho (comprimento) das senhas.
*  Permite escolher quais tipos de caracteres incluir:
    * Letras **maiúsculas (A-Z)**
    * Letras **minúsculas (a-z)**
    * **Números (0-9)**
    * **Símbolos** especiais (`!@#$%...`)
*  Interface de terminal (CLI) simples e intuitiva.
*  Utiliza o módulo `secrets` para geração criptograficamente segura, preferível ao módulo `random` para senhas.

---

## Tecnologias Utilizadas

* **Python 3**
* Módulos Nativos:
    * `secrets`: Para a geração segura de caracteres aleatórios.
    * `string`: Para obter os conjuntos de caracteres (letras, números, símbolos).
    * `os`: Para limpar a tela do terminal, melhorando a experiência de uso.

---

## Como Executar

### Pré-requisitos

* Você precisa ter o **Python 3.8+** instalado em sua máquina.

### Passos

1.  Clone este repositório (ou baixe os arquivos):
    ```bash
    git clone [https://github.com/](https://github.com/)[SEU-USUARIO]/gerador-senhas.git
    ```

2.  Navegue até o diretório do projeto:
    ```bash
    cd gerador-senhas
    ```

3.  Execute o script Python:
    ```bash
    python gerador_senhas.py
    ```

---

## Exemplo de Uso

Ao executar o script, você verá a seguinte interface:

## Exemplo de Uso

Ao executar o script, você verá a seguinte interface:

```plaintext
=========================================
   Gerador de Senhas Seguras em Python
=========================================

Qual o tamanho da senha desejada? 12
Quantas senhas você deseja gerar? 3

--- Escolha os tipos de caracteres ---
Incluir letras maiúsculas (A-Z)? (s/n): s
Incluir letras minúsculas (a-z)? (s/n): s
Incluir números (0-9)? (s/n): s
Incluir símbolos (!@#$%)? (s/n): n

=========================================
      Senhas Geradas com Sucesso!
=========================================

Senha 1: Lp4kzQ7cJd2r  
Senha 2: Hz5qRm9Bt1Lf  
Senha 3: Qj2sWp8Dz6xH

Lembre-se de salvar suas senhas em um local seguro!
=========================================
