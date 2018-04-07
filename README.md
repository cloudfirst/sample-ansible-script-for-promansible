# sample-ansible-script-for-promansible
sample ansible script for promansible


2.0 assuming the existence of ansible playbook
```
.
├── example.txt
├── geninventory.py
├── playbook
│   ├── alert
│   │   └── roles
│   │       ├── handle_cpu_threshold_exceeded
│   │       │   └── README.md
│   │       ├── handle_DiskWillFillIn4Hours
│   │       │   └── README.md
│   │       ├── handle_HighErrorRate
│   │       │   └── README.md
│   │       ├── handle_net_device_down
│   │       │   └── README.md
│   │       └── handle_server_down
│   │           └── README.md
│   └── routine
│       └── roles
│           ├── check_dns_sinobot_biz
│           │   └── README.md
│           ├── check_EXSi_port
│           │   └── README.md
│           ├── check_ftp_connect
│           │   └── README.md
│           ├── check_LAN_speed
│           │   └── README.md
│           ├── check_vpn_dns
│           │   └── README.md
│           ├── check_vpn_website_abroad_connect
│           │   └── README.md
│           ├── restart_l2tp_vpn
│           │   └── README.md
│           └── restart_pptp_vpn
│               └── README.md
└── README.md
```
```
cmdline:
   ansible-playbook <task>            -i <inventory_path>  -u <user> -K --extra-vars "user=<user>"
   ansible-playbook playbook/ping.yml -i ./geninventory.py -u luhya -k


ping.yml   # task file name
--------------
- hosts: 192.168.56.101  # ip addr comes from alert message
  roles:
      - ping  # role name, namely what shoud be done in playbook/roles/ping/tasks/main.yml

$ ./geninventory.py --list  # dynamic inventory generation
{'monitor-dev': ['192.168.56.101']}

```
