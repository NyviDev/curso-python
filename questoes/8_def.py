def make_album(name_artist, name_album, number = ''):
    album = {'Nome do artista': name_artist.title(), 'nome do album': name_album.title()}
    if number:
        album['nº de faixas'] = number
    return album

while True:
    nome_artista = input('Digite um artista: ')
    if nome_artista == 'q':
        break
    nome_album = input('Digite um album desse artista: ')
    if nome_album == 'q':
        break
    num_faixa = input('Digite o Nº de faixas: ')
    if num_faixa == 'q':
        break
    artista = make_album(nome_artista, nome_album, num_faixa)
    print(artista)