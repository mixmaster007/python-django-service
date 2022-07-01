
from threading import Thread


from apps.home import cnio_api
import pprint
import time
import mysql.connector
import json



class TestThread(Thread):
    def connect_db():
        return 
   
    pp = pprint.PrettyPrinter(indent = 4)  
    cnio = cnio_api.cnio() 
    while True:
    # cnio.api_key(apiKey)
        try:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Richman929!@#$%",
            database='MyDatabase',
            auth_plugin='mysql_native_password'
            )
          
            mycursor =mydb.cursor(buffered=True)
            mycursorA = mydb.cursor(buffered=True)
            mycursorB = mydb.cursor(buffered=True)
            mycursor.execute("SELECT Api_key FROM home_paymentmanage ")
            myresult = mycursor.fetchall()
            pp.pprint(myresult[0][0])
            cnio.api_key(myresult[0][0])

           
            mycursor.execute("SELECT * FROM home_transaction  WHERE Transaction_Status != 'finished'")
            myresult = mycursor.fetchall()
            for mst in myresult:
                pp.pprint(mst[1])
                result = cnio.get_transaction_status(mst[1])
                new_res = result.decode('utf-8')
                json_res = json.loads(new_res)
                mycursorA = mydb.cursor(buffered=True)
                       
                
                spl = "UPDATE home_transaction SET Transaction_Status = %s WHERE Transaction_ID = %s"
                mycursorA.execute(spl,(json_res['status'],mst[1]))
                spl = "UPDATE home_transaction SET From_Ticket=%s  WHERE Transaction_ID = %s"
                mycursorA.execute(spl,(json_res['fromCurrency'],mst[1]))
                spl = "UPDATE home_transaction SET  USDT_Reciver_Address=%s  WHERE Transaction_ID = %s"
                mycursorA.execute(spl,(json_res['payinAddress'],mst[1]))
                spl = "UPDATE home_transaction SET  USDT_Reciver_Address=%s  WHERE Transaction_ID = %s"
                mycursorA.execute(spl,(json_res['payinAddress'],mst[1]))
                spl = "UPDATE home_transaction SET  USDT_Reciver_Address=%s  WHERE Transaction_ID = %s"
                mycursorA.execute(spl,(json_res['payinAddress'],mst[1]))
               # spl = "UPDATE home_transaction SET  Deposit_Received_At=%s  WHERE Transaction_ID = %s"
                #mycursorA.execute(spl,(json_res['createdAt'],mst[1]))
               
                #m_trans_array.filter(Transaction_ID =t_id).update(Deposit_Received_At=json_res['createdAt'],User_Balance_updated_At=json_res['updatedAt'])
                #m_trans_array.filter(Transaction_ID =t_id).update(From_Ticket=json_res['fromCurrency'],USDT_Reciver_Address=json_res["payinAddress"],Transaction_Status=json_res["status"])
                #spl = "UPDATE home_transaction SET From_Ticket=%s  WHERE Transaction_ID = %s"
                #mycursorA.execute(spl,(json_res['status'],json_res['fromCurrency'],mst[1]))
                mydb.commit()
               
                if json_res['status'] == "finished":
                
                    spl = "SELECT * FROM auth_user WHERE username= %s"
                    pp.pprint(mst[8])
                    mycursorA.execute(spl,(mst[8],))
                    tmp_user_id = mycursorA.fetchall()
                    m_balance = float(mst[9]) + float(json_res['amountReceive'])
                    pp.pprint(m_balance)
                    pp.pprint(tmp_user_id[0][0])
                    spl = "UPDATE home_balance SET balance =%s WHERE user_id= %s"
                    mycursorA.execute(spl,(str(m_balance),str(tmp_user_id[0][0]),))
                    spl = "UPDATE home_transaction SET User_Balance =%s WHERE Transaction_ID = %s"
                    mycursorA.execute(spl,(str(m_balance),mst[1],))
                   # spl = "UPDATE home_transaction SET  User_Balance_updated_At=%s  WHERE Transaction_ID = %s"
                   # mycursorA.execute(spl,(json_res['updatedAt'],mst[1]))
                    spl = "UPDATE home_transaction SET  Amount_Recived=%s  WHERE Transaction_ID = %s"
                    mycursorA.execute(spl,(json_res['amountReceive'],mst[1]))
                    mydb.commit()
                   
                    
                   # balance.objects.filter(user=user).update(balance = m_balance)
                    #m_trans_array.filter(Transaction_ID =t_id).update(Amount_Recived=json_res['amountReceive'],User_Balance=m_balance)
                #sql = "UPDATE customers SET address = 'Canyon 123' WHERE id = 'Valley 345'"
               # mycursor.execute("UPDATE home_transaction SET address = 'Canyon 123' WHERE id = 'Valley 345'")
                pp.pprint(json_res)
            mycursorA.close()
            mycursor.close()
            mydb.close()
            time.sleep(1) # train the model every 5 minutes
        except Exception as e:
            print(e)
    

   
