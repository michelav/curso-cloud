from flask import Flask
from flask import request
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/counter")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    nome = request.args.get('nome', default = 'Anônimo', type = str)


    html = "<h3>Oi {nome}!</h3>" \
           "<b>Sou o Host:</b> {hostname}<br/>" \
           "<b>Visitas:</b> {visits}"
    return html.format(nome=nome, hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)