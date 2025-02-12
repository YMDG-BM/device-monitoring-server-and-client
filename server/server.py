from flask import Flask, jsonify, request, render_template
import threading
import time

app = Flask(__name__)

# 用于存储客户端发送的数据
client_data = {}
client_last_seen = time.time()
client_timeout = 30  # 超时时间，单位为秒

def monitor_client_status():
    global client_last_seen
    while True:
        if time.time() - client_last_seen > client_timeout:
            client_data.clear()  # 清空客户端数据，表示客户端下线
        time.sleep(5)

@app.route('/status', methods=['GET'])
def get_status():
    global client_data
    if not client_data:
        return jsonify({"error": "No data received from client"}), 404
    return jsonify(client_data)

@app.route('/monitor', methods=['POST'])
def monitor():
    global client_data, client_last_seen
    client_data = request.json
    client_last_seen = time.time()
    return jsonify({"status": "success"})

@app.route('/display', methods=['GET'])
def display():
    return render_template('display.html')

@app.route('/client_data', methods=['GET'])
def client_data_endpoint():
    global client_data
    if not client_data:
        return jsonify({"error": "No data received from client"}), 404
    return jsonify(client_data)

if __name__ == '__main__':
    threading.Thread(target=monitor_client_status, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
