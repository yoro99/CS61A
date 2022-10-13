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
>
> * vscode扩展
>   * PEP8：格式化代码，`Shift + Alt + F`

# week1

> * `python ok --local`  加入`--local`可以在本地测试并保存
> * 按下快捷键Ctrl+Shift+S，即可自动滚动屏幕，截取整个网页
> * `python ok -q <question name> -i`可以在案例失败后继续测试
> * `python ok -q <question name> --trace`a browser window should open up with your code，environment diagram
> * `python ok -u --local -v`如果有locked测试可以看完成的百分比
> * `python ok --score --local`可以查看每个问题的成绩
> * `C^c`可以在shell中中断python运行（infinite loop）
> * 可视化运行python代码的[website](https://pythontutor.com/composingprograms.html#mode=edit)
> * `help(function_name)`：可以查看具体函数的详情

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

- `ls`: lists all files in the current directory

- `cd <path to directory>`: change into the specified directory

- `mkdir <directory name> `: make a new directory with the given name

- `mv <source path> <destination path> `: move the file at the given source to the given destination

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

* **python在一个frame内不分什么局部变量，即使使用for之后其中的迭代元素也存在于frame中**

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

* 函数中的**参数**[函数的参数 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888)

  * 可以设置默认值，放在后面

  * 可变参数`*args`，传入后以tuple显示，如果要传入list和tuple在前面加`*`

  * 关键字参数`**kw`，键值对形式传入，传入后以dictionary显示

  * 命名关键字（传入时必须说明参数名）`def person(name, age, *, city, job):/def person(name, age, *args, city, job):`

  * 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数；复合传参的例子：

    ```python
    def f2(a, b, c=0, *, d, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
        
    >>> f2(1, 2, d=99, ext=None)
    a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
    >>> args = (1, 2, 3)
    >>> kw = {'d': 88, 'x': '#'}
    >>> f2(*args, **kw)
    a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
    ```

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

  *  A lambda expression evaluates to a function that has **a single return expression as its body**. Assignment and control statements are not allowed.

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

* **Decorators装饰器！：**

  * decorators are used for **tracing**

  * 可以引入build-in funcion

    ```python
    from ucb import trace
    
    @trace
    def func(...)
    	...
    ```

  * selecting which functions to call when a program is run from the command line.（？？？）

  * 表示为@符号后面跟着封装的函数名，在def执行时会**先进行封装**，再将**原函数名绑定到封装的返回结果中（装饰器的位置需要在被装饰函数的前部）**

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
    
  * **装饰递归函数：**递归函数体**内**的出现的位置都会转化为被装饰后的函数

  * 多重装饰器：多层装饰器在装饰的时候，它的顺序是**由下往上**，而在执行的时候，它的顺序由**上到下**

    ```python
    '语法糖会将紧挨着的被装饰对象的名字当做参数自动传入装饰器函数中'
    #代码示例：
    def outter1(func1):
        print('加载了outter1')
        def wrapper1(*args, **kwargs):
            print('执行了wrapper1')
            res1 = func1(*args, **kwargs)
            return res1
        return wrapper1
    
    def outter2(func2):
        print('加载了outter2')
        def wrapper2(*args, **kwargs):
            print('执行了wrapper2')
            res2 = func2(*args, **kwargs)
            return res2
        return wrapper2
    
    @outter1
    @outter2
    def index():
        print('from index')
        
    #输出结果：
    加载了outter2
    加载了outter1
    执行了wrapper1
    执行了wrapper2
    from index
    ```

  * **Count和Memoization：**下例中count(fib)每个n只会调用一次，memo(fib)中会检查是否存在（而多次调用，存在则不会递归调用的了）

    ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220905203338.png)

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

  * **With mutable data（list&dictionary）, methods called on one name can affect another name at the same time.！！！！**

    * **对mutable data比较**

      * `==`：变量绑定的value的内容相同
      * `is/is not`：变量绑定的是**同一个value**

    * **A default argument value is part of a function value（value是会和函数def时一起创建的，但是bind会变），not generated by a call（mutable value会产生一些危险的行为）**！！即小心默认参数是mutable data的情况！！！！！！！！！！！！！！！！！！！

      ```python
      def f(s=[]):
      	s.append(3)
      	return len(s)
      f() # 1 
      f() # 2
      f() # 3
      ```

  * len：返回长度

  * 索引：index -n 等于 len(l) - n，**即索引为-1时就是最后一个元素**

    * 索引`array[n][m][k] `等价于`array[n,m,k]`

  * **切片**：形式`seq[begin:end:step]`，**create a new list!**

    * step是在**最后位置**，如果**负数是从结尾到开头，默认值为1**
    * **省略的值为默认值**`[0::2]`：则begin = 1，end为长度，step为2！
    * `...`：表示其他维度不变，代替切片操作前/后面所有的`:`，即`[:,:,2]`和`[... , 2]`的输出等价

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

  * **内置的聚合函数**：`max`第二个参数如果是func返回的是列表中带入函数最大的列表中的值（与之对应的有`min`）：与`all`对应的是`any`，只要有一个True即可

    ```python
    >>>sum([[1,2],[3]],[])
    [1,2,3]
    ```

    * 注意`max`/`min`用法要带关键词`key=`！可以加参数`default=`指定最小/大值不存在时（空seq）的默认返回值

    ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220613220259.png)

    * me：**判断两个np.array或tensor是否相等使用all**（因为直接使用比较运算符会得到element-wise的结果）：

      ```python
      x = np.array([1,2,3])
      y = np.array([1,2,2])
      all(x == y) # 如果不相等输出False
      ```

  * `.check(value)`：计算value第一次出现的下标（list，tuple可用）

  * `.count(value)`：计算value出现的次数（list，tuple，string可用）

