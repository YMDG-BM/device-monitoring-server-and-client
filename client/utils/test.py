import cpuinfo

def main():
    # 获取CPU信息
    info = cpuinfo.get_cpu_info()
    
    # 打印CPU名称
    print("CPU Name:", info['brand_raw'])

if __name__ == "__main__":
    main()
