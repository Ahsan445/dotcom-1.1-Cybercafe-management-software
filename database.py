import sqlite3
import datetime
from os import remove, path
from tkinter import messagebox

class pc_data:
    def __init__(self):
        conn = sqlite3.connect('data.db',timeout=60)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS pc_data(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT(10),
            time TEXT(10),
            pc_name TEXT(10),
            pc_time TEXT(10),
            rate TEXT(10),
            received TEXT(10),
            difference TEXT(10))''')
        conn.commit()
        conn.close()
        
    def insert(self, date, time, pc_name, pc_time, rate, received, difference):
        '''(date, pc_name, time, rate, difference) -> None
        Create pc_data.db if not exists, creates table pc_data1 if not exists and inserts data into it'''
        conn = sqlite3.connect('data.db', timeout=20)
        cur = conn.cursor()
        cur.execute('''INSERT INTO pc_data(
            date,
            time,
            pc_name,
            pc_time,
            rate,
            received,
            difference) VALUES(
            :date,
            :time,
            :pc_name,
            :pc_time,
            :rate,
            :received,
            :difference)''',{'date':date,'time':time,'pc_name':pc_name,
                             'pc_time':pc_time, 'rate':rate,
                             'received':received,
                             'difference':difference})
        conn.commit()
        conn.close()


    def retrive(self, date):
        '''Detailed view of pc data'''
        l = list()
        each = ''
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM pc_data WHERE date=(?)''',(date,))
        for line in cur:
            l.append(line)
         
        conn.commit()
        conn.close()
        return l

    def retrive_today(self, date):
        '''today page view of pc data'''
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('Select received, difference from pc_data where date=(?)',(date,))
        count = 0
        total_rate = 0
        total_difference = 0
        for x in cur:
            total_rate += int(x[0])
            total_difference += int(x[1])
            count += 1
        conn.commit()
        conn.close()
        return {'total_rate':total_rate, 'total_difference':total_difference, 'qty':count}

    def retrive_administrator(self, from_date, to_date):
        '''today page view of pc data'''
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT received, difference
            from pc_data
            where date BETWEEN (?) AND (?)''',(from_date, to_date))
        count = 0
        total_rate = 0
        total_difference = 0
        for x in cur:
            total_rate += int(x[0])
            total_difference += int(x[1])
            count += 1
        conn.commit()
        conn.close()
        return {'total_rate':total_rate, 'total_difference':total_difference, 'qty':count}

    def admin_detail_pc_data(self,  from_date, to_date):
        l = list()
        each = ''
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM pc_data
            WHERE date BETWEEN (?) AND (?)
            ORDER BY date''',(from_date, to_date))
        for line in cur:
            l.append(line)
         
        conn.commit()
        conn.close()
        return l

class expances_and_income:
    def __init__(self):
        with open('final_date','r') as final:
            self.date = final.readline()
        self.today_date = str(datetime.date.today())
        
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS expances(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT(10),
            time TEXT(10),
            description TEXT(20),
            amount TEXT(10))''')
        cur.execute('''CREATE TABLE IF NOT EXISTS income(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT(20),
            time TEXT(10),
            description TEXT(20),
            amount TEXT(10))''')
        conn.commit()
        conn.close()
    def insert_expances(self, description, amount):
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO expances(
        date,
        time,
        description,
        amount) VALUES(
        :date,
        :time,
        :description,
        :amount)''',{'date':self.date,'time':current_time,'description':description,'amount':amount})
        conn.commit()
        conn.close()
        return None
        
    def insert_income(self, description, amount):
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO income(
        date,
        time,
        description,
        amount) VALUES(
        :date,
        :time,
        :description,
        :amount)''',{'date':self.date,'time':current_time,'description':description,'amount':amount})
        conn.commit()
        conn.close()
        return None

    def retrive_expances(self, date):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT description,amount FROM expances WHERE date=(?)''',(date,))
        amount = 0
        for (x, y) in cur:
            amount = amount+int(int(y))
        conn.commit()
        conn.close()
        return amount
    def retrive_income(self, date):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT description,amount FROM income WHERE date=(?)''',(date,))
        amount = 0
        for (x, y) in cur:
            amount = amount+int(int(y))
        conn.commit()
        conn.close()
        return amount

    def retrive_administrator_expances(self, from_date, to_date):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT description,amount
            FROM expances
            WHERE date BETWEEN (?) AND (?)''',(from_date, to_date))
        amount = 0
        for (x, y) in cur:
            amount = amount+int(int(y))
        conn.commit()
        conn.close()
        return amount

    def retrive_administrator_income(self, from_date, to_date):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT description,amount
            FROM income
            WHERE date BETWEEN (?) AND (?)''',(from_date, to_date))
        amount = 0
        for (x, y) in cur:
            amount = amount+int(int(y))
        conn.commit()
        conn.close()
        return amount

    def retrive_income_for_text_box(self, date):
        '''(self)-> list

        Connects to data.db income table and retrives
        all data by date with description and income in list form'''
        l = list()
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT description,amount FROM income WHERE date=(?)''',(date,))
        amount = 0
        for x in cur:
            l.append(x)
        conn.commit()
        conn.close()
        return l

    def retrive_expances_for_text_box(self, date):
        '''(self)-> list

        Connects to data.db expances table and retrives
        all data by date with description and income in list form'''
        l = list()
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT description,amount FROM expances WHERE date=(?)''',(date,))
        for x in cur:
            l.append(x)
        conn.commit()
        conn.close()
        return l
    
    def retrive_income_for_text_box_admin(self, from_date, to_date):
        '''(self)-> list

        Connects to data.db income table and retrives
        all data by date with description and income in list form'''
        l = list()
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT date, time, description,amount
            FROM income
            WHERE date BETWEEN (?) AND (?)
            ORDER BY date''',(from_date, to_date))
        amount = 0
        for x in cur:
            l.append(x)
        conn.commit()
        conn.close()
        return l

    def retrive_expances_for_text_box_admin(self, from_date, to_date):
        '''(self)-> list

        Connects to data.db expances table and retrives
        all data by date with description and income in list form'''
        l = list()
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute('''SELECT date, time, description, amount
            FROM expances
            WHERE date BETWEEN (?) AND (?)
            ORDER BY date''',(from_date, to_date))
        for x in cur:
            l.append(x)
        conn.commit()
        conn.close()
        return l

