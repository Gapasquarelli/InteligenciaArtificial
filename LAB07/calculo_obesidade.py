import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define the new universe for each variable
eat = ctrl.Antecedent(np.arange(0, 11, 1), 'eat')
weight = ctrl.Antecedent(np.arange(0, 11, 1), 'weight')
exercise = ctrl.Antecedent(np.arange(0, 11, 1), 'exercise')
obesity = ctrl.Consequent(np.arange(0, 11, 1), 'obesity')

# Triangular MF
eat['healthy_tri'] = fuzz.trimf(eat.universe, [7, 10, 10])
eat['unhealthy_tri'] = fuzz.trimf(eat.universe, [0, 0, 3])
weight['normal_tri'] = fuzz.trimf(weight.universe, [0, 3, 5])
weight['over_tri'] = fuzz.trimf(weight.universe, [4, 6, 8])
weight['obese_tri'] = fuzz.trimf(weight.universe, [7, 10, 10])
exercise['regular_tri'] = fuzz.trimf(exercise.universe, [7, 10, 10])
exercise['irregular_tri'] = fuzz.trimf(exercise.universe, [0, 0, 3])
obesity['low_tri'] = fuzz.trimf(obesity.universe, [0, 0, 3])
obesity['medium_tri'] = fuzz.trimf(obesity.universe, [2, 5, 8])
obesity['high_tri'] = fuzz.trimf(obesity.universe, [7, 10, 10])

# Gaussian MF
eat['healthy_gauss'] = fuzz.gaussmf(eat.universe, 9, 1)
eat['unhealthy_gauss'] = fuzz.gaussmf(eat.universe, 1, 1)
weight['normal_gauss'] = fuzz.gaussmf(weight.universe, 3, 1)
weight['over_gauss'] = fuzz.gaussmf(weight.universe, 6, 1)
weight['obese_gauss'] = fuzz.gaussmf(weight.universe, 9, 1)
exercise['regular_gauss'] = fuzz.gaussmf(exercise.universe, 9, 1)
exercise['irregular_gauss'] = fuzz.gaussmf(exercise.universe, 1, 1)
obesity['low_gauss'] = fuzz.gaussmf(obesity.universe, 1, 1)
obesity['medium_gauss'] = fuzz.gaussmf(obesity.universe, 5, 1)
obesity['high_gauss'] = fuzz.gaussmf(obesity.universe, 9, 1)

# Trapezoidal MF
eat['healthy_trap'] = fuzz.trapmf(eat.universe, [7, 8, 10, 10])
eat['unhealthy_trap'] = fuzz.trapmf(eat.universe, [0, 0, 1, 3])
weight['normal_trap'] = fuzz.trapmf(weight.universe, [0, 0, 3, 5])
weight['over_trap'] = fuzz.trapmf(weight.universe, [4, 5, 6, 8])
weight['obese_trap'] = fuzz.trapmf(weight.universe, [7, 8, 10, 10])
exercise['regular_trap'] = fuzz.trapmf(exercise.universe, [7, 8, 10, 10])
exercise['irregular_trap'] = fuzz.trapmf(exercise.universe, [0, 0, 1, 3])
obesity['low_trap'] = fuzz.trapmf(obesity.universe, [0, 0, 1, 3])
obesity['medium_trap'] = fuzz.trapmf(obesity.universe, [2, 3, 5, 8])
obesity['high_trap'] = fuzz.trapmf(obesity.universe, [7, 8, 10, 10])

# Fuzzy rules
rule1 = ctrl.Rule(eat['unhealthy_tri'] & weight['obese_tri'] & exercise['irregular_tri'], obesity['high_tri'])
rule2 = ctrl.Rule(eat['unhealthy_gauss'] & weight['over_gauss'] & exercise['irregular_gauss'], obesity['medium_gauss'])
rule3 = ctrl.Rule(eat['healthy_trap'] & weight['normal_trap'] & exercise['regular_trap'], obesity['low_trap'])

rule4 = ctrl.Rule(eat['healthy_tri'] & weight['normal_tri'] & exercise['regular_tri'], obesity['low_tri'])
rule5 = ctrl.Rule(eat['healthy_gauss'] & weight['over_gauss'] & exercise['irregular_gauss'], obesity['medium_gauss'])
rule6 = ctrl.Rule(eat['unhealthy_trap'] & weight['obese_trap'] & exercise['regular_trap'], obesity['high_trap'])

rule7 = ctrl.Rule(eat['unhealthy_tri'] & weight['normal_tri'] & exercise['irregular_tri'], obesity['medium_tri'])
rule8 = ctrl.Rule(eat['healthy_gauss'] & weight['normal_gauss'] & exercise['regular_gauss'], obesity['low_gauss'])
rule9 = ctrl.Rule(eat['unhealthy_trap'] & weight['over_trap'] & exercise['irregular_trap'], obesity['high_trap'])

