import json, os
import ast
"""
This will accept ballots that contain dictionary objects
"""

# TODO: 1 function to accept ballot-dict and add it to a dict of ballots
# TODO: 2 first pair in ballot should be VoterID:Pin; check this against voter_list
# TODO: 3 voter registration
# TODO: 4 real-time count and complete count
# TODO: 5 check voter is registered; mark votes; delete id from ballot; remove voter from list
# TODO: 6 add database


# {'1':'me', '2':'you', '3':'Busch'},
# {'1':'you', '2':'me', '3':'your mom'}
# {'1':'eric', '2':'idc', '3':'me'},
# {'1':'alex', '2':'jon', '3':'Busch'},
# {'1':'me', '2':'you', '3':'Busch'},
# {'1':'me', '2':'you', '3':'Busch'}
#{'eric':1234, '1':'Rogan', '2':'elon', '3':'musk'}


voter_list = {'eric':1234, 'jon':4321, 'alex':5678, 'karl':8765, 'beth':1111, 'hannah':2222}
all_ballots = []
ballot = {'alex':5678, '1':'eric', '2':'idc', '3':'me'}
ballot_box = 'ballot_box.json'
tally = 'tally.json'


with open(ballot_box, 'r+') as file:
    all_ballots = json.load(file)

def collect_ballot(ballot):
    # can't change size of dict while iterating
    for id in list(ballot.keys()):
        if id in voter_list:
            del ballot[id]
            all_ballots.append(ballot)

            with open(ballot_box, 'r+') as file:
                json.dump(all_ballots, file)
            print("{}'s ballot was cast!".format(id))
        else:
            continue


def count(all_ballots):
    current_rank = 0
    votes = {}
    for ballot in all_ballots:
        current_rank += 1
        for rank, candidate in ballot.items():
            print(current_rank)
            if int(rank) == current_rank:
                if os.stat(tally).st_size != 0:
                    with open(tally, 'r+') as file:
                        votes = json.load(file)
                        print(votes)
                        print(candidate)

                        if candidate in votes:
                            votes[candidate] += 1
                            print(votes)
                            json.dump(votes, file)
                        else:
                            continue





# count(all_ballots)
count(all_ballots)
