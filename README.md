# 智能家居Demo
> 这是我的自己因兴趣而做的项目，所有代码写的并不怎么样，后期也没有太多的时间去重构，欢迎大家开issue提问，我尽自己最大努力帮助大家。**现在只上传了服务器相关代码和配置文件，树莓派代码之后上传**

- [x] 温湿度数据采集上传、接收与处理
- [x] 人脸识别开门（Face++）
- [x] 微信公众号控制
- [x] 自动浇花
- [ ] 还能做很多，有空继续...

![硬件训练](http://ooiaw5slt.bkt.clouddn.com/硬件训练.png)
![逻辑框图](http://ooiaw5slt.bkt.clouddn.com/逻辑框图.png)


## 服务器环境
* Aliyun ECS CentOS

## 树莓派 3B
* Ubuntu mate

## Requirements
* python 2.7
* [werobot](https://github.com/whtsky/WeRoBot)
* nginx 1.10.2
* supervisord 3.1.4
* flask
* gunicorn 19.7.1

## Installation
```
$ yum install -y nginx
```

```
$ yum install -y  gunicorn
```

```
$ yum install supervisor
```

```
$ pip install werobot
```

## Nginx & supervisor configuration

```
$ vim /etc/nginx/nginx.conf
```

```
server {
        listen       80;
        server_name  YOUR_SERVER_IP;

        # Load configuration files for the default server block.
	       location /spy{
		          proxy_pass http://127.0.0.1:5000;
	       }
	       location /sensor{
		          proxy_pass http://127.0.0.1:5000;
	       }
         location /weixin {
	           proxy_pass http://127.0.0.1:8000;
         }

         error_page 404 /404.html;
         location = /40x.html {
         }

         error_page 500 502 503 504 /50x.html;
         location = /50x.html {
         }
    }
```


```
$ vim /etc/supervisord.conf
```


```
[program:wechat]
command = python /root/wechat/wechat.py
directory = /root/wechat
timeout = 60*60
autostart = true
autorestart = true
redirect_stderr = true
stdout_logfile = /root/wechat/logs/wechat.log
stderr_logfile= /root/wechat/logs/wechat.err


[program:web]
command =/usr/bin/gunicorn -w4 -b0.0.0.0:5000 web:app
directory=/root/wechat
startsecs=0
stopwaitsecs=0  
autostart=false
autorestart=false
stdout_logfile = /root/wechat/logs/web.log
stderr_logfile= /root/wechat/logs/web.err
```