rule10 = ctrl.Rule(eat['healthy_tri'] & weight['obese_tri'] & exercise['regular_tri'], obesity['medium_tri'])
rule11 = ctrl.Rule(eat['unhealthy_gauss'] & weight['normal_gauss'] & exercise['irregular_gauss'], obesity['medium_gauss'])
rule12 = ctrl.Rule(eat['healthy_trap'] & weight['over_trap'] & exercise['regular_trap'], obesity['medium_trap'])

rule13 = ctrl.Rule(eat['healthy_tri'] | weight['normal_tri'] | exercise['regular_tri'], obesity['low_tri'])
rule14 = ctrl.Rule(eat['healthy_gauss'] | weight['over_gauss'] | exercise['irregular_gauss'], obesity['medium_gauss'])
rule15 = ctrl.Rule(eat['unhealthy_trap'] | weight['obese_trap'] | exercise['regular_trap'], obesity['high_trap'])

rule16 = ctrl.Rule(eat['unhealthy_tri'] | weight['normal_tri'] | exercise['irregular_tri'], obesity['medium_tri'])
rule17 = ctrl.Rule(eat['healthy_gauss'] | weight['normal_gauss'] | exercise['regular_gauss'], obesity['low_gauss'])
rule18 = ctrl.Rule(eat['unhealthy_trap'] | weight['over_trap'] | exercise['irregular_trap'], obesity['high_trap'])

rule19 = ctrl.Rule(eat['healthy_tri'] | weight['obese_tri'] | exercise['regular_tri'], obesity['medium_tri'])
rule20 = ctrl.Rule(eat['unhealthy_gauss'] | weight['normal_gauss'] | exercise['irregular_gauss'], obesity['medium_gauss'])
rule21 = ctrl.Rule(eat['healthy_trap'] | weight['over_trap'] | exercise['regular_trap'], obesity['medium_trap'])

rule22 = ctrl.Rule(eat['unhealthy_tri'] & (weight['over_tri'] | weight['obese_tri']), obesity['high_tri'])
rule23 = ctrl.Rule((eat['healthy_gauss'] | eat['unhealthy_gauss']) & weight['normal_gauss'], obesity['low_gauss'])
rule24 = ctrl.Rule(eat['unhealthy_trap'] & (weight['normal_trap'] | weight['over_trap']), obesity['medium_trap'])

# Create control systems for each type of membership function
obesity_control_tri = ctrl.ControlSystem([rule1, rule4, rule7, rule10, rule13, rule16, rule19, rule22])
obesity_control_gauss = ctrl.ControlSystem([rule2, rule5, rule8, rule11, rule14, rule17, rule20, rule23])
obesity_control_trap = ctrl.ControlSystem([rule3, rule6, rule9, rule12, rule15, rule18, rule21, rule24])

# Create simulation objects for each control system
obesity_sim_tri = ctrl.ControlSystemSimulation(obesity_control_tri)
obesity_sim_gauss = ctrl.ControlSystemSimulation(obesity_control_gauss)
obesity_sim_trap = ctrl.ControlSystemSimulation(obesity_control_trap)

inputs = {
    'eat': 2,
    'weight': 6.5,
    'exercise': 1.5,
}

# Use triangular membership functions
obesity_sim_tri.input['eat'] = inputs['eat']
obesity_sim_tri.input['weight'] = inputs['weight']
obesity_sim_tri.input['exercise'] = inputs['exercise']
obesity_sim_tri.compute()
print("Obesity level (Triangular MF):", obesity_sim_tri.output['obesity'])

# Use Gaussian membership functions
obesity_sim_gauss.input['eat'] = inputs['eat']
obesity_sim_gauss.input['weight'] = inputs['weight']
obesity_sim_gauss.input['exercise'] = inputs['exercise']
obesity_sim_gauss.compute()
print("Obesity level (Gaussian MF):", obesity_sim_gauss.output['obesity'])

# Use trapezoidal membership functions
obesity_sim_trap.input['eat'] = inputs['eat']
obesity_sim_trap.input['weight'] = inputs['weight']
obesity_sim_trap.input['exercise'] = inputs['exercise']
obesity_sim_trap.compute()
print("Obesity level (Trapezoidal MF):", obesity_sim_trap.output['obesity'])

# Plot the results

#Eat
eat.view(sim=obesity_sim_tri)
eat.view(sim=obesity_sim_gauss)
eat.view(sim=obesity_sim_trap)

#Weight
weight.view(sim=obesity_sim_tri)
weight.view(sim=obesity_sim_gauss)
weight.view(sim=obesity_sim_trap)

#Exercise
exercise.view(sim=obesity_sim_tri)
exercise.view(sim=obesity_sim_gauss)
exercise.view(sim=obesity_sim_trap)

#Obesity
obesity.view(sim=obesity_sim_tri)
obesity.view(sim=obesity_sim_gauss)
obesity.view(sim=obesity_sim_trap)

#Show the plots
plt.show()

