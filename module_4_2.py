def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
inner_function()

# Я в области видимости функции test_function
# python-BaseException
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.2.1\plugins\python-ce\helpers\pydev\pydevd.py", line 1557, in _exec
#     pydev_imports.execfile(file, globals, locals)  # execute the script
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.2.1\plugins\python-ce\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
#     exec(compile(contents+"\n", file, 'exec'), glob, loc)
#   File "D:\UrbanUniversity\ProjectPanov1\module_4_2.py", line 9, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
