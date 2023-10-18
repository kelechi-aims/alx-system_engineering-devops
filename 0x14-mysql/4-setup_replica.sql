-- Step 1: Modify MySQL Configuration on Primary Server (web-01)
-- Edit MySQL Configuration File
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
-- Comment Out bind-address
 #bind-address            = 127.0.0.1
-- Restart MySQL
 sudo service mysql restart
-- Create a MySQL User for Replication
mysql -u root -p
CREATE USER 'replica_user'@'web-02' IDENTIFIED BY 'replica_user_pwd';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'web-02';
FLUSH PRIVILEGES;
EXIT;

-- Step 2: Modify MySQL Configuration on Replica Server (web-02)
-- Edit MySQL Configuration File
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
-- Comment Out bind-address
#bind-address            = 127.0.0.1
-- Restart MySQL
sudo service mysql restart

-- Step 3: Verify Replication
-- Check UFW Rules
sudo ufw allow 3306
-- Start Replication
CHANGE MASTER TO MASTER_HOST='web-01', MASTER_USER='replica_user', MASTER_PASSWORD='replica_user_pwd', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=XXX;
START SLAVE;

-- Step 3: Verify Replication
-- Check UFW Rules
sudo ufw allow 3306
-- Start Replication
mysql -u root -p
CHANGE MASTER TO MASTER_HOST='web-01', MASTER_USER='replica_user', MASTER_PASSWORD='replica_user_pwd', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=XXX;
START SLAVE;

-- Test Replication
USE tyrell_corp;
INSERT INTO nexus6 (name) VALUES ('Roy');
-- Then, on the replica server, check if the new record is replicated
USE tyrell_corp;
SELECT * FROM nexus6;
