set up on AWS

install docker

https://docs.docker.com/engine/install/centos/

use docker without sudo

sudo usermod -aG docker centos

sudo systemctl restart docker

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
