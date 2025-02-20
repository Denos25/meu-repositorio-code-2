def concatenar_dados():
  """
  Recebe dois dados diferentes do usuário e os concatena em uma única string.
  """

  # Recebe o primeiro dado do usuário
  dado1 = input("Digite o primeiro dado: ")

  # Recebe o segundo dado do usuário
  dado2 = input("Digite o segundo dado: ")

  # Concatena os dados
  string_concatenada = dado1 + " " + dado2

  # Imprime o resultado
  print("String concatenada:", string_concatenada)


# Chama a função para executar o programa
concatenar_dados()