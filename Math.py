import sympy as sp
from sympy.solvers import solve
from sympy import Eq, symbols, simplify
from sympy.solvers.solveset import linear_eq_to_matrix

def solve_equation_with_steps(equation_str):
    # Define the symbol
    x = symbols('x')
    
    # Parse the equation
    try:
        lhs, rhs = equation_str.split('=')
        lhs_expr = sp.sympify(lhs)
        rhs_expr = sp.sympify(rhs)
        equation = Eq(lhs_expr, rhs_expr)
    except Exception as e:
        return f"Error parsing equation: {e}"

    print(f"\n🔍 Original Equation: {equation_str}")
    print(f"➡️ Step 1: Convert to SymPy Equation: {equation}")

    # Move all terms to one side
    step2 = simplify(lhs_expr - rhs_expr)
    print(f"➡️ Step 2: Move all terms to one side: {step2} = 0")

    # Solve the equation
    try:
        solution = solve(equation, x)
        print(f"✅ Step 3: Solve for x: x = {solution[0]}")
    except Exception as e:
        return f"Error solving equation: {e}"

    return solution

# Example usage
if __name__ == "__main__":
    print("🧮 Math Equation Solver with Steps")
    eq = input("Enter an equation (e.g., 2*x + 3 = 7): ")
    solve_equation_with_steps(eq)
