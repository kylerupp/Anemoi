from datetime import datetime
import mysql.connector

def create_connection(config):
    return mysql.connector.connect(pool_name = "pool", pool_size = 6, **config)

def get_connection():
    return mysql.connector.connect(pool_name = "pool")

def create_endpoint(mac, cnx, cur):
    date = datetime.now()
    q = "INSERT INTO `id` (`mac`, `time`) VALUES (%s, %s)"
    cur.execute(q, (mac, date))
    cnx.commit()

    q = "SELECT * FROM `id` WHERE `mac` = %s"
    cur.execute(q, (mac,))
    result = cur.fetchone()
    parse = {
        'id': result[0],
        'mac': result[1],
        'time': result[2]
    }
    return parse

def create_temp(mac, temp, log, cnx, cur):
    date = datetime.now()
    q = "INSERT INTO `temp` (`mac`, `temp`, `log`, `time`) VALUES (%s, %s, %s, %s)"
    cur.execute(q ,(mac, temp, log, date))
    cnx.commit()

    q = "SELECT * FROM `temp` WHERE (`mac` = %s AND `log` = %s)"
    cur.execute(q, (mac, log))
    result = cur.fetchone()
    parse = {
        'mac': result[0],
        'temp': result[1],
        'log': result[2],
        'time': result[3]
    }
    return parse

def update_location(mac, loc, cnx, cur):
    cur.execute("SELECT * FROM `location` WHERE `mac`=%s", (mac,))
    result = cur.fetchAll()
    if (result.length > 1):
        q = "UPDATE `location` SET `location`=%s WHERE `mac`=%s"
        cur.execute(q, (loc, mac))
        cnx.commit()
    else:
        q = "INSERT INTO `location` (`mac, `location`) VALUES (%s, %s)"
        cur.execute(q, (mac, loc))
        cnx.commit()