import mysql.connector as con
from mysql.connector import errorcode
import datetime as dt
import pytz as tz

#isodate lib to parse the ISO 8601 format into date time,
#for example: PT30M = 30 mins
import isodate


def get_ven_energy(DB):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)
      #for dynamic operation
      #endday=str(dt.date.today())
      #startday=str(dt.date.today()-dt.timedelta(days=1))
      startday='2013-04-05'
      endday='2013-06-06'
      print startday,endday
      cursor.execute("select DATE(dtstamp) as groupday, SUM(energy) from test.venusage where dtstamp>=%s and dtstamp<=%s GROUP BY DATE (groupday) ORDER BY groupday",(startday,endday,))
      data = cursor.fetchall()
      #print data
      temp=[]
      temp.append(['Date','EnergyUsage'])
      for time,power in data:
          temp.append([str(time)[5:],power])
      return temp

    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()


def get_ven_power(DB):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)
      #for dynamic operation
      #endday=str(dt.date.today())
      #startday=str(dt.date.today()-dt.timedelta(days=1))
      startday='2013-01-05'
      endday='2013-01-06'
      print startday,endday
      cursor.execute("select dtstamp,power from test.venpower where dtstamp>=%s and dtstamp<=%s",(startday,endday,))
      data = cursor.fetchall()
      #print data
      temp=[]
      for time,power in data:
          temp.append([str(time)[-8:-3],power])
      return temp

    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()

def get_events(DB):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)
      #for dynamic operation
      endday=str(dt.date.today())
      startday=str(dt.date.today()-dt.timedelta(days=120)) #get the event timeline for 120 days

      #startday='2013-01-01'
      #endday='2013-01-30'


      print startday,endday
      cursor.execute("select eventStatus,eventID,startTime,duration from test.eventinfo where startTime>=%s AND startTime<=%s ORDER BY startTime",(startday, endday,))
      data = cursor.fetchall()
      #print data
      temp=[]
      for eventStatus, eventID,startTime,duration in data:
          temp.append([str(eventStatus),str(eventID),str(startTime),str(startTime + isodate.parse_duration(duration))]) # the final element is the event end time = startTime + duration
      return temp

    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()

def get_ven_log(DB):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)
      #for dynamic operation

      current_time = dt.datetime.now()
      print(current_time.tzinfo)
      print(current_time)

      timezone = tz.timezone("Europe/London")
      #print(timezone)

      local_time = timezone.localize(current_time)
      print(local_time.tzinfo)
      print(local_time)

      endday=str(dt.date.today())
      startday=str(dt.date.today()-dt.timedelta(days=1))


      print("Startday is: %s" %startday)
      print("Endday is: %s" %endday)

      #startday='2018-07-19'
      #endday='2018-07-19'
      #print startday,endday
      #cursor.execute("select * from test.venlog where dtstamp>=%s and dtstamp<=%s ORDER BY dtstamp",(startday,endday,))

      cursor.execute("select dtstamp, responseTime, venRequest, vtnResponse, responseCode, responseDescription from test.venlog where DATE(dtstamp)>=%s and DATE(dtstamp)<=%s ORDER BY dtstamp DESC", (startday, endday))
      data = cursor.fetchall()
      #print data
      temp=[]
      for dtstamp, responseTime, venRequest, vtnResponse, responseCode, responseDescription in data:
          temp.append([str(dtstamp),str(responseTime),str(venRequest),str(vtnResponse),str(responseCode),str(responseDescription)])
      return temp

    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()


def get_ven_info(DB):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)
      cursor.execute("select venName, venID, vtnID, vtnURL, pollFrequency from test.veninfo where recordID=1")
      data = cursor.fetchall()
      #print data
      temp=[]
      for venName, venID, vtnID, vtnURL, pollFrequency in data:
          temp.append([str(venName),str(venID), str(vtnID), str(vtnURL), str(pollFrequency)])
      return temp

    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()


def get_ven_defaultoptmode(DB):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)
      cursor.execute("select defaultopt from test.vendefaultopt where recordID=1")
      data = cursor.fetchall()
      #print data
      temp=data

      #for defaultopt in data:
      #    temp.append([str(defaultopt)])

      return temp

    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()


def get_ven_event(DB):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)

      # for dynamic operation
      endday = str(dt.date.today())
      startday = str(dt.date.today() - dt.timedelta(days=120)) # display events occurred in 120 days

      cursor.execute("select eventID, startTime, duration, eventStatus, optState, marketContext, vtnComment, testEvent, responseRequired, modificationNumber from test.eventinfo where DATE(startTime)>=%s and DATE(startTime)<=%s ORDER BY startTime DESC",(startday,endday,))
      data = cursor.fetchall()

      # print data
      temp = []
      for eventID, startTime, duration, eventStatus, optState, marketContext, vtnComment, testEvent, responseRequired, modificationNumber in data:
          temp.append([str(eventID), str(startTime), str(duration), str(eventStatus), str(optState), str(marketContext), str(vtnComment),
                       str(testEvent), str(responseRequired), str(modificationNumber)])
      return temp


      #for defaultopt in data:
          #temp.append([str(defaultopt)])
      return temp

    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()


