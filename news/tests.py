from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt

# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.cecilia = Editor(first_name='Cecilia', last_name='Barasa', email='cecibarasa@gmail.com')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cecilia, Editor))

     # Testing Save Method
    def test_save_method(self):
        self.cecilia.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):
    def setUp(self):
        self.cecilia = Editor(first_name='Cecilia', last_name='Barasa', email='cecibarasa@gmail.com')
        self.cecilia.save_editor()

        self.new_tag = tags(name='Jvne')
        self.new_tag.save()

        self.new_article = Article(title='Test Jvne', post='Mama Rocks', editor=self.cecilia)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)              
