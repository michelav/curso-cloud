# Criando Instâncias EC2
Ao logar no [Console Web](https://console.aws.amazon.com) da AWS, você pode navegar até o dashboard do EC2 ou usar um atalho para
criação de instâncias (ver figura abaixo).

![Atalho Instancias](/imagens/atalho-criar-inst.png)

Use o wizard para criar uma nova máquina virtual. Os pontos mais importantes e que você deve estar atento são:

1. Selecione uma AMI e tipos de instância compatíveiscom a zona livre de custo (*free tier*). Sugestão: Use a a Amazon Linux AMI e tipo 
de instância `t2.micro`;

![Amazon AMI](/imagens/amazon-ami.png)

2.  Você pode configurar alguns detalhes da instância. Em especial, a quantidade de instância criadas, a rede (VPC), sub-rede  e o papel
de acesso ou usar as configurações padrão;

3. Para nossos exercícios, você não precisará ajustar tamanho de storage ou tags;

4. Crie um grupo de segurança que permita qualquer tráfego de qualquer origem. Eu sei, é inseguro! Mas para efeito de exercício, podemos
deixar assim;

![Security groups](/imagens/sec-group.png)

5. Revise as configurações (atente para a *free tier*) e lance a instância;

6. Use o arquivo de certificado para acessar a máquina por meio do ssh e configurá-la conforme necessário.
