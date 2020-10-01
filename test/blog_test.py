 
import unittest
from ..models import Blog
Blog = blog.blog

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Blog(1,'Anon','Lorem ipsum....','http://quotes.stormconsultancy.co.uk/quotes/1')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))


if __name__ == '__main__':
    unittest.main()