# Biology Diversity Panel

## 准备工作

```
Python >= 3.8.0 (推荐3.8+版本)
nodejs >= 16.0 (推荐最新)
Mysql >= 5.7.0 (可选，默认数据库sqlite3，推荐8.0版本)
Redis(可选，最新版)
```

## 前端 ♝

```bash
# 克隆项目
git https://gitee.com/fuadmin/fu-admin.git

# 进入项目目录
cd web

# 安装依赖
yarn install --registry=https://registry.npm.taobao.org

# 启动服务
yarn run dev
# 浏览器访问 http://localhost:8080
# .env 文件中可配置启动端口等参数
# 构建生产环境
# yarn run build
```

## 后端 💈

```bash
# 克隆项目
git https://gitee.com/fuadmin/fu-admin.git
# 进入项目目录
cd backend
# 在 `env.py` 中配置数据库信息
# 默认是Mysql，如果使用SqlServer，qing在requirements.txt中打开 
   mssql-django==1.1.2 
   pyodbc==4.0.32
# 安装依赖环境
	pip3 install -r requirements.txt
# 执行迁移命令：
	python3 manage.py makemigrations system
	python3 manage.py migrate
# 初始化数据
	python3 manage.py init
# 初始化省市县数据:
	python3 manage.py init_area
# 启动项目
	python3 manage.py runserver 0.0.0.0:8000
# 或使用 daphne :
    daphne -b 0.0.0.0 -p 8000 application.asgi:application
```

### 访问项目

- 文档访问地址：[http://localhost:8080/api/docs](http://localhost:8080/api/docs) (默认为此地址，如有修改请按照配置文件)
- 账号：`superadmin` 密码：`123456`
