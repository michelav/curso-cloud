# Criando um Balanceador de Carga

1. Crie duas instâncias e instale um servidor web em ambas;

2. Inicie a criação e selecione um balanceador a nível de aplicação;

3. Configure o balanceador para receber requisições da Internet (*Internet-Facing*), selecione qualquer zona de 
disponibilidade;

4. Nas configurações de grupo de segurança. selecione o grupo usado nos exercícios anteriores;

5. Use o roteamento padrão;

6. Selecione as instâncias que estarão registradas no balanceador;

7. Revise as configurações e crie o balanceador.


Uma forma interessante de acompanhar a relação entre o balanceador e os servidores é ver o log dos servidor web.
 Para isso, abra um terminal, conecte-se com cada servidor e utilize o comando tail:

     sudo tail -f /var/log/httpd/access_log

Após isso, utilize qualquer ferramenta que dispare requisições HTTP para o balanceador e observe o resultado nos
 logs de cada servidor. Nesse exemplo, utilizaremos a ferramenta ab (do *apache-tools*)

      ab -n 200 -c 15 http://balancer.sa-east-1.elb.amazonaws.com/
