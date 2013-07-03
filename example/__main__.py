import familytree as ft
import ast

print 'Creating the abstract syntax tree that contains x = 5'
print 'and printing it'
v = ast.VariableNode('x')
l = ast.Literal(5)
n = ast.AssignmentExpression(v, l)
visitor = ast.AbstractSyntaxTreeVisitor()
visitor.visit(n)
print ''

print ''
print 'Creating me and my dependents and printing them'
me = ft.Person('Curtis')
me.add_dependent(ft.Person('Son'))
me.add_dependent(ft.Person('Daughter'))
me.add_dependent(ft.Pet('Lola', 'Shitzu'))
visitor = ft.DescendantsVisitor()
visitor.visit(me)
print ''

