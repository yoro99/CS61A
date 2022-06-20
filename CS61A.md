> Python 3的[源码的默认编码方式为utf-8](http://www.python.org/dev/peps/pep-3120/)
>
> 可以在第一行说明编码方式
>
> ```python
> # -*- coding: windows-1252 -*-
> 
> ## 或者
> 
> #!/usr/bin/python3
> # -*- coding: windows-1252 -*-
> ```

# week1

> * `python ok --local`  加入`--local`可以在本地测试并保存
> * 按下快捷键Ctrl+Shift+S，即可自动滚动屏幕，截取整个网页
> * `python ok -q <question name> -i`可以在案例失败后继续测试
> * `python ok -q <question name> --trace`a browser window should open up with your code，environment diagram
> * `python ok -u --local -v`如果有locked测试可以看完成的百分比
> * `python ok --score --local`可以查看每个问题的成绩
> * `C^c`可以在shell中中断python运行（infinite loop）
> * 可视化运行python代码的[website](https://pythontutor.com/composingprograms.html#mode=edit)

## lecture1

### powershell常用命令

> *Windows PowerShell tip:* If you're using PowerShell, you can start it directly by holding Shift, right-clicking inside any folder, and selecting ["Open PowerShell Window here"](https://www.tenforums.com/attachments/tutorials/248020d1568908726-open-powershell-window-here-context-menu-add-windows-10-a-open_powershell_window_here_context_menu.png). It will automatically `cd` to that folder, so you'll have to run `cd ~` to change to your home directory

```powershell
echo "$HOME"  # displays the path to your home directory.
ls # 列出文件
cd 
cd .. # 回到父级目录
cd ~  # 回到主目录
unzip lab00.zip  # cmd解压文件
Expand-Archive -Force lab00.zip  # powershell解压文件
start .  # 打开当前的文件夹
```

- `ls`: **l**i**s**ts all files in the current directory

- `cd <path to directory>`: **c**hange into the specified **d**irectory

- `mkdir <directory name> `: **m**a**k**e a new **dir**ectory with the given name

- `mv <source path> <destination path> `: **m**o**v**e the file at the given source to the given destination

- **debug**（`assert`、`doctest`、`print`）：

  - `assert`：在程序遇到不正确的结果时奔溃是一个好的选择，所以使用`assert`，关于assert（me：**感觉可以检查参数在suite执行前**）

    - `assert fib(8) == 13, 'The 8th Fibonacci number should be 13'`后面可以接一个解释的字符串
    -  This is useful if you know that certain conditions need to be true at certain points in your program Exhaustive
    - 可以永久留在程序中
  - 断言会减慢python程序的运行速度，解释命令加入后缀`-O`（字母）可以**跳过所有断言**`python -O`，可以通过内置的boolean变量`__debug__`查看断言是否有效
  
- `doctest`
  
  - 写在函数名下面的备注是**doctest**，第一行可以用于解释函数功能，后面按shell的调用的格式写出测试用例（函数调用用例），有缩进且和`>>>`中间要有空格！：
  
    - **格式**：第一行是对函数的总介绍，空一行再介绍各个参数，在输入测试用例
  
      - ```python
        def f(x):
        	''' information
        
        	>>> f(4)
        	4
        	>>> f(5)
        	5
        	>>> a = f(6)
        	>>> a
        	6
        	'''
        ```
  
  - `python -m doctest file.py`可以查看**整个**文件是否满足测试用例
  
  - `python -m doctest file.py -v`显示**整个**文件的每个测试用例的详情
  
  - 对单独函数的doctest测试`run_docstring_examples`：第一个参数是函数名，第二个参数固定`globals()`，第三个参数如果是`True`会显示每个测试点的结果
  
      ```python
      >>> from doctest import run_docstring_examples
      >>> run_docstring_examples(sum_naturals, globals(), True)
      Finding tests in NoName
      Trying:
          sum_naturals(10)
      Expecting:
          55
      ok
      Trying:
          sum_naturals(100)
      Expecting:
          5050
      ok
    ```
  
  - `EOL`means “End of Line"

### python operator

Numbers may be combined with mathematical operators to form compound expressions. In addition to `+` operator (addition), the `-` operator (subtraction), the `*` operator (multiplication) and the `**` operator (exponentiation), there are three division-like operators to remember:

- Floating point division (`/`): divides the first number number by the second, evaluating to a number with a decimal point *even if the numbers divide evenly*.
- Floor division (`//`): divides the first number by the second and then rounds down, evaluating to an integer.
- Modulo (`%`): evaluates to the positive remainder left over from division.

## lecture2

* `a,b,c = 1,2,3`同时赋值

* `f = max`可以赋值函数

* `max = 1`可以将内置函数当初普通变量，并且内置函数不能在使用

* 全局变量会影响包含它的函数的返回值

* `from file1.pyfile import func`在shell，中引用某python文件中的函数，python文件不用加.py后缀

* **变量与右边的结果值绑定**

* 函数

  * ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220507114329.png)
  * ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220507114345.png)

