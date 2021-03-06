## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

---

###Part I - Regular Expressions  

Use regular expressions to:

####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> phd (31); scd (6); mph (2); ms (2); 0 (1); bsed (1); jd (1); ma (1); md (1)


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> professor (37); assistant professor (12); associate professor (12)


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> bellamys@mail.med.upenn.edu; warren@upenn.edu; bryanma@upenn.edu; jinboche@upenn.edu; sellenbe@upenn.edu; jellenbe@mail.med.upenn.edu; ruifeng@upenn.edu; bcfrench@mail.med.upenn.edu; pgimotty@upenn.edu; wguo@mail.med.upenn.edu; hsu9@mail.med.upenn.edu; rhubb@mail.med.upenn.edu; whwang@mail.med.upenn.edu; mjoffe@mail.med.upenn.edu; jrlandis@mail.med.upenn.edu; liy3@email.chop.edu; mingyao@mail.med.upenn.edu; hongzhe@upenn.edu; rlocalio@upenn.edu; nanditam@mail.med.upenn.edu; knashawn@mail.med.upenn.edu; propert@mail.med.upenn.edu; mputt@mail.med.upenn.edu; sratclif@upenn.edu; michross@upenn.edu; jaroy@mail.med.upenn.edu; msammel@cceb.med.upenn.edu; shawp@upenn.edu; rshi@mail.med.upenn.edu; hshou@mail.med.upenn.edu; jshults@mail.med.upenn.edu; alisaste@mail.med.upenn.edu; atroxel@mail.med.upenn.edu; rxiao@mail.med.upenn.edu; sxie@mail.med.upenn.edu; dxie@upenn.edu; weiyang@mail.med.upenn.edu



####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> @mail.med.upenn.edu (23); @upenn.edu (12); @mail.chop.edu (1); @cceb.med.upenn.edu (1);

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```
>> updated
---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }
```
Print the first 3 key and value pairs of the dictionary:

>> {'name Mary E. Putt': {'email': 'mputt@mail.med.upenn.edu', 'degree': ' PhD ScD', 'title': 'Professor of Biostatistics'}, 'name Yimei Li': {'email': 'liy3@email.chop.edu', 'degree': ' Ph.D.', 'title': 'Assistant Professor of Biostatistics'}, 'name Rui Xiao': {'email': 'rxiao@mail.med.upenn.edu', 'degree': ' PhD', 'title': 'Assistant Professor of Biostatistics'}

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
```

Print the first 3 key and value pairs of the dictionary:

>> {'Wei (Peter) Yang:': set(['weiyang@mail.med.upenn.edu', ' Ph.D.', 'Assistant Professor of Biostatistics']), 'Kathleen Joy Propert:': set(['propert@mail.med.upenn.edu', ' Sc.D.', 'Professor of Biostatistics']), 'Dawei Xie:': set([' PhD', 'Assistant Professor of Biostatistics', 'dxie@upenn.edu'])

####Q8.  It looks like the current dictionary is sorted by first name.  Sort by last name and print the first 3 key and value pairs.  

>> A. Russell Localio: [' JD MA MPH MS PhD', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu']
Alisa Jane Stephens: [' Ph.D.', 'Assistant Professor of Biostatistics', 'alisaste@mail.med.upenn.edu']
Andrea Beth Troxel: [' ScD', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu']

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

---

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)
