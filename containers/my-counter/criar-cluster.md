#Criando um cluster no Swarm

1. Construa a imagem da aplicãção counter:
`docker build -t counter-img .`


2. Crie as máquinas virtuais que participarão do cluster com a ferramenta docker-machine: 
`docker-machine create node1`. Você pode checar a situação das máquinas por meio da opção ls. Por exemplo:
`docker-machine ls`;


3. Crie o cluster no manager:
docker-machine ssh <manager> "docker swarm init --advertise-addr <manager_ip>"
docker-machine ssh <manager> "mdkir ./data"


4. Conecte os nós clientes ao manager. O próprio manager informa como após criar o cluster:
`docker-machine ssh node1 "docker swarm join --token ...`

5. Configure seu shell para conectar-se diretamente ao manager:
`eval $(docker-machine env manager)`

6. Faça o deploy dos seus serviços no cluster:
`docker stack deploy -c docker-compose.yml counter-app`


7. Cheque o status com `docker stack ps counter-app`