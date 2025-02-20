def repetir_string(string, numero_vezes):
  """
  Repete uma string um determinado número de vezes.

  Args:
    string: A string a ser repetida.
    numero_vezes: O número de vezes que a string deve ser repetida (inteiro).

  Returns:
    A string repetida o número de vezes especificado. Retorna None se a entrada
    não for válida.
  """
  if not isinstance(string, str):
    print("Erro: O primeiro argumento deve ser uma string.")
    return None

  if not isinstance(numero_vezes, int):
    print("Erro: O segundo argumento deve ser um número inteiro.")
    return None

  if numero_vezes < 0:
    print("Erro: O número de vezes deve ser um inteiro não negativo.")
    return None

  return (string + " ") * numero_vezes


# Obtém a string e o número de vezes do usuário
string_usuario = input("Digite uma string: ")
try:
  numero_vezes_usuario = int(input("Digite um número inteiro (quantas vezes repetir a string): "))
except ValueError:
  print("Erro: Por favor, digite um número inteiro válido.")
  exit()  # Encerra o programa se a entrada for inválida

# Chama a função para repetir a string
string_repetida = repetir_string(string_usuario, numero_vezes_usuario)

# Imprime o resultado, se a repetição foi bem-sucedida
if string_repetida is not None:
  print("String repetida:", string_repetida)