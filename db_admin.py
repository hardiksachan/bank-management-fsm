from connection import cur, con


def check_customer_exists(id):
    sql = "select count(*) from customers where customer_id = %s"
    cur.execute(sql, (id,))
    res = cur.fetchall()
    count = res[0][0]
    if count == 1:
        return True
    else:
        return False
