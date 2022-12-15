from django.db import connection
from models import *

print(connection.queries)