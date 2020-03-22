# testing out running code at runtime
import sys

code = compile('a = 1 + 2', '<string>', 'exec')
exec(code)
print(a)