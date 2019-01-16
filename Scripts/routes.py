import secrets, os
from PIL import Image
from flask import render_template, flash, redirect, url_for, request
from Scripts.forms import RegisterForm, LoginForm, UpdateDetails, TodoList, RequestResetForm, ResetPasswordForm, FoodForm, ExerciseForm, SearchForm
from Scripts import app, db, bcrypt, mail
from Scripts.models import User, Schedule, Food, Fitness, Breakfast, Lunch, Dinner
from random import randint
from Scripts.Exercises import Exercises
from Scripts.Fitness import Record, YourPlan
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route("/")
@app.route("/home")
def home():
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    else:
        image_file = url_for('static', filename='profile_pics/default.png')
    return render_template("home.html", image_file=image_file)

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data.lower(), username=form.username.data.lower(), password=hashed_password, age=form.age.data, weight=form.weight.data, height=form.height.data )
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    flash('Logged Out successfully!', 'success')
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn

@app.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    form = UpdateDetails()
    bfastt = Breakfast.query.all()
    lunchh = Lunch.query.all()
    dinnerr = Dinner.query.all()
    app.logger.debug('in profile method')
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.height = form.height.data
        current_user.weight = form.weight.data
        current_user.age = form.age.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.height.data = current_user.height
        form.weight.data = current_user.weight
        form.age.data = current_user.age

    kcal = 0
    for food in bfastt:
        kcal += food.calories
    app.logger.debug(kcal)
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile.html', title='Profile',
                           image_file=image_file, form=form, bfastt=bfastt, lunchh=lunchh, dinnerr=dinnerr)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='app.noreply1206@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}
    
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