* **list**（mutable sequence）

  * **`is`用于判断是不是指向同一个mutable sequence（identity，身份），`==`用于判断内容是不是相等（equality）**

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

  * 可以使用乘法和加法，会**create a new list ！！！**

    ```python
    >>> [1]+[2]*2
    [1, 2, 2]
    ```

  * list做constructor：**创建副本或者强制类型转化**，如果对一个list的类型使用强制转换`L = list(L)`，没有意义，相当于什么都没做（不会加一层），但是`L1 = list(L2)`**相当于L2的副本，对L1的改动不会传递到L2**

  * 列表的增删，注意以切片的方式插入的时候插入元素是**副本**，返回的切片也是**副本**，还有用切片的形式删除，如果用切片的形式赋值也是**副本**`sub = L[1:3]`（对sub的修改不会影响L）

    **增加**，`.insert(n,value)`在指定位置加入值![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220612213209.png)

    **删除**，`remove`删除是元素在列表中第一次出现的位置，`.pop(n)`可以删除并返回第n个元素

    ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220612213404.png)

* **range**：多用于for循环中表示连续的整数序列

  * `range(a)`：范围[0,a)
  * `range(a,b)`：范围[a,b)

* **string**（immutable sequence）

  * `ord('A') # 65`：得到字符的ascii码值；

  * `.strip()/.lstrip()/.rstrip()`：只包含一个参数，删除首尾/首/尾指定字符；如果不指定参数：**默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。**

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

    * `</>/^`：表示左对齐/右对齐/居中

  * 使用`in`检查是否包含字串**：

    ```python
    s1 = 'yang wei'
    s2 = 'yang'
    s2 in s1 # True
    ```

  * 大小写转化：`'STR'.lower()/'str'.upper()`；大小写相互转化`'Str'.swapcase()`

  * 对指定子串计数：`'STRSTR'.count('STR')`

  * **拆分键值对构造词典`split()`：**解析url的请求参数(query parameters)

    * `split()`：如果分隔符为空，**默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。（会将单词间*所有*空格都不算入，注意和单个空格的行为不同）**

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

  * 标点符号

    ```python
    import string
    string.punctuation # 返回所有标点符号的字符串
    ```
    
    * **除去标点符号，sample：(原理？)**
    
    ```python
    punctuation_remover = str.maketrans('','',string.punctuation)
    'i ? like you?'.strip().translate(puntctuation_remover)
    ```

