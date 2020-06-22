from django.test import TestCase
from .models import Editor,Article,tags

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
