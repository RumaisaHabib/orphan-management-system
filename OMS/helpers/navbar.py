def which_nav(request):
    logged_in = request.session.get('logged_in')
    if not logged_in:
        return 'navbar.html'
    else:
        return "logged_navbar.html"