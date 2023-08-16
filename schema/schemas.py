#the function is expected to return a dictionnary
def individual_serial_todo(todo) -> dict:
    return {
        "id": str(todo['_id']),
        "name": todo['name'],
        'description': todo['description'],
        'complete': todo['complete']
    }
    
def individual_serial_user(user) -> dict:
    return {
        "id": str(user['_id']),
        "name": user['name'],
        'email': user['email'],
        'password': user['password']
    }
    
    
#the function is expected to return a list of dictionnaries
def list_serial(items,func) -> list:
    return [func(item) for item in items]