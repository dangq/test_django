from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from extract_dict import extract_dict as ed
import pickle
import sys

reload(sys)
sys.setdefaultencoding('utf8')

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
file_name='data/result_1606.txt'

SKILL_LIST=[]
with open(file_name,'r') as f:
    file=pickle.loads(f.read())
    for skill in file:
        skill=unicode(skill)
        SKILL_LIST.append((skill,skill. lower()))

SKILL_LIST=sorted(SKILL_LIST)
STYLE_CHOICES=sorted([(item, item) for item in range(1,10)])



class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #title = models.CharField(max_length=100, blank=True, default='')
    #code = models.TextField()
    #linenos = models.BooleanField(default=False)
    language = models.CharField(choices=SKILL_LIST, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default=3, max_length=100)
    relevant_skill=models.TextField(default=('python',1))
    owner = models.ForeignKey('auth.User', related_name='extract_skill')

    class Meta:
        ordering = ('created','owner',)



# Create your models here.
