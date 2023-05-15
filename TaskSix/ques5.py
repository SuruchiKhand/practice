# 5. Write an example on decorators.

def make_comments(func):
    def public_comments():
        print("These comments are public")
        func()
    return public_comments
    
def only_closefriends():
    print("These comments are only seen by close friends")

decorated_func = make_comments(only_closefriends)
decorated_func()



