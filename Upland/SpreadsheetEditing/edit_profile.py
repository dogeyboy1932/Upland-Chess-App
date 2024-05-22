from FIXED_VARIABLES import profiles_db


def FillingLichessInfo(uplandID, lichessID, lichessRating, password):
   user = profiles_db.find_one({"Upland Username": uplandID})
   
   update_operation = {}
   if password == -1:
      update_operation["LichessReplaced"] = user.get('LichessReplaced') + 1
   else:
      update_operation["Password"] = password

   update_operation["Lichess ID"] = lichessID
   update_operation["Lichess Rating"] = lichessRating

   profiles_db.update_one({"Upland Username": uplandID}, {"$set": update_operation})



def DeleteProfile(uplandID, password):
   user = profiles_db.find_one({"Upland Username": uplandID})
   if not user: return -1

   if user.get("Password") != password: return "Incorrect Password"

   profiles_db.delete_one({"Upland Username": uplandID})

   return "success"