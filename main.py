from flask import Flask, render_template, request
import math
import numpy as np


def function(x):
    ret = math.sqrt(math.pow(math.sin(x), 2) + 0.1)
    if ret.real:
        return ret
    return 0


app = Flask(__name__)

name = "FlaskSite"
resultsFirst = []
resultsSecond = []
n = 100000


@app.route('/', methods=['GET', 'POST'])
def index():
    resultsFirst.clear()
    resultsSecond.clear()
    return render_template('index.html', title=name)


@app.route('/first', methods=['GET', 'POST'])
def first():
    if request.method == 'POST':
        mu = float(request.form.get('mu'))
        sigma = float(request.form.get('sigma'))
        massive = np.random.normal(mu, sigma, n)
        massive[np.logical_not(massive >= -1)] = -1
        massive[np.logical_not(massive <= 1)] = 1
        result = np.array(list(map(function, massive)))
        resultsFirst.append(result)
        return render_template("first.html", resultFirst=resultsFirst, mu=mu, sigma=sigma, np=np)
    return render_template("first.html")


@app.route('/second', methods=['GET', 'POST'])
def second():
    if request.method == 'POST':
        x = float(request.form.get('x'))
        y = float(request.form.get('y'))
        max = 20
        min = 1
        a = np.random.randint(min, max, size=n)
        b = np.random.randint(min, max, size=n)
        result = sum(map(lambda z: z[0] == x and (y < z[1] < 2 * y), zip(a, b)))
        resultsSecond.append(result)
        return render_template("second.html", resultSecond=resultsSecond)
    return render_template('second.html', title=name)


if __name__ == "__main__":
    app.run(debug=True)
