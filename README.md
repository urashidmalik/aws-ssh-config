# AWS-SSH-Config
config file generator for ssh based on tags

- Make sure you have python-pip (https://pip.pypa.io/en/stable/installing/#pip-included-with-python)

- Install boto framework
```shell
sudo pip install boto
```

- export following shell varible to access aws
```shell
export AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXX
export AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

- Generate config
```shell
python aws_ssh_config.py
```
