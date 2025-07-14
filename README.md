# 🌌 Star Wars API

API RESTful em FastAPI com Docker, Firebase e Cloud Run, para consulta e gerenciamento de dados do universo Star Wars.

## ✨ Funcionalidades

- Cadastro e login de usuários
- Consulta de recursos: personagens, filmes, planetas, veículos, naves. 
- Ordenação por `name`  e `title` (A a Z - Z a A)  
- Busca por `name`  e `title`
- Filtros e paginação dos recursos
- Busca por recurso específico
- Documentação interativa via Swagger
- Testes automatizados com Pytest
- Deploy automatizado no Google Cloud Run
- CI/CD com GitHub Actions e Docker Hub

## 🚀 Tecnologias

- Python 3.11
- FastAPI
- Firebase (Auth & Firestore)
- Docker
- Google Cloud Run
- Pytest
- GitHub Actions
- Uvicorn

## 🛠️ Instalação local

1️⃣ Clone o repositório
```
git clone https://github.com/Biiars00/starwars-api.git
cd starwars-api
```

2️⃣ Crie e ative o ambiente virtual
```
python -m venv venv
source venv/bin/activate
```

3️⃣ Instale as dependências
```
pip install -r requirements.txt
```

> Para atualizar dependências: `pip freeze > requirements.txt`

4️⃣ Variáveis de ambiente

Crie um arquivo `.env`:
```
FIREBASE_API_KEY=
GOOGLE_APPLICATION_CREDENTIALS_JSON=
DOCKERHUB_USERNAME=
DOCKERHUB_TOKEN=
GCLOUD_SERVICE_KEY=
SERVICE_NAME=
GCP_REGION=
GCP_PROJECT_ID=
```
> 🔒 Para gerar `GOOGLE_APPLICATION_CREDENTIALS_JSON` em `base64`:
```
cat caminho/para/service-account.json | base64
```

5️⃣ Executar localmente
```
uvicorn main:app --reload
```

- Acesse: `http://localhost:8080`

## 🐳 Executar com Docker
- Build
    ```
    docker build -t starwars-api .
    ```
- Run
    ```
    docker run -d -p 8080:8080 starwars-api
    ```

## ☁️ Deploy no Google Cloud Run

## 🛡️ Autenticação
Utiliza Firebase Auth para acesso aos endpoints protegidos.

1️⃣ /signup: Cria um usuário e retorna token

2️⃣ /login: Retorna o token a ser utilizado nos demais endpoints da aplicação

Envie o token no header:

```
Authorization: Bearer <seu_token>
```

## 🧪 Testes
Executar testes unitários com:
```
pytest
```
> Por enquanto, só há testes na camada de serviço da aplicação.

Executar o coverage:
```
pytest --cov=src/services --cov-report=term-missing
```

## 🤖 CI/CD
A aplicação está pronta para CI/CD:

✅ Build e push automático no Docker Hub a cada push na main
✅ Deploy automático no Google Cloud Run após o push

## 🪐 Endpoints principais

- **Localhost:** `http://localhost:8000`
- **Deploy Cloud Run:** `https://starwars-api-821347683149.southamerica-east1.run.app`

