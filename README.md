# Twos-Complement-Calculator
Calculates the two's complement of the given decimal number.

Introduction
-
Inspired by our way at university of calculating the Two's Complement of a number. We
use the defined Function <code>Zkpl_n(x)</code> which takes the number x to convert and the length n
for the output.
<p>
  So if you would use <code>Zkpl_4(-2)</code> you would calculate the result as following:
  <ol>
    <li> We calculate the <strong>positive</strong> binary value for the number. So 2 -> 10. </li>
    <li> We add as many <strong>0</strong> to the front of the number until we reach the total length of n. In this case: 10 -> 0010 </li>
    <li> We now <strong>invert</strong> the whole number. In this case: 0010 -> 1101</li>
    <li> Finally we add <strong>1</strong> to the number. In this case: 1101 + 1 -> 1110</li>
  </ol><p>
  So the final result would be <code>Zkpl_4(-2) = 1110</code>.

How to use
-
As above explained enter the to values for x and n: <code>First enter the number you want to convert and then the output length</code>.

Be aware of
-
If you enter a number <code>x = 4</code> but use <code>n = 2</code> an error will occur because you have to use ate least
the minimum length of the number's binary value.
<p>
And also be aware that this is definitely not the best solution for this (especially when using <code>Python</code>) but
I just was bored and wanted to make it.
