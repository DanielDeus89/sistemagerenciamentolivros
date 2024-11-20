# Sistema de Gerenciamento de Livros

 Atividade: Sistema de Gerenciamento de Livros

Crie um programa que gerencie uma lista de livros. O programa deve oferecer as seguintes opções no menu:

 Funcionalidades do Sistema
1. Cadastrar novo livro:
   - Solicite o nome do livro, o autor e o ano de publicação.
   - Verifique se o nome do livro já está cadastrado (não permita duplicatas).
   - Certifique-se de que o ano é um número válido.

2. Listar livros cadastrados:
   - Exiba todos os livros em uma tabela formatada com as colunas:
     - Nome do Livro
     - Autor
     - Ano de Publicação

3. Atualizar informações de um livro:
   - Solicite o nome do livro.
   - Permita alterar o autor e/ou o ano de publicação.

4. Excluir um livro:
   - Solicite o nome do livro a ser excluído.
   - Remova-o da lista, caso exista.

5. Sair do programa:
   - Finalize o programa exibindo uma mensagem de despedida.

---

 Regras
- Use uma lista para armazenar os livros no formato:
  python
  {'nome': 'O Pequeno Príncipe', 'autor': 'Antoine de Saint-Exupéry', 'ano': 1943}
  
- Valide as entradas do usuário:
  - O nome do livro não pode estar vazio.
  - O ano de publicação deve ser um número válido e positivo.
- Se a lista estiver vazia, exiba uma mensagem apropriada ao listar ou excluir livros.

---

 Estrutura do Menu
O menu deve ser exibido repetidamente até que o usuário escolha sair. Exemplo:


██████████████████████████████████
      GERENCIAMENTO DE LIVROS
██████████████████████████████████

1. Cadastrar novo livro
2. Listar livros cadastrados
3. Atualizar informações de um livro
4. Excluir um livro
5. Sair

Escolha uma opção: _

Exemplo de Saída

Cadastro de Livro

Digite o nome do livro: O Pequeno Príncipe
Digite o autor do livro: Antoine de Saint-Exupéry
Digite o ano de publicação: 1943

✅ O livro 'O Pequeno Príncipe' foi cadastrado com sucesso!


 Listagem

📚 Lista de Livros Cadastrados
Nome do Livro           | Autor                      | Ano de Publicação
----------------------------------------------------------------------
O Pequeno Príncipe      | Antoine de Saint-Exupéry   | 1943


 Atualização

Digite o nome do livro que deseja atualizar: O Pequeno Príncipe
Digite o novo autor (ou pressione Enter para manter o atual): Antoine de Saint-Exupéry
Digite o novo ano de publicação (ou pressione Enter para manter o atual): 2000

✅ As informações do livro 'O Pequeno Príncipe' foram atualizadas com sucesso!


 Exclusão

Digite o nome do livro que deseja excluir: O Pequeno Príncipe

✅ O livro 'O Pequeno Príncipe' foi excluído com sucesso!

 Dica para Começar
1. Organize cada funcionalidade em uma função separada.
2. Use um loop para exibir o menu até que o usuário escolha sair.
3. Teste cada funcionalidade com entradas válidas e inválidas.

