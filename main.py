#Function: This program determines if a student will be admitted or rejected.
#Input:  Interactive
#Output: Accept or Reject

# Get input and convert to correct data type for testScore and classRank

# Test using admission requirements and print Accept or Reject

#Write an interactive input statement
#Retrive a Student's test score (testScoreString) 
#Retrive a Studnet's class rank (classRankString)

#testScore = 87
#classRank = 60
#testScoreString = input("Enter test score: ")  
#classRankString = input("Enter class rank: ")
#print ("Student's test score: " + str(testScore))
#print ("Student's class rank: " + str(classRank))
#Convert the String to integer data 
testScore = int(input("Enter your test score: ")) 
classRank = int(input("Enter your class rank: ")) 
if testScore >= 90:
  if classRank >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")
