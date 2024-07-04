### 1. Create virtual environment and install packages in requirements.txt file
```
python3 -m venv <myenvname>
source venv/bin/activate
pip install -r requirements.txt  

```

### 2. COPY + PASTE WSGI CONFIG FILE 

import sys
```
# add your project directory to the sys.path
project_home = u'/home/trademamba/dash'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path


from app import app
application = app.server
```
