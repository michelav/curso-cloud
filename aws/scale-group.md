# Criando Scale Groups

1. Crie uma configuração de lançamento. Selecione uma AMI e instância da *free tier*. Configure agora os
 detalhes;

2. Siga até a seção para Configurar Grupos de Segurança. Selecione o grupo criado no exercício anterior;

3. Após criar a configuração, lembre-se de selecionar o par de chaves criado anteriormente;

4. Escolha um nome para o grupo e informe a quantidade desejada de instâncias criadas. No nosso caso, uma 
máquina;

5. Informe que deseja configurar uma política de ajuste de capacidade para o grupo. Utilize a métrica de uso de CPU com o valor de *40%*;

6. Revise e Crie o Grupo;

7. Aguarde até a Instância ficar disponível na aba *Instances*.



## Validando o Scale Group

Iremos utilizar um *software* que aumenta a carga na CPU chamado `stress`. Acesse a instância e instale o 
software utilizando o yum. Após isso, é só usar o comando abaixo e acompanhar a criação de uma nova instância.

    $ stress --cpu 2 --timeout 400 &

