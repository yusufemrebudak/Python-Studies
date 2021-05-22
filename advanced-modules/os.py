import os
result = dir(os)
# print(result)
# ['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR',
# 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH',
#  'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET',
#   'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__cached__',
#   '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe',
#   '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort',
#   'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath',
#   'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv',
#    'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate',
#     'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd',
#      'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty',
# 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name',
#  'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink',
#   'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep',
# 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv',
# 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror',
# 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd',
#  'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result',
#  'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']  os modulune ait tüm classlar ve methodlar gelir

result = os.name
print(result) # nt windows işletim sistemini belirtir.
result = os.getcwd()
print(result) # C:\Users\yusuf\desktop\python_temelleri\advanced-modules dosyanın bulunduğu dizini döner
# os.mkdir("new directory")  yeni klasörü mevcut dizine  oluşturur.
# os.chdir('C:\\') dizin değiştirmek için
# os.chdir('C:..') bir üst dizine geçmek için
# os.makedirs("newdirectory/yeniklasor") klasör + dosya oluşturma
result=os.listdir()
print(result) # ['date.py', 'os.py'] advanced-modules klasörü altındaki dosyaları gösterir.
result = os.stat("date.py") #dosyayla ilgili bilgiler veriyor en son erişim boyut vs..
print(result)
result=os.path.abspath("os.py")
print(result) # os.py dosyasının tam konumunu verir--> C:\Users\yusuf\desktop\python_temelleri\advanced-modules\os.py
result=os.path.dirname("C:/Users/yusuf/desktop/python_temelleri/advanced-modules/os.py")
print(result)  # C:/Users/yusuf/desktop/python_temelleri/advanced-modules  dosyanın bulunduğu yolu veriyor.
result = os.path.dirname(os.path.abspath("os.py"))
print(result) # C:\Users\yusuf\desktop\python_temelleri\advanced-modules 
result=os.path.exists("os.py")
print(result) # True döner
result=os.path.exists("os1.py")
print(result) # False döner
result=os.path.isdir("C:/Users/yusuf/desktop/python_temelleri/advanced-modules")
print(result) # Verilen konumdaki klasör ise true döner dosya ise false döner
result=os.path.isfile("C:/Users/yusuf/desktop/python_temelleri/advanced-modules")
print(result) # dosya olup olmadığını sorgular yani false döner
result = os.path.join("C://","deneme","deneme1")
print(result) # C://deneme\deneme1 
result = os.path.split("C://deneme")
print(result) # ('C://', 'deneme') ayırır
result = os.path.splitext("os.py") 
print(result) # ('os', '.py')
print(result[0]) # os
print(result[1]) # .py
