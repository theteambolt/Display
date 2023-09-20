from flask import Flask , render_template
import paho.mqtt.client as mqtt 
#till this works above
#till this works below
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")

client = mqtt.Client() 
client.on_connect = on_connect 


if __name__ == "__main__":
    app.run(debug=True)
    client.connect("localhost", 1883, 60) 
    client.loop_forever()