* **tuple**（immutable sequence），内容不可以改变

  * **1个元素的tuple**：`(1,)`和0个元素的tuple：`()或tuple()`

  * 不可以改变每个element指向的value，但可以对指向的mutable value进行修改

    ```python
    t  = (1,2,[3,4])
    t[2].pop()
    ```

* **dictionaries**（mutable sequence）

  * **key不能是list或者dictionary或者any mutable type**（**tuple**可以，但是tuple中的元素不可以为mutable type）

  * 创建顺序和显示顺序无关

  * 可以通过赋值语句**插入**键值对

    ```python
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['L'] = 50
    >>> numerals
    {'I': 1, 'X': 10, 'L': 50, 'V': 5}
    ```
    
    * `.pop(key)`：**删除键，并返回对应的value**
  
    * dictionary comprehension（和list comprehension相似）
  
  ```python
  {x:x*x for x in range(2)}
  # {0:0,1:1,2:4}
  ```
  
    * 对一个list，如果每个元素都是pair`[x,y] or (x,y)`，可以使用强制类型转换`dict()`
  
    * `.get(key,default_v)`：**如果存在key值返回对应的value（可以设为None），否则返回defaul_v**（me：可以用于if）
  
    * `key in dict`：`in`可以判断一个key在不在dictionary中
  
    * 内置方法，`.keys() .values() .items()`，（me：对其返回值使用list强制类型转换为list）,**返回的都是iterator**
  
      <img src="https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220612211010.png" style="zoom: 67%;" />
      
  * **for迭代时**，me：对于第三种方式`a,b`的形式应该是一个tuple，而字典一个键值对不是以tuple存在的
  
    ```python
    for a in disc:  # 等价于keys()
    	print(a)
    for a,b in disc.items(): # 同时迭代键值
    	print(a,b)
    for a,b in disc:  # 错误！！！！！！！！！！！！！
    	print(a,b)
    ```
  
* **set**（mutable sequence）

  * 对应有一个**frozenset**，是immutable的，包含除了mutation method以外所有的set的method
  * 不能包括mutable data（list，dictionaries，or other set，这些值都是 **unhashable**）
  * <img src="C:\Users\杨蔚\AppData\Roaming\Typora\typora-user-images\image-20220906114112841.png" alt="image-20220906114112841" style="zoom: 50%;" />
  * set("string")：返回字符串中所有字符组成的set`{'s','t','r','i','n','g'}`

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

  * `_`：**不会使用的变量**
  * `pass`：防止循环体为空

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

* raise：抛出异常，异常可以使用带字符串说明，也可以什么都不带

  ```python
   if not (0 < n < 4000):
          raise OutOfRangeError('number out of range (must be 1..3999)')
  if not isinstance(n, int):                                          ①
          raise NotIntegerError
  ```

  * 抛出的区别（不是上面那个demo）：

    <img src="https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220927222554.png" style="zoom:80%;" />

## ？Tree

* constructor返回的是一个新的指针

# Week4

## local state

* me：可能是因为python没有声明过程

* python中赋值默认是绑定到一个**新的局部变量**的过程（没有其他声明的时）

* 对于nonlocal：一个函数每次调用都会生成一个新的frame（其中的local data 都是全新的），但是其parent frame不变，因此parent frame中可以存储一些可以保留操作过程的变量（**可以使用mutable value去实现和nonlocal相同的效果！！！**）

* The `nonlocal` statement indicates that the name appears somewhere in the environment other than the first (local) frame or the last (global) frame.（assignment语句的默认功能是将等式右侧的值绑定到当前框架）

  ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220621180600.png)

* If `balance` has not previously been bound to a value, then the `nonlocal` statement will give an error.

* within the body of a function, all instances of a name must refer to the same frame.**This restriction allows Python to pre-compute which frame contains each name before executing the body of a function.** When this restriction is violated, a confusing error message results. 

* In fact, assignment statements already had a dual role: they either created new bindings or re-bound existing names.

* As we study interpreter design, we will see that pre-computing facts about a function body before executing it is quite common.

