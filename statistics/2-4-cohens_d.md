[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> REPLACE THIS TEXT WITH YOUR RESPONSE

>>firsts = df[df.birthord==1]
>>others = df[df.birthord>1]
#
>>  def CohenEffectSize(firsts, others):
>>  diff = firsts.mean() - others.mean()
#
>>  var1 = firsts.var()
>>  var2 = others.var()
>>  n1, n2 = len(firsts), len(others)
#
>>  pooled_var = ((n1 * var1) + (n2 * var2)) / (n1 + n2)
>>  d = diff / math.sqrt(pooled_var)
>>  return d
