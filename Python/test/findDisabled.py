def solution(participant, completion):
    dict_participant = {i : participant[i] for i in range(len(participant))}
    dict_completion = {i : completion[i] for i in range(len(completion))}

    # print(dict_participant)
    # print(dict_completion)

    for key, value in dict_participant.items():
        print(key, value)
        if value in dict_completion:
            print(key)
            del dict_participant[key]

    answer = dict_participant[0]
    return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))
