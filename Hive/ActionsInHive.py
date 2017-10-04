import  pymysql
import  re


def get_table_info(table,schema = '',ispartition = True):
    '''
    table =  为表名，mysql,hive表名一致
    schema = 为hive中的库名
    ispartition : 是否分区默认为分区
    '''
    cols = []
    create_head = '''
    create external table if not exists {0}.{1}('''.format(schema,table)
    if ispartition:
        create_tail = r'''
        partitioned by(inc_day string
        row format delimited fields terminated by '\001'
        location '/hivetable/{0}';'''.format(table)
    else:
        create_tail = r'''
        row format delimited fields terminated by '\001'
        location '/hivetable/{0}';'''.format(table)
    connection=pymysql.connect(host='hostname',
                               user='username',
                               password='password',
                               db='mysqldb',
                               port=3306,
                               charset='utf8'
                               )
    try:
    #获取一个游标
        with connection.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            sql='SHOW FULL FIELDS FROM  {0}'.format(table)
            cout=cursor.execute(sql) #返回记录条数
            try:
                for row in cursor:#cursor.fetchall()
                    #print(row)
                    cols.append(row['Field'])
                    if 'bigint' in row['Type']:
                        row['Type'] = "bigint"
                    elif 'int' in row['Type'] or 'tinyint' in row['Type'] or 'smallint' in row['Type'] or 'mediumint' in row['Type'] or 'integer' in row['Type']:
                        row['Type'] = "int"
                    elif 'double' in row['Type'] or 'float' in row['Type'] or 'decimal' in row['Type']:
                        row['Type'] = "double"
                    else:
                        row['Type'] = "string"
                    create_head += row['Field'] + ' '+ row['Type'] +' comment \'' + row['Comment'] + '\' ,\n'
            except:
                print('程序异常!')
    finally:
        connection.close()
    create_str = create_head[:-2] + '\n' + ')'+ create_tail
    return cols,create_str # 返回字段列表与你建表语句
cols,create_str = get_table_info("tablename")
print(cols)
print(create_str)