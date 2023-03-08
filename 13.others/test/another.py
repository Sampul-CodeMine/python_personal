def is_at_rich(dna):
    length = len(dna)
    a_count = dna.count('a')
    t_count = dna.count('t')
    at_content = (a_count + t_count) / length
    final_c = at_content > 0.65
    answer = "T Count = {}\nA Count = {}\nFinal Answer = {}".format(t_count, a_count, final_c)
    answer += "\nWord Length = {}\nWord is {}".format(length, dna)
    return answer


print(is_at_rich('tttttttttttttaaaaaaaaaaaaaaaaaaasample'))