* Referential Transparency, Lost：函数的调用会影响相同函数的调用结果（me：在使用nonlocal的时候注意）

  ```python
  def f(x):
      x = 4
      def g(y)
      	nonlocal x
          x = x+1
          return y+x
     	return g
  f1 = f(2)
  s = f1(3)+f1(4) # 18
  # s = 8 + f1(4) # 17
  ```

## Iterator&Generator

* *lazy computation（延迟计算）* describes any program that delays the computation of a value until that value is needed.
*  Calls to `__next__` make a mutating change to the iterator: they advance the position of the iterator.

### Iterator-对sequence的隐式表示

* 针对顺序访问的数据（不用全部显式的存储在内存中，一个在undlying series之上的顺序访问的工具，如map、fliter等操作本质都是共享底层序列的），一般的list、dict都是随机存储的数据

* The usefulness of iterators is derived from the fact that the underlying series of data for an iterator may not be represented explicitly in memory.（适用于*sequential access*）

* Iterator的两个mechanism，`iter()` and `next()`**都是build-in funtion，而不是method**

  * retrieving the next element in the sequence being processed（通过`next()`）

    ```python
    primes = [2, 3, 5, 7]
    >>> iterator = iter(primes)
    >>> type(iterator)
    >>> next(iterator)
    2
    >>> next(iterator)
    3
    >>> next(iterator)
    5
    ```

  * signaling that the end of the sequence has been reached and no further elements remain.（通过`StopIteration`）

    ```python
    try:
         next(iterator)
    except StopIteration:
         print('No more values')
    ```
    
  * **为了防止`StopIteration`，可以使用`next(it,k)`：**如果访问到结束就一直返回`k`

    ```python
    # terminal
    >>> x = [1,2,3]
    >>> t= iter(x)
    >>> next(t,'end')
    1
    >>> next(t,'end')
    2
    >>> next(t,'end')
    3
    >>> next(t,'end')
    'end'
    >>> next(t,'end')
    'end'
    ```

* In Python, an **iterable value** is anything that can be passed to the built-in `iter` function（或有`.__iter__()`，iterator本身也有）；an **iterator** is anything that can be passed to the built-in `next` function（或有`.__next__()`）

* **The built-in `next` function in Python invokes the `__next__` method on its argument.The built-in `iter` function in Python invokes the `__iter__` method on its argument.（iterator都是一次性的）**

* 对一个iterable values使用`iter()`或`.__iter__()`，都会创建一个new iterator（**iterator本身除外**，返回自己）

* 对iterator强制转为list时会执行所有的`next`，如果再使用`next`会报StopIeration异常

  ```python
  x = [1,2,3]
  t = iter(x)
  >>> next(t)
  1
  >>> l = list(t)
  >>> l
  [2, 3]
  >>> next(t)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  StopIteration
  ```

* 每次对sequence的构造的iterator都是独立迭代的，而且是mutable data，**对一个iterator使用`iter()`或`.__iter__()`返回的是与参数相同的value而不是copy（without having to worry about whether it is an iterator or a container.），所以都会跟踪当前iterator的迭代进度**

* 如果改变sequence的元素（list的第i个元素，或者dict每个key对应的value）不会影响已有的iter，可以看见改变；**但是如果sequence的长度变了，会影响已有的iter，出现RuntimeError**（仅对dictionary，不包括list！）

* 对iterator可以使用`list()`/`tuple()`/`sorted()`（返回有序的list）**转化为显示表示**，并且作为参数传入的iterator作废（因为迭代到了最后一个）

* **Built-in functions**（传入一个iterable values**返回一个iterator**，下面内置函数都是惰性计算的）

  * map：`map(func,seq)`，传入一个函数（对每个next的元素操作）和iterable value

    ```python
    # exp1
    >>> def double_and_print(x):
            print('***', x, '=>', 2*x, '***')
            return 2*x
    >>> s = range(3, 7)
    >>> doubled = map(double_and_print, s)  # double_and_print not yet called
    >>> next(doubled)                       # double_and_print called once
    *** 3 => 6 ***
    6
    >>> next(doubled)                       # double_and_print called again
    *** 4 => 8 ***
    8
    >>> list(doubled)                       # double_and_print called twice more
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    ```

  * **filter：**`filter(func,seq)`，传入一个函数（对当前`next`如果func的结果是True则返回）和iterable value

  * zip：返回iterator

  * reversed：返回原sequence反向的iterator

  * 一个iterator迭代完成后，在next就会一直抛出`StopIteration` exception；通常在一个iterator使用完成之后如果还要迭代都是创建一个新的iterator

