
from core import view
def index():
    table_d = ''.join([f'<tr><td>{s}</td></tr>' for s in range(100)])
    
    return view.view_func('table',{"mainPage":"sssssssss", 'table_d':table_d})

def home():
    return view.view_func('index',{"mainPage":"Good for you"})

def test():
    return view.view_func('index',{"mainPage":"test the post"})