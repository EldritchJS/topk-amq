import psycopg2

conn = psycopg2.connect("""
    dbname=salesdb user=daikon password=daikon host=postgresql port=5432
    """)
cur = conn.cursor()

cur.execute("""
        SELECT * FROM sales
        WHERE itemid = %s;
        """,
        (itemID,))

if(cur.fetchone()==None):
    cur.execute("""
        INSERT INTO sales(itemid, quantity)
        VALUES(%s, %s);
        """,
        (itemID, 1))
else:
    cur.execute("""
        UPDATE sales
        SET quantity = quantity + 1
        WHERE itemid = %s;
        """,
        (itemID,))

conn.commit()
conn.close()

