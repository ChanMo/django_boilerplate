# Django Boilerplate

Django项目的简易Docker模板

## 包含

* django2.2
* postgres
* gunicorn
* redis


## 开发

复制项目代码
```
$ git clone https://github.com/ChanMo/cdjango.git demo && cd demo
```

启动测试环境
```
$ docker-compose up
```

浏览器访问 http://0.0.0.0:8000

## 执行Python命令

执行数据库同步
```
$ docker-compose run --rm web python manage.py migrate
```

## 部署

启动服务
```
$ docker-compose -f docker-compose-deploy.yml
```
