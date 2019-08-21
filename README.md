# Django Boilerplate

Django项目的简易Docker模板

## 包含

* django2.2
* postgres
* gunicorn
* redis

## 开发

### 复制项目代码
```
$ git clone https://github.com/ChanMo/cdjango.git demo && cd demo
```

### 生成Secret_key
```
$ python generate_key.py
```
将生成的key放入.env文件中

### 启动测试环境
```
$ docker-compose up
```

浏览器访问 http://0.0.0.0:8000

### 执行Python命令

执行数据库同步
```
$ docker-compose exec web python manage.py migrate
```

## 部署

### 创建文件
```
$ mv deploy.conf.sample deploy.conf
$ mv nginx.conf.sample nginx.conf
$ cp .env .deploy_env
```

### 启动服务
```
$ docker-compose -f deploy.yml
```

### 使用Systemctl
```
$ vim example.service
$ sudo cp example.service /etc/systemd/system/demo.service
$ sudo systemctl enable demo # 允许开机运行
$ sudo systemctl start demo
$ sudo journalctl -u demo -f # 查看日志
```

### 使用Fabric持续集成
详细文档请参考[Fabric官方文档](http://www.fabfile.org/)
```
$ fab -H demo deploy
```

## Next

- [] 自动测试
- [] 统一命令行脚本
- [] 自动secret_key
- [] 日志收集
