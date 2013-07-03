# pyvisitor

An implementation of the visitor pattern for Python.

Find more details at [Follow-Up to Python Visitor](http://curtis.schlak.com/2013/06/20/follow-up-to-python-visitor-pattern.html).

# usage

First, import the module.

```python
import visitor
```

Then, define a class that you want to act as the visitor.

```python
class SomeVisitor(object):
  pass
```

Then, mark the method and parameter that provides dynamic dispatching.

```python
class SomeVisitor(object):
  @visitor.on('node') # Note the name of the parameter in the on decorator
  def visit(self, node);
    pass
```

Now, override the method on classes that you want called specifically based on
the type of the argument.

```python
class SomeVisitor(object):
  @visitor.on('node') # Note the name of the parameter in the on decorator
  def visit(self, node);
    pass

  @visitor.when(MyFirstClass)
  def visit(self, node):
    print 'I am going first class!'

  @visitor.when(MyOtherClass)
  def visit(self, node):
    print 'Whatever. Boring.'
```

# run the example

```bash
> git clone git@github.com:realistschuckle/pyvisitor.git
> cd pyvisitor
> python example
x=5
```