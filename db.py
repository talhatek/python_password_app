import psycopg2
from cryptography.fernet import Fernet
from model import Password

key="urKEY"
f = Fernet(key.encode())
user="holder"
conn=None

def connect():
        return psycopg2.connect(user="urUserName",
                                password="urPassword",
                                host="urHost",
                                port="urPort",
                                database="urDB")
         
def count():
        try:
                conn=connect()
                cur=conn.cursor()
                cur.execute(f'SELECT count(*) FROM {user}')
                res = cur.fetchone()
        except Exception as ex:
                print("I am unable to connect to the database" + str(ex))
                return -1
        else:
                conn.close()
                if (res[0] % 3) != 0:
                        print("Something is wrong about rows in database " + str(res[0])+" rows found!!")
                        return -1
                return (res[0])

def fetchMissing(missing):
        try:
                conn=connect()
                cur=conn.cursor()
                cur.execute(f'SELECT * FROM {user} ORDER BY id DESC LIMIT {missing}')
                rows = cur.fetchall()
                processed=castToClass(rows)
        except Exception as ex:
                print("I am unable to connect to the database" + str(ex))
                return -1
        else:
                conn.close()
                return processed
# Parameters:
# raw must be multiples of three 
# 3 equals 1 password
def castToClass(raw):
        personList = []
        divided = len(raw) / 3
        temp = 0
        i=0
        while i< (int(divided)):
                personList.append(decrypt(Password(raw[temp+2][2], raw[temp + 1][2], raw[temp][2])))
                temp += 3
                i += 1
        return personList
     
     
# Parameters:
# type 0 -> site_name
# type 1 -> user_name
# type 2 -> password   
# type 0 => parent_id 0    
def save(passworD):
        password=encrypt(passworD)
        try:
                conn=connect()
                conn.autocommit = False
                cur=conn.cursor()
                cur.execute(f'INSERT INTO {user}(type, value,parent_id) VALUES(0,\'{password.site_name}\',0) RETURNING id')
                parent_id = cur.fetchone()[0]
                cur.execute(f'INSERT INTO {user}(type, value,parent_id) VALUES(1,\'{password.user_name}\',{parent_id})')
                cur.execute(f'INSERT INTO {user}(type, value,parent_id) VALUES(2,\'{password.password}\',{parent_id})')
        except Exception as ex:
                print("I am unable to connect to the database" + str(ex))
                conn.rollback()
                conn.close()
        else:
                print("added successfully")
                conn.commit()
                conn.close()      

def encrypt(password):
        encryptedSiteName=f.encrypt(password.site_name.encode())
        encryptedUserName=f.encrypt(password.user_name.encode())
        encryptedPassword=f.encrypt(password.password.encode())
        return Password(encryptedSiteName.decode(),encryptedUserName.decode(),encryptedPassword.decode())

def decrypt(password):
        decryptedSiteName=f.decrypt(password.site_name.encode())
        decryptedUserName=f.decrypt(password.user_name.encode())
        decryptedPassword=f.decrypt(password.password.encode())
        return Password(decryptedSiteName.decode(),decryptedUserName.decode(),decryptedPassword.decode())

def delete(password):
        try:
                conn=connect()
                conn.autocommit = False
                cur=conn.cursor()
                cur.execute(f'SELECT value,id FROM {user} where type = 0')
                rows = cur.fetchall()
                for row in rows:
                        value=f.decrypt(row[0].encode())
                        if password == value.decode():
                                cur.execute(f'DELETE FROM {user} WHERE id = {row[1]}')
                                cur.execute(f'DELETE FROM {user} WHERE id = {row[1]+1}')
                                cur.execute(f'DELETE FROM {user} WHERE id = {row[1]+2}')
        except Exception as ex:
                print("I am unable to connect to the database" + str(ex))
                conn.rollback()
                conn.close()
        else:
                print("deletedd successfully")
                conn.commit()
                conn.close()     
