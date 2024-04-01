#### 1. Script for set up EC2 with docker + Git

```
#!/bin/bash
yum update -y

# Install Docker
amazon-linux-extras install docker -y
service docker start
systemctl enable docker
usermod -a -G docker ec2-user
chmod 666 /var/run/docker.sock

# Install Docker Compose
curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Install Git  
sudo yum install git -y
```

#### 2. Script to install docker on Ubuntu VM

```
#!/bin/bash
# Add Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Verify the fingerprint
sudo apt-key fingerprint 0EBFCD88

  

# Add Docker repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

  

# Update package index
sudo apt update

  

# Install Docker
sudo apt install docker-ce docker-ce-cli containerd.io

# Install Docker-compose
sudo apt install docker-compose

# Add user to docker groupx`
sudo usermod cloud_user -aG docker
```