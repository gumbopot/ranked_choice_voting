import datetime
import json
import os
import sqlite3

"""
This will accept ballots that contain dictionary objects
"""

# TODO: 1 function to accept ballot-dict and add it to a dict of ballots
# TODO: 2 first pair in ballot should be VoterID:Pin; check this against voter_list
# TODO: 3 voter registration
# TODO: 4 real-time count and complete count
# TODO: 5 check voter is registered; mark votes; delete id from ballot; remove voter from list
# TODO: 6 add database
# TODO: 7 make candidate ID system
# TODO: 8 find way to make # of candidates can be dynamically decided


# {'1':'me', '2':'you', '3':'Busch'},
# {'1':'you', '2':'me', '3':'your mom'}
# {'1':'eric', '2':'idc', '3':'me'},
# {'1':'alex', '2':'jon', '3':'Busch'},
# {'1':'me', '2':'you', '3':'Busch'},
# {'1':'me', '2':'you', '3':'Busch'}
# {'eric':1234, '1':'Rogan', '2':'elon', '3':'musk'}


voter_list = {'eric': 1234, 'jon': 4321, 'alex': 5678, 'karl': 8765, 'beth': 1111, 'hannah': 2222}
all_ballots = []
ballot = {'alex': 5678, '1': 'eric', '2': 'idc', '3': 'me'}
ballot_box = 'ballot_box.json'
tally = 'tally.json'

conn = sqlite3.connect('voting.db')
c = conn.cursor()


def create_tables():
	# ballots
	c.execute(
		'CREATE TABLE IF NOT EXISTS ballots(voter_id INTEGAR, name VARCHAR, first INTEGER, second INTEGER, third INTEGER, date TEXT)')
	# mstr_tally
	c.execute('CREATE TABLE IF NOT EXISTS mstr_tally(candidate VARCHAR, tally INTEGER, round_eliminated INTEGER)')
	# rnd_tally
	c.execute('CREATE TABLE IF NOT EXISTS rnd_tally(candidate VARCHAR, tally INTEGER)')


def collect_ballot(ballot: tuple):
	column = 0
	for obj in list(ballot):
		# count loops to decide what value is
		# hopefully think of a better way to do this
		column += 1

		# ID
		if column == 1:
			voter_id = obj
		elif column == 2:
			name = obj
		elif column == 3:
			first = obj
		elif column == 4:
			second = obj
		elif column == 5:
			third = obj
		else:
			print("Invalid entry on ballot.")

		date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
		c.execute("INSERT INTO ballots (voter_id, name, first, second, third,datestamp) VALUES (?, ?, ?, ?)",
		          (voter_id, name, first, second, third, date))
	# CHECK DATE/TIME STAMP

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
