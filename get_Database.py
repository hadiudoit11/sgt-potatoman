import psycopg2

DB_NAME = "jwjuiwdg"
DB_USER = "jwjuiwdg"
DB_PASS = "o8dUXLTQev50L-yuZ8F8mRllAvFCoNke"
DB_HOST = "rajje.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                            password = DB_PASS, host = DB_HOST, port = DB_PORT)

cur = conn.cursor()
cur.execute("""SELECT body_Review FROM review_data;""")
database_Response = cur.fetchone()

body_Response = {
    'body_Review' : []
}

def runGetDatabase():
    body_Response['body_Review'].append('{}'.format(database_Response))
    conn.commit()
    return \
        body_Response

conn.close()