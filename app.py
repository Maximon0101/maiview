from flask import Flask, send_from_directory, render_template

app = Flask(__name__)


@app.route('/<path:path>')  # for all static content
def send_static(path):
    return send_from_directory('static', path)


@app.route('/')
@app.route('/index.htm')
@app.route('/index.html')
@app.route('/schedule')
def schedule():
    return render_template('schedule.html')


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
