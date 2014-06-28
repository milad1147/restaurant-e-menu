import time
import hashlib
import os
from http import cookies
from .controller import *
from model.user import *
from model.session import *


class LogInController(Controller):

    def logIn(self, params):
        username = params["username"]
        password = params["password"]
        user = User(username, password)

        cookie = cookies.SimpleCookie()
        sid = hashlib.sha1(repr(time.time()).encode('utf-8')).hexdigest()
        cookie['sid'] = sid
        cookie['sid']['expires'] = 7 * 24 * 60 * 60

        session = Session(sid)
        session.addData('username', user.username)
        session.addData('userRoles', user.userRoles)

        print(cookie)
        return {'user': username, 'sid': sid}

    def logOut(self, params):
        string_cookie = os.environ.get('HTTP_COOKIE')
        cookie = cookies.SimpleCookie()
        cookie.load(string_cookie)
        sid = cookie['sid']
        cookie['sid'] = 0
        cookie['sid']['expires'] = 0

        Session.destroy(sid)

        print(cookie)
        return True

    def checkLoggedIn(self, params):
        string_cookie = os.environ.get('HTTP_COOKIE')
        if string_cookie:
            cookie = cookies.SimpleCookie()
            cookie.load(string_cookie)
            if 'sid' in cookie.keys():
                sid = cookie['sid'].value
                session = Session(sid)
                return True
        raise PermissionError
