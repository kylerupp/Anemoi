from datetime import datetime
import mysql.connector

def create_connection(config):
    return mysql.connector.connect(pool_name = "pool", pool_size = 6, **config)

def get_connection():
    return mysql.connector.connect(pool_name = "pool")

def create_endpoint(mac, cnx, cur):
    date = datetime.now()
    format_date = date.strftime('%Y-%m-%d %H:%M:%S')
    q = "INSERT INTO `id` (`mac`, `time`) VALUES (%s, %s)"
    cur.execute(q, (mac, format_date))
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


def create_entry(mac, temp, cnx, cur):
    date = datetime.now()
    q = "INSERT INTO `temp` (`mac`, `temp`, `time`) VALUES (%s, %s, DATE(%s))"
    cur.execute(q ,(mac, temp, date))
    cnx.commit()

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
        