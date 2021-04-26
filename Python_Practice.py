# How many votes did you get?
# my_votes = int(input("How many votes?"))
# total_votes=int(input("Total votes?"))
# pct_votes=(my_votes/total_votes)*100
# print("I received "+str(pct_votes)+"%")
# counties_list = ["Arapahoe","Denver","Jefferson"]
# counties_dict={"Arapahoe":4223,"Denver":3000,"Jeffy":7000}
# if pct_votes > 6.77:
#     print("Winner")
# elif pct_votes>5:
#     print("Semi-Loser")
# else:
#     print("loser")
# for i in range(len(counties_list)):
#     print(counties_list[i])
# for county in counties_dict:
#     print (county)
# for county in counties_dict.keys():
#     print(county)
# for county,voters in counties_dict.items():
#     print(str(county) + " county has "+ str(voters) + " voters")
#     print(f"{county} county has {voters} voters")

# for county,voters in counties_dict.items():
#     print(f"{county} county has {voters} voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for dict in voting_data:
    print(dict["county"] + " county has " + str(dict["registered_voters"]) + " voters")





