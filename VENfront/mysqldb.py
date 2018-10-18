import mysql.connector as con
from mysql.connector import errorcode
import datetime as dt
import pytz as tz

#isodate lib to parse the ISO 8601 format into date time,
#for example: PT30M = 30 mins
import isodate


def get_ven_energy(DB):
    try:
      cnx = con.connect(user='xx', password='xx', host='localhost', database=DB)
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
      cnx = con.connect(user='xx', password='xx', host='localhost', database=DB)
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
      cnx = con.connect(user='xx', password='xx', host='localhost', database=DB)
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
      cnx = con.connect(user='xx', password='xx', host='localhost', database=DB)
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
      cnx = con.connect(user='xx', password='xx', host='localhost', database=DB)
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
      cnx = con.connect(user='xx', password='xx', host='localhost', database=DB)
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
      cnx = con.connect(user='xx', password='xx', host='localhost', database=DB)
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
      cnx = con.connect(user='xx', password='xx', host='localhost', database=DB)
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
      cnx = con.connect(user='xx', password='xx', host='localhost', database=DB)
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

    dataG = get_events('test')
    print dataG