@app.route('/reset_password', methods=['GET','POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'success')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

@app.route('/ExGuide')
@login_required
def guide():
    exercises_list = []
    int_list = []
    e1 = Exercises(
        "A Push-up is a common exercise that involves beginning from the prone position,then raising and lowering the body using the arms.",
        ['Pectoral muscles',
         'Abdominal muscles',
         'Triceps'],
        ["Extend your legs backwards and place hands on the ground, slightly more than shoulder-width apart.",
         "Start by bending your elbows to lower your chest until it is just above the floor.",
         "Push yourself back to the starting position. An ideal push-up would be a 1-second push, pause and a 2 second down count.",
         "Repeat steps 1 to 3 for preferably 10 to 15 times."],
        "https://cdn-ami-drupal.heartyhosting.com/sites/muscleandfitness.com/files/styles/full_node_image_1090x614/public/media/1109-pushups_0.jpg?itok=QyFVWqN6",
        "https://www.youtube.com/embed/IODxDxX7oi4")
    e2 = Exercises(
        'Crunching is an exercise that involves lying face-up on the floor, bending the knees then curling the shoulders towards the waist.',
        ['Abdominal muscles'],
        ['Lie on your back with your knees bent and feet flat on the floor hip-width apart.',
         'Place your hands behind your head such that your thumbs are behind your ears',
         'Hold your elbows to the sides, slightly facing in.',
         'Slightly tilt your chin, leaving some space between your chin and chest.',
         'Gently pull your abdominals inward.',
         'Curl up and forward so that your head, neck and shoulders lift off the floor',
         'Hold for a moment at the top of the movement in Step 6 and slowly lower yourself back down',
         'Repeat Steps 1 to 7 for preferably 10 to 15 times.'],
        "https://cdn2.coachmag.co.uk/sites/coachmag/files/styles/16x9_480/public/images/dir_30/mens_fitness_15427.jpg?itok=T3OF7wPv&timestamp=1369282187",
        "https://www.youtube.com/embed/Xyd_fa5zoEU")
    e3 = Exercises(
        'Jumping Jacks is an exercise that involves jumping with the legs spread wide and hands touching overhead then returning to a position with the feet together and arms at the sides.',
        ['Calve muscles',
         'Shoulder muscles',
         'Hip muscles'],
        ['Stand with your feet together and pointing forward, arms hanging straight at the sides.',
         'In one jump, bend your knees and extend both legs out to the sides while simultaneously extending your arms out to the sides and then up and over the head.',
         'Immediately reverse this motion, jumping back to the starting or neutral standing position.',
         'Repeat Steps 1 to 3 for preferably 10 to 15 times.'],
        "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/1104-jumping-jacks-1441032989.jpg",
        "https://www.youtube.com/embed/UpH7rm0cYbM")
    e4 = Exercises(
        'Tuck jumping is an exercise that involves standing in a shoulder width position, slowly descending into a squat and use your feet to explode off the floor while driving your knees towards your chest.',
        ['Abdominal muscles',
         'Hamstrings',
         'Calve muscles'],
        ['Start in a standing position, slightly bending your knees',
         'Hold your hands out at chest level.',
         'Lower your body quickly into a squatting position, then explode upwards bringing your knees up towards your chest.',
         'Repeat Steps 1 to 3 for preferably 10 to 15 times.'],
        "http://fitmw.com/wp-content/uploads/2015/07/Exercises-Tuck-Jump.jpg",
        "https://www.youtube.com/embed/ZR6aFqdRi2Y")
    e5 = Exercises(
        'Squatting is an exercise that involves standing in a shoulder width position, bending your knees all the way down and then suddenly propelling yourself back up to a standing position.',
        ['Hip muscles',
         'Hamstrings',
         'Quads'],
        ['Stand with your feet apart, directly under your hips, and place your hands on your hips.',
         'Standing up tall, put your shoulders back, lift your chest, and pull in your abdominal muscles.',
         'Bend your knees while keeping your upper body as straight as possible, like a sitting position. Lower yourself down as far as you can without leaning your upper body more than a few inches forward.',
         'Straighten your legs so you do not lock your knees when you reach a standing position.',
         'Repeat Steps 1 to 4 for preferably 10 to 15 times.'],
        "https://19jkon2dxx3g14btyo2ec2u9-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/squats.jpg",
        "https://www.youtube.com/embed/aclHkVaku9U")
    e6 = Exercises(
        'Flutter kicks is an exercise that involves lying down face-up, straightening your legs until they are level with your hips and alternating between lifting each leg.',
        ['Abdominal muscles',
         'Hip muscles',
         'Quads'],
        ['Lie on your back with your legs extended and your arms alongside your hips, palms down.',
         'Lift your legs about 4 to 6 inches off the floor. Press your lower back into the floor or gym mat.',
         'Keep your legs straight as you rhythmically raise one leg higher, then switch. Move in a fluttering, up and down motion.',
         'Repeat Steps 1 to 3 for preferably 15 to 20 times.'],
        "https://i.pinimg.com/originals/74/d8/55/74d855acc30ffdfe3c7410f3c278918b.jpg",
        "https://www.youtube.com/embed/ANVdMDaYRts")
    exercises_list.extend([e1, e2, e3, e4, e5, e6])

    exercise = ""
    exercise1 = ""
    exercise2 = ""

    while exercise == "":
        cycle = randint(0, 5)
        if cycle not in int_list:
            exercise = exercises_list[cycle]
            int_list.append(cycle)

    while exercise1 == "":
        cycle = randint(0, 5)
        if cycle not in int_list:
            exercise1 = exercises_list[cycle]
            int_list.append(cycle)

    while exercise2 == "":
        cycle = randint(0, 5)
        if cycle not in int_list:
            exercise2 = exercises_list[cycle]
            int_list.append(cycle)

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

    return render_template('ExGuide.html', exercise=exercise, exercise1=exercise1, exercise2=exercise2, image_file=image_file)

@app.route('/schedule')
@login_required
def schedule():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('schedule.html',image_file=image_file)

@app.route('/schedule/ToDoList', methods=['GET','POST'])
@login_required
def todolist():
    form = TodoList()
    Todos = Schedule.query.all()
    if form.validate_on_submit():
        activity = Schedule(description=form.description.data, remarks=form.remarks.data, name=current_user)
        db.session.add(activity)
        db.session.commit()
        app.logger.debug('Activities added')
        flash('Activity have been added to your schedule', 'success')
        return redirect(url_for('todolist'))
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('todolist.html',title='ToDoList',image_file=image_file, form=form, Todos=Todos )

@app.route('/HealthTracker')
@login_required
def HealthTracker():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('HealthTracker.html',image_file=image_file)

@app.route('/food',methods=['GET','POST'])
@login_required
def _Food():
    form = SearchForm()
    if form.meal.data == 'breakfast':
        searches = Food.query.filter_by(name=form.name.data).first()
        app.logger.debug(form.meal.data)
        breakfast = Breakfast(name=current_user, foodname=searches.name, mass=searches.mass, calories=searches.calories, protein=searches.protein, carbohydrates=searches.carbohydrates, fats=searches.fats)
        db.session.add(breakfast)
        flash('Commit!', 'success')
    elif form.meal.data == 'lunch':
        searches = Food.query.filter_by(name=form.name.data).first()
        lunch = Lunch(name=current_user, foodname=searches.name, mass=searches.mass, calories=searches.calories, protein=searches.protein, carbohydrates=searches.carbohydrates, fats=searches.fats)
        db.session.add(lunch)
        flash('Commit!', 'success')
    elif form.meal.data == 'dinner':
        searches = Food.query.filter_by(name=form.name.data).first()
        dinner = Dinner(name=current_user, foodname=searches.name, mass=searches.mass, calories=searches.calories, protein=searches.protein, carbohydrates=searches.carbohydrates, fats=searches.fats)
        db.session.add(dinner)
        flash('Commit!', 'success')
    else:
        searches=""
    db.session.commit()
    app.logger.debug(form.meal.data)


    r1 = Record('food1')
    p1 = YourPlan('2500', 'bulk')

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('food.html', items=r1, kcal=p1, image_file=image_file, form=form, searches=searches)
@app.route('/exercise',methods=['GET','POST'])
@login_required
def exercise():
    form = ExerciseForm()
    if form.validate_on_submit():
        exercise1 = Fitness(name=form.name.data, duration=form.mass.data)
        db.session.add(exercise1)
        db.session.commit()
        flash('Your entry has been entered!', 'success')

    return render_template('exercise.html', form=form)

@app.route('/addfood',methods=['GET','POST'])
def addFood():
    form = SearchForm()
    if form.validate_on_submit():
        print('asd')
        food = Food(name=form.name.data, mass=form.mass.data, calories=form.calories.data, protein=form.protein.data, carbohydrates=form.carbohydrates.data, fats=form.fats.data)
        db.session.add(food)
        db.session.commit()
        flash('Your entry has been entered!','success')
    return render_template('addFood.html', form=form)

@app.route('/test', methods=['GET','POST'])
def test():
    form = SearchForm()
    if form.validate_on_submit():
        searches = Food.query.filter_by(name=form.name.data).first()
        if form.meal.data == 'breakfast':
            search = Breakfast(name=current_user, foodname=searches.name, mass=searches.mass, calories=searches.calories, protein=searches.protein, carbohydrates=searches.carbohydrates, fats=searches.fats)
            db.session.add(search)
        db.session.commit()
        flash('Commit!','success')
        app.logger.debug(searches)
    else:
        searches = ''


    return render_template('test.html', form=form, searches=searches)
