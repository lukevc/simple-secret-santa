# simple-secret-santa
A simple project to assign secret santa participants 

- This was created to arbitrate my families secret santa.
- People are added to the "hat" using a data class [str: "giver", str: "reciever"] and then added to a list.
- The list is then shuffled randomly.
- The "reciever" is then swapped with the previous index.
- The last person on the list is assigned the first person as their ss to complete the loop.
- Finally, for each person a text file is generated containing the person they are buying for. The .txt file can then be emailed to each person. 
