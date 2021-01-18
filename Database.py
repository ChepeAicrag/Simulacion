import sqlite3

def load_data_in_db(fileName, table):
    conn = sqlite3.connect('spider.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS ''' + table 
        + ''' (id INTEGER PRIMARY KEY AUTOINCREMENT, from_node_id INTEGER, to_node_id INTEGER, weight_node INTEGER)''')
    conn.commit()
    cur.execute('''SELECT * FROM ''' + table)
    r = cur.fetchone()
    if r is None:
        try:
            file = open('./Datasets/' + fileName)    
        except EOFError:
            return False
        for line in file:
            n, m, w = line.split()
            cur.execute('INSERT INTO ' + table + ' (from_node_id, to_node_id, weight_node) VALUES (?, ?, ?)',(n,m,w))
        conn.commit()
        return True    
    else:
        print('Ya existe base de datos')
        return True