* import，def和赋值语句都相当于在当前/global环境做一个键值绑定。

* **shell中输入函数会有一个identifying description，如`<built-in function max>`，如果变量是函数，会有提示**

* =右边的表达式先执行

* `print`返回**None**，表达式的值如果为None在交互式会话中不会显示，但是`print(None)`可以显示None

* ```python
  def with_if_function():
      """
      >>> result = with_if_function() 
      42
      47
      >>> print(result)
      None
      """
      return if_function(cond(), true_func(), false_func()) # 传入的为None
  ```
  
* **Name Evaluation.** A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found.

* The ***domain*** of a function is the set of arguments it can take. The ***range*** of a function is the set of values it can return. The ***intent*** of a function is the relationship it computes between inputs and output (as well as any side effects it might generate). 

* **def**一个函数在环境图中是**先创造一个函数对象（指定名字，参数和父环境/def所在的框架），在绑定到当前框架的一个name中（通过pointer）**

* 函数中的参数可以设置默认值，（只能从最后的参数开始？）

* `python -i ex.py`可以用于解释都是函数的文件，以**交互**的形式测试

## lecture3

* me：pure function 有返回值；no-pure function没有返回值的函数
* python中缩进的内容叫**suite**（if，def等等中）
* if语句本意是按条件只执行一个suite，如果使用函数调用实现if可能会先执行所有的”suite“
* **python中False值**（boolean表达式）：`False`，`‘’`，`0`，`None`，`[]`等等
  * `and`和`or`，先评估左边的值，再评估右边的值，**如果左侧的值可以确定表达式的值了，就不会评估右侧的值（这个行为叫short-circuit）**
  * 还有`not`
  * 优先级：**not > and > or**
  * ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220511151642.png)
* `<>if<>else<>`**语句，可以用于检查非法运算**![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220508222819.png)
* 常见错误：`SyntaxError`、`IndentationError`、`TypeError`、`NameError`、`IndexError`
* 内置的返回boolean 的函数，带前缀`is...`
  * `isinstance(var,type)`：检查var的数据类型

## *lecture4 Higher-order functoins（HOF）

> 1、function as arguments
>
> 2、functions as general methods
>
> 3、nested definitions
>
> 4、function as returned values
>
> 5、**currying**
>
> 6、lambda
>
> 8、function **decorators**
>
> ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220511222638.png)

* **绑定函数的name绑定的value是pointer（函数地址）**

* **函数先评估函数名，再评估参数（参数从左到右评估）**

* 环境图中**调用函数时**进入一个local frame，其对应的函数名是**intrinsic name或者λ**

* **function as arguments**：可以用parent frame去存储函数，而返回的函数只需要关注输入即可（用途之一：**组合**函数）还一个为一个general function传入特别的处理函数

  ```python
  def compose(f1,f2):
  	def func(x):
  		return f1(f2(x))
  	return func
  ```

* One negative consequence of this approach is that the global frame becomes cluttered with names of small functions, which must all be unique. Another problem is that we are constrained by particular function signatures: the `update` argument to `improve` must take exactly one argument. Nested function definitions address both of these problems, but require us to enrich our environment model.

* This discipline of sharing names among nested definitions is called *lexical scoping*. Critically, the inner functions have access to the names in the environment **where they are defined (not where they are called).**

  ```python
  def func(f,x):
      f()
      print(a)
      print(x)
  
  def funa(a):
      def fp():
          print(a)
      return func(fp,2)
  funa(12134)
  # func中不能找到a，而fp中可以找到
  ```

