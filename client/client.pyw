import os
import ctypes
import sys
import requests
import json
import time
import argparse
import utils
import getmac

class MonitoringClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.device_key = getmac.get_mac_address()

    def send_data(self, data):
        headers = {'Content-Type': 'application/json'}
        payload = {
            "device_key": self.device_key,
            "performance_data": data
        }
        try:
            response = requests.post(self.server_url, data=json.dumps(payload), headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None
        
    def get_performance_data(self):
        return utils.get_performance()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server-url", required=True)
    parser.add_argument("-r", "--retry-duration", type=int, default=3)
    parser.add_argument("-t", "--target", type=str, default="monitor")
    
    try:
        args = parser.parse_args()
    except SystemExit:
        sys.exit(1)
    
    url = args.server_url + "/" + args.target
    retry_duration = args.retry_duration
    client = MonitoringClient(url)
    while True:
        try:
            performance_data = client.get_performance_data()
            response = client.send_data(performance_data)
        except Exception:
            pass
        finally:
            try:
                pass
            except UnboundLocalError:
                pass
        time.sleep(retry_duration)