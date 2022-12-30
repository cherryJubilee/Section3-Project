import pymysql

RDS_ENDPOINT = '127.0.0.1'
RDS_PORT = 3306
RDS_USER = 'root'
RDS_PASSWORD = '12345678'
RDS_DATABASE = 'survey_proj'
RDS_TABLE = 'survey'

# ---------RDS Connect--------------
conn = pymysql.connect(
    host=RDS_ENDPOINT,
    port=RDS_PORT,
    user=RDS_USER,
    password=RDS_PASSWORD,
    db=RDS_DATABASE
)


# --------Table Creation----------
def createTable():
    cursor = conn.cursor()
    create_table_sql = f"""
        create table {RDS_TABLE} (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            answer01 INT NOT NULL,
            answer02 INT NOT NULL,
            answer03 INT NOT NULL,
            answer04 INT NOT NULL,
            answer05 INT NOT NULL
            );
        """
    try:  # 테이블이 없으때만 실행
        cursor.execute(create_table_sql)
    except:
        print('Table Already Exist')


# ------------INSERT QUERY----------
def insertHuman(name, contact, resume, blog):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {RDS_TABLE} (name,contact,resume,blog) VALUES (%s,%s,%s,%s)",
                (name, contact, resume, blog))
    conn.commit()


# -----------RDS INSERT FUNCTION---------
def insertData(answer):
    cur = conn.cursor()
    cur.execute(f"""
        INSERT INTO {RDS_TABLE} (answer01, answer02, answer03, answer04, answer05)
        VALUES ('{answer[0]}', '{answer[1]}', '{answer[2]}', '{answer[3]}', '{answer[4]}') 
    """)
    conn.commit()


createTable()
