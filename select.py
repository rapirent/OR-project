from gurobipy import*

course = {
    '作業研究': {
        'time': 3,
        'credit': 3,
        'cost_time': 9,
        'award': 10,
        'date': 5,
    },
    '軟體工程導論': {
        'time': 3,
        'credit': 3,
        'cost_time': 9,
        'award': 10,
        'date': 2,
    },
    '微算機原理與應用（含實驗）': {
        'time': 6,
        'credit': 4,
        'cost_time': 48,
        'award': 1,
        'date': 4,
    },
    '軟體設計': {
        'time': 3,
        'credit': 3,
        'cost_time': 7,
        'award': 5,
        'date': 3,
    },
    'python研讀': {
        'time': 0,
        'credit': 0,
        'cost_time': 3,
        'award': 8,
        'date': 0,
    },
    '情緒與壓力管理': {
        'time': 2,
        'credit': 2,
        'cost_time': 1,
        'award': 10,
        'date': 1,
    },
    '空間資料分析專論': {
        'time': 3,
        'credit': 3,
        'cost_time': 4,
        'award': 10,
        'date': 4,
    },
    'Javascript讀書會': {
        'time': 2,
        'credit': 0,
        'cost_time': 4,
        'award': 8,
        'date': 0,
    },
    '環境,職業與健康人生': {
        'time': 2,
        'credit': 2,
        'cost_time': 1,
        'award': 2,
        'date': 3,
    }
}

required=[1,1,2,3,6,6,7,8,9,8,8,8,7,6,6,5,5,4,4,3,2,2,2,2]

t=24

x={}
staffNumber={}
m=Model("course_schedule")

for d in course:
    x[d] = m.addVar(vtype=GRB.BINARY, name="x_%s" % d)

m.update()

m.setObjective(quicksum(x[d] * course[d]['award'] for d in course), GRB.MAXIMIZE)

m.addConstr(quicksum(x[d] * course[d]['credit'] for d in course), GRB.LESS_EQUAL, 15)
m.addConstr(quicksum(x[d] * course[d]['cost_time'] for d in course), GRB.LESS_EQUAL, 40)

for i in range(1, 7):
    m.addConstr(quicksum(x[d] * course[d]['date'] for d in course if course[d]['date'] == i), GRB.LESS_EQUAL, 5)

m.optimize()
m.write("course_schedule.lp")

print("Optimal objective value is %g" % m.objVal)


if m.status == GRB.Status.OPTIMAL:
    solution = m.getAttr('x', x)
    for d in course:
                if solution[d] == 1:
                    print("The selected course is %s" % d)