* **！ for statements**

  * 使用对象是iterable values

  * To execute a `for` statement, Python evaluates the header , which must yield an iterable value. Then, the `__iter__` method is invoked on that value. Until a `StopIteration` exception is raised, Python repeatedly invokes the `__next__` method on that iterator and binds the result to the `<item>` in the `for` statement. Then, it executes the `suite`.

    ```python
    # for example
    >>> counts = [1, 2, 3]
    >>> for item in counts:
            print(item)
    1
    2
    3
    # 等价于
    >>> items = counts.__iter__()
    >>> try:
            while True:
                item = items.__next__()
                print(item)
        except StopIteration:  # 可以跳出while
            pass
    1
    2
    3
    ```
  
  * `StopIteration`：for循环检测到这个异常会**自动停止并且不会中断**程序，所以`__iter__`在满足迭代结束条件时要加`raise StopIteration`

### Genrators

* 只要函数体中有yield就会被当作Generator function，**返回Generator（也是iterator）**，用于进行延迟计算（**调用函数generator函数相当于创建一个生成器对象，不会执行函数体里的语句**，`next`进行迭代时才会执行，每次执行到`yield`停止**并保存变量和局部数据**，一般配合for语句使用）

* The generator **does not start executing any of the body statements** of its generator function until the first time `__next__` is invoked. The generator raises a `StopIteration` exception whenever its generator function returns.

* `yield`后面的元素即为`next()`返回的元素，如果generator中有iterator可以用`yield from`访问

  ```python
  def prefixed(s): # 获得字符串的所有前缀
  	if s:
  		yield from prefixed(s[:-1])
  		yield s
  # list(prefixed('both'))
  # ['b','bo','bot','both']
  def substrings(s): # 获得字符串的所有子串
  	if s:
      	yield from prefixed(s)
      	yield from substring(s[1:])
  ```

* **note：**生成器执行到函数结束就会自动跳出循环了，所以不需要`StopIteration`，一般生成器要么有个循环中产生`yield`，或者递归（如上）
* 将一个生成器传递给 `list()` 函数，它将遍历整个生成器（就像前例中的 `for` 循环）并返回所有数值的列表。

# Week5 Class

> Tree Class&List  Class见2.9

* `class`的`<suite>`里的assigment语句和def都会变成的**class attributes**，instance的`self`设立的是**object attributes**

  * class attribute对所有同类的instances相同

  * **self就是实例**

  * `__init__()` 方法调用时，对象**已经创建了**，你已经有了一个合法类对象的引用。

  * 访问顺序：instance的dot表达式先查找object attribute再查找class attribute，再查找基类属性

  * instance不能修改class attribute，如果对class attribute使用赋值语句修改**会生成一个对应instance attribute**

    ```python
    class Exm:
    	at1 = 1
    a = Exm()
  a.at1 = 2 # 变成a的instance attribute，不影响其他instance访问class attribute
    ```

* **dot notation**获取来自instance或者对应class里的attributes，先**evaluate左侧是class还是instance**

* **method = object + Function：method会自动绑定dot表达式左侧的实例到参数中**，即：

  * dot表达式会先判定左侧的是instance还是class
  * 如果是instance可以自动绑定到self
  * 如果是class，调用的是function，要传入instance

* `getattr(obj_name,'attr_name')/hasattr(obj_name,'attr_name')`获取/查看类或者对象中对应的属性

* `isinstance(instance_name, class_name)`：检查对应实例的类型是否是对应类或子类

