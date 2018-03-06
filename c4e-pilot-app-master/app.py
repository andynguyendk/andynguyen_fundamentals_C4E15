from flask import *

from models.service import Service

import mlab

mlab.connect()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/<int:gender>')
def search(gender):
    services = Service.objects(gender=gender, yob__lte=1998)
    return render_template('search.html', all_services=services)



@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services=services)

@app.route('/delete/<service_id>')
def delete(service_id):

    service_to_delete = Service.objects().with_id(service_id)

    if service_to_delete is None:
        return "Not found"

    service_to_delete.delete()
    return redirect(url_for('admin'))


@app.route('/new-service', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        new_service = Service(name='YYYYYYYY',

                              phone='111')
        new_service.save()
        return render_template('new-service.html')

    elif request.method == 'POST':
        form = request.form

        name = form['name']
        yob = form['yob']
        phone = form['phone']

        new_service = Service(name=name,
                              yob=yob,
                              phone=phone

                              )
        new_service.save()

        return "Saved"




if __name__ == '__main__':
  app.run(debug=True)
