# 你想要怎样的生活
# 开发时间：2025/2/23 23:36
import pymysql

from component.log_untils import logger
from component.read_file import base_data

data = base_data.read_ini()['mysql']
DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "user": data['MYSQL_USER'],
    "password": data['MYSQL_PASSWD'],
    "db": data['MYSQL_DB']
}

class MysqlDb:
    def __init__(self):
        # mysql连接
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    # 查询一条
    def select_db_one(self, sql):
        logger.info(f'执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchone()
        logger.info(f'sql执行结果：{result}')
        return result

    # 查询多条
    def select_db_all(self, sql):
        logger.info(f'sql执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchall()
        logger.info(f'执行结果：{result}')
        return result

    def execute_db(self, sql):
        try:
            logger.info(f'执行sql：{sql}')
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行sql出错{}".format(e))


db = MysqlDb()
if __name__ == '__main__':
    db = MysqlDb()
    result = db.select_db_one(
        "select code from users_verifycode where mobile = '15000000000' order by id desc limit 1;")
    print(result['code'])
