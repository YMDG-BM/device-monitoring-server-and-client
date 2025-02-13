# 监控服务项目

该项目用于监视计算机的性能参数，包括CPU、GPU、内存和硬盘使用情况。项目分为服务端和客户端两部分。

## 项目结构

```
monitoring-service
├── server
│   ├── static
│   │   ├── css
│   │   │   └── style.css				# 样式文件
│   │   ├── img
│   │   │   └── background.jpg				# 背景图片
│   │   └── js
│   │       └── script.js				# JavaScript 文件
│   ├── templates
│   │   └── display.html				# HTML 模板文件
│   ├── server.py				# 服务端入口点，设置HTTP服务器并处理请求
│   └── requirements.txt				# 项目依赖项
├── client
│   ├── utils
│   │   └── __init__.py				# 工具函数
│   └──client.py				# 客户端入口点，发送请求并处理响应
├── dockerfile				# Docker 配置文件
├── README.md				# 项目文档
└── requirements.txt				# 项目依赖项
```

## 环境设置

1. 克隆项目到本地：
```
git clone https://github.com/YMDG-BM/device-monitoring-server-and-client.git
cd monitoring-service
```

2. 安装依赖项：
```
pip install -r requirements.txt
```

## 运行服务端

在终端中，导航到 `server` 目录并运行：
```
python server.py
```

服务端将开始监听来自客户端的请求。

## 运行客户端

在另一个终端中，导航到 `client` 目录并运行：
```
python client.py -s http://localhost:5000 -t monitor
```

客户端将向服务端发送请求并接收性能参数的响应。

## 依赖项

- GPUtil
- Flask
- psutil
- requests

## 贡献

欢迎任何形式的贡献！请提交问题或拉取请求。

## 开源项目引用

本项目中使用了以下开源项目和资源：

- [Font Awesome Free](https://fontawesome.com) - 图标库
  - License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), [SIL OFL 1.1](https://scripts.sil.org/OFL), [MIT License](https://opensource.org/licenses/MIT)
- [GPUtil](https://github.com/anderskm/gputil) - 获取GPU信息的Python库
  - License: [MIT License](https://opensource.org/licenses/MIT)
- [Flask](https://flask.palletsprojects.com/) - Python的Web框架
  - License: [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)
- [psutil](https://github.com/giampaolo/psutil) - 获取系统和进程信息的Python库
  - License: [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)
- [requests](https://github.com/psf/requests) - 简单易用的HTTP库
  - License: [Apache 2.0](https://opensource.org/licenses/Apache-2.0)

## License

本项目采用 [MIT License](https://opensource.org/licenses/MIT) 许可。
