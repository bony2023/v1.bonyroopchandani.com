from flask import Flask, render_template
import datetime

app = Flask(__name__)
app.debug = False
app.config.from_pyfile('flaskapp.cfg')
currentYear = datetime.datetime.now().year

@app.route('/sitemap.xml')
def sitemap():
    return app.send_static_file('sitemap.xml')

@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Bony Roopchandani | Web Designer, Programmer, Algorithmist.', namespace = 'index', currentYear = currentYear)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About | Bony Roopchandani', namespace = 'about', currentYear = currentYear)

@app.route('/projects')
def projects():
    return render_template('projects.html', title = 'Projects | Bony Roopchandani', namespace = 'projects', currentYear = currentYear)

@app.route('/resume')
def resume():
    return app.send_static_file('resume.pdf')

@app.route('/.well-known/acme-challenge/EEB_TH4OjncPvgDNaYH9oajzVCmSwPYtXrm4G8qmRgA')
def well_known_main():
    return 'EEB_TH4OjncPvgDNaYH9oajzVCmSwPYtXrm4G8qmRgA.WkABxUOfpy_vQ3uc2FmJJtWRJ8LCGB5wWyr4YRSXPVI'

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('err404.html', title = '404 Error, Page not found.', namespace = 'err404', currentYear = currentYear), 404

if __name__ == '__main__':
    app.run()
