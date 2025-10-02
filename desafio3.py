contatos = [('José', '83 991184087', 'eudavioliveira87@gmail.com')]
contatos.append(('Ana', '83 99175843', 'maluf3759@gmail.com'))
i = 0
while i < len(contatos):
    nome, numero, email = contatos[i]
    print(f'{nome} - {numero} - {email}')
    i += 1
