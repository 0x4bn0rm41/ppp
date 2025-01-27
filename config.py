from pathlib import Path
import os



class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7ssad231234asdv'

    DATABASE_CONNECT_OPTIONS = {}

    # Turn off Flask-SQLAlchemy event system
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(Path(__file__).parent / 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    WTF_CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')

    # Secret key for signing cookies
    # if os.environ.get('SECRET_KEY'):
    #     SECRET_KEY = os.environ.get('SECRET_KEY')
    # else:
    #     SECRET_KEY = '23rsddf4fd3fAAAAAAAAAA1z'

    RATE_LIMITER_OPTS = [ '200 per day', '50 per hour']

    # Mail Configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'you-will-never-guess@gmail.com'
    MAIL_PASSWORD = 'you-will-never-guess'

    # ADMINS
    ADMINS = ['admin@gmail.com']

    # Session API config
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    # Password min/max
    PASSWORD_CHECKER_MIN = 2
    PASSWORD_CHECKER_MAX = 5

    @staticmethod
    def init_app(app):
        pass



# class APIConfig(Config):
#     """Statement for enabling the api environment"""
#     # Define the database - we are working with
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.db')
#     WTF_CSRF_ENABLED = False


# class TestingConfig(Config):
#     TESTING = True
#     WTF_CSRF_ENABLED = False
#     PRESERVE_CONTEXT_ON_EXCEPTION = False
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')


