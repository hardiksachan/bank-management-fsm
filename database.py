import datetime

from classes.accounts import AccountType, TransactionType, AccountStatus
from classes.current_account import Current
from classes.customer import Customer
from classes.savings_account import Savings
from connection import con, cur, database_name


def make_all_tables():
    sql = f"""SELECT count(*) 
                FROM information_schema.tables
                WHERE table_schema = '{database_name}'
                AND table_name = 'customers'
                LIMIT 1;"""
    cur.execute(sql)
    res = cur.fetchall()

    if res[0][0] != 0:
        return

    sql = """create table customers(
                      customer_id int(5) auto_increment primary key,
                      first_name varchar(10),
                      last_name varchar(10),
                      status varchar(10),
                      login_attempts int(3),
                      password varchar(20))"""
    cur.execute(sql)

    sql = """create table address(
                      customer_id int(5),
                      line1 varchar(30),
                      line2 varchar(30),
                      city varchar(30),
                      state varchar(30),
                      pincode int(6),
                      constraint fk_addr foreign key(customer_id) references customers(customer_id))"""
    cur.execute(sql)

    sql = """create table accounts(
                      customer_id int(5),
                      account_no int(5) auto_increment primary key,
                      opened_on date,
                      account_type varchar(10),
                      status varchar(10),
                      balance int(8),
                      withdrawals_left int(3),
                      next_reset_date date,
                      constraint fk_acc foreign key(customer_id) references customers(customer_id))"""
    cur.execute(sql)

    sql = """create table fd(
                      account_no int(5) primary key,
                      amount int(8),
                      deposit_term int(5),
                      constraint fk_fd_acc foreign key(account_no) references accounts(account_no))"""
    cur.execute(sql)

    sql = """create table loans(
                      customer_account_no int(5),
                      loan_id int(5) auto_increment primary key,
                      loan_amount int(8),
                      repay_term int(5),
                      constraint fk_loan_acc foreign key(customer_account_no) references accounts(account_no))"""
    cur.execute(sql)

    sql = """create table transactions(
                      transaction_id int(5) auto_increment primary key,
                      account_no int(5),
                      type varchar(10),
                      amount int(8),
                      balance int(8),
                      transaction_date date,
                      constraint fk_transaction_account_no foreign key(account_no) references accounts(account_no))"""
    cur.execute(sql)

    sql = """create table admin(
                      admin_id int(5),
                      password varchar(10))"""
    cur.execute(sql)

    sql = """create table closed_accounts(
                      account_no int(5),
                      closed_on date,
                      constraint fk_closed_acc foreign key(account_no) references accounts(account_no))"""
    cur.execute(sql)

    sql = """create or replace view accounts_fd as
                    select a.customer_id,a.account_no,fd.amount,fd.deposit_term from accounts a,fd where a.account_no = fd.account_no"""
    cur.execute(sql)

    sql = """create or replace view accounts_loans as
                    select a.customer_id,a.account_no,loans.loan_id,loans.loan_amount,loans.repay_term from accounts a,loans
                    where a.account_no = loans.customer_account_no"""
    cur.execute(sql)

    sql = "insert into admin values(227,'helloadmin')"
    cur.execute(sql)


def sign_up_customer(customer):
    fname = customer.get_first_name()
    lname = customer.get_last_name()
    password = customer.get_password()
    status = customer.get_status()
    att = customer.get_login_attempts()
    sql = "insert into customers(first_name, last_name, status, login_attempts, password) " \
          "values(%s,%s,%s,%s,%s)"
    data = (fname, lname, status, att, password)
    cur.execute(sql, data)
    customer_id = int(cur.lastrowid)
    line1 = customer.get_addr_line1()
    line2 = customer.get_addr_line2()
    city = customer.get_addr_city()
    state = customer.get_addr_state()
    pincode = customer.get_addr_pincode()
    sql = "insert into address values(%s,%s,%s,%s,%s,%s)"
    data = (customer_id, line1, line2, city, state, pincode)
    cur.execute(sql, data)
    con.commit()
    print("Congratulations ! Your Account was Created Successfully")
    print("Your Customer ID : ", customer_id)


def login_customer(c_id, password):
    sql = "select count(*) from customers where customer_id = %s and password = %s"
    cur.execute(sql, (c_id, password))
    res = cur.fetchall()
    count = res[0][0]
    if count == 1:
        return True
    else:
        return False


def open_new_account_customer(account, cus_id):
    withdrawals_left = None
    account_type = account.get_account_type()
    bal = account.get_balance()
    opened_on = datetime.datetime.now().strftime("%Y-%m-%d")
    status = AccountStatus.open
    if account_type == AccountType.savings:
        withdrawals_left = 10
    sql = "select date_add(CURRENT_DATE(), INTERVAL 1 MONTH) from dual"
    cur.execute(sql)
    res = cur.fetchall()
    next_date = res[0][0].strftime("%Y-%m-%d")
    sql = "insert into accounts(customer_id, opened_on, account_type, status, balance, withdrawals_left, next_reset_date) " \
          "values(%s, %s, %s, %s, %s, %s, %s);"
    data = (cus_id, opened_on, account_type.value, status.value, bal, withdrawals_left, next_date)
    cur.execute(sql, data)
    acc_no = int(cur.lastrowid)
    if account_type == "fd":
        term = account.get_deposit_term()
        sql = "insert into fd values (%s,%s,%s)"
        data = (acc_no, bal, term)
        cur.execute(sql, data)

    con.commit()
    print("Account Opened Successfully")
    print("Account No is : ", acc_no)


