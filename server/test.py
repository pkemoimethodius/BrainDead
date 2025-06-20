import sys
from unittest import TestCase, main
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from faker import Faker

class FlaskDependenciesTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize test resources"""
        cls.app = Flask(__name__)
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Initialize extensions
        cls.db = SQLAlchemy(cls.app)
        cls.migrate = Migrate(cls.app, cls.db)
        cls.fake = Faker()

        # Create simple model for testing
        class User(cls.db.Model):
            id = cls.db.Column(cls.db.Integer, primary_key=True)
            name = cls.db.Column(cls.db.String(80))
            email = cls.db.Column(cls.db.String(120))

        cls.User = User

        # Create tables
        with cls.app.app_context():
            cls.db.create_all()

    def test_faker_functionality(self):
        """Test if Faker can generate fake data"""
        name = self.fake.name()
        email = self.fake.email()
        self.assertIsInstance(name, str)
        self.assertIsInstance(email, str)
        self.assertIn('@', email)
        print(f"\n✅ Faker test data: {name} | {email}")

    def test_sqlalchemy_operations(self):
        """Test basic SQLAlchemy CRUD operations"""
        with self.app.app_context():
            # Create
            user = self.User(name=self.fake.name(), email=self.fake.email())
            self.db.session.add(user)
            self.db.session.commit()

            # Read
            fetched_user = self.User.query.first()
            self.assertIsNotNone(fetched_user)
            self.assertEqual(user.id, fetched_user.id)

            print(f"\n✅ SQLAlchemy test record: {fetched_user.name}")

    def test_flask_migrate_initialized(self):
        """Test if Flask-Migrate is properly initialized"""
        self.assertTrue(hasattr(self, 'migrate'))
        self.assertIsInstance(self.migrate, Migrate)
        print("\n✅ Flask-Migrate initialized correctly")

    @classmethod
    def tearDownClass(cls):
        """Clean up resources"""
        with cls.app.app_context():
            cls.db.drop_all()

if __name__ == '__main__':
    print("Testing essential Flask dependencies...")
    main()