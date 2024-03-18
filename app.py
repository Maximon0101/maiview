import json
import prepareData
from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

schedule_ = '{"name":"М4О-106Б-23","created":1710692662,"cached":0,"days":[{"date":{"year":2024,"month":2,"day":29},"day":"Пт","lessons":[{"name":"Математический анализ","time_start":{"time":"12:15:00"},"time_end":{"time":"12:15:00"},"lectors":[{"name":"Данилина Ирина Александровна","uid":"4e16fbff-aa98-11e6-8e0c-003048dec27f"}],"rooms":[{"name":"ГУК В-228","uid":"4e16fbff-aa98-11e6-8e0c-003048dec27f"}],"lms":"reserved","teams":"reserved","other":"reserved"}]}]}'


@app.route('/<path:path>')  # for all static content
def send_static(path):
    return send_from_directory('static', path)


@app.route('/')
@app.route('/index.htm')
@app.route('/index.html')
@app.route('/schedule')
def schedule():
    schedule = json.loads(schedule_)
    schedule["days"] = list(map(prepareData.prepareScheduleDay, schedule["days"]))
    print(schedule["days"][0])
    return render_template('schedule.html',
                           schedule=schedule)


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
    app.run()
