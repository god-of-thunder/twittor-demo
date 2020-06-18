set up on AWS
________________________________________________________________________________________________________________________________________
install git(linux)

https://git-scm.com/book/zh-tw/v2/%E9%96%8B%E5%A7%8B-Git-%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8
________________________________________________________________________________________________________________________________________
install docker(centos)

https://docs.docker.com/engine/install/centos/
________________________________________________________________________________________________________________________________________
use docker without sudo

[centos@AWS上創建EC2的IP~]$ sudo usermod -aG docker centos

[centos@AWS上創建EC2的IP~]$ sudo systemctl enable docker

[centos@AWS上創建EC2的IP~]$ sudo systemctl restart docker
________________________________________________________________________________________________________________________________________
[centos@AWS上創建EC2的IP~]$ docker version

Client: Docker Engine - Community

 Version:           19.03.11
 
 API version:       1.40
 
 Go version:        go1.13.10
 
 Git commit:        42e35e61f3
 
 Built:             Mon Jun  1 09:13:48 2020
 
 OS/Arch:           linux/amd64
 
 Experimental:      false

Server: Docker Engine - Community

 Engine:
 
  Version:          19.03.11
  
  API version:      1.40 (minimum version 1.12)
  
  Go version:       go1.13.10
  
  Git commit:       42e35e61f3
  
  Built:            Mon Jun  1 09:12:26 2020
  
  OS/Arch:          linux/amd64
  
  Experimental:     false
