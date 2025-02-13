from flask import Flask, jsonify, request, render_template
import time

app = Flask(__name__)

client_data = {}
client_last_seen = None  # 初始化为None，表示从未收到数据
client_timeout = 10  # 客户端超时时间，单位为秒

with open("./device_key.txt", "r") as f:
    device_key = f.read().strip()

@app.route('/status', methods=['GET'])
def get_status():
    global client_data, client_last_seen, client_timeout
    # 检查是否从未收到过数据
    if client_last_seen is None:
        return jsonify({"error": "No data received from client"}), 404
    # 检查客户端是否超时
    current_time = time.time()
    if current_time - client_last_seen > client_timeout:
        return jsonify({"error": "Client offline"}), 503
    # 检查数据是否存在
    if not client_data:
        return jsonify({"error": "No data received from client"}), 404
    return jsonify(client_data)

@app.route('/monitor', methods=['POST'])
def monitor():
    global client_data, client_last_seen
    data = request.json
    # 验证设备密钥
    if data.get("device_key") != device_key:
        return jsonify({"error": "Unauthorized"}), 401
    # 更新客户端数据和最后活跃时间
    client_data = data.get("performance_data", {})
    client_last_seen = time.time()
    return jsonify({"status": "success"})

@app.route('/display', methods=['GET'])
def display():
    return render_template('display.html')

@app.route('/client_data', methods=['GET'])
def client_data_endpoint():
    global client_data, client_last_seen, client_timeout
    # 检查是否从未收到过数据
    if client_last_seen is None:
        return jsonify({"error": "No data received from client"}), 404
    # 检查客户端是否超时
    current_time = time.time()
    if current_time - client_last_seen > client_timeout:
        return jsonify({"error": "Client offline"}), 503
    # 检查数据是否存在
    if not client_data:
        return jsonify({"error": "No data received from client"}), 404
    return jsonify(client_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)