# sample-ansible-script-for-promansible
这是和[PromAnsible](https://github.com/cloudfirst/PromAnsible)配套使用的ansible脚本。

在PromAnsible的管理界面上，可以设置并下载配套的ansible脚本的git仓库代码。

通过这个脚本，可以无限制的扩展PromAnsible的功能，直到实现IT运维的全自动化。
- 定义收到特定报警信息后被自动调用的一个或多个任务处理模块
- 定义日常管理中需要的定时任务模块或一次性任务模块

# script architecture
用户可以在此基础上编写自己的PromAnsible扩展脚本，只要它遵循如下的目录结构
```
.
|-- example.txt
|-- geninventory.py.      # 读取PromAnsible管理的所有机器的ip地址，包括服务器和网络设备
|-- playbook
|   |-- alert             # 警报任务处理模块，用户可为每个警报添加一个或多个任务处理模块
|   |   |-- alerthandler.yml
|   |   `-- roles
|   |       |-- handle_cpu_threshold_exceeded
|   |       |   `-- README.md                   
|   |        |-- handle_DiskWillFillIn4Hours
|   |       |   `-- README.md
|   |       |-- handle_HighErrorRate
|   |       |   `-- README.md
|   |       |-- handle_net_device_down
|   |       |   `-- README.md
|   |       `-- handle_server_down
|   |           |-- README.md    # 每个模块必须有的REDAME文件，PromAnsible会读取这个文件的内容并显示在模块说明里面
|   |           `-- tasks
|   |               `-- main.yml
|   `-- routine          # 日常管理任务模块，用户可根据日常管理需要编写定时任务模块或一次性任务模块
|       |-- roles
|       |   |-- install-node-exporter
|       |   |   |-- files
|       |   |   |   `-- node-exporter_1.1_all.deb  # 文件来源于PromAnsible的编译输出
|       |   |   |-- README.md    # 每个模块必须有的REDAME文件，PromAnsible会读取这个文件的内容并显示在模块说明里面
|       |   |   `-- tasks
|       |   |       `-- main.yml
|       |   `-- install-node-exporter-for-win
|       |       |-- files
|       |       |   |-- wmi_exporter-0.2.7-386.msi    # 网络下载的windows版的node_exporter 32bit安装文件
|       |       |   `-- wmi_exporter-0.2.7-amd64.msi  # 网络下载的windows版的node_exporter 64bit安装文件
|       |       |-- README.md
|       |       `-- tasks
|       |           `-- main.yml
|       |-- routinehandler-win.yml
|       `-- routinehandler.yml
`-- README.md
```
