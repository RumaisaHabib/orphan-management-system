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
