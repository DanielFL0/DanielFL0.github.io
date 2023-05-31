---
layout: "../../layouts/MarkdownPostLayout.astro"
title: "Stack virtual machines for fun and profit"
date: 2023-05-31
author: "Daniel"
description: "Always wondered how interpreters like Python and Ruby work? Here's your answer"
image: {
  url: "https://www.brickfanatics.com/wp-content/uploads/2023/01/REDDIT-LEGO-purple-Classic-Space-astronaut-minifigure-1009x1024.jpeg"
}
---

Last year I started diving deep into the art of compiler 
engineering, I didn't write any production grade compiler, 
but instead just experimented with small snippets of code 
I've found during my research.

The more I found out about the algorithms and data structures 
that rule this specific domain the more I was left astonished. 
I've yet to come to an end in this journey, in fact, I'm just 
getting started, but I think it's time I leave the research 
phase and start building stuff.

In this post my aim is to build a small stack virtual machine 
using the C programming language, but don't let yourself be 
fooled by the word "small", it will be indeed a small 
implementation but it's capabilities and limitations will only 
be determined by the programmer using it.

# What is a virtual machine

In simple terms, a stack virtual machine is just a program 
(emulator) that takes in some bytecode and executes each instruction.

For some instances this virtual machine can actually emulate the 
behaviour of existing hardware, some popular examples are one of the
many gameboy emulatores, on the other hand, the virtual machine can
emulate a new one of it's kind "architecture" like a chip-8 emulator.

# The big idea

As I've stated before I'm not an expert on virtual machines nor 
programming language development in general, however, that wasn't
enough to stop me to come up with the bright idea of reverse
engineering one of the many existing bytecode interpretes (like in
ruby, python, php) and use some of these instructions in my own
virtual machine. The main idea is to check some of the  Python's 
bytecode interpreter source code and use the **dis** module in
some python code to figure out what each instruction in a Python
program does.

# Following along

This is more of an experimental tour of the development of my
virtual machine than a tutorial for implementing general-purpose
virtual machines, but if you're like me and like to learn new
stuff by hacking existing projects then this is a good way to
learn how stack virtual machine A.K.A. bytecode interpreters
work and how you can use this series as an inspiration to build 
your own stack virtual machine! So hop on, grab your latest 
Python interpreter and C compiler and let's get started.

# The test program

I will start by figuring out how Python's bytecode interpreter
handles arithmetic operations, since this is probably the easiest
part of the virtual machine.

**test.py**
```
a = 5 + 3
```
using `python -m dis test.py`
```
  0           0 RESUME                   0

  1           2 LOAD_CONST               0 (8)   
              4 STORE_NAME               0 (a)   
              6 LOAD_CONST               1 (None)
              8 RETURN_VALUE
```

So what does this mean? Well first the interpreter loads 
a constant (8) into the stack, then the interpreter stores the 