| Método | URL              | Desccrição                                            |
| ------ | ---------------- | ----------------------------------------------------- |
| POST    | /signup         | Cadastra usuário                                      |
| POST    | /login          | Autentica usuário cadastrado                          |
| GET    | /starwars/{resource}      | Lista recursos da [API Star Wars](http://swapi.info/) |
| GET    | /starwars/{resource}/{id} | Busca um recurso específico                           |

> resource: string | id: int

Exemplos de recursos:
- "films"
- "people"
- "planets"
- "species"
- "vehicles"
- "starships"

#### Modelos de body JSON:

| /signup |
| ------- |
```json
   {
      "name": "Beatriz Ribeiro",
      "email": "biiar@powerofdata.com.br",
      "password": "success2025"
   }
```

| /login |
| ------ |
```json
   {
      "email": "biiar@powerofdata.com.br",
      "password": "success2025"
   }
```

#### Modelos de respostas JSON:

| /signup |
| ----------- |
```json
   {
      "message": "User created successfully!",
      "uid": "xxxx"
   }
```

| /login |
| ----------- |
```json
   {
      "idToken": "xxxx",
      "refreshToken": "xxxx",
      "uid": "xxxx"
   }
```

| /starwars/{resource} |
| ----------- |

- "people":
```json
   {
      "page": 1,
      "page_size": 1,
      "total_pages": 1,
      "total_items": 1,
      "items": [
         {
            "name": "string",
            "height": "string",
            "mass": "string",
            "hair_color": "string",
            "skin_color": "string",
            "eye_color": "string",
            "birth_year": "string",
            "gender": "string",
            "homeworld": "string",
            "films": ["string"],
            "species": ["string"],
            "vehicles": ["string"],
            "starships": ["string"]
         }
      ]
   }
  ```
    
- "films":
```json
   ...
   {
      "title": "string",
      "episode_id": "string",
      "opening_crawl": "string",
      "director": "string",
      "producer": "string",
      "release_date": "string",
      "characters": ["string"],
      "planets": ["string"],
      "starships": ["string"],
      "vehicles": ["string"],
      "species": ["string"]
   }
 ```

- "planets":
```json
   ....
   {
    "name": "string",
    "rotation_period": "string",
    "orbital_period": "string",
    "diameter": "string",
    "climate": "string",
    "gravity": "string",
    "terrain": "string",
    "surface_water": "string",
    "population": "string",
    "residents": ["string"],
    "films": ["string"]
   }
  ```

- "species":
```json
   ...
   {
      "name": "string",
      "classification": "string",
      "designation": "string",
      "average_height": "string",
      "skin_colors": "string",
      "hair_colors": "string",
      "eye_colors": "string",
      "average_lifespan": "string",
      "homeworld": "string",
      "language": "string",
      "people": ["string"],
      "films": ["string"]
   }
  ```
  
  - "vehicles":
```json
   ...
   {
      "name": "string",
      "model": "string",
      "manufacturer": "string",
      "cost_in_credits": "string",
      "length": "string",
      "max_atmosphering_speed": "string",
      "crew": "string",
      "passengers": "string",
      "cargo_capacity": "string",
      "consumables": "string",
      "vehicle_class": "string",
      "pilots": ["string"],
      "films": ["string"]
   }
  ```
  
- "starships":
```json
   ...
    {
      "name": "string",
      "model": "string",
      "manufacturer": "string",
      "cost_in_credits": "string",
      "length": "string",
      "max_atmosphering_speed": "string",
      "crew": "string",
      "passengers": "string",
      "cargo_capacity": "string",
      "consumables": "string",
      "hyperdrive_rating": "string",
      "MGLT": "string",
      "starship_class": "string",
      "pilots": ["string"],
      "films": ["string"]
   }
  ```

| /starwars/{resource}/{id} |
| ----------- |
> Retorna um objeto (Dict) específico do items.

#### Exemplos de funcionalidades suportadas

✅ Busca (search)
- Para films, busca pelo `title`. 
- Para demais recursos, busca pelo `name`.

✅ Ordenação (order_by, order)
- Para `films`, ordena por `title`.
- Para demais recursos, ordena por `name`.
- order=asc ou order=desc.

✅ Paginação
- Padrão de 5 itens por página.
- Retorna: `page`, `page_size`, `total_pages`, `total_items`, `items`.

#### Exemplos de uso
   1. Listar todos os planetas ordenados por nome crescente: `GET /starwars/planets?order_by=name&order=asc`

   2. Buscar por personagem chamado Luke: `GET /starwars/characters?name=Luke`

   3. Listar filmes ordenados por título decrescente: `GET /starwars/films?order_by=title&order=desc`

   5. Filtrar planetas e exibir a segunda página: `GET /starwars/planets?&page=5`

## 🙌 Contribuição
- Fork este repositório
- Crie sua branch: `git checkout -b feature/nova-feature`
- Commit suas alterações: `git commit -m 'feat: nova feature'`
- Push na sua branch: `git push origin feature/nova-feature`
- Abra um Pull Request

## 🪐 Créditos
Desenvolvido por [Beatriz Ribeiro](https://github.com/Biiars00) 🚀✨