* **Function as Returned Values：**可以将两个函数结合为一个函数作为返回值

  ```python
  def merge(f,g):
  	def ff(x):
  		return f(g(x))
  	return ff
  # 不可以 ff = f(g())
  ```

* 环境之间的关系（chain）是在**定义**时确定的，即**在一个frame中调用def语句的时候确定其parent frame（parent就是执行def语句当前的frame）**，并且执行时在函数体中找一个name绑定的value沿着parent的关系找到的**first value**就是其值；me：函数**return**是沿着调用关系返回的。

* def中的参数默认值也在parent frame中

  ![image-20220521160517218](C:\Users\杨蔚\AppData\Roaming\Typora\typora-user-images\image-20220521160517218.png)

* **在环境图中如果创造的function object名称相同parent不同，也要再次创建，parent框架中的first value可能不同（me：只要调用一次def或者lambda就会在一个新的地址存放函数信息）**

* 函数调用**传参**时也是也是用相同的规则去查找传入参数的值；如果**参数是lambda表达式**`f(lambda x:x+y)`，那么lambda表达式的parent就是调用此函数的框架。

* Hence, we realize two key advantages of **lexical scoping** in Python.（me：因为是在定义时觉得而不是在调用时所以叫lexical）
  * The names of a local function do not interfere with names external to the function in which it is defined, because the local function name will be bound in the current local environment in which it was defined, rather than the global environment.（重名）
  * A local function can access the environment of the enclosing function, because the body of the local function is evaluated in an environment that extends the evaluation environment in **which it was defined.(但是调用的时候才可以确定其parent frame中的需要用到值)**

* **lambda表达式**

  *  A lambda expression evaluates to a function that has a single return expression as its body. Assignment and control statements are not allowed.

  * the result of a lambda expression is a function 

  * lambda和def的区别就是，def有intrinsic name，而lambda没有（**即使绑定到一个name其函数object的名称也是λ**），绑定lambda表达式的name即使调用**框架名也是λ**

  * 在环境图中，调用lambda函数时会返回lambda语句中查看

  * 可以有两个参数，也可以没有参数

    ```python
    g = lambda x,y : x+y
    print(g(1,2))
    # 3
    f = lambda :5
    print(f())
    # 5
    ```

* Functions as Returned Values时其local frame**不会释放！**可以**保存一些local date或者防止重名（用处之一）**，还是要返回定义处调用（me：根据**environment model**就可以在函数调用时做到对于函数变量对应的函数）

* **currying**

  * We can use higher-order functions to **convert a function that takes multiple arguments into a chain of functions that each take a single argument.** *（最外层的参数是原多参数的func）*

  * 自动化封装二参数currying

    ```python
    def curry2(f):
            """Return a curried version of the given two-argument function."""
            def g(x):
                def h(y):
                    return f(x, y)
                return h
            return g
    ```

  * 解除二参数的currying

    ```python
    def uncurry2(g):
            """Return a two-argument version of the given curried function."""
            def f(x, y):
                return g(x)(y)
            return f
    ```

* programming languages impose restrictions on the ways in which computational elements can be manipulated. Elements with the **fewest restrictions** are said to have **first-class status**. Some of the "rights and privileges" of first-class elements are:（**？**）

  1. They may be bound to names.
  2. They may be passed as arguments to functions.
  3. They may be returned as the results of functions.
  4. They may be included in data structures.

* **Decorators装饰器**

  * decorators are used for **tracing**

  * 可以引入build-in funcion

    ```python
    from ucb import trace
    
    @trace
    def func(...)
    	...
    ```

  * selecting which functions to call when a program is run from the command line.（？？？）

  * 表示为@符号后面跟着封装的函数名，在def执行时会**先进行封装**，再将**原函数名绑定到封装的返回结果中**

    ```python
    def trace(fn):       # 参数为函数
    	def wrapped(x):  # 和原函数参数相同
    		print('-> ', fn, '(', x, ')')
    		return fn(x)
    	return wrapped
    @trace
    def triple(x):   # environment中triple实际绑定为wrapped
    	return 3 * x
    res = triple(12)
    ```

