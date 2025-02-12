# 监控服务项目

该项目用于监视计算机的性能参数，包括CPU、GPU、内存和硬盘使用情况。项目分为服务端和客户端两部分。

## 项目结构

```
monitoring-service
├── server
│   ├── server.py          # 服务端入口点，设置HTTP服务器并处理请求
│   └── utils
│       └── gputil_helper.py # GPU性能信息获取工具
├── client
│   └── client.py          # 客户端入口点，发送请求并处理响应
├── requirements.txt       # 项目依赖项
└── README.md              # 项目文档
```

## 环境设置

1. 克隆项目到本地：
   ```
   git clone <项目地址>
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
python client.py
```

客户端将向服务端发送请求并接收性能参数的响应。

## 依赖项

- GPUtil
- Flask (或其他HTTP库，根据实际使用情况)

## 贡献

欢迎任何形式的贡献！请提交问题或拉取请求。