from __future__ import print_function
import sys
import os

# Put the path to the visitor module on the search path
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if not path in sys.path:
  sys.path.insert(1, path)

import visitor

class BaseNode:
  def accept(self, visitor):
    visitor.visit(self)


class Literal(BaseNode):
  def __init__(self, val):
    self.value = val


class VariableNode(BaseNode):
  def __init__(self, name):
    self.name = name


class AssignmentExpression(BaseNode):
  def __init__(self, left, right):
    self.children = [left, right]


class AbstractSyntaxTreeVisitor(object):
  @visitor.on('node')
  def visit(self, node):
    """
    This is the generic method that initializes the
    dynamic dispatcher.
    """

  @visitor.when(BaseNode)
  def visit(self, node):
    """
    Will run for nodes that do specifically match the
    provided type.
    """
    print("Unrecognized node:", node)

  @visitor.when(AssignmentExpression)
  def visit(self, node):
    """ Matches nodes of type AssignmentExpression. """
    node.children[0].accept(self)
    sys.stdout.write('=')
    node.children[1].accept(self)

  @visitor.when(VariableNode)
  def visit(self, node):
    """ Matches nodes that contain variables. """
    sys.stdout.write(str(node.name))

  @visitor.when(Literal)
  def visit(self, node):
    """ Matches nodes that contain literal values. """
    sys.stdout.write(str(node.value))
