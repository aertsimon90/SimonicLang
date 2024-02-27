- Each command should be initiated on a single line for optimization, but if your loop or long code creates complexity, you can use the "splitCode" command as follows:
  ```
  splitCode;log;
  Hello
  splitEnd
  ```
  Remember that when using "splitCode," each argument and code will be added to your split code. For example, if you write "log" on the first line and "hello" on the second line, this is incorrect. The correct way is to write "log;" on the first line because if you make such a mistake, your code will be like this: "loghello," but if you correct it as we said, it will be like this: "log;hello."
- When using loop commands, inserting " %& " allows running two or more codes in a single command.
- You can use " && " to split codes on each line.
- There should be a space before and after the splitting symbols.
- Each code is divided into parts by a semicolon. The first part is the method, and the rest are options.
- When creating a function, double colons (::) must be placed between the arguments, for example:
```sl
func;example;a::b;logf;Hello $<args.a>! my name is $<args.b>.
```
Similarly, when calling the function, double colons (::) should be inserted between the arguments, for example:
```sl
func.run;example;User::Game
```
