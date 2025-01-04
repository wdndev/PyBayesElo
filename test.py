#!/usr/bin/env python
# encoding: utf-8
# cmake .. -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release
# cmake --build . --config Release
import bayeselo
import numpy as np

if __name__=='__main__':
    
    r = bayeselo.ResultSet()
    r.append(1, 0, 2)
    r.append(2, 1, 1)
    r.append(3, 2, 2)
    e = bayeselo.EloRating(r, ['player1', 'player2', 'player3', 'player44'])
    e.offset(1000)
    e.mm()
    e.exact_dist()
    print(e)
    # x = e.__str__().split("\n")
    # table = []
    # for row in x:
    #     table.append(row.split())
    # table = np.array(table[:-1])
    # agent_order = table[:, 1]
    # elo = table[:, 2]
    # agent_order = agent_order[1:].astype(int)
    # elo = elo[1:].astype(float)
    # elo = elo[agent_order.argsort()]
    # print(elo)

