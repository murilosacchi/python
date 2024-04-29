def valida_senha(senha):
  # Verifica o tamanho mínimo da senha
  if len(senha) < 7:
    return False

  # Verifica se há pelo menos uma letra maiúscula
  maiuscula = False
  for char in senha:
    if char.isupper():
      maiuscula = True
      break

  if not maiuscula:
    return False

  # Verifica se há pelo menos uma letra minúscula
  minuscula = False
  for char in senha:
    if char.islower():
      minuscula = True
      break

  if not minuscula:
    return False

  # Verifica se há pelo menos um dígito numérico
  digito = False
  for char in senha:
    if char.isdigit():
      digito = True
      break

  if not digito:
    return False

  # Se todos os requisitos forem atendidos, a senha é válida
  return True

senha = str(input('Digite sua senha: '))
while not valida_senha(senha):
    senha = str(input('Senha inválida, digite novamente: '))
print('Senha válida')


