from flask import make_response

def nocache(view):
	def no_cache(*args, **kwargs):
		response = make_response(view(*args, **kwargs))
		# response.headers['Last-Modified'] = datetime.now()
		response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
		response.headers['Pragma'] = 'no-cache'
		response.headers['Expires'] = '-1'
		return response
	return no_cache
	

# class fg:
#     BLACK   = '\033[30m'
#     RED     = '\033[31m'
#     GREEN   = '\033[32m'
#     YELLOW  = '\033[33m'
#     BLUE    = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN    = '\033[36m'
#     WHITE   = '\033[37m'
#     RESET   = '\033[39m'

# class bg:
#     BLACK   = '\033[40m'
#     RED     = '\033[41m'
#     GREEN   = '\033[42m'
#     YELLOW  = '\033[43m'
#     BLUE    = '\033[44m'
#     MAGENTA = '\033[45m'
#     CYAN    = '\033[46m'
#     WHITE   = '\033[47m'
#     RESET   = '\033[49m'

# class style:
#     BRIGHT    = '\033[1m'
#     DIM       = '\033[2m'
#     NORMAL    = '\033[22m'
#     RESET_ALL = '\033[0m'