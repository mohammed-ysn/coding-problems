def runoff(voters):
    blacklist = set()

    for i in range(10):
        # create dict of all candidates still in the race
        first_choice = {candidate: 0 for candidate in voters[0] if candidate not in blacklist}

        for ballot in voters:
            # count first vote for a non-blacklisted candidate
            for choice in ballot:
                if choice not in blacklist:
                    first_choice[choice] += 1
                    break

        max_candidate = max(first_choice, key=first_choice.get)

        if first_choice[max_candidate] > sum(first_choice.values()) / 2:
            # candidate with max votes takes more than half of votes
            return max_candidate
        elif len(set(first_choice.values())) == 1:
            # complete tie between candidates
            break
        else:
            min_vote_count = min(first_choice.values())
            min_candidates = [candidate for candidate, vote_count in first_choice.items()
                              if vote_count == min_vote_count]
            # blacklist all candidates with the lowest vote count
            for candidate in min_candidates:
                blacklist.add(candidate)

    return None


input_voters = [["dem", "ind", "rep"],
                ["rep", "ind", "dem"],
                ["ind", "dem", "rep"],
                ["ind", "rep", "dem"]]
print(runoff(input_voters))
