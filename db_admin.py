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

def get_loan_report(cus_id):
    sql = "select loan_id,loan_amount,repay_term from accounts_loans where customer_id = %s"
    cur.execute(sql, (cus_id,))
    res = cur.fetchall()
    return res

def get_fd_report(cus_id):
    sql = "select account_no,amount,deposit_term from accounts_fd where customer_id = %s"
    cur.execute(sql, (cus_id,))
    res = cur.fetchall()
    return res
