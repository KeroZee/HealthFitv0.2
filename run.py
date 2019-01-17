from Scripts import app, db
import datetime
from Scripts.models import Breakfast, Lunch, Dinner

#Check if logged in
# def is_logged_in(f):
#     @wraps(f)
#     def wrap(*args,**kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Unauthorized, Please log in','danger')
#             return redirect(url_for('login'))
#     return wrap
if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.debug = True
    app.run()
now = datetime.datetime.now()
midnight = datetime.time(0, 0, 0)
print(now, midnight)
if now == midnight:
    resetBreakfast = Breakfast.query.all()
    for i in resetBreakfast:
        db.session.delete(i)
        db.session.commit()
    resetLunch = Lunch.query.all()
    for i in resetLunch:
        db.session.delete(i)
        db.session.commit()
    resetDinner = Dinner.query.all()
    for i in resetDinner:
        db.session.delete(i)
        db.session.commit()

