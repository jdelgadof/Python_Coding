from flask import Flask, request
import mysql.connector

# Exercise 13-1
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='jefer014',
    autocommit=True)
mycursor = connection.cursor()
app = Flask(__name__)


@app.route('/prime_number/<input>')
def echo(input):
    numero = int(input)
    serPrimo = True
    for n in range(2, numero):
        if numero % n == 0:
            serPrimo = False
            break
    if serPrimo:
        response = {
            "Number": numero,
            "isPrime": serPrimo
        }
        print("game works!") # Try it later
    else:
        response = {
            "Number": numero,
            "isPrime": serPrimo
        }

    return response


# Exercise 13-2. Implement a backend service that gets the ICAO code of an airport and
# then returns the name and location of the airport in JSON format.
# The information is fetched from the airport database used on this course.
# For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK.
# The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.


@app.route('/airport/<icao>')
def airport(icao):
    mycursor.execute("SELECT ident, name, municipality FROM airport WHERE ident = '" + icao + "'")
    user = mycursor.fetchall()
    for row in user:
        ident = row[0]
        name = row[1]
        mun = row[2]

    answer = {
        "ICAO": ident,
        "Name": name,
        "Location": mun
        }
    return answer


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
