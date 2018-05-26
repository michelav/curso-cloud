# Criando um Webserver com Docker

1. Crie um Dockerfile e indique qual o servidor web você utilízará. No nosso exemplo, sugerimos o nginx para
o alpine. Procure qual a imagem adequada no Docker Hub. Utilize o FROM para informar a imagem base;

2. Adicione um conteúdo para ser servido pelo webserver com ADD;

3. Construa uma nova imagem: `docker build -t webserver-img .` Cheque as imagens existentes com o comando
`docker images`;

4. Execute o container com o comando `docker run`. Por exemplo: 
`docker run --name my-server -p 7070:80 webserver-img`. Lembre-se de tornar a porta 80 acessível via a opção 
`-p`. Você também pode checar o container criado com `docker container ls`;

5. Acesse o servidor web.