import os , socket, random
from flask import Flask,redirect

app = Flask(__name__)
public_ip = '161.156.106.180'

def get_port():
    start_port = random.randint(8080,8500)
    v_port = start_port
    while True:
        print "Trying port " + str(v_port) + "..."
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((public_ip,v_port))
        if result == 0:
            print "Port is open"
            v_port += 1
        else:
            print "Port is not open"
            sock.close()
            return v_port
            break

@app.route('/')
def hello():
    free_port = str(get_port())
   # os.system('ttyd -p ' + free_port + ' login &')
    os.system('ttyd -o -m 1 -p '+ free_port + ' docker run -it --network host --rm  -v /etc/.kube/:/.kube/ iac:latest &')
    return redirect("http://"+ public_ip + ":" + free_port, code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