def get_ven_event_signal_by_eventID(DB, eventID):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)

      # for dynamic operation
      #endday = str(dt.date.today())
      #startday = str(dt.date.today() - dt.timedelta(days=60)) # display events occurred in 60 days

      cursor.execute("select signalID, signalName, signalType, signalInterval, UID, targetValue, currentValue, modificationNumber from test.eventsignal where eventID=%s",(eventID,))
      data = cursor.fetchall()

      # print data
      temp = []
      for signalID, signalName, signalType, signalInterval, UID, targetValue, currentValue, modificationNumber in data:
          temp.append([str(eventID), str(signalID), str(signalName), str(signalType), str(signalInterval), str(UID), str(targetValue), str(currentValue),
                       str(modificationNumber)])
      return temp


      #for defaultopt in data:
          #temp.append([str(defaultopt)])
      #return temp

    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()


def get_ven_event_active_period_by_eventID(DB, eventID):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)

      # for dynamic operation
      #endday = str(dt.date.today())
      #startday = str(dt.date.today() - dt.timedelta(days=60)) # display events occurred in 60 days

      cursor.execute("select startTime, duration, startAfter, eiNotification, eiRampUp, eiRecovery from test.eventinfo where eventID=%s",(eventID,))
      data = cursor.fetchall()

      # print data
      temp = []
      for startTime, duration, startAfter, eiNotification, eiRampUp, eiRecovery in data:
          temp.append([str(startTime), str(duration), str(startAfter), str(eiNotification), str(eiRampUp), str(eiRecovery)])
      return temp



    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()


def get_gtnet1_record_substation(DB):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)

      # for dynamic operation
      #endday = str(dt.date.today())
      #startday = str(dt.date.today() - dt.timedelta(days=1)) # display substation record in 1 day

      # get the last P and Q of substation from db
      cursor.execute("select dtstamp, P, Q from test.substation ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()

      # print data
      temp = []
      for dtstamp, P, Q in data:
          temp.append([str(dtstamp), str(P), str(Q)])
      return temp



    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()


def get_gtnet1_record_house21(DB):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)

      # for dynamic operation
      #endday = str(dt.date.today())
      #startday = str(dt.date.today() - dt.timedelta(days=1)) # display substation record in 1 day

      # get the last P and Q of substation from db
      cursor.execute("select dtstamp, P, Q from test.house21 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()

      # print data
      temp = []
      for dtstamp, P, Q in data:
          temp.append([str(dtstamp), str(P), str(Q)])
      return temp



    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()


def get_gtnet_record_allhouses(DB):
    try:
      cnx = con.connect(user='hao', password='111111', host='localhost', database=DB)
      cursor=cnx.cursor()
      print ('database: %s is connected' %DB)

      # for dynamic operation
      #endday = str(dt.date.today())
      #startday = str(dt.date.today() - dt.timedelta(days=1)) # display substation record in 1 day

      # define data container temp
      temp = []

      # get the last P and Q of all houses of GTNET1 from db
      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house21 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 21", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house22 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 22", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house23 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 23", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house24 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 24", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house25 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 25", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house26 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 26", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house27 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 27", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house28 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 28", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house29 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 29", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house30 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 30", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house31 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 31", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house48 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 48", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house49 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 49", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house50 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 50", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house51 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 51", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house52 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 52", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house53 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 53", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house54 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 54", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house55 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 55", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house56 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 56", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house57 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 57", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house59 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 59", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house60 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 60", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house61 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 61", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house62 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 62", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house63 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 63", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house64 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 64", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house65 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 65", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house66 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 66", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house67 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 67", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house68 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 68", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house69 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 69", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.house70 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["House 70", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.section42 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["Section 42", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.section43 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["Section 43", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.section44 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["Section 44", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.section45 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["Section 45", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.section46 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["Section 46", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.section47 ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["Section 47", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      cursor.execute("select dtstamp, P, Q, temperature, opt from test.section47B ORDER BY dtstamp DESC LIMIT 1")
      data = cursor.fetchall()
      for dtstamp, P, Q, temperature, opt in data:
          temp.append(["Section 47B", str(dtstamp), str(P*1000), str(Q*1000), str(temperature), str(opt)])

      return temp



    except con.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print (err)
    finally:
        cnx.close()


if __name__=='__main__':
    data=get_ven_defaultoptmode('test')
    print data

    dataA=get_ven_info('test')
    print dataA

    dataB=get_ven_log('test')
    print dataB

    #dataC=get_ven_energy('test')
    #print dataC


    #dataD=get_ven_event('test')
    #print dataD
    #print dataD[0][0]


    #eventID = dataD[0][0]
    #dataE=get_ven_event_signal_by_eventID('test', eventID)
    #print dataE

    #dataF=get_ven_event_active_period_by_eventID('test', eventID)
    #print dataF

    #dataG = get_events('test')
    #print dataG

    #data_gtnet1_substation = get_gtnet1_record_substation('test')
    #print data_gtnet1_substation

    #data_gtnet1_house21 = get_gtnet1_record_house21('test')
    #print data_gtnet1_house21

    data_gtnet_all_houses = get_gtnet_record_allhouses('test')
    print data_gtnet_all_houses