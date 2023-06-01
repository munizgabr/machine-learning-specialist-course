import requests
import os

def download_images(search_query, num_images):
    # Parâmetros da API do Pexels
    base_url = 'https://api.pexels.com/v1/search'
    headers = {
        'Authorization': '424HkBXscycNH6atCg90alEgOb5c3SzIm2L7PfIGTsIm9gA2OxDUp7ut'
    }
    params = {
        'query': search_query,
        'per_page': num_images
    }

    # Envio da solicitação à API
    response = requests.get(base_url, headers=headers, params=params)
    data = response.json()

    # Verificação do status da resposta
    if response.status_code != 200 or 'error' in data:
        print('Erro ao realizar a solicitação à API do Pexels.')
        return

    # Criação do diretório para salvar as imagens
    directory = 'images'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Download das imagens
    for photo in data['photos']:
        image_url = photo['src']['original']
        image_name = str(photo['id']) + '.jpg'
        image_path = os.path.join(directory, image_name)

        # Download da imagem
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_path, 'wb') as file:
                file.write(response.content)
                print(f'Imagem "{image_name}" baixada com sucesso.')
        else:
            print(f'Erro ao baixar a imagem "{image_name}".')

    print('Download das imagens concluído.')

# Exemplo de uso
search_query = 'dog'
num_images = 200

download_images(search_query, num_images)