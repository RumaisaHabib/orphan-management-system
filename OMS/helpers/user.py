from .format import executeSQL

def exists(email, utype):
    sql = fr"SELECT * FROM Users WHERE Email='{email}' AND Usertype='{utype}'"
    result = executeSQL(sql, ['Email', 'Usertype'])
    if len(result) == 0:
        return 0
    return 1