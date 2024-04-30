from routes import routes
def handle_request(request):
    """Handles the HTTP request."""
    try:
        headers = request.split('\n')
        method = headers[0].split()[0]
        route = headers[0].split()[1]
    except IndexError:
        print("Error in header")
        
    try:
        if isinstance(routes[route]['method'],list):
            upper_string_methods = [s.upper() for s in routes[route]['method']]
            if method in upper_string_methods:

                content = routes[route]['action'][upper_string_methods.index(method)]
                response = 'HTTP/1.0 200 OK\n\n' + content


        elif method == routes[route]['method'].upper() and isinstance(routes[route]['method'], str): 

            content = routes[route]['action']
            response = 'HTTP/1.0 200 OK\n\n' + content

        else:
            response = 'HTTP/1.0 405 METHOD NOT ALLOWED\n\nMethod Not Allowed'
    except Exception:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'


    return response
