from app import app, db
import unittest
from flask import app

import os
os.environ['DATABASE_URL'] = 'sqlite://'


class TestSigninPage(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['SECRET_KEY'] = 'testingdb123'
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.drop_all()
        self.app_ctxt.pop()
        self.app = None
        self.app_ctxt = None
        self.client = None

    def test_app(self):
        assert self.app is not None
        assert app == self.app

    def test_user_login(self):
        response = self.client.post('/signIn', data={
            'username': 'group3',
            'password': 'finalproject2023'
        }, follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/profile'

    def test_password_mismatch(self):
        response = self.client.post('/register', data={
            'username': 'harry',
            'password': '12345',
            'confirm_password': '1234'
        })
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Field must be equal to password." in html