* **Inheritance：**

  * ```python
    class <name>(<base class>):
    	<suite>
    ```

  * 子类会override与基类不同的属性，共享相同的属性（不用在子类中标明）

  * Base class attributes aren‘t copied into subclasses（子类中没有的attributes回去基类中look up）

  * 注意传入的self（是一个instance），`self.<attribute>`都会创建/修改instance attribute

  * 有重载或重写吗？

  * designing for Inheritance：

    * Don't repeat yourself; use existing implementations.(使用base class attribute)
    * inheritance represents is-a；composition represents has-a(e.g. bank instance has a attribute accounts)

  * Multiple Inheritance：

    * Complicated Inheritance不建议使用

    * ```python
      class <name>(<base class1>, <base class2>):
      	<suite>
      ```

    * **attribute查找顺序**：根据继承顺序，**从左至右**，**逐层**查找

* **Property Methods：**

  * `@property decorator`：可以像调用属性一样调用方法

  * `@<attribute>.setter`：可以用于模拟给属性赋值的行为，`<attribute>`必须存在于property method中

    <img src="https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220905193637.png"  />

* *？？？？？？？？？*![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220905200353.png)

## Polymorphism（多态）

* **polymorphic functions（多态函数）**：**适用于许多不同类型数据的函数**（如`repr/str`）
  * **调用的是对应的class attribute**，而不是instance attribute（见下图）
  * 没有`__str__`属性会调用`__repr__`替代
  * ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220905234019.png)

* **interface:**

  * shared message：不同object classes中的有相同行为的attribute name

  * 接口就是share message的**集合**，和他们的specification（me：**一系列类**中都实现的**同名同行为**的attribute）

    ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220905234907.png)

* **Special Method**（python的特点）：
  * 左右两侧都有双下划线，并且定义了很多built-in operators

  * ![image-20220906000445937](C:\Users\杨蔚\AppData\Roaming\Typora\typora-user-images\image-20220906000445937.png)

  * 注意使用`__radd__`的情况

  * ![image-20220906000818776](C:\Users\杨蔚\AppData\Roaming\Typora\typora-user-images\image-20220906000818776.png)

  * **type dispatching**（检查参数的类型做出对应的操作），**type coercion**（强制类型转换）

  * `__iter__`：一般如果class实现了`__next__`返回`self`(指定迭代的起始条件，类似于`self.x = 1`)

  * `__class__`：返回object的类型，可以用于**object访问类属性：**

    ```python
    class LazyRules:
        rules_filename = 'plural6-rules.txt'
    r2.__class__.rules_filename   
    ```

* 所有object value都会产生两种字符串表示
  
  * `__repr__`：返回易被python interpreter识别的**字符串（即表达式本身）**，用于编译器交互界面的输出（`>>>repr(obect)`输出字符串，`>>>object`输出字符串内的内容）
  * `__str__`：返回易被人类识别的**字符串**，用于print输出（`>>>str(obect)`输出字符串，`>>>print(object)`输出字符串内的内容）
  * `__eval__`：参数是**字符串**表达式，会输出表达式的结果
  * str和repr返回的字符串经常相等
  
* Modular design
  * ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220906001434.png)
  * 

## other

* 对于exponentiation（幂运算），将复杂度从O(n)降到O(logn)

  ![image-20220905205150694](C:\Users\杨蔚\AppData\Roaming\Typora\typora-user-images\image-20220905205150694.png)

* ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220906111853.png)

# Week_6 Interpreter

* ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220910155446.png)

# other

## 正则表达式

* `import re`

  ![image-20220912162411863](C:\Users\杨蔚\AppData\Roaming\Typora\typora-user-images\image-20220912162411863.png)

  ![image-20220912162423810](C:\Users\杨蔚\AppData\Roaming\Typora\typora-user-images\image-20220912162423810.png)

  * `[abc]/[^abc]`：匹配abc其一/除了abc之外的任意字符

  <img src="https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20221008191555.png" style="zoom: 67%;" />

* `re.search`匹配不成功什么都不返回，匹配成功返回一个object

* `re.findall(正则表达式,string)`返回string中满足表达式的所有字符的list

* 松散的正则表达式

  * 需要传递`ree.VERBOSE`参数

  * ![image-20220912162608592](C:\Users\杨蔚\AppData\Roaming\Typora\typora-user-images\image-20220912162608592.png)

