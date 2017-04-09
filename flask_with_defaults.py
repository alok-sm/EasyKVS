from flask import Flask

class FlaskWithDefaults(Flask):
    def add_url_rule(self, *args, **kwargs):
        kwargs['strict_slashes'] = False
        kwargs['methods'] = ['GET', 'POST', 'PUT', 'DELETE']
        super(FlaskWithDefaults, self).add_url_rule(*args, **kwargs)