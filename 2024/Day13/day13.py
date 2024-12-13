from sympy import symbols, solve, sympify
from sympy.abc import a,b,c,d

def isint(i):
    try: as_int(i, strict=False)
    except: return False
    return True



#open file in
result = 0
result_2 = 0
add = 10000000000000
with open("input.in") as input_file:
    for line in input_file:
        if line.strip() == "":
            sol = solve((a*ax+b*bx-(sol_x),a*ay+b*by-(sol_y)), (a, b), dict=True)
            sol_2 = solve((a*ax+b*bx-(add+sol_x),a*ay+b*by-(add+sol_y)), (a, b), dict=True)
            if len(sol) > 1:
                print("error")
            else:
                sol = sol[0]
                if sympify(sol[a]).is_integer and sympify(sol[b]).is_integer:
                    result += sol[a]*3 + sol[b]

            if len(sol_2) > 1:
                print("error")
            else:
                sol_2 = sol_2[0]
                if sympify(sol_2[a]).is_integer and sympify(sol_2[b]).is_integer:
                    result_2 += sol_2[a]*3 + sol_2[b]


        if "Button A" in line:
            parsed = line.strip().split(":")[1].strip().split(",")
            ax = int(parsed[0].strip().replace("X+",""))
            ay = int(parsed[1].strip().replace("Y+",""))
        if "Button B" in line:
            parsed = line.strip().split(":")[1].strip().split(",")
            bx = int(parsed[0].strip().replace("X+",""))
            by = int(parsed[1].strip().replace("Y+",""))   
        if "Prize" in line:
            parsed = line.strip().split(":")[1].strip().split(",")
            sol_x = int(parsed[0].strip().replace("X=",""))
            sol_y = int(parsed[1].strip().replace("Y=",""))   

print(result, result_2)