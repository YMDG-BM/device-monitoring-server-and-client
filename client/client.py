import requests
import json
import time
import psutil
import GPUtil
import subprocess
import pygetwindow as gw

def get_active_window():
    try:
        window = gw.getActiveWindow()
        if window is not None:
            return {
                'title': window.title,
                'hwnd': window._hWnd
            }
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_cpu_name():
    try:
        # 执行wmic命令获取CPU名称
        command = 'wmic cpu get name'
        cpu_name = subprocess.check_output(command, shell=True).decode('utf-8').split('\n')[1].strip()
        return cpu_name
    except Exception as e:
        print("无法获取CPU名称:", e)
        return None


class MonitoringClient:
    def __init__(self, server_url):
        self.server_url = server_url

    def send_data(self, data):
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(self.server_url, data=json.dumps(data), headers=headers)
            response.raise_for_status()  # 如果响应状态码不是200，抛出HTTPError
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error sending data: {e}")
            return None

    def get_cpu_model(self):
        return get_cpu_name()

    def get_performance_data(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')
        gpus = GPUtil.getGPUs()
        gpu_info = [{"name": gpu.name, "load": gpu.load * 100, "memory_total": gpu.memoryTotal, "memory_used": gpu.memoryUsed, "memory_percent": gpu.memoryUtil * 100} for gpu in gpus]

        performance_data = {
            "cpu": {
                "name": self.get_cpu_model(),
                "usage": round(cpu_usage, 1)
            },
            "memory": {
                "percent": memory_info.percent
            },
            "disk": {
                "percent": disk_info.percent
            },
            "gpu": {
                "name": gpu_info[0]["name"] if gpu_info else "No GPU",
                "load": round(gpu_info[0]["load"], 1) if gpu_info else 0,
                "memory_total": int(gpu_info[0]["memory_total"]) if gpu_info else 0,
                "memory_percent": round(gpu_info[0]["memory_percent"], 1) if gpu_info else 0
            },
            "active_window": {
                #"title": "Test Window",
                #"hwnd": 123456
                "title": get_active_window()["title"],
            }
        }
        return performance_data

if __name__ == "__main__":
    client = MonitoringClient("http://localhost:5000/monitor")
    while True:
        retry_duration = 3  # 重试间隔时间
        performance_data = client.get_performance_data()
        response = client.send_data(performance_data)
        if response:
            print("Response from server:", response)
        else:
            print(f"Failed to send data, will retry in {retry_duration} seconds.")
        time.sleep(retry_duration)  # 每隔retry_duration秒重试一次