class restore_pc:
    def __init__(self, location):
        self.location = location

    def create_restore(self):
        conn = sqlite3.connect(self.location, timeout=60)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS restore(
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        s INTEGER(2) NOT NULL,
        m INTEGER(2) NOT NULL,
        h INTEGER(2) NOT NULL,
        time TEXT(10) NOT NULL)''')
        conn.commit()
        conn.close()
        return None

    def restore_insert(self, s, m, h, time):
        conn = sqlite3.connect(self.location, timeout=60)
        cur = conn.cursor()
        cur.execute('''INSERT INTO restore(
        s,
        m,
        h,
        time) VALUES(
        :s,
        :m,
        :h,
        :time)''',{'s':s,'m':m ,'h':h,'time':time})
        conn.commit()
        conn.close()

        return None

    def restore_retrive(self):
        tup = None
        try:
            conn = sqlite3.connect(self.location, timeout=60)
        except:
            restore_error = messagebox.askokcancel('Restore Problem ',
                message='There was a problem connecting to '+self.location)
            return
        try:
            cur = conn.cursor()
            cur.execute('''SELECT s, m, h, time FROM restore WHERE  ID = (
                SELECT MAX(id) FROM restore)''')
            for x in cur:
                tup = x
            conn.commit()
            conn.close()
            return tup
        except:
            restore_error = messagebox.askokcancel('Restore Problem ',
                message='Could not recover data from '+self.location)
            return

    def restore_delete(self):
        if path.exists(self.location):
            try:
                remove(self.location)
            except:
                restore_error = messagebox.askokcancel('Restore Problem ',
                    message='Could not delete '+self.location)
                return
        else:
            return

class customer_debt:
    def __init__(self):
        conn = sqlite3.connect('debt.db',timeout=60)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE if not exists customer_debt(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT(20),
            phone TEXT(11),
            recv_name TEXT(20),
            description TEXT(20),
            amount INTEGER(5),
            received INTEGER(5),
            debt INTEGER(5),
            time TEXT(10),
            date TEXT(10))''')
        conn.commit()
        conn.close()

    def debt_insert(self, name, phone, recv_name, description, amount, received, debt, date, time):
        conn = sqlite3.connect('debt.db', timeout=60)
        cur = conn.cursor()
        cur.execute('''INSERT INTO customer_debt(name, phone, recv_name, description, amount, received, debt, date, time) VALUES(
            ?,?,?,?,?,?,?,?,?)''',(name, phone, recv_name, description, amount, received, debt, date, time))
        conn.commit()
        conn.close()

    def debt_retrive_tv(self):
        l = list()
        conn = sqlite3.connect('debt.db', timeout=60)
        cur = conn.cursor()
        cur.execute('''  SELECT id,
                                name,
                                phone,
                                recv_name,
                                description,
                                amount,
                                received,
                                debt,
                                date,
                                time from customer_debt''')
        for columns in cur:
            l.append(columns)
        conn.commit()
        conn.close()
        return l

    def search_by_name(self, text):
        l = list()
        conn = sqlite3.connect('debt.db', timeout=60)
        cur = conn.cursor()
        cur.execute("""  SELECT * from customer_debt
            WHERE name like (?)""", (text,))
        
        for columns in cur:
            l.append(columns)
        conn.commit()
        conn.close()
        return l

    def search_by_phone(self, text):
        l = list()
        conn = sqlite3.connect('debt.db', timeout=60)
        cur = conn.cursor()
        cur.execute("""  SELECT * from customer_debt
            WHERE phone like (?)""", (text,))
        for columns in cur:
            l.append(columns)
        conn.commit()
        conn.close()
        return l

    def search_by_description(self, text):
        l = list()
        conn = sqlite3.connect('debt.db', timeout=60)
        cur = conn.cursor()
        cur.execute("""  SELECT * from customer_debt
            WHERE description like (?)""", (text,))
        for columns in cur:
            l.append(columns)
        conn.commit()
        conn.close()
        return l

    def delete_record(self, row_id):
        conn = sqlite3.connect('debt.db', timeout=60)
        cur = conn.cursor()
        cur.execute("""  DELETE from customer_debt
            WHERE id = (?)""", (row_id,))
        conn.commit()
        conn.close()

    def get_debt_from_row(self, row_id):
        conn = sqlite3.connect('debt.db', timeout=60)
        cur = conn.cursor()
        cur.execute("""  SELECT debt from customer_debt
            WHERE id = (?)""", (row_id,))
        debt = cur.fetchone()
        conn.commit()
        conn.close()
        return debt

# d = customer_debt()
# t = d.search('name', '%300%')
# print(t)
