
# Append header file search paths to specified Environment Object
# env:     Environment object
# paths:   array of absolute paths
def header_file_search_paths(env, paths):
	env.Append(CPPPATH = paths)

def get_cur_path(env):
	return env.Dir('.').abspath
