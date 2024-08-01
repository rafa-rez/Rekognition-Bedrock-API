<h1 align="center">Compass Uol - Faces classification</h1>

![Logo](https://s3.sa-east-1.amazonaws.com/remotar-assets-prod/company-profile-covers/cl7god9gt00lx04wg4p2a93zt.jpg)


## 📌 Índice
- [Descrição do Projeto](#-Descrição-do-Projeto)
- [Descrição da API](#-Descrição-da-API)
- [Estrutura de pastas](#-Estrutura-de-pastas)
- [Arquitetura AWS](#️-arquitetura-aws)
- [Como usar o sistema](#-como-usar-o-sistema)
- [Experiências obtidas](#-experiências-obtidas)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Dificuldades encontradas](#️-dificuldades-encontradas)
- [Autores](#-autores)


## 📖 Descrição do Projeto
Este projeto, relizado na Sprint 8 do programa de bolsas da CompassUOL, tem como finalidade criar APIs com a capacidade de:
- Classificar a emoção principal de faces humanas em imagens usando o serviço de reconhecimento de imagem [Amazon Rekognition](https://aws.amazon.com/pt/rekognition/)
- Detectar pets na imagem
- Gerar com o [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/?icmpid=docs_homepage_ml), dicas de quantidade de exercícios, temperamento, comportamento, cuidados, baseadas na espécie do animal
- Utilizar o [CloudWatch](https://docs.aws.amazon.com/pt_br/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html) para gravar os logs dos resultados

## 📂 Estrutura de pastas
```
├── assets
├── visao-computacional
│   ├── .serverless
│   │    ├── cloudformation-template-create-stack.json
│   │    ├── cloudformation-template-update-stack.json
│   │    ├── meta.json
│   │    ├── serverless-state.json
│   │    └── vizions.zip
│   │
│   ├── handlers
│   │    ├── analyzeV1.py
│   │    ├── analyzeV2.py
│   │    ├── descriptions.py
│   │    ├── health.py
│   │    └── utils.py
│   │         
│   ├── gitignore.txt
│   └── serverless.yml     
│                   
├── .gitignore                      
└── README.MD                        
                                           
```


## 🏗️ Arquitetura AWS
![arquitetura-base](./assets/arquitetura-base.jpg)  



## 🚀 Como usar o sistema
### Instale o framework [Serverless](https://www.serverless.com/#How-It-works) em seu computador
```
npm install -g serverless
```
### Configure as credenciais do [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
```
aws configure
```
### Clone o repositório em seu computador
```
https://github.com/Compass-pb-aws-2024-ABRIL/sprint-8-pb-aws-abril.git
```
### Navegue até a pasta onde encontra-se o arquivo serverless.yml
```
cd sprint-8-pb-aws-abril.git/visao-computacional
```
### Faça o deploy dos recursos na sua conta AWS
```
serverless deploy
```
### Após finalizar o deploy, você terá um retorno como este:
```
Deploying vision to stage dev (us-east-1) 
  
Service deployed to stack vision-dev (85s) 
  
endpoints:
   GET - https://oac0j5ppr4.execute-api.us-east-1.amazonaws.com/
   GET - https://oac0j5ppr4.execute-api.us-east-1.amazonaws.com/v1
   GET - https://oac0j5ppr4.execute-api.us-east-1.amazonaws.com/v2
   POST - https://oac0j5ppr4.execute-api.us-east-1.amazonaws.com/v1/vision      # Endpoint de classifição de emoções de faces humanas
   POST - https://oac0j5ppr4.execute-api.us-east-1.amazonaws.com/v2/vision      # Endpoint de classificação de emoções de faces humans com detecção de pets
   
functions: 
   health: visions-dev-health 
   v1Description: visions-dev-v1Description 
   v2Description: visions-dev-v2Description
   analyze_image_v1: visions-dev-analyze_image_v1
   analyze_image_v2: visions-dev-analyze_image_v2 
```
### Teste a solução
**Observação**: Crie um bucket no S3 e faça o upload da imagem que deseja extrair informações.
- 1. Escolha um serviço de testes de API (Postman, ThunderClient, Insomnia)
- 2. Selecione o método POST para o Endpoint desejado e envie a requisição
```json 
{ 
   "bucket": "myphotos", 
   "imageName": "test-happy.jpg" 
} 
``` 

Você terá uma resposta no seguinte formato:

![image](https://github.com/user-attachments/assets/1c19fb52-6f88-46ca-9a70-6a750bab1214)



## ✍️ Exemplos de Requisições

    - Rotas V1 e V2
    
         - {
             "bucket": "sprint-8-images",
            "imageName": "bird.jpg"
            }

         - {
             "bucket": "sprint-8-images",
            "imageName": "cat.jpg"
            }

         - {
             "bucket": "sprint-8-images",
            "imageName": "dog.jpg"
            }

         - {
             "bucket": "sprint-8-images",
            "imageName": "fish.jpg"
            }

         - {
             "bucket": "sprint-8-images",
            "imageName": "forest.jpg"
            }

         - {
             "bucket": "sprint-8-images",
            "imageName": "wolf.jpg"
            }

         - {
             "bucket": "sprint-8-images",
            "imageName": "doghuman.jpg"
            }

## 🏆 Experiências obtidas
Neste projeto, foram exploradas várias tecnologias avançadas da AWS, incluindo o Amazon Rekognition para análise de imagens e detecção de emoções em rostos humanos, além de identificação de pets. A integração com o Amazon Bedrock permitiu a utilização de inteligência artificial generativa para fornecer dicas sobre o cuidado com os animais, enriquecendo a aplicação com conteúdo relevante e personalizado. O uso do Amazon CloudWatch foi essencial para monitoramento e logging das operações, garantindo que todas as interações com os serviços fossem registradas adequadamente. Este projeto possibilitou uma experiência prática de implementação de APIs robustas e escaláveis, demonstrando a capacidade da nuvem AWS na criação de aplicações inteligentes e integradas.

## 💻 Tecnologias utilizadas
- [Amazon Rekognition](https://aws.amazon.com/pt/rekognition/) Serviço de reconheciemento de imagem
- [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/?icmpid=docs_homepage_ml) Serviço de IA generativa com modelos avançados
- [Amazon S3](https://aws.amazon.com/pt/s3/) Serviço de armazenamento de objetos
- [Amazon CloudWatch](https://docs.aws.amazon.com/pt_br/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html) Serviço de gerenciamento e monitoramento de logs nos serviços AWS

## 🛠️ Dificuldades encontradas
- Ajuste de permissões IAM para executar as tarefas
- Configurações do Bedrock

## ✍🏻 Autores
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/120669342?v=4" width=115><br><sub>José Acerbi Almeida Neto</sub>](https://github.com/JoseJaan) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/81874524?v=4" width=115><br><sub>Davi Hermógenes</sub>](https://github.com/DaviSiq) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/137515142?v=4" width=115><br><sub>Rafael Alves Silva Rezende</sub>](https://github.com/rafa-rez) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/107402049?v=4" width=115><br><sub>Ítalo Rabelo</sub>](https://github.com/italo-rabelo)
| :---: | :---: | :---: | :---: |
