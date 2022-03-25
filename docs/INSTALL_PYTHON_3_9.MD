# Install Python 3.9 Using Source Code
As the Debian packages are available, We don’t recommend installing Python 3.9 packages from source code. But in some cases, you may need to install Python from the source code.

So follow the below instructions to install Python 3.9 using source code on Ubuntu 18.04 Linux system.


First of all, install essential packages for compiling source code. Open a terminal and execute following commands:

```sh
sudo apt install wget build-essential checkinstall 
sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev 
```
Now, download the Python 3.9 source code from the official download site. Switch to a relevant directory and use wget to download the source file.
```sh
cd /opt 
sudo wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz 
```
Next, extract the downloaded archive file and prepare the source for the installation.
```sh
tar xzf Python-3.9.6.tgz 
cd Python-3.9.6 
sudo ./configure --enable-optimizations 
```
Python source is ready to install. Execute make altinstall command to install Python 3.9 on your system.
sudo make altinstall 
make altinstall is used to prevent replacing the default python binary file /usr/bin/python.

The Python 3.9 has been installed on Ubuntu 18.04 system. Verify the installed version:
```sh
python3.9 -V 
```
Remove the downloaded archive to free space
```sh
sudo rm -f /opt/Python-3.9.6.tgz 
```

https://tecadmin.net/how-to-install-python-3-9-on-ubuntu-18-04/