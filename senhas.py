import secrets
import string
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_numero(prompt: str) -> int:
    while True:
        try:
            numero = int(input(prompt))
            if numero > 0:
                return numero
            else:
                print("Erro: Por favor, insira um número maior que zero.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número inteiro.")

def obter_sim_ou_nao(prompt: str) -> bool:
    while True:
        resposta = input(prompt).lower().strip()
        if resposta in ['s', 'sim']:
            return True
        elif resposta in ['n', 'nao', 'não']:
            return False
        else:
            print("Erro: Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

def gerar_senhas(tamanho: int, quantidade: int, tipos_caracteres: str) -> list[str]:

    senhas_geradas = []
    for _ in range(quantidade):
        senha = ''.join(secrets.choice(tipos_caracteres) for i in range(tamanho))
        senhas_geradas.append(senha)
    return senhas_geradas

def main():
    limpar_tela()
    print("=========================================")
    print("   Gerador de Senhas Seguras em Python   ")
    print("=========================================\n")

    tamanho = obter_numero("Qual o tamanho da senha desejada? ")
    quantidade = obter_numero("Quantas senhas você deseja gerar? ")
    
    print("\n--- Escolha os tipos de caracteres ---")
    incluir_maiusculas = obter_sim_ou_nao("Incluir letras maiúsculas (A-Z)? (s/n): ")
    incluir_minusculas = obter_sim_ou_nao("Incluir letras minúsculas (a-z)? (s/n): ")
    incluir_numeros = obter_sim_ou_nao("Incluir números (0-9)? (s/n): ")
    incluir_simbolos = obter_sim_ou_nao("Incluir símbolos (!@#$%)? (s/n): ")

    caracteres_permitidos = ""
    if incluir_maiusculas:
        caracteres_permitidos += string.ascii_uppercase
    if incluir_minusculas:
        caracteres_permitidos += string.ascii_lowercase
    if incluir_numeros:
        caracteres_permitidos += string.digits
    if incluir_simbolos:
        caracteres_permitidos += string.punctuation

    if not caracteres_permitidos:
        print("\nErro: Nenhuma opção de caractere foi selecionada. Não é possível gerar a senha.")
        return

    try:
        senhas = gerar_senhas(tamanho, quantidade, caracteres_permitidos)
        
        limpar_tela()
        print("\n=========================================")
        print("          Senhas Geradas com Sucesso!      ")
        print("=========================================\n")
        
        for i, senha in enumerate(senhas, 1):
            print(f"  Senha {i}: {senha}")
        
        print("\nLembre-se de salvar suas senhas em um local seguro!")
        print("=========================================")

    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao gerar as senhas: {e}")

if __name__ == "__main__":
    main()
