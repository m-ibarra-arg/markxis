from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_pagedown import PageDown
from flask_pagedown.fields import PageDownField
from wtforms.fields import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
pagedown = PageDown(app)


class VentanaEdicion(FlaskForm):
    pagedown = PageDownField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = VentanaEdicion()
    text = None
    if form.validate_on_submit():
        text = form.pagedown.data
    else:
        form.pagedown.data = ('# This is demo #2 of Flask-PageDown\nThe '
                               '*preview* is rendered separately from the '
                               '*input*, and in this case it is located above.')
    return render_template('index.html', form=form, text=text)


if __name__ == '__main__':
    app.run(debug=False)
