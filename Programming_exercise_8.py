import mysql.connector
from geopy import distance

# 8_1


def find_airport_1(ident):
    sql = "SELECT ident, name, municipality FROM airport"
    sql += " WHERE ident = '" + ident + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"airport: {row[1]}\nplace: {row[2]}")
    return


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='jefer014',
    autocommit=True
    )

ident = input("enter the ICAO code of an airport: ")
find_airport_1(ident)

# 8_2


def find_airport_2(ident):
    sql = "select country.name as name, airport.type, count(*) from airport, country " \
          "where airport.iso_country = country.iso_country and airport.iso_country = '" + ident + "' " \
            "group by airport.type order by 'type' desc;"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Country: {row[0]} type: {row[1]}: {row[2]}")
    return


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='jefer014',
    autocommit=True
    )

ident = input("enter the area code of a country: ")
find_airport_2(ident)


# 8_3

def find_airport_3(ident):
    sql = "select name, latitude_deg, longitude_deg from airport"
    sql += " WHERE ident = '" + ident + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"This is the airport: {row[0]}")
            deg = (row[1], row[2])
    return deg


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='jefer014',
    autocommit=True
    )

ident = input("enter the ICAO code of the first airport: ")
a = find_airport_3(ident)

ident_2 = input("enter the ICAO code of the second airport: ")
b = find_airport_3(ident_2)


distant = distance.great_circle(a, b).km

print(f"And the distance between the two airports is {distant:.2f} km")