* **self reference**：函数的返回值是本身

  * 典型形式:

    ```python
    def print_all(x):
    	print(x)
    	return print_all
    ```

  * 根据HOF的性质可以用于**存储先前的值**，两个例子

  * ```python
    # 延迟打印
    def print_all(n):
        def print_m(m):
            print(n)
            return print_all(m)
        return print_m
    ```

  * ```python
    # 累计求和
    def print_sum(x):
        print(x)
        def num_sum(y):
            return print_sum(x+y)
        return num_sum 
    ```

* 主要是注重name-value的绑定，一个video中复杂的例子（5.8）

  ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220519125705.png)

* **HOF的应用1：函数功能累加**：用默认参数在parent frame中保留前一个函数的功能

  ```python
  def compose(func = lambda x:x):
      def gandf(g):
          def ff(x): ## 当前组合的函数
              return g(func(x))
          return compose(ff)
      return func,gandf
  cf,fadd = compose()
  ```

* **HOF应用2**：利用外层函数保存目标值（返回的函数都是g，但是g的parent frame中的值不同，以为def的frame不同）

  ```python
  def func(max = 0): # 得到输入过的最大值
      def g(x):
          if x > max:
              print(x)
              return func(x)
          else:
              return func(max)
      return g
  ```

## 牛顿迭代

* 用于可以用于解方程`y=f(x)`

  * 输入y和方程
  * 构建函数**F(x)=f(x)-y**，使其收敛为0
  * 设置x的初始值（建议是接近0的值），每次x的迭代值为**F(x)的切线与x轴的交点(x=x1-y1/df)**
  * **注意**：不一定会收敛

* code：其中improve和close都抽象出来，注意close的使用

  ```python
  def improve(update,close,guess = 1):
      while not close(guess):
          print(guess)
          guess = update(guess)
      return guess
  
  def close(a,b,h = 1e-6):
      return abs(a-b) < h
  
  def efunc(y,n):
      def f(x):
          return x**n-y
      def df(x):
          return n*(x**(n-1))
      def update(x):
          return x-f(x)/df(x)
      def nclose(x):
          return close(f(x),0)
      return improve(update,nclose) 
  import math
  def logfunc(y,a):
      def f(x):
          return math.log(x,a)-y
      def df(x):
          return 1/(x*math.log(a))
      def update(x):
          return x-f(x)/df(x)
      def lclose(x):
          return close(f(x),0)
      return improve(update,lclose)
  ```

# week2 Recursion

> 递归就是将问题分解为一个**更简单**的问题去处理（要相信子递归调用的结果，抽象去理解），直到base case

## lecture1

* **mutual recursion**一个两个函数相互递归的例子，计算银行卡的检测值，没第二个数就将其乘二再求每位的和，再将每位相加（递归只要考虑逻辑意义就行）

  ```python
  def split(n):
      return n//10,n%10
  
  def sum_digit(n):
      if n < 10:
          return n
      else:
          all_but_last, last = split(n)
          return sum_digit(all_but_last)+last
  
  def luhn_sum(n):
      if n < 10:
          return n
      else:
          all_but_last,last  = split(n)
      return luhn_sum_double(all_but_last)+last
  
  def luhn_sum_double(n):
      all_but_last,last = split(n)
      last = sum_digit(last*2)
      if n < 10:
          return last
      else:
          return luhn_sum(all_but_last)+last
  ```

* example2：inverse cascade

  ![image-20220519164434579](C:\Users\杨蔚\AppData\Roaming\Typora\typora-user-images\image-20220519164434579.png)

## Tree-Recursion

* tree recursion：**a function calls itself more than once.** （遍历不同的可能性）

* 在Tree-Recursion时注意输入**问题规模**，其时间复杂度呈**指数**增长

* 在递归时显示其调用状态可以使用装饰器：

  ```python
  from ucb import trace
  @trace
  def recursion_func(...)
  ```

* Chapter 1.7 中的例子（将一个数n分解为一连串非递减整数的和，分解的集合中的整数要小于等于m，问有多少种情况），sample<img src="https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220521154807.png" style="zoom: 67%;" />

  * 可以分解为两个更小规模的问题：1、分解集合已经包含m的情况下，剩下n-m可以怎么分解；2、分解集合最大为m-1的情况数

  * code

    ```python
    def count_partitions(n, m):
            """Count the ways to partition n using parts up to m."""
            if n == 0:
                return 1
            elif n < 0:
                return 0
            elif m == 0:
                return 0
            else:
                return count_partitions(n-m, m) + count_partitions(n, m-1)
    ```

  * me：非递归形式可以用dp

