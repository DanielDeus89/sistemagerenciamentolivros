from fileinput import lineno

livros = [{'titulo': 'daniel', 'autor': 'daniel', 'ano_publicacao': 1111},{'titulo': 'Heitor', 'autor': 'Heitor', 'ano_publicacao': 1111}]

def exibir_opcoes():
    print('1. Cadastrar novo livro')
    print('2. Listar livros cadastrados')
    print('3. Atualizar informações de um livro')
    print('4. Excluir um livro')
    print('5. Sair')

def cadastrar_livro():
    while True:
        # Validação do título do livro
        titulo = input('Digite o título do livro: ').strip()
        if not titulo:
            print('❌ O título do livro não pode estar vazio! Tente novamente.')
            continue


        # Verificar duplicatas
        for livro in livros:
            if livro['titulo'].lower() == titulo.lower():
                print('❌ Este título já está cadastrado! Tente outro.')
                cadastrar_livro()
                break
        else:  # Executa apenas se o loop não encontrar duplicatas
            break

    # Validação do autor do livro
    while True:
        autor = input('Digite o autor do livro: ').strip()
        if not autor:
            print('❌ O autor do livro não pode estar vazio! Tente novamente.')
            continue
        break

    # Validação do ano de publicação
    while True:
        ano_publicacao = input('Digite o ano de publicação: ').strip()
        if not ano_publicacao.isdigit() or int(ano_publicacao) <= 0 or len(ano_publicacao) > 4:
            print('❌ O ano de publicação deve ser um número positivo válido! Tente novamente.')
            continue
        ano_publicacao = int(ano_publicacao)
        break

    # Armazenar o livro na lista
    dados_do_livro = {'titulo': titulo, 'autor': autor, 'ano_publicacao': ano_publicacao}
    livros.append(dados_do_livro)

    print(f"\n✅ O título '\033[92m{titulo.upper()}\033[0m' foi cadastrado com sucesso!")

    # Perguntar se deseja cadastrar outro livro
    while True:
        continuar = input('Deseja cadastrar outro título? (s/n) ').strip().lower()
        if continuar in ['s', 'n']:
            break
        print('❌ Opção inválida! Digite "s" para Sim ou "n" para Não.')

        if continuar == 'n':
            break
        else:
            print('\n👍 Cadastro concluído! Retornando ao menu principal...')
            return

def listar_livros():
    print('📚 Lista de Livros Cadastrados')
    print('-'*65)
    if not livros:
        print("❌ Nenhum titulo cadastrado ainda.")
        return

    print(f"{'Título'.ljust(20)} | {'Autor'.ljust(20)} | {'Ano de Publicação'}")
    print('-' * 65)

    for livro in livros:
        titulo = livro['titulo']
        autor = livro['autor']
        ano_publicacao = livro['ano_publicacao']

        print(f"{titulo.ljust(20)} | {autor.ljust(20)} | {ano_publicacao}")


def atualizar_info():
    titulo = input('Digite o nome do livro que deseja atualizar: ').strip()
    for livro in livros:
        if livro['titulo'].lower() == titulo.lower():
            print(f"\nInformações atuais do livro: {livro}")

        novo_autor = input(f'Digite o novo autor (ou pressione Enter para manter o atual): ')
        if novo_autor:
            livro['autor']=novo_autor


        novo_ano_publicacao = int(input('Digite o novo ano de publicação (ou pressione Enter para manter o atual):'))
        if novo_ano_publicacao > 0:
            livro['ano_publicacao'] = int(novo_ano_publicacao)

        print(f"\n✅ As informações do livro '{livro['titulo']}' foram atualizadas com sucesso!")

        return

    print(f"❌ Livro '{titulo}' não encontrado.")


def excluir_titulo():
    titulo = print(input('Digite o nome do livro que deseja excluir: '))
    for i, livro in enumerate(livros):
        livros.pop(i)
        print(f"\n✅ O aluno {livro['titulo']} foi excluído com sucesso!")
        return


def main():
    while True:
        print()
        exibir_opcoes()
        try:
            opcao = int(input('Escolha uma opção: _ '))
            print('')
            if opcao == 1:
                cadastrar_livro()
            elif opcao == 2:
                listar_livros()
            elif opcao == 3:
                atualizar_info()
            elif opcao == 4:
                excluir_titulo()

            elif opcao == 5:
                print("\n👍 Saindo do sistema...")
                break
            else:
                print('❌ Opção inválida. Escolha entre 1 e 5.')
        except ValueError:
            print('❌ Insira um número válido.')

if __name__ == '__main__':
    main()