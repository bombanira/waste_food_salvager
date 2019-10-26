from flask import Flask, request, abort, render_template,redirect

import psycopg2


conn = psycopg2.connect(
    '''
    dbname=d4bli17istimjb 
    host=ec2-174-129-43-40.compute-1.amazonaws.com
    user=jbzvogvoorcldg
    password=a87ca8b49a7286eff37cd854e52196e0e4e996feca64e19701dad2a8df3b704d
    '''
)
conn.autocommit = True

#とりあえず。
sql = "SELECT * FROM stores;"
with conn.cursor() as cur:
        cur.execute(sql)
        cur.fetchall()


## /notice　にPOSTでユーザと店舗情報を組み合わせてapp.pyに HTTPにリクエストを投げる。 
