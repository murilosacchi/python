import uuid

menu_pratos = {
    "1": "arroz, feijão e fritas",
    "2": "arroz e frango à parmegiana",
    "3": "frango à milanesa"
}

menu_bebidas = {
    "1": "coca",
    "2": "coca zero",
    "3": "suco de laranja",
    "4": "suco de uva"
}

estado = "inicio"
pedido = {}

while True:
    if estado == "inicio":
        print("bot: Olá, aqui é o bot de atendimento do restaurante Comida Boa. 🤖")
        print("bot: Digite o número da opção desejada:\n1 - Escolher prato\n2 - Escolher bebida")
        estado = "menu"

    elif estado == "menu":
        msg = input("usuario: ").strip()
        if msg == "1":
            print("bot: Escolha o prato que deseja:")
            for key, value in menu_pratos.items():
                print(f"{key} - {value}")
            estado = "escolhendo_prato"
        elif msg == "2":
            print("bot: Escolha a bebida que deseja:")
            for key, value in menu_bebidas.items():
                print(f"{key} - {value}")
            estado = "escolhendo_bebida"
        else:
            print("bot: Opção inválida. Digite 1 ou 2.")

    elif estado == "escolhendo_prato":
        msg = input("usuario: ").strip()
        if msg in menu_pratos:
            pedido["prato"] = menu_pratos[msg]
            print(f"bot: o prato escolhido foi: {pedido['prato']}")
            print("bot: deseja escolher sua bebida?\n1 - sim\n2 - não")
            estado = "pergunta_bebida"
        else:
            print("bot: Escolha inválida. Tente novamente.")

    elif estado == "pergunta_bebida":
        msg = input("usuario: ").strip()
        if msg == "1":
            print("bot: Escolha a bebida que deseja:")
            for key, value in menu_bebidas.items():
                print(f"{key} - {value}")
            estado = "escolhendo_bebida"
        elif msg == "2":
            pedido["bebida"] = "nenhuma"
            estado = "resumo"
        else:
            print("bot: Opção inválida. Digite 1 ou 2.")

    elif estado == "escolhendo_bebida":
        msg = input("usuario: ").strip()
        if msg in menu_bebidas:
            pedido["bebida"] = menu_bebidas[msg]
            print(f"bot: a bebida escolhida foi: {pedido['bebida']}")
            estado = "resumo"
        else:
            print("bot: Vi que você não escolheu nenhuma das opções acima.\nEscolha uma das opções para eu te ajudar!")

    elif estado == "resumo":
        print("bot: resumo do pedido:")
        print(f"prato: {pedido.get('prato', 'nenhum')}")
        print(f"bebida: {pedido.get('bebida', 'nenhuma')}")
        print("bot: deseja alterar ou confirmar o pedido?\n1 - alterar\n2 - confirmar pedido")
        estado = "confirmacao"

    elif estado == "confirmacao":
        msg = input("usuario: ").strip()
        if msg == "1":
            estado = "menu"
        elif msg == "2":
            numero_pedido = str(uuid.uuid4())
            print("bot: pedido confirmado")
            print(f"bot: número do pedido: {numero_pedido}")
            break
        else:
            print("bot: Opção inválida. Digite 1 ou 2.")
