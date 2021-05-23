# Lost
A simple text adventure to use as a template


** NEXT **

* Consider easiest way to have doors locked/blocke or unlocked/unblocked.
      - Change doors dict values from string to a list
      - e.g. doors = {"south": ["Room 2": True]}
 This will start to get complicated as this is redefined each time you enter a room function.
 This means you would have to find a way to override this each time, which is less good.
 You might then have to define the rooms and doors upfront, but this is more difficult.
 You could use the flags option, but that requires a bit of custom code each time.
 ## have a flag that means the door is now unlocked and then compare in the specific functions?? ##
 ## not sure about this..##
 
 At a certain point it makes sense to start using classes. 
