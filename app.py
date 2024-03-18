import json
import prepareData
from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

schedule_ = '{"name":"М4О-106Б-23","created":1710791691,"cached":0,"days":[{"date":{"year":2023,"month":9,"day":4},"day":"Пн","lessons":[{"name":"Линейная алгебра и аналитическая геометрия","time_start":{"time":"13:00:00"},"time_end":{"time":"14:30:00"},"lectors":[{"name":"Булатникова Ирина Вячеславовна","uid":"f94601ee-1d99-11e0-9baf-1c6f65450efa"}],"type":"ПЗ","rooms":[{"name":"Орш. В-210","uid":"302df5f2-f076-11ec-bbe4-3cecef1c132f"}],"lms":"","teams":"","other":""},{"name":"Основы российской государственности","time_start":{"time":"14:45:00"},"time_end":{"time":"16:15:00"},"lectors":[{"name":"","uid":"00000000-0000-0000-0000-000000000000"}],"type":"ПЗ","rooms":[{"name":"Орш. А-218","uid":"4e16fc0d-aa98-11e6-8e0c-003048dec27f"}],"lms":"","teams":"","other":""},{"name":"Общая физика","time_start":{"time":"16:30:00"},"time_end":{"time":"18:00:00"},"lectors":[{"name":"","uid":"00000000-0000-0000-0000-000000000000"}],"type":"ПЗ","rooms":[{"name":"Орш. В-309","uid":"4e16fc7d-aa98-11e6-8e0c-003048dec27f"}],"lms":"","teams":"","other":""}]},{"date":{"year":2023,"month":9,"day":5},"day":"Вт","lessons":[{"name":"Начертательная геометрия и инженерная графика","time_start":{"time":"9:00:00"},"time_end":{"time":"10:30:00"},"lectors":[{"name":"","uid":"00000000-0000-0000-0000-000000000000"}],"type":"ПЗ","rooms":[{"name":"ГУК А-718","uid":"c814b806-f3e6-11e9-8169-003048dec27f"}],"lms":"","teams":"","other":""}]},{"date":{"year":2023,"month":9,"day":6},"day":"Ср","lessons":[{"name":"Физическая культура","time_start":{"time":"10:45:00"},"time_end":{"time":"12:15:00"},"lectors":[{"name":"","uid":"00000000-0000-0000-0000-000000000000"}],"type":"ПЗ","rooms":[{"name":"--каф.","uid":"b74722b0-6af3-11e6-ba19-003048dec27f"}],"lms":"","teams":"","other":""},{"name":"Иностранный язык","time_start":{"time":"14:45:00"},"time_end":{"time":"16:15:00"},"lectors":[{"name":"Аникеева Ирина Годерзовна","uid":"eb7d5de5-1d99-11e0-9baf-1c6f65450efa"}],"type":"ПЗ","rooms":[{"name":"Орш. Б-605","uid":"3fec64f6-fc67-11ec-bbe4-3cecef1c132f"}],"lms":"","teams":"","other":""},{"name":"Линейная алгебра и аналитическая геометрия","time_start":{"time":"16:30:00"},"time_end":{"time":"18:00:00"},"lectors":[{"name":"ВЫСК НАТАЛИЯ ДМИТРИЕВНА","uid":"dac35864-0d8e-11e4-b897-005056c00008"}],"type":"ЛК","rooms":[{"name":"Орш. В-101","uid":"4e16fc74-aa98-11e6-8e0c-003048dec27f"}],"lms":"","teams":"","other":""},{"name":"История России","time_start":{"time":"18:15:00"},"time_end":{"time":"19:45:00"},"lectors":[{"name":"","uid":"00000000-0000-0000-0000-000000000000"}],"type":"ЛК","rooms":[{"name":"Орш. В-101","uid":"4e16fc74-aa98-11e6-8e0c-003048dec27f"}],"lms":"","teams":"","other":""}]},{"date":{"year":2023,"month":9,"day":7},"day":"Чт","lessons":[{"name":"Математический анализ","time_start":{"time":"9:00:00"},"time_end":{"time":"10:30:00"},"lectors":[{"name":"ДАНИЛИНА ИРИНА АЛЕКСАНДРОВНА","uid":"dac35a9c-0d8e-11e4-b897-005056c00008"}],"type":"ЛК","rooms":[{"name":"Орш. В-101","uid":"4e16fc74-aa98-11e6-8e0c-003048dec27f"}],"lms":"","teams":"","other":""},{"name":"Общая физика","time_start":{"time":"10:45:00"},"time_end":{"time":"12:15:00"},"lectors":[{"name":"","uid":"00000000-0000-0000-0000-000000000000"}],"type":"ЛК","rooms":[{"name":"Орш. В-301","uid":"4e16fc75-aa98-11e6-8e0c-003048dec27f"}],"lms":"","teams":"","other":""},{"name":"Основы российской государственности","time_start":{"time":"13:00:00"},"time_end":{"time":"14:30:00"},"lectors":[{"name":"","uid":"00000000-0000-0000-0000-000000000000"}],"type":"ЛК","rooms":[{"name":"Орш. В-501","uid":"5413f242-aa98-11e6-8e0c-003048dec27f"}],"lms":"","teams":"","other":""}]},{"date":{"year":2023,"month":9,"day":8},"day":"Пт","lessons":[{"name":"Физическая культура","time_start":{"time":"13:00:00"},"time_end":{"time":"14:30:00"},"lectors":[{"name":"","uid":"00000000-0000-0000-0000-000000000000"}],"type":"ПЗ","rooms":[{"name":"--каф.","uid":"b74722b0-6af3-11e6-ba19-003048dec27f"}],"lms":"","teams":"","other":""}]},{"date":{"year":2023,"month":9,"day":9},"day":"Сб","lessons":[{"name":"Математический анализ","time_start":{"time":"9:00:00"},"time_end":{"time":"10:30:00"},"lectors":[{"name":"Парёнкина Виктория Игоревна","uid":"b9ce6dc7-3a75-11ed-bbea-ac1f6b64c5eb"}],"type":"ПЗ","rooms":[{"name":"Орш. А-218","uid":"4e16fc0d-aa98-11e6-8e0c-003048dec27f"}],"lms":"","teams":"","other":""},{"name":"Математический анализ","time_start":{"time":"10:45:00"},"time_end":{"time":"12:15:00"},"lectors":[{"name":"Парёнкина Виктория Игоревна","uid":"b9ce6dc7-3a75-11ed-bbea-ac1f6b64c5eb"}],"type":"ПЗ","rooms":[{"name":"Орш. А-218","uid":"4e16fc0d-aa98-11e6-8e0c-003048dec27f"}],"lms":"","teams":"","other":""}]}]}'


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
    app.run(host='0.0.0.0', port=80)
