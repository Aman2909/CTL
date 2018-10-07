A = [1,2,3,4,5,6,7,8,9,10]
B = A[0:2]
B

'''
C:\Users\Pathak\AppData\Local\Programs\Python\Python36\python.exe
"C:\Program Files\JetBrains\PyCharm Community Edition 2018.1.1\helpers\pydev\pydevconsole.py"
63124
63125
import sys;

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['D:\\Coding\\CTL (Aman)\\Sudoku', 'D:/Coding/CTL (Aman)/Sudoku'])
Python
3.6
.6(v3
.6
.6: 4
cf1f54eb7, Jun
27
2018, 03: 37:03) [MSC v.1900 64 bit(AMD64)]
Type
'copyright', 'credits' or 'license'
for more information
    IPython
    6.5
    .0 - - An
    enhanced
    Interactive
    Python.Type
    '?'
    for help.
        PyDev
    console: using
    IPython
    6.5
    .0
Python
3.6
.6(v3
.6
.6: 4
cf1f54eb7, Jun
27
2018, 03: 37:03) [MSC v.1900 64 bit(AMD64)]
on
win32
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = A[0:3]
B = A[1:3]
B = A[4:8]
B = A[8:8]
B = A[8:9]
B = A[8:10]
B = A[8:11]
B = A[8:-1]
B = A[8:3]
B = A[3:8]
B = A[3:-1]
B = A[3:8]
B = A[3:9]
B = A[3:10]
B = A[3:10:2]
B = A[3:10:3]
B = A[3:10:4]
B = A[0:-1]
C = A[-1]
C = A[-2]
C = A[-7]
C = A[-3:-7]
C = A[-7:-3]
C = A[-7:-3:2]
C = A[-7:-3:-2]
C = A
C = B
C = [A, B]
C = [A, A]
C = [A[3:5], B[-5:-1]]
C
Out[33]: [[4, 5], [5, 6, 7, 8]]
C[1]
Out[34]: [5, 6, 7, 8]
C[0]
Out[35]: [4, 5]
C[0][1]
Out[36]: 5
C[][1]
;
File
"<ipython-input-37-eb4ec620c31b>", line
1
C[][1]
^
SyntaxError: invalid
syntax
for i in range(2):
    C[i][1]

for i in range(2):
    C[i][0]
for i in range(2):
    D.append(C[i][0])
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-40-494ab0c0431e>", line
2, in < module >
D.append(C[i][0])
NameError: name
'D' is not defined
D = []
for i in range(2):
    D.append(C[i][0])
C
Out[43]: [[4, 5], [5, 6, 7, 8]]
C[0][1] = 7
C[0][1] = 12
for i in range(2):
    D.append(C[i][0])
D.remove
Out[47]: < function
list.remove >
D.remove()
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-48-41f06be899ed>", line
1, in < module >
D.remove()
TypeError: remove()
takes
exactly
one
argument(0
given)
D.remove(D)
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-49-fdda6c7aa1eb>", line
1, in < module >
D.remove(D)
ValueError: list.remove(x): x not in list
D.remove(4)
D.remove(4)
D.clear
Out[52]: < function
list.clear >
D.clear()
C[0].append(13)
C[0].append(19)
type(C)
Out[56]: list
TYPE(I)
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-57-4908f22611b9>", line
1, in < module >
TYPE(I)
NameError: name
'TYPE' is not defined
type(i)
Out[58]: int
for i in range(2):
    D.append(C[i][1])

for i in range(2):
    D.append(C[i][i])

D.clear()
for i in range(2, 4):
    C[i].append([0] * 4)

Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-62-1e8f0519dd34>", line
2, in < module >
C[i].append([0] * 4)
IndexError: list
index
out
of
range
for i in range(2, 4):
    C[i].append(A)

Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-63-9d30ced19497>", line
2, in < module >
C[i].append(A)
IndexError: list
index
out
of
range
C.append[[0] * 4]
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-64-1ab0b840a473>", line
1, in < module >
C.append[[0] * 4]
TypeError: 'builtin_function_or_method'
object is not subscriptable
C.append[2]
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-65-f9072295dca6>", line
1, in < module >
C.append[2]
TypeError: 'builtin_function_or_method'
object is not subscriptable
C.append[2][2]
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-66-1bd17f64c89a>", line
1, in < module >
C.append[2][2]
TypeError: 'builtin_function_or_method'
object is not subscriptable
C.append[0](3)
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-67-d678a12ca452>", line
1, in < module >
C.append[0](3)
TypeError: 'builtin_function_or_method'
object is not subscriptable
C[0].append(3)
C[0].remove(3)
C[2].append(0, 2, 1, 2)
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-70-61a21ee359ef>", line
1, in < module >
C[2].append(0, 2, 1, 2)
IndexError: list
index
out
of
range
C[1].extend(1, 2, 3)
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-71-53832885e3cc>", line
1, in < module >
C[1].extend(1, 2, 3)
TypeError: extend()
takes
exactly
one
argument(3
given)
C[1].extend(2)
Traceback(most
recent
call
last):
File
"C:\Users\Pathak\AppData\Local\Programs\Python\Python36\lib\site-packages\IPython\core\interactiveshell.py", line
2961, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-72-125b888764a5>", line
1, in < module >
C[1].extend(2)
TypeError: 'int'
object is not iterable
E = [0] * 10
E = [[0][0]] * 10
E = [[0], [0]] * 10
E = [[0]] * 10
E = [5] * 10
E = [i for i in range(11, 21)] * 10
E = [i for i in range(11, 21)]
E = [i for i in range(12, 48, 12)]
'''