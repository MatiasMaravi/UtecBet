import unittest
from flask_sqlalchemy import SQLAlchemy
from server import create_app
from models import setup_db
import json

user1 = {
    'id':1000,
    'username': 'test_user',
    'password': '123456789'

}
userFail = {
    'id':9999,
    'username': None,
    'password': None

}

class TestPlantaApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client
        self.database_name = 'utecbet_test'
        self.database_path = 'postgresql+psycopg2://{}@{}/{}'.format('postgres:123', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def test_post_user_success_200(self):
        res = self.client().post('/register',json=user1)
        
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['token'])
        self.assertTrue(data['user_id'])

        self.client().delete(f'/users/{user1["id"]}')
    

    def test_post_user_failed_422(self):
        res = self.client().post('/register',json=userFail)
        
        #Doble post de la misma entidad falla 
        data = json.loads(res.data)
        self.assertEqual(res.status_code,422)
        self.assertEqual(data['success'],False)
    
    def test_delete_user_success_200(self):
        self.client().post('/register',json=user1)
        res = self.client().delete(f'/users/{user1["id"]}')
        #Doble post de la misma entidad falla 
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['delete_user'],user1["id"])

    def tearDown(self):
        self.app_context.pop()