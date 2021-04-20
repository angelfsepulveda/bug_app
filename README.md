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
![Alt Text](https://drive.google.com/file/d/1t2SkRhsP7D_E1WR4G6gmcCWK-Cxyv5MM/view?usp=sharing)