def change_address_customer(ch, _id, addr):
    if ch == 1:
        sql = "update address set line1 = %s where customer_id = %s"
        cur.execute(sql, (addr, _id))

    elif ch == 2:
        sql = "update address set line2 = %s where customer_id = %s"
        cur.execute(sql, (addr, _id))

    elif ch == 3:
        sql = "update address set state = %s where customer_id = %s"
        cur.execute(sql, (addr, _id))

    elif ch == 4:
        sql = "update address set city = %s where customer_id = %s"
        cur.execute(sql, (addr, _id))

    elif ch == 5:
        sql = "update address set pincode = %s where customer_id = %s"
        cur.execute(sql, (addr, _id))

    else:
        return

    con.commit()
    print("Details Updated Successfully")


def get_all_info_customer(id):
    sql = "select * from customers where customer_id = %s"
    cur.execute(sql, (id,))
    res = cur.fetchall()
    if len(res) == 0:
        return None
    customer = Customer()
    status = res[0][3]
    att = res[0][4]
    customer.set_customer_id(id)
    customer.set_status(status)
    customer.set_login_attempts(att)
    return customer


def get_all_info_account(acc_no, id, msg):
    account = None
    sql = None
    if msg == "transfer":
        sql = "select * from accounts where account_no = %s and account_type != 'fd' and status = 'open'"
        cur.execute(sql, (acc_no))
    elif msg == "loan":
        sql = "select * from accounts where account_no = %s and customer_id = %s and account_type = 'savings' and status = 'open'"
        cur.execute(sql, (acc_no, id))
    else:
        sql = "select * from accounts where account_no = %s and customer_id = %s and account_type != 'fd' and status = 'open'"
        cur.execute(sql, (acc_no, id))

    res = cur.fetchall()
    if len(res) == 0:
        return None

    account_no = res[0][1]
    account_type = res[0][3]
    balance = res[0][5]
    wd_left = res[0][6]
    if account_type == "savings":
        account = Savings()
    else:
        account = Current()

    account.set_account_type(account_type)
    account.set_balance(balance)
    account.set_account_no(account_no)
    account.set_withdrawals_left(wd_left)
    return account


def money_deposit_customer(account, amount):
    bal = account.get_balance()
    acc_no = account.get_account_no()
    type = TransactionType.credit
    sql = "update accounts set balance = %s where account_no = %s"
    cur.execute(sql, (bal, acc_no))
    sql = "insert into transactions(account_no, type, amount, balance, transaction_date) values (%s, %s, %s, %s, %s);"
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    data = (acc_no, type, amount, bal, date)
    cur.execute(sql, data)
    con.commit()


def money_withdraw_customer(account, amount, msg):
    acc_type = account.get_account_type()
    wd_left = account.get_withdrawals_left()
    bal = account.get_balance()
    acc_no = account.get_account_no()
    type = TransactionType.debit
    sql = "update accounts set balance = %s where account_no = %s"
    cur.execute(sql, (bal, acc_no))
    sql = "insert into transactions(account_no, type, amount, balance, transaction_date) values (%s, %s, %s, %s, %s);"
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    data = (acc_no, type, amount, bal, date)
    cur.execute(sql, data)
    if acc_type == AccountType.savings and msg != "transfer":
        wd_left -= 1
        sql = "update accounts set withdrawals_left = %s where account_no = %s"
        cur.execute(sql, (wd_left, acc_no))
    con.commit()


def get_transactions_account(acc_no, date_from, date_to):
    sql = """select transaction_date,type,amount,balance from transactions where account_no = %s
              and transaction_date between %s and %s order by transaction_id"""
    cur.execute(sql, (acc_no, date_from, date_to))
    res = cur.fetchall()
    return res


def transfer_money_customer(account_sender, account_receiver, amount):
    if account_sender.withdraw(amount):
        account_receiver.deposit(amount)
        money_withdraw_customer(account_sender, amount, "transfer")
        money_deposit_customer(account_receiver, amount)
        print("Transfer Completed !")
        print("New Balance for Account No ", account_sender.get_account_no(), " : ", account_sender.get_balance())
        print("New Balance for Account No ", account_receiver.get_account_no(), " : ", account_receiver.get_balance())


def login_admin(id, password):
    sql = "select count(*) from admin where admin_id = %s and password = %s"
    cur.execute(sql, (id, password))
    res = cur.fetchall()
    count = res[0][0]
    if count == 1:
        return True
    else:
        return False


def close_account_customer(account):
    acc_no = account.get_account_no()
    balance = account.get_balance()
    sql = "update accounts set status='closed',balance = 0 where account_no = %s"
    cur.execute(sql, (acc_no,))
    closed_on = datetime.datetime.now().strftime("%Y-%m-%d")
    sql = "insert into closed_accounts values(%s, %s)"
    cur.execute(sql, (acc_no, closed_on))
    print("Account Closed Successfully !")
    print("Rs ", balance, " will be delivered to your address shortly")
    con.commit()


def get_loan_customer(acc_no, loan_amt, loan_term):
    sql = "insert into loans(customer_account_no, loan_amount, repay_term) values (%s,%s,%s)"
    cur.execute(sql, (acc_no, loan_amt, loan_term))
    con.commit()
    print("Loan Availed Successfully")


def reset_withdrawals():
    sql = """update accounts set withdrawals_left = 10,next_reset_date = date_add(next_reset_date, interval 1 month)
              where account_type = 'savings' and curdate() >= next_reset_date"""
    cur.execute(sql)
    con.commit()


def reset_login_attempts(id):
    sql = "update customers set login_attempts = 3 where customer_id = %s"
    cur.execute(sql, (id,))
    con.commit()


def update_customer(customer):
    id = customer.get_customer_id()
    status = customer.get_status()
    att = customer.get_login_attempts()
    sql = "update customers set status = %s,login_attempts = %s where customer_id = %s"
    cur.execute(sql, (status, att, id))
    con.commit()
