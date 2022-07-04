import requests
import pprint
from threading import Thread
import threading
import pprint
import time
import mysql.connector
import json
from datetime import datetime
def get_status(api,phonenumber,day,month,year,zipcode,gatelink):
    pp = pprint.PrettyPrinter(indent = 4)  
    endpoint = str("phonenumber="+phonenumber+"&day="+day+"&month="+month+"&year="+year+"&zipcode="+zipcode+"&gatelink="+gatelink)
    endpoint = str(api + endpoint)
    pp.pprint(endpoint)
    return requests.get(endpoint).content
def getData_Thread(api,user_id,price,id,phonenumber,day,month,year,zipcode,gatelink):
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Richman929!@#$%",
        database='MyDatabase',
        auth_plugin='mysql_native_password'
        )
    except:
        pp = pprint.PrettyPrinter(indent = 4) 
        pp.pprint("Error MyDB connect in getData_Thread")
    mycursor =mydb.cursor(buffered=True)
    pp= pprint.PrettyPrinter(indent=4)
    pp.pprint("GetData_Thread START")

    m_result = get_status(api,phonenumber,day,month,year,zipcode,gatelink) 
    pp.pprint(m_result)
    mydb.commit() 
    if (m_result == bytes("phone registered successfully", 'utf-8') or m_result == bytes("Registration success", 'utf-8')) or (m_result == bytes("Thank you for your Registration", 'utf-8')):
        pp.pprint("_________________Success__________________")
        tmp = "UPDATE home_gate SET result1 =%s WHERE id= %s"
        mycursor.execute(tmp,("phone registered successfully",int(id)))
        tmp = "UPDATE home_gate SET result2 =%s WHERE id= %s"
        mycursor.execute(tmp,("Date accepted",int(id)))
        tmp = "UPDATE home_gate SET result3 =%s WHERE id= %s"
        mycursor.execute(tmp,("zipcode accepted",int(id)))
        tmp = "UPDATE home_gate SET status =%s WHERE id= %s"
        mycursor.execute(tmp,(3,int(id)))
        
        tmp = "UPDATE home_gate SET result5 =%s WHERE id= %s"
        mycursor.execute(tmp,(float(price),int(id)))
        
        mydb.commit()  
    elif (m_result == bytes("Phone Registration Fails .", 'utf-8') or m_result == bytes("Phone number is no more active.", 'utf-8')) or (m_result == bytes("Please check your phone number.", 'utf-8')):
        pp.pprint("_________________ERROR__________________")
        tmp = "UPDATE home_gate SET result2 =%s WHERE id= %s"
        mycursor.execute(tmp,("Phone Registration Fails",int(id)))
        tmp = "UPDATE home_gate SET result2 =%s WHERE id= %s"
        mycursor.execute(tmp,("Registration Fails",int(id)))
        tmp = "UPDATE home_gate SET result3 =%s WHERE id= %s"
        mycursor.execute(tmp,("Registration Fails",int(id)))
        tmp = "UPDATE home_gate SET status =%s WHERE id= %s"
        mycursor.execute(tmp,(3,int(id)))
        tmp = "UPDATE home_gate SET result5 =%s WHERE id= %s"
        mycursor.execute(tmp,(0.00,int(id)))

        tmp = "SELECT balance FROM home_balance WHERE user_id=%s"
        m_userID = int(user_id)
        mycursor.execute(tmp,(m_userID,))
        m_result = mycursor.fetchall()
        m_userBalance = float(m_result[0][0])
        m_userBalance = m_userBalance + float(price)
        tmp = "UPDATE home_balance SET balance =%s WHERE user_id= %s"
        mycursor.execute(tmp,(format(m_userBalance,".2f"),m_userID))

        mydb.commit() 

     
    elif (m_result == bytes("Please try again ", 'utf-8') or m_result == bytes("Please try again later", 'utf-8')) or (m_result == bytes("Problem while processing your request. ", 'utf-8'))  :
   
        pp.pprint("__________________ERROR1_________________")
        tmp = "UPDATE home_gate SET result1 =%s WHERE id= %s"
        mycursor.execute(tmp,("Please try again Later",int(id)))
        tmp = "UPDATE home_gate SET result2 =%s WHERE id= %s"
        mycursor.execute(tmp,("-",int(id)))
        tmp = "UPDATE home_gate SET result3 =%s WHERE id= %s"
        mycursor.execute(tmp,("-",int(id)))
        tmp = "UPDATE home_gate SET status =%s WHERE id= %s"
        mycursor.execute(tmp,(2,int(id)))
        tmp = "UPDATE home_gate SET result5 =%s WHERE id= %s"
        mycursor.execute(tmp,(0.00,int(id)))

        tmp = "SELECT balance FROM home_balance WHERE user_id=%s"
        m_userID = int(user_id)
        mycursor.execute(tmp,(m_userID,))
        m_result = mycursor.fetchall()
        m_userBalance = float(m_result[0][0])
        m_userBalance = m_userBalance + float(price)
        tmp = "UPDATE home_balance SET balance =%s WHERE user_id= %s"
        mycursor.execute(tmp,(format(m_userBalance,".2f"),m_userID))


        mydb.commit() 
    elif(m_result == bytes("Can’t process your request at the moment", 'utf-8') or m_result == bytes("Service is over load please try again later", 'utf-8')):
        pp.pprint("__________________ERROR1_________________")
        tmp = "UPDATE home_gate SET result1 =%s WHERE id= %s"
        mycursor.execute(tmp,("Please try again Later",int(id)))
        tmp = "UPDATE home_gate SET result2 =%s WHERE id= %s"
        mycursor.execute(tmp,("-",int(id)))
        tmp = "UPDATE home_gate SET result3 =%s WHERE id= %s"
        mycursor.execute(tmp,("-",int(id)))
        tmp = "UPDATE home_gate SET status =%s WHERE id= %s"
        mycursor.execute(tmp,(2,int(id)))
        tmp = "UPDATE home_gate SET result5 =%s WHERE id= %s"
        mycursor.execute(tmp,(0.00,int(id)))

        tmp = "SELECT balance FROM home_balance WHERE user_id=%s"
        m_userID = int(user_id)
        mycursor.execute(tmp,(m_userID,))
        m_result = mycursor.fetchall()
        m_userBalance = float(m_result[0][0])
        m_userBalance = m_userBalance + float(price)
        tmp = "UPDATE home_balance SET balance =%s WHERE user_id= %s"
        mycursor.execute(tmp,(format(m_userBalance,".2f"),m_userID))


        mydb.commit()
    else :
        pp.pprint("__________________ERROR1_________________")
        tmp = "UPDATE home_gate SET result1 =%s WHERE id= %s"
        mycursor.execute(tmp,("Unknown error please contact support ",int(id)))
        tmp = "UPDATE home_gate SET status =%s WHERE id= %s"
        mycursor.execute(tmp,(2,int(id)))
        tmp = "SELECT balance FROM home_balance WHERE user_id=%s"
        m_userID = int(user_id)
        mycursor.execute(tmp,(m_userID,))
        m_result = mycursor.fetchall()
        m_userBalance = float(m_result[0][0])
        m_userBalance = m_userBalance + float(price)
        tmp = "UPDATE home_balance SET balance =%s WHERE user_id= %s"
        mycursor.execute(tmp,(format(m_userBalance,".2f"),m_userID))


        mydb.commit() 

    ##Batch Status Update___RUNNIG(1) ######################################
    tmp = "SELECT batch_id FROM home_gate WHERE id= %s"
    mycursor.execute(tmp,(int(id),))
    m_result = mycursor.fetchall()
    m_batchID = int(m_result[0][0])

    tmp = "SELECT status FROM home_gate WHERE batch_id= %s"
    mycursor.execute(tmp,(m_batchID,))
    m_result = mycursor.fetchall()
    pp.pprint(m_batchID)
    pp.pprint("______________BATHID_GATE_STATUS____")
    m_inq = 0
    m_proc = 0
    m_fail = 0
    m_done = 0

    for ii in m_result:
        if ii[0] == 0:
            m_inq +=1
        elif ii[0] == 1:
            m_proc += 1
        elif ii[0] == 2:
            m_fail += 1
        elif ii[0] == 3:
            m_done += 1
    tmp = "UPDATE home_batch SET succeed =%s WHERE batch_id= %s"
    mycursor.execute(tmp,(int(m_done),m_batchID))
    tmp = "UPDATE home_batch SET done =%s WHERE batch_id= %s"
    m_fd = m_fail+m_done
    mycursor.execute(tmp,(int(m_fd),m_batchID))
    tmp = "UPDATE home_batch SET fail =%s WHERE batch_id= %s"
    mycursor.execute(tmp,(int(m_fail),m_batchID))
    tmp = "UPDATE home_batch SET remains =%s WHERE batch_id= %s"
    m_reamin =m_inq+m_proc
    mycursor.execute(tmp,(int(m_reamin),m_batchID))
    if m_inq == 0 and m_proc == 0:
        tmp = "UPDATE home_batch SET status =%s WHERE batch_id= %s"
        mycursor.execute(tmp,("Finished",m_batchID))
       
   
    mydb.commit()
    mycursor.close()
    mydb.close()
    pp.pprint("GetData_Thread END")
    return 