# Week3 Data Abstraction

## sequence

* 有三种类型的数据`int`/`float`/`comlpex`，可以用内置函数`type`检查

* 内置的gcd：`from fractions import gcd `

* sequence（所有公共操作）：

  * **With mutable data, methods called on one name can affect another name at the same time.！！！！**

  * len

  * 切片

  * in：对string类型特别，可以查看多个元素`'yang' in 'yangwei'`

  * **`'str'. join()`**：将序列（也就是**字符串、元组、列表、字典**）中的元素以指定的用`'str'`连接生成一个新的字符串（必须插入在字符元素中间？！）

    ```python
    x = ['1','2','3']
    print('+'.join(x))
    # 1+2+3
    
    a='I love China !'
    print(' '.join(a))
    print('-'.join(a))
    print('*'.join(a))
    #结果：
    '''
    I   l o v e   C h i n a   !
    I- -l-o-v-e- -C-h-i-n-a- -!
    I* *l*o*v*e* *C*h*i*n*a* *!
    '''
    
    a={"I":1,'love':2,'China!':3}
    print(' '.join(a))
    print('-'.join(a),'\n')
    
    b={"I":2,'love':1,'China!':0}
    print(' '.join(b))
    print('-'.join(b))
    '''
    I love China!
    I-love-China! 
    
    I love China!
    I-love-China!
    '''
    ```

  * 内置的聚合函数：`max`第二个参数如果是func返回的是列表中带入函数最大的列表中的值（与之对应的有`min`）：与`all`对应的是`any`，只要有一个True即可

    ```python
    >>>sum([[1,2],[3]],[])
    [1,2,3]
    ```

    ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220613220259.png)

  * `.check(value)`：计算value第一次出现的下标（list，tuple可用）

  * `.count(value)`：计算value出现的次数（list，tuple，string可用）

* **list**（mutable sequence）

  * **`is`用于判断是不是指向同一个mutable sequence（identity），`==`用于判断内容是不是相等（equality）**

    ```python
  suits = ['heart', 'diamond', 'spade', 'club']
    nest = list(suits)
  nest[0] = suits
    >>> suits is nest[0]
    True
    >>> suits is ['heart', 'diamond', 'spade', 'club']
    False
    >>> suits == ['heart', 'diamond', 'spade', 'club']
    True
    ```

  * **差不多就和指针类似（`np.array`也近似于指针）**

  * 访问列表元素的方式

    ```python
    pair = [10,20]
    x,y = pair  # m1
    x = pair[0] # m2
    from operator import getitem
    x = getitem(pair,0) # m3
    ```

  * 可以使用乘法和加法

    ```python
    >>> [1]+[2]*2
    [1, 2, 2]
    ```

  * list做constructor：**创建副本或者强制类型转化**，如果对一个list的类型使用强制转换`L = list(L)`，没有意义，相当于什么都没做（不会加一层），但是`L1 = list(L2)`**相当于L2的副本，对L1的改动不会传递到L2**

  * 列表的增删，注意以切片的方式插入的时候插入元素是**副本**，返回的切片也是**副本**，还有用切片的形式删除，如果用切片的形式赋值也是**副本**`sub = L[1:3]`（对sub的修改不会影响L）

    增加，`.insert(n,value)`在指定位置加入值![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220612213209.png)

    删除，`remove`删除是元素在列表中第一次出现的位置，`.pop(n)`可以删除并返回第n个元素

    ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220612213404.png)

* **range**：多用于for循环中表示连续的整数序列

  * `range(a)`：范围[0,a)
  * `range(a,b)`：范围[a,b)

