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
            answer05 INT NOT NULL,
            answer_mbti INT NOT NULL
            );
        """
    try:  # 테이블이 없으때만 실행
        cursor.execute(create_table_sql)
    except:
        print('Table Already Exist')


# -----------RDS INSERT FUNCTION---------
def insertData(answer):
    cur = conn.cursor()
    mbti_dict = {
        "ESFP": "0",
        "ESFJ": "1",
        "ESTP": "2",
        "ESTJ": "3",
        "ENFP": "4",
        "ENFJ": "5",
        "ENTP": "6",
        "ENTJ": "7",
        "ISFP": "8",
        "ISFJ": "9",
        "ISTP": "10",
        "ISTJ": "11",
        "INFP": "12",
        "INFJ": "13",
        "INTP": "14",
        "INTJ": "15"
    }
    cur.execute(f"""
        INSERT INTO {RDS_TABLE} (answer01, answer02, answer03, answer04, answer05, answer_mbti)
        VALUES ('{answer[0]}', '{answer[1]}', '{answer[2]}', '{answer[3]}', '{answer[4]}', '{mbti_dict[answer[5]]}') 
    """)
    conn.commit()


createTable()
