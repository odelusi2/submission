from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'post'])
def view_form():
    if request.method == 'POST':
        firstname = request.form['Firstname'];
        surname = request.form['Lastname'];
        email = request.form['Email'];
        number = request.form['Telephonenumber']
        return render_template('form_simple.html', Firstname=name,  Lastname=name,  Email=email, Telephonenumber=number)
    else:
        return render_template('form_simple.html')


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)