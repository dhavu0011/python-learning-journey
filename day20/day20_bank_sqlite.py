import sqlite3
def connect_db():
    connection = sqlite3.connect("bank1.db")
    cursor = connection.cursor()
    return connection, cursor

def add_account():
    account_name=input("Enter name:")
    while True:
        try:
            account_number = int(input("Enter account number: "))
            break
        except ValueError:
            print("Please enter numbers only.")
    account_type=input("Account type:")
    while True:
        try:
            balance=int(input("Enter balance:"))
            break
        except ValueError:
            
            
            print("Please enter numbers only.")
    
    connection, cursor = connect_db()
    try:
        cursor.execute(
            """
            INSERT INTO bank1
            (account_name, account_number, account_type, balance)
            VALUES (?, ?, ?, ?)
            """,
            (account_name, account_number, account_type, balance)
            )
        connection.commit()
        print("Account added successfully.\n")
        
    except sqlite3.IntegrityError:
        print("Account number already exist.")
    
    finally:
        connection.close()
    
    
def show_accounts():
    connection, cursor = connect_db()
    try:
        cursor.execute("SELECT * from bank1")
        rows=cursor.fetchall()
        if not rows:
            print("No accounts found.")
        else:
            for row in rows:
                print("ID:", row[0])
                print("Holder:", row[1])
                print("Number:", row[2])
                print("Type:", row[3])
                print("Balance:", row[4])
                print("----------------")
    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        connection.close()


def deposit():
    connection, cursor = connect_db()
    while True:
        try:
            account_number = int(input("Enter account number: "))
            break
        except ValueError:
            print("Please enter numbers only.")
    cursor.execute(
        "SELECT * FROM bank1 WHERE account_number = ?",
        (account_number,)
    )
    account = cursor.fetchone()
    if account is None:
        print("Account not found.")
    else:
        while True:
            try:
                deposit_amount = int(input("Enter deposit amount: "))
                break
            except ValueError:
                print("Please enter numbers only.")
        if deposit_amount <= 0:
            print("Enter a valid deposit amount.")
        else:
            try:
                cursor.execute(
                    """
                    UPDATE bank1 
                    SET balance = balance + ?
                    WHERE account_number = ?
                    """,
                    (deposit_amount, account_number)
                    )
                connection.commit()
                print("Deposit successful.")
            except sqlite3.Error as error:
                print("Database error:", error)

    connection.close()
    
    
def withdraw():
    connection, cursor = connect_db()

    while True:
        try:
            account_number = int(input("Enter account number: "))
            break
        except ValueError:
            print("Please enter numbers only.")

    cursor.execute(
        "SELECT * FROM bank1 WHERE account_number = ?",
        (account_number,)
    )

    account = cursor.fetchone()

    if account is None:
        print("Account not found.")
    else:
        while True:
            try:
                withdraw_amount = int(input("Enter withdraw amount: "))
                break
            except ValueError:
                print("Please enter numbers only.")
        if withdraw_amount <= 0:
            print("Enter a valid withdraw amount.")
        elif withdraw_amount <= account[4]:
            cursor.execute(
                """
                UPDATE bank1
                SET balance = balance - ?
                WHERE account_number = ?
                """,
                (withdraw_amount, account_number)
            )
            connection.commit()
            print("Withdraw successful.")
            
        else:
            print("Insufficient funds.")

    connection.close()

def transfer():
    connection, cursor = connect_db()
    try:
        while True:
            try:
                sender_number = int(input("Enter sender account number: "))
                break
            except ValueError:
                print("Please enter numbers only.")
        cursor.execute(
            "SELECT * FROM bank1 WHERE account_number = ?",
            (sender_number,)
            )
        sender = cursor.fetchone()
        if sender is None:
            print("Sender account not found")
        else:
            while True:
                try:
                    receiver_number = int(input("Enter receiver account number: "))
                    break
                except ValueError:
                    print("Please enter numbers only.")
            cursor.execute(
                "SELECT * FROM bank1 Where account_number = ?",
                (receiver_number,)
                )
            receiver=cursor.fetchone()

            if receiver is None:
                print("Receiver account not found")
            else:
                while True:
                    try:
                        transfer_amount = int(input("Enter transfer amount: "))
                        break
                    except ValueError:
                        print("Please enter numbers only.")
                if transfer_amount <= 0:
                    print("Invalid amount")
                elif transfer_amount <= sender[4]:
                    
                    cursor.execute(
                        """
                        UPDATE bank1
                        SET balance = balance - ?
                        WHERE account_number = ?
                        """,
                        (transfer_amount, sender_number)
                        )
                    cursor.execute(
                        """
                        UPDATE bank1
                        SET balance = balance + ?
                        WHERE account_number = ?
                        """,
                        (transfer_amount, receiver_number)
                        )
                    connection.commit()
                    print("Transfer successful.")
                else:
                    print("Insufficient funds.")
    except sqlite3.Error as error:
        connection.rollback()
        print("Transfer failed.")
        print("Database error:", error)
    finally:
        connection.close()
                
def delete_account():
    connection,cursor= connect_db()
    try:
        while True:
            try:
                delete_acc = int(input("Enter account number to delete: "))
                break
            except ValueError:
                print("Please enter numbers only.")

        cursor.execute(
            "SELECT * FROM bank1 WHERE account_number = ?",
            (delete_acc,)
        )

        del_account = cursor.fetchone()

        if del_account is None:
            print("Account not found.")
        else:
            cursor.execute(
                "DELETE FROM bank1 WHERE account_number = ?",
                (delete_acc,)
            )

            connection.commit()
            print("Account deleted successfully.")

    except sqlite3.Error as error:
        print("Error deleting account:", error)

    finally:
        connection.close()
            
def search_account():
    connection,cursor=connect_db()
    while True:
        try:
            search_acc_number=int(input("Enter account number to search:"))
            break
        except ValueError:
            print("Please enter numbers only.")
    cursor.execute(
        "SELECT * from bank1 where account_number=?",
        (search_acc_number,)
        )
    searched_acc=cursor.fetchone()
    if searched_acc is None:
        print("Account not found.")
    else:
        print("ID:", searched_acc[0])
        print("Holder:", searched_acc[1])
        print("Number:", searched_acc[2])
        print("Type:", searched_acc[3])
        print("Balance:", searched_acc[4])
        print("----------------")
    
    connection.close()
    
    
while True:
    try:
        print("""
        1.Add account
        2.Show accounts
        3.deposit
        4.Withdraw
        5.Transfer
        6.Delete account
        7.Search account
        8.exit
        """)
        choice=int(input("Enter choice:"))
    except ValueError:
        print("Please enter numbers only.")
        continue
    if choice==1:
        add_account()
    elif choice==2:
        show_accounts()
    elif choice ==3:
        deposit()
    elif choice==4:
        withdraw()
    elif choice==5:
        transfer()
    elif choice==6:
        delete_account()
    elif choice==7:
        search_account()
    elif choice==8:
        print("Goodbye.")
        break
    else:
        print("Wrong input.")
    