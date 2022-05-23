
from pyomo.environ import *

model = ConcreteModel()

#variable
model.x = Var([1,2],[1,2,3], domain=NonNegativeReals)

#definition of the objective function

model.OBJ = Objective(expr = 90*(2.5*model.x[1,1]+1.7*model.x[1,2]+1.8*model.x[1,3]+2.5*model.x[2,1]+1.8*model.x[2,2]+1.4*model.x[2,3]))

model.cons1 = Constraint(expr = model.x[1,1]+model.x[2,1]>=325)
model.cons2 = Constraint(expr = model.x[1,2]+model.x[2,2]>=300)
model.cons3 = Constraint(expr = model.x[1,3]+model.x[2,3]>=275)

model.cons4 = Constraint(expr = model.x[1,1]+model.x[1,2]+model.x[1,3]<=350)
model.cons5 = Constraint(expr = model.x[2,1]+model.x[2,2]+model.x[2,3]<=600)
