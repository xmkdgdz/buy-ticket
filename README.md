# buy-ticket

针对大麦app自动购票，需要连接手机或模拟机，使用时需要开启 appium 服务器

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