# Dive into python3

* `sys,argv`：获取python脚本文件的时候命令行参数，来执行脚本里面的内容。第一个元素返回值是**编译命令后的**文件名

  ```python
  import sys
  filename = sys.argv[0]
  print filename
  # python .\sys.py
  # >>> .\sys.py  # 对应字符串值为'.\\sys.py'
  import sys
  filename = sys.argv[1]
  print filename
  # python sys.py yw
  # >>> yw
  ```

## 单元测试

* *测试驱动开发* 或 tdd：先写测试再开发

* 需要导入的模块和main

```python
import test_func_file
import unittest
class ToRomanBadInput(unittest.TestCase):
    def test_to_roman_known_values(self):           
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = test_func_file.to_roman(integer)       
            self.assertEqual(numeral, result)       
    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman3.OutOfRangeError, test_func_file.to_roman, 4000)  

    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(roman3.OutOfRangeError, test_func_file.to_roman, 0)     

    def test_negative(self):
        '''to_roman should fail with negative input'''
        self.assertRaises(roman3.OutOfRangeError, test_func_file.to_roman, -1)    
if __name__ == '__main__':
    unittest.main()
```

* 可以写好几个继承类去做单元测试也可以把测试方法写在一个类中
* shell的命令`python testfile.py -v`：去编译测试单元在的文件
* 测试单元的类中测试方法前缀必须为`test`

* `OK/FAIL/ERROR`三种测试状态（不满足测试条件返回FAIL）
* `self.assertEqual/self.assertRaises`：分别检测对应值的输出结果/抛出的异常（**即必须对异常的输入进行处理**）

* 异常类的编写

  ```python
  class OutOfRangeError(ValueError): pass
  class NotIntegerError(ValueError): pass
  ```

* 输出：会先输出每个测试方法结果，再输出FAIL/ERROR的详情

  <img src="https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220927214341.png" style="zoom:80%;" />

* **重构**是修改可运作代码，使其表现更佳的过程
* 测试时可逆操作的输入输出可以相互比较来判断运行是否正确

## 高级迭代器

* `()`构造生成器，和使用`tuple()`不同（返回一个tuple）
  * <img src="C:\Users\杨蔚\AppData\Roaming\Typora\typora-user-images\image-20221008200449225.png" alt="image-20221008200449225" style="zoom: 67%;" />

* **排列**(有序)，返回一个迭代器，第一个参数是string或list，第二个参数是一个排列对的成员个数

  ```python
  import itertools                              
  perms = itertools.permutations([1, 2, 3], 2)  
  >>> next(perms)                                   
  (1, 2)
  ```

  * 组合(有序)`itertools.combinations`，参数和用法同排列

  * `itertools.product()`函数返回包含两个序列的笛卡尔乘积的迭代器。

    <img src="https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20221008200937.png" style="zoom:50%;" />

* `itertools.groupby()`：函数接受一个序列和一个key 函数, 并且返回一个生成**二元组**的**迭代器**。每一个二元组包含`key_function(each item)`的结果和另一个包含着所有共享这个key结果的元素的**迭代器**（**将序列中key()返回值相同的元素分为一组**）

* `itertools.chain()`函数接受两个迭代器，返回一个迭代器，它包含第一个迭代器的所有内容，以及跟在后面的来自第二个迭代器的所有内容。(实际上，它接受任何数目的迭代器，并把它们按传入顺序串在一起。)

*  `itertools.zip_longest(iter1，iter2)`函数在到达**最长的**序列的结尾的时候才停止, 对短序列结尾之后的元素填入`None`值.

  * `zip`结合到最短长度就会停止

* `'SEND + MORE == MONEY'.translate(translation_table)`：translation_table是一个dict，可以将字符串在字典中的key值转化为对应的value值（key和value需要为ASCII码，可以使用`ord`）

* `eval('string')`：可以计算字符串形式的表达式的值（`eval('2 * 5') # 10`）

