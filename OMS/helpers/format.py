from django.db import connection

def format_query(data, attributes): 
    '''
    Returns a list of dictionaries of the given query set for ease of accessing data.
    
    params:
    @data
    This is the raw query set we get after an SQL query.

    @attributes
    These are the attributes we want to map the data onto. It's important that the order
    of attributes matches how the data is represented in the databse.
    '''
    result = []
    for row in data:
        result.append(dict(zip(attributes, row)))
    return result


def executeSQL(sqlcom, colnames=[]):
    '''
    Returns a list (results) of dictionaries (attributes of results) of the given query.
    If no colnames provided, it adds arbitrary names, such as col1, col2, col3 and so on.
    
    params:
    @sqlcom
    SQL query to be executed

    @colnames
    column names of the table being accessed
    '''
    with connection.cursor() as cursor:
        cursor.execute(sqlcom)
        data = cursor.fetchall()

    if len(colnames) == 0 and len(data) != 0:
        colnames = ['col' + str(x + 1) for x in range(len(data[0]))]

    result = []
    for row in data:
        result.append(dict(zip(colnames, row)))
    return result
