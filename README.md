### 1. 

### 2. COPY + PASTEWSGI CONFIG FILE 
import sys

# add your project directory to the sys.path
project_home = u'/home/trademamba/dash'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path


from app import app
application = app.server