* **`subprocess` 模块允许你执行任何shell命令并以字符串形式获得输出**。

  * `"subprocess.getoutput('rm /some/random/file')"`

  * 使用`__import__`以字符串表达式的形式导入模块`eval("__import__('subprocess').getoutput('rm /some/random/file')")`

    ```python
    >>> eval("__import__('math').sqrt(5)", {}, {})  ②
    2.2360679774997898
    ```

* `__builtins__`：包含了“内建”函数，可以覆盖为None从而拒绝访问内建函数（如`__import__`）

## 文件

* windows的文件子目录`\`，linux和Macos的子目录为`/`

* `locale.getpreferredencoding()`获得python环境的默认编码，可以在`open(...,encoding = )`中修改

  * `mode = w/a`此参数决定读写方式，写会如果文件不存在会创建文件（`w`会覆盖原先内容）
  * `\n`自己添加换行符

* 打开文件对象的方法

  * `read()`：读取文件剩下所有的内容，`read(int n)`返回后面的n个**字符**
  * `seek(int n)`：定位到文件特定**字节**（**不可以定位到一个字符的中间字节再开始读取**）
  * `tell()`：返回当前的**字节**位置

* 使用`with`的对象

  * `with object`：后面跟着一个创建的（文件，也可以是其他）对象
  * 进入`with`时会调用`def __enter__(self):`，**该方法的返回值（self）赋值给`as`指向的变量！（没有`as`也可以不返回）**
  * 退出`with`时会调用`def __exit__(self, *args):`，不管是否执行完with中的内容只要退出函数体都会调用此方法。**实际上，如果引发了例外，该例外信息将会被传递给 `__exit__()` 方法（可以防止发生意外时程序中断，但是文件没被关闭/打开文件的方式可能会使得其他程序不能访问）；**
  * `with createObject() as o1,createObject() as o2:`从左到右执行，可以创建多个对象

* 按行读取文件

  * `f.readline()`

  * ```python
    with open('examples/favorite-people.txt', encoding='utf-8') as a_file:  ①
        for a_line in a_file: 
    ```

* `io.StringIO("..")`：对文件相同的处理方式处理内存的字符串
* `.gz`：windows下的一种压缩方式的文件后缀
* 标准输入输出
  
  * `import sys/sys.stdout`：修改后一可以用于**重定向**

## 序列化

* me：就是将对象转化为某种格式进行可持久化存储
* pickle文件（二进制文件，**python独有**）
  * 需要以二进制的方式读写` with open('entry.pickle', 'rb') as f`
  * `.dump`写入
  * `.load`读出
  * **可以直接不用转化读入一个对象/二进制数据**
* json文件（文本文件，**跨语言**）
  * 以dict的形式序列化数据
  * 不同类型的数据在序列化结果的value如下
  * ![](https://mdgraph-1301162508.cos.ap-shanghai.myqcloud.com/2022/20220930171347.png)
  * `.dump/.load`写/读
  * 写入时对object或者不在表格中的数据要转化为字符串或dict来作为序列化的value，并且load时需要转化为原先的形式：` json.dump(entry, f, default=customserializer.to_json)`可以设置instance类型检查和转换函数
  * tuple如果作为value写入json文件会**变为list**，且再load时还是list

# lab&&hw&&perplex

* 关于模块`import`
  * python文件可以作为模块，`import`时不加后缀名
  * **对于`if __name__ == __main__`：**在import模块时，会执行模块中其他部分（**只执行一次**），顶层执行文件（主程序main program）的`__name__`为`__main__`，其他导入模块的`__name__`为**模块名**，可以控制模块中一些语句不被执行
  * 内层和外层模块有`import`相同的模块时，模块将**只被导入一次（对比c/c++中的`#include`）**，随后被缓存了。如果导入一个已导入模块，将不会导致任何事情发生。因此对应模块中这段代码将只在第一此导入时运行
  * 模块如果没有在if语句中的可执行语句会被执行

* python中一切都是对象包括函数，在动态函数中使用外部参数值的技术称为 **闭合【closures】**

* `pass`：相当于c/c++中`{}`，在空函数或者while/for中使用

* `print(something,end='')`：指定输出结束是否换行

* `float('inf')`：表示无穷大

* `ord('c')`：返回字符的ascii码

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
  
