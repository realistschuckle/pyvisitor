from __future__ import print_function
import familytree as ft
import ex_ast as exast

print('Creating the abstract syntax tree that contains x = 5')
print('and printing it')
v = exast.VariableNode('x')
l = exast.Literal(5)
n = exast.AssignmentExpression(v, l)
visitor = exast.AbstractSyntaxTreeVisitor()
visitor.visit(n)
print('')

print('')
print('Creating me and my dependents and printing them')
me = ft.Person('Curtis')
me.add_dependent(ft.Person('Son'))
me.add_dependent(ft.Person('Daughter'))
me.add_dependent(ft.Pet('Lola', 'Shitzu'))
visitor = ft.DescendantsVisitor()
visitor.visit(me)
