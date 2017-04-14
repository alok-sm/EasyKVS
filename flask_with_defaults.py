from flask import Flask

# child class of the Flask class with 
# default methods and "strict slashes" set
class FlaskWithDefaults(Flask):
    def add_url_rule(self, *args, **kwargs):
        if 'strict_slashes' not in kwargs:
            kwargs['strict_slashes'] = False
        if 'methods' not in kwargs:
            kwargs['methods'] = ['GET', 'POST', 'PUT', 'DELETE']
        super(FlaskWithDefaults, self).add_url_rule(*args, **kwargs)