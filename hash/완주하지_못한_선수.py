def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant, completion)
    for i in range(0,len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        



print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
