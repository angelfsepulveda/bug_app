# pre requirements 📋
```
sudo apt-get install python3-dev default-libmysqlclient-dev libmysqlclient-dev
# database
create database bug_tracker;
CREATE USER 'bug_trackeruser'@'localhost' IDENTIFIED BY '.bug.';
GRANT ALL PRIVILEGES ON bug_tracker . * TO 'bug_trackeruser'@'localhost';
flush privileges;
```
# Results 
_Example_
![1](https://user-images.githubusercontent.com/37251039/115451734-2f692480-a1e3-11eb-9488-ef2e884de143.png)
![2](https://user-images.githubusercontent.com/37251039/115451761-36903280-a1e3-11eb-94f6-136f7c86aeae.png)
![3](https://user-images.githubusercontent.com/37251039/115451765-3859f600-a1e3-11eb-951c-9b192cfce7f8.png)
![4](https://user-images.githubusercontent.com/37251039/115451766-398b2300-a1e3-11eb-95fb-0b1fa4589066.png)
![5](https://user-images.githubusercontent.com/37251039/115451772-3abc5000-a1e3-11eb-9412-2fb4e520866d.png)

