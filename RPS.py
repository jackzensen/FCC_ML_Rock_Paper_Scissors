# Used to generate a longer dictionary

# from itertools import product
# count_values = {}
# play_order = []
# values = list(product("RPS", repeat=4))
# for i in values:
#   count_values[''.join(i)] = 0
# play_order.append(count_val


# This program remembers and counts the opponent's previous 4 plays, since 3 did not seem sufficient to meet the test case criteria

#It is the same strategy that Abbey uses, only with a longer memory.

def player(prev_opponent_play,
          opponent_history=[],
          
          play_order = [{'RRRR': 0, 'RRRP': 0, 'RRRS': 0, 'RRPR': 0, 'RRPP': 0, 'RRPS': 0, 'RRSR': 0, 'RRSP': 0, 'RRSS': 0, 'RPRR': 0, 'RPRP': 0, 'RPRS': 0, 'RPPR': 0, 'RPPP': 0, 'RPPS': 0, 'RPSR': 0, 'RPSP': 0, 'RPSS': 0, 'RSRR': 0, 'RSRP': 0, 'RSRS': 0, 'RSPR': 0, 'RSPP': 0, 'RSPS': 0, 'RSSR': 0, 'RSSP': 0, 'RSSS': 0, 'PRRR': 0, 'PRRP': 0, 'PRRS': 0, 'PRPR': 0, 'PRPP': 0, 'PRPS': 0, 'PRSR': 0, 'PRSP': 0, 'PRSS': 0, 'PPRR': 0, 'PPRP': 0, 'PPRS': 0, 'PPPR': 0, 'PPPP': 0, 'PPPS': 0, 'PPSR': 0, 'PPSP': 0, 'PPSS': 0, 'PSRR': 0, 'PSRP': 0, 'PSRS': 0, 'PSPR': 0, 'PSPP': 0, 'PSPS': 0, 'PSSR': 0, 'PSSP': 0, 'PSSS': 0, 'SRRR': 0, 'SRRP': 0, 'SRRS': 0, 'SRPR': 0, 'SRPP': 0, 'SRPS': 0, 'SRSR': 0, 'SRSP': 0, 'SRSS': 0, 'SPRR': 0, 'SPRP': 0, 'SPRS': 0, 'SPPR': 0, 'SPPP': 0, 'SPPS': 0, 'SPSR': 0, 'SPSP': 0, 'SPSS': 0, 'SSRR': 0, 'SSRP': 0, 'SSRS': 0, 'SSPR': 0, 'SSPP': 0, 'SSPS': 0, 'SSSR': 0, 'SSSP': 0, 'SSSS': 0}]):


    if not prev_opponent_play:
        prev_opponent_play = 'SSS'
    opponent_history.append(prev_opponent_play)

    last_three = "".join(opponent_history[-4:])    
    if len(last_three) == 4:                     
        try:
          play_order[0][last_three] += 1
        except:
          play_order[0][last_three] = 1


    potential_plays = [
        last_three[-3:] + "R",
        last_three[-3:] + "S",
        last_three[-3:] + "P",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }
    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]