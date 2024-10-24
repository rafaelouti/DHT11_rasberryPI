import Adafruit_DHT
from bottle import route, run
import RPi.GPIO as GPIO

# Configurações do sensor DHT
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Usando GPIO 4 (Pino 7)


# Função para obter a leitura do sensor
def ler_sensor():
    umidade, temperatura = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if umidade is not None and temperatura is not None:
        return {"temperatura": temperatura, "umidade": umidade}
    else:
        return {"error": "Falha ao ler o sensor"}


# Rota principal para exibir os dados do sensor
@route("/")
def index():
    dados = ler_sensor()
    if "error" in dados:
        return "<h1>Erro ao ler o sensor</h1>"
    else:
        return f"<h1>Temperatura: {dados['temperatura']}°C</h1><h1>Umidade: {dados['umidade']}%</h1>"


# Executa o servidor Bottle
if __name__ == "__main__":
    run(host="0.0.0.0", port=8080)