* **string**

  * `.strip()/.lstrip()/.rstrip()`：只包含一个参数，删除首尾/首/尾指定字符

    ```python
    str1="0002300000"
    print(str1.strip("0"))
    # 23
    ```

  * **格式化字符串：`{}`中的数值表示`format`的第几个参数，当成对象看待**；还有格式化表示

    ```python
    # 普通形式
    username = 'Y'
    password = '123'
    "{0}'s password is {1}".format(username, password) 
    # "Y's password is 123"
    
    # 当作对象  
    >>> si_suffixes = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    >>> '1000{0[0]} = 1{0[1]}'.format(si_suffixes)  
    '1000KB = 1MB'
    
    >>> import humansize
    >>> import sys
    >>> '1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys)
    '1MB = 1000KB'
    
    
    # 格式说明符，和c一样
    >>> '{0:.1f} {1}'.format(698.24, 'GB')
    '698.2 GB'
    >>> '{0:f}'.format(1.222) 
    '1.222000'
    >>> '{0}'.format(1.222)   
    '1.222'
    >>> '{0:05d}'.format(23)    
    '00023'
    ```

  * 大小写转化：`'STR'.lower()/'str'.upper()`

  * 对指定子串计数：`'STRSTR'.count('STR')`

  * **拆分键值对构造词典`split()`：**解析url的请求参数(query parameters)

    ```python
    >>> query = 'user=pilgrim&database=master&password=PapayaWhip'
    >>> a_list = query.split('&')                            
    >>> a_list
    ['user=pilgrim', 'database=master', 'password=PapayaWhip']
    >>> a_list_of_lists = [v.split('=', 1) for v in a_list]  
    >>> a_list_of_lists
    [['user', 'pilgrim'], ['database', 'master'], ['password', 'PapayaWhip']]
    >>> a_dict = dict(a_list_of_lists)                       
    >>> a_dict
    {'password': 'PapayaWhip', 'user': 'pilgrim', 'database': 'master'}
    ```

  * `str.encode('type')`：字符串编码为bytes对象（一连串十六进制的数值，形式`b'\xe6\xb7\xb1\xe5\x85\xa5 Python'`）；`bytes.decode('type')`：bytes解码为字符串

* **tuple**（immutable sequence），内容不可以改变

  * 1个元素的tuple和0个元素的tuple

    ```python
>>> ()
    ()
>>> (1,)
    (1,)
  ```
    
  * 不可以改变每个element指向的value，但可以对指向的mutable value进行修改

    ```
  t  = (1,2,[3,4])
    t[2].pop()
  ```
  
* **dictionaries**（immutable sequence）

  * key不能是list或者dictionary或者any mutable type（**tuple**可以）

  * 创建顺序和显示顺序无关

  * 可以通过赋值语句插头键值对

    ```python
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['L'] = 50
    >>> numerals
    {'I': 1, 'X': 10, 'L': 50, 'V': 5}
    ```

  * dictionary comprehension（和list comprehension相似）

    ```python
    {x:x*x for x in range(2)}
    # {0:0,1:1,2:4}
    ```

  * 对一个list，如果每个元素都是pair`[x,y] or (x,y)`，可以使用强制类型转换`dict()`

  * `.get(key,default_v)`：如果存在key值返回对应的value，否则返回defaul_v（me：可以用于if）

  * 内置方法，`.keys() .values() .items()`，（me：对其返回值使用list强制类型转换为list）

    <img src="https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220612211010.png" style="zoom: 67%;" />

* 数据抽象边界，高层的函数只使用第一层的函数实现

  ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220605213249.png)

* for语句

  * 可以解包，类似`x,y = [1,2]`

  ```python
  l1 = [[1,2],[3,4]]
  for x,y in l1:
  	print(x,y)
  # 12
  # 34
  ```

  * `_`，不会使用的变量
  * `pass`：防止循环体为空

* 

## Exception

* 如果python解释器检测到Error就会停止，对Exception的处理就是防止python解释器停止运行

* 异常出处理可以不遵守正常的python控制链：（me：）当函数嵌套时`f(g(h(x)))`，h内抛出的异常会Traceback到global，在这个chain上都可以捕获处理

* raise statement：抛出一个异常，`BaseException/TypeError/NameError/KeyError/RuntimeError`

  * 异常构造函数可以传入字符串（异常说明），`raise TypeError('bad argument!')`

* try statement语法

  ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220613155408.png)
  * try中抛出异常的语句之后的都不会执行

  * 多重try嵌套时（比如函数调用）：会在满足exception的**最近**的try中捕获，执行对应的except的suite

    ```python
    # Multiple try staements
    def invert(x):
    	try:
    		res = 1/x
    	except ZeroDivisionError as e:
    		print('handled',type(e))
    	return res
    	
    def go(f,x):
    	try:
    		return f(x)
    	except NameError as e:
    		print('handle',e)
    ```


