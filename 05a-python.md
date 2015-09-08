# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both ways to store long or long-ish lists of information that won't change over time.

>> Lists contain a list of values that are numbered starting with zero. You can change values in a list.

>> Tuples are similar but you can't change the values within for the rest of the program they're used in. Lists are mutable, tuples are immutable. Tuple values are also numbered starting with zero.

>> The syntax is different between lists and tuples too. And tuples can be used for performance optimization, since they're immutable, they're easier on memory and processor.

>> Values in a tuple should express different concepts, but values in a list should all express the same concept or belong to the same category.

>> Tuples are usable as dictionary keys, but lists aren't. Basically, an object must support the hash function and lists can't do this. Lists are containers and other operations treat them like containers. Hashing lists by id could produce errors in instances where different lists have the same content or would produce a KeyError. Lists can be hashed by contents like tuples, but the errors would occur because of the mutability property of lists themselves.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are only made up of values, but sets require hashable items (lists don't). Lists maintain the order of items and sets don't.
>> Duplicate items aren't allowed with sets, but can exist within lists.

>> Performance with sets is much quicker when looking for an element because the hash lookup is used, since sets only allow hashable items.
>> Some stats from the site bogdan.org.ua include a 12% bump in speed when adding new items to lists versus sets:

	$python -mtimeit -s 'myset = set()' 'for x in xrange(1000): myset.add(x)'
	10000 loops, best of 3: 133 usec per loop
	$python -mtimeit -s 'tmp = list()' 'for x in xrange(1000): tmp.append(x)'
	loops, best of 3: 116 usec per loop

>> The author does a speed comparison between lists and sets for membership testing also, using the following:

	$python -mtimeit -s 'tmp = set()' -s 'for x in xrange(1000): tmp.add(x)' 'for x in xrange(100000): x in tmp'
	100 loops, best of 3: 7.27 msec per loop
	$python -mtimeit -s 'tmp = list()' -s 'for x in xrange(1000): tmp.append(x)' 'for x in xrange(100000): x in tmp'
	10 loops, best of 3: 2.12 sec per loop

>> Here, sets performed much faster since they were created differently from lists for exactly such a reason.



>> A quick summary of best use cases for lists and sets:

>> Lists: for ordered data, mixed collection of data in a central place, mutability required, no need for data indexing by custom value, no need for stack or queue, and when data doesn't need to be unique.

>> Sets: unique set of data necessary, mutability required, values/items need to be manipulated mathematically (difference, union, intersection, etc), no need for nested lists, sets, or dictionaries (since sets don't support unhashable types). 


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> In Python, Lambda is a construct that allows for fuctions that aren't bound to a name (anonymous functions).
>> It's often used with common functional concepts such as map(), reduce(), or filter(). An example from secnetix.de illustrates the difference between lambda as a normal function definition ("f") and a lambda function ("g"):

	def f (x): return x**2
	...
	print f(8)
	64
	
	g = lambda x: x**2
	print g(8)
	64
	
>> Lambda can be used anywhere a function is expected, and it doesn't have to be assigned to a variable.
>> Some users point out lambda being more useful that a typical function when developing GUIs with Python. For example, if you're creating
>> several buttons, you can use a single parameterized callback instead of a unique callback per button:

	for value in ["one", "two", "three"]:
		b = tk.Button(label=value, command=lambda arg=value: my_callback(arg))
		b.pack()
		
>> Another stackoverflow user finds it useful for a list of functions that do the same thing, but for different circumstances:

	plural_rules = [
		lambda n: 'all'
		lambda n: 'singular' if n == 1 else 'plural',
		lambda n: 'singular' if 0 <= n <= 1 else 'plural',
		...
	]
	# Call plural rule #1 with argument 4 to find out which sentence form to use.
	plural_rule[1](4) # returns 'plural'
	
>> 
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





