# Lost
A simple text adventure to use as a template


** NEXT **

* Consider easiest way to have doors locked/blocke or unlocked/unblocked.
      - Change doors dict values from string to a list
      - e.g. doors = {"south": ["Room 2": True]}
 This will start to get complicated as this is redefined each time you enter a room function.
 This means you would have to find a way to override this each time, which is less good.
 ** Now changed so that doors dictionary is defined in an if/else statement.
 
 This is a bit less than lovely.

 At a certain point it makes sense to start using classes. 
