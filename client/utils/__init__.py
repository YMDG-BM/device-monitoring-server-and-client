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
    
def get_performance():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    gpus = GPUtil.getGPUs()
    gpu_info = [{"name": gpu.name, "load": gpu.load * 100, "memory_total": gpu.memoryTotal, "memory_used": gpu.memoryUsed, "memory_percent": gpu.memoryUtil * 100} for gpu in gpus]

    performance_data = {
        "cpu": {
            "name": get_cpu_name(),
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