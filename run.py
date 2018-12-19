from functools import wraps
from Scripts import app

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
    app.secret_key='secret123'
    app.debug = True
    app.run()

