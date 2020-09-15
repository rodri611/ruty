from flask import Flask, Markup, render_template
import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", password="", database="ruty")

mycursor = mydb.cursor()

mycursor.execute("select * from temperatura")

result = mycursor.fetchall()

for datos in result:
    print(str(datos[0])+" "+str(datos[1])+" "+str(datos[2]))

app = Flask(__name__)

"""DATE"""
labels = [
    (datos[1])
]
"""TEMP"""
values = [
    (datos[2])
]

@app.route('/line')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Temperatura', max=50, labels=line_labels, values=line_values)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)