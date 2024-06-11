# misc/JailBreak 1

<p align = "center"><img src="challenge.JPG" alt="alt text" width="75%" height="75%" /></p>

<details> 
  <summary><b>Hint 1</b></summary>
   How can you access variables in python?
</details>

This is the first of three PyJail challenges in this CTF. For all three challenges, the flag is initialized as a local variable.

```python
flag = open('flag.txt').read().strip()
```

For this challenge, we get to input a message. Before `exec()` is run on our message, we would only need to bypass the banned character list as shown below:

```python
BANNED_CHARS = "gdvxftundmnt'~`@#$%^&*-/.{}"
```

`"f"` and `"g"` are banned, so we cannot output the flag directly. However, we can make use of hex or octal values since backslash is allowed. `locals()` is also allowed here to get all of the variables that were initialized.

It should also be noted that `exec()` does not output any values, so we would need a function to output the flag. While `print()` does not work due to the restrictions,  `help()` can be used as an alternative, and as a plus it can create a "pseudo-shell".

We used the following payload directly on the netcat server:

```python
help(locals()["\146\154\141\147"])
```

Ah yes, we found the flag!

<p align = "center"><img src="result.JPG" alt="alt text" width="75%" height="75%" /></p>

```
bcactf{PyTH0n_pR0_03ed78292b89c}
```