## Tree

* constructor返回的是一个新的指针

## local state

* me：可能是因为python没有声明过程
* 对于nonlocal：一个函数每次调用都会生成一个新的frame（其中的local data 都是全新的），但是其parent frame不变，因此parent frame中可以存储一些可以保留操作过程的变量

*  The `nonlocal` statement indicates that the name appears somewhere in the environment other than the first (local) frame or the last (global) frame.
* If `balance` has not previously been bound to a value, then the `nonlocal` statement will give an error.
* within the body of a function, all instances of a name must refer to the same frame.This restriction allows Python to pre-compute which frame contains each name before executing the body of a function. When this restriction is violated, a confusing error message results. 
* In fact, assignment statements already had a dual role: they either created new bindings or re-bound existing names.
* . As we study interpreter design, we will see that pre-computing facts about a function body before executing it is quite common.

# lab&&hw&&perplex

* `float('inf')`：表示无穷大

* 切片

* hw02的Q3

* 在lab2中**Q9**`f = lambda x:f1(f(x))`为什么会无效递归（me：lambda的parent是当前frame，f和f混淆了）？必须使用额外的`compose1`去组合函数（f会绑定到一个局部值）

* hw03的Q6

* HOG

  * `global`对于**全局变量**（函数也是，局部定义函数不能和全局重名）如果使用时需要修改，要先声明再修改，**否则会有**`UnboundlocalError`

    ```python
    gcount = 0
    def global_test():
        global gcount
        gcount +=1
        print (gcount)
    global_test() # 1
    ```

    * `global`定义时不能进行赋值操作，即使在函数中定义，也可以被全局使用（函数调用后）

    ```python
    def add_a():
        global  a
        a =   3
    add_a()
    print(a) # 3
    ```

  * `nonlocal`nonlocal关键字用来在函数或其他作用域中使用外层(**非全局**)变量（否则调用的框架会生成一个同名的局部变量）

    ```python
    def add_b():
        '''
        10
        10
        '''
        b = 42
        def do_global():
            nonlocal  b
            b = 10
            print(b)
        do_global()
        print(b)
    add_b()
    ```

  * `def func(*args):`可变参数

* lab05：

  * 随意从一个列表list中选择一个元素

    ```python
    import random
    random.choice([1,2,3])
    # 2
    ```
    
  * **`zip`：想从多个列表中分别迭代元素，这时我们就可以使用python中的zip方法,事例如下：**
  
    ```python
    l1 = [1,2,3,4,5]
    l2 = ['a','b','c','d','e','f']
    for x,y in zip(l1,l2):
        print(x,y)
    '''
      结果：
    1 a
    2 b
    3 c
    4 d
    5 e
    '''
    
    import numpy as np
    a=[1,2,3,4,5]
    b=(1,2,3,4,5)
    c=np.arange(5)
    d="zhang"
    zz=zip(a,b,c,d)
    print(zz)
    
    '''
    输出：
    [(1, 1, 0, 'z'), (2, 2, 1, 'h'), (3, 3, 2, 'a'), (4, 4, 3, 'n'), (5, 5, 4, 'g')]
    '''
    ```
  
    如果zip中的sequence不等长，只会结合到**最小**的长度：
  
    ```python
    import numpy as np
    a=[1,2,3]
    b=[1,2,3,4]
    c=[1,2,3,4,5]
    zz=zip(a,b,c)
    print(zz)
    
    输出：[(1, 1, 1), (2, 2, 2), (3, 3, 3)]
    ```
  
    可以用`itertools.zip_longest`来处理，空出的位置返回`None`，也可以指定
  
    ```python
    from itertools import zip_longest
    
    l1 = [1,2,3,4,5]
    l2 = ['a','b','c','d','e','f']
    for i in zip_longest(l1,l2):
        print(i)
    '''
     结果：
     (1, 'a')
    (2, 'b')
    (3, 'c')
    (4, 'd')
    (5, 'e')
    (None, 'f')
    '''
    
    for i in zip_longest(l1,l2,fillvalue=0):
        print(i)
    '''
    结果：
    (1, 'a')
    (2, 'b')
    (3, 'c')
    (4, 'd')
    (5, 'e')
    (0, 'f')
    '''
    ```
  
    
  
    