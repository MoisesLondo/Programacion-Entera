from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, LpMinimize


class EnteraPura:
    def __init__(self, value1, value2, coefRes1, coefRes2, res1, coefRes3, coefRes4, res2, type) -> None:
        self.value1 = value1
        self.value2 = value2
        self.coefRes1 = coefRes1
        self.coefRes2 = coefRes2
        self.coefRes3 = coefRes3
        self.coefRes4 = coefRes4
        self.res1 = res1
        self.res2 = res2
        self.type = type

        # Crear un problema de maximización
        if self.type == "max":
            self.prob = LpProblem("Programacion_Entera_Pura", LpMaximize)
        else:
            self.prob = LpProblem("Programacion_Entera_Pura", LpMinimize)

        # Definir las variables de decisión (enteras)
        self.x = LpVariable('x', lowBound=0, cat='Integer')
        self.y = LpVariable('y', lowBound=0, cat='Integer')

        # Definir la función objetivo
        self.prob += self.value1 * self.x + self.value2 * self.y, "Función Objetivo"

        # Definir las restricciones
        self.prob += self.coefRes1 * self.x + self.coefRes2 * self.y <= self.res1, "Restriccion_1"
        self.prob += self.coefRes3 * self.x + self.coefRes4 * self.y <= self.res2, "Restriccion_2"

    def solve(self)-> None:
        # Resolver el problema
        self.prob.solve()

    def result(self) -> None:
        # Mostrar el estado de la solución
        print(f"Estado de la solución: {LpStatus[self.prob.status]}")

        # Mostrar los valores óptimos de las variables
        print(f"x = {self.x.varValue}")
        print(f"y = {self.y.varValue}")

        # Mostrar el valor óptimo de la función objetivo
        print(f"Valor óptimo de Z = {self.prob.objective.value()}")
