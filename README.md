<h1 align="center">Простой генератор на Python!</h1>
<p>В функции у нас запрашивается:</p>
<ul>
  <li>Колличество элементов и чисел, которые будут находиться в масиве.</li>
</ul>
<p>И в конце кода выводится масив чисел, от 1 до n.</p><br><br>

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/701px-Python-logo-notext.svg.png" wisth="100" height="100">
</p>

```Python
def generateNumbers(count):
numbers = [];

for i in range(1, count + 1):
    numbers.append(i);
    
return numbers;

print(generateNumbers(5));
```