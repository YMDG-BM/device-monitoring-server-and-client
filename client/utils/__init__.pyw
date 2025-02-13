import psutil
import GPUtil
import time
import platform
import cpuinfo
def get_active_window():
    import pygetwindow as gw
    try:
        window = gw.getActiveWindow()
        if window is not None:
            return {
                'title': window.title,
                #'hwnd': window._hWnd
            }
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

"""
def get_cpu_name():
    try:
        print("get_cpu_name function running...")
        time.sleep(5)
        info = cpuinfo.get_cpu_info()
        cpu_name = info['brand_raw']
        print("get_cpu_name function running...")
        time.sleep(5)
        return cpu_name
    except Exception as e:
        print("无法获取CPU名称:", e)
        print("get_cpu_name function running...")
        time.sleep(5)
        return None
"""
    
def get_performance():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    gpus = GPUtil.getGPUs()
    gpu_info = [{"name": gpu.name,
                "load": gpu.load * 100,
                "memory_total": gpu.memoryTotal,
                "memory_used": gpu.memoryUsed,
                "memory_percent": gpu.memoryUtil * 100}
                for gpu in gpus]
    active_window = {"title": "Null"}
    if platform.system() != 'Linux':
        active_window = get_active_window()
    active_window_title = active_window["title"] if active_window else "Null"
    

    performance_data = {
        "cpu": {
            #"name": get_cpu_name(),
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
            "load": round(gpu_info[0]["load"], 1) if gpu_info else 0.0,
            "memory_total": int(gpu_info[0]["memory_total"]) if gpu_info else 0,
            "memory_percent": round(gpu_info[0]["memory_percent"], 1) if gpu_info else 0.0
        },
        "active_window": {
            "title": active_window_title,
        }
    }
    return performance_data