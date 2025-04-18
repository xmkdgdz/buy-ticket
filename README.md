# buy-ticket

针对大麦app自动购票，需要连接手机或模拟机，使用时需要开启 appium 服务器

运行本程序前，请先登录大麦，打开想要购票的演出界面

创建 config.ini 文件，在其中书写配置

示例：

``` 
[config_name]
session = 1  // 场次
price = 3 // 票档
```
注：
* 场次和票档的编号为，如有n个场次，场次从1开始，票档从n+1开始。需点击特定场次，找到票档编号。
* 目前仅支持一个场次和一个票档

用法：

`pip install -r requirements.txt`

`python main.py {config_name}`

## 免责声明：

本程序仅用于个人学习和技术研究，旨在帮助开发者了解 Android UI 自动化测试的相关技术，无任何实际作用。请注意以下条款：

1. 本程序仅限于个人学习和研究，禁止用于任何商业目的。
2. 使用本程序时，用户应遵守相关法律法规及目标应用的使用条款，不得用于任何违反法律或损害他人权益的行为。
3. 使用本程序可能涉及对目标应用的自动化操作，任何由于使用本程序导致的账号封禁、数据丢失、网站限制访问等风险，由用户自行承担。
4. 本程序的开发者不对任何由于使用该程序所造成的直接或间接损失负责，包括但不限于应用访问受限、账号处罚或其他不可预见的后果。
5. 请勿使用本程序进行恶意操作，如批量下单、爬取敏感信息等行为，否则可能导致目标应用方采取法律措施。
6. 请在使用本程序前仔细阅读并理解上述免责声明，若不同意上述条款，请立即停止使用本程序。