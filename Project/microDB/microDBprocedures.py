import mysql.connector
from mysql.connector import Error

# Globals to keep track on mean
count = 0
tempMean = 0.0
lightMean = 0.0

def insertVariablesIntomicrobit(temperature,light):
    try: 
        mydb = mysql.connector.connect(
                host="localhost",
                user="user",
                passwd="pass",
                database="microb"
                )

        temperatureString = str(temperature)
        lightString = str(light)
        cursor = mydb.cursor()
        MySql_insert_query = """ INSERT INTO myapp_microbit(lastTemperatureReading,lastLightReading)
                                VALUES ( %s, %s)"""
        recordTuple = (temperatureString, lightString)
        cursor.execute(MySql_insert_query,recordTuple)
        mydb.commit()
        print("insertion into microbit was successful")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")

def insertVariablesIntomicrobitsummary(temperature,light):
    #writing them global here to be able to modify them in function
    global count
    global tempMean
    global lightMean
    # This keeps track of the mean values so that correct means are inserted in summary.
    tempMean = count*tempMean
    lightMean = count*lightMean
    count += 1
    tempMean += temperature
    lightMean += light

    #rounding the means to one decimal
    tempMean = round(float(tempMean/count),1)
    lightMean = round(float(lightMean/count),1)
    
    # changing type to match database   
    tempMeanString = str(tempMean)
    lightMeanString = str(lightMean)

    try: 
        mydb = mysql.connector.connect(
                host="localhost",
                user="user",
                passwd="pass",
                database="microb"
                )
    
        cursor = mydb.cursor()
        MySql_insert_query = """ INSERT INTO myapp_microbitsummary(temperatureMean,lightMean)
                                VALUES ( %s, %s)"""
        recordTuple = (tempMeanString, lightMeanString)
        cursor.execute(MySql_insert_query,recordTuple)
        mydb.commit()
        print("insertion into microbitsummary was successful")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")