# config.py

#Begini Buat Databasenya
# CREATE DATABASE fira_asdos;
# USE fira_asdos;
# CREATE TABLE asdos (
#     id INT(11) NOT NULL AUTO_INCREMENT,
#     name VARCHAR(100) NOT NULL,
#     c1 VARCHAR(100) NOT NULL,
#     c2 VARCHAR(100) NOT NULL,
#     c3 VARCHAR(100) NOT NULL,
#     c4 VARCHAR(100) NOT NULL,
#     c5 VARCHAR(100) NOT NULL,
#     c6 VARCHAR(100) NOT NULL,
#     bobot VARCHAR(100) DEFAULT NULL,
#     PRIMARY KEY (id)
# );


class Config:
    # MySQL configurations
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'fira_asdos'


