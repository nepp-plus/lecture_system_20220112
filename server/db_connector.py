import pymysql
from pymysql.cursors import DictCursor

class DBConnector:
    def __init__(self):
        self.db = pymysql.connect(
            host='finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='admin',
            passwd='Vmfhwprxm!123',  # 프로젝트!123  첫글자만 대문자로.
            db='test_202112_python',
            charset='utf8',
            cursorclass=DictCursor
        )
        
        # 커서도 변수로 담아두자.
        self.cursor = self.db.cursor()