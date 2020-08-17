from  myproject import db,app
from flask import render_template,request,url_for,redirect,abort
from flask_login import login_required,login_user,logout_user
from myproject.models import User
from myproject.forms import LoginForm,Registration,RegistrationForm#registration name check

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout()
    flash("you are logged out")
    return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not none:
            login_user(user)
            flash('login succesfully')
            next=request.args.get('next')#for the current page visiting that required login

            if next==None or not next[0]=='/':#if there is no page return to the home page
                next=url_for('welcome_user')

            return redirect(next)
        return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(email=form.email.data,
                    username=form.username.database,password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('thanks for registration')
        return render_template(url_for('login'))
    return render_template('register.html',form=form)

if __name__=='__main__':
    app.run(debug=True)
