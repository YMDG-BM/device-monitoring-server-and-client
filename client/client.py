import requests
import json
import time
import argparse
import utils

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
        
    def get_performance_data(self):
        return utils.get_performance()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server-url", help="The URL of the server to send data to. Example: http://localhost:5000", required=True)
    parser.add_argument("-r", "--retry-duration", help="The duration to wait before retrying to send data. Must be int. Default: 3s", type=int, default=3)
    parser.add_argument("-t", "--target", help="The target to monitor. Example: monitor", type=str, default="monitor")
    url = parser.parse_args().server_url+"/"+parser.parse_args().target
    retry_duration = parser.parse_args().retry_duration
    client = MonitoringClient(url)
    while True:
        # retry_duration = 3  # 重试间隔时间
        performance_data = client.get_performance_data()
        response = client.send_data(performance_data)
        if response:
            print("Response from server:", response)
        else:
            print(f"Failed to send data, will retry in {retry_duration} seconds.")
        time.sleep(retry_duration)  # 每隔retry_duration秒重试一次