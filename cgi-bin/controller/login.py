import time
import hashlib
import os
from http import cookies
from .controller import *
from model.user import *


class LogInController(Controller):

    def logIn(self, params):
        username = params.getfirst("username")
        password = params.getfirst("password")

        user = User(username, password)

        cookie = cookies.SimpleCookie()
        sid = hashlib.sha1(repr(time.time()).encode('utf-8')).hexdigest()
        cookie['sid'] = sid
        cookie['sid']['expires'] = 7 * 24 * 60 * 60
        print(cookie)
        return {'user': username}

    def logOut(self, params):
        cookie = cookies.SimpleCookie()
        cookie['sid'] = 0
        cookie['sid']['expires'] = 0
        print(cookie)
        return True

    def checkLoggedIn(self, params):
        string_cookie = os.environ.get('HTTP_COOKIE')
        if string_cookie:
            cookie = cookies.SimpleCookie()
            cookie.load(string_cookie)
            if 'sid' in cookie.keys():
                sid = cookie['sid'].value
                return True
        return False
