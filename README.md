开发框架2.0使用说明：https://docs.bk.tencent.com/blueapps/USAGE.html

# conda
# pyenv + virtualenv python虚拟环境管理

# 切换PIP镜像源为腾讯源，具体命令参考稍后给出的命令文档

# 镜像源 
https://mirrors.tencent.com/repository/pypi/tencent_pypi/simple, http://mirrors.cloud.tencent.com/pypi/simple/


# 1、在PaaS平台（开发者中心）创建新应用

# 2、在Github创建仓库

# 3、参照开发者中心提供的指引命令，将对应的代码包落到本地
    ## 将代码文件，上传至GitHub仓库

# 4、在开发者中心  部署管理->选择对应要部署的分支，进行部署

# 5、本地开发配置
    ## 1、创建python虚拟环境 （这里推荐pyenv+virtualenv）  当然，也可以用miniconda
    ## 2、更换PIP源 为腾讯源
        https://mirrors.tencent.com/repository/pypi/tencent_pypi/simple, http://mirrors.cloud.tencent.com/pypi/simple/
    ## 3、安装依赖（注意，需要先激活此前创建的虚拟环境）
        pip install -r requirements.txt
        如果安装依赖时遇到了问题，那么我们需要升级pip  pip install --upgrade pip
    ## 4、配置环境变量（推荐使用pycharm，.env插件）通过编写.env文件，快速管理环境变量
    ## 5、参考config/dev.py中的数据库配置，在本地创建数据库，并更改数据库链接信息
    ## 6、执行Django迁移
        ## python manage.py makemigrations
        ## python manage.py migrate
    ## 7、更改本地的host
        sudo vim /etc/hosts
        在其中添加一行
        127.0.0.1  dev.ce.bktencent.com
    ## 8、在Pycharm中，设置对应Django服务的启动配置（主要选择解释器、选择env文件）
    ## 9、Cheer 运行成功✅