little_mermaid = 3
brother_bear = 5
hercules = 1 
print("You owe", 3*(little_mermaid + brother_bear + hercules), "dollars.")

google_pay = 400 
amazon_pay = 380 
facebook_pay = 350
print("You made", 6*google_pay + 4*amazon_pay + 10*facebook_pay, "dollars.")

class_scedule_conflict = True 
class_not_full = False
can_be_enrolled =class_scedule_conflict and class_not_full
print(can_be_enrolled)

bought_more_than_2 = True 
not_expired = True 
offer_can_be_applied = bought_more_than_2 and not_expired
print(offer_can_be_applied)

username = 'codeup'
password = 'notastrongpassword'

print(len(password) >=  5)
print(len(username) < 20)
print(username != password)
username = username.strip or username != username.strip
password = password.strip or password != password.strip