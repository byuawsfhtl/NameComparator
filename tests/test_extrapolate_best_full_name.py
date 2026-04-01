# TODO: NOTE: This file is not yet finished. It is mostly created thus far
# to track a specific test case that will likely be very insightful. This
# will be updated later to be comprehensive and actually include meaningful
# test cases

full_final_name = 'John Jacob Jingleheimer Schmidtt'

list_of_input_names = ['J J J S', 'John Schmidtt', 'J. Jingleheimer', 'John J. J. S.', 'Jacob Jingleheimer Schmidtt']

# TODO: NOTE: What do we want to do with this next one? It won't be possible 
# to get the full final name and it will be difficult to determine where
# the extra J should go. You'll need to think through this. It might have
# overlap with the test case after this one, at least in terms of figuring
# out the logic

another_full_final_name = 'John Jacob Jingleheimer Schmidtt'

returned_still_unknown_names = [] # Empty because there should be no unknowns left

list_of_input_names = ['J J J S', 'John Schmidtt', 'J. Jingleheimer', 'John J. J. S.']

# TODO: NOTE: For this next one if there are two possible names with an unclear 'winner',
# we should probably just take the initial of the name and use that for now

# TODO: NOTE: This next test case would also be a *GREAT* one to use for the add another
# name function to help clarify more information as part of the flexible name

yet_another_full_final_name = 'John Jacob Jingleheimer Schmidtt'

intended_final_result_if_no_new_info = 'J. J. Jingleheimer Schmidtt' # This works since we know that Jingleheimer has to be after both John and Jacob to work

returned_still_unknown_names = ['John', 'Jacob'] # We would hold on to these as having an unknown position in case we get more information later, in something
                                                 # like an add name function for FlexibleName

list_of_input_names = ['J J J S', 'John Jingleheimer Schmidtt', 'Jacob Jingleheimer Schmidtt']

# TODO: NOTE: None of these cases figure out what we should do with abbreviations or titles
# you will need to figure out how to handle those. I think we should probably just have a list
# of titles such as ms., mr., mrs., lt., etc. that we should just note to throw at the beginning
# or end based on where they were before. But for abbreviations things will be a little bit
# trickier. Can I borrow some code from what is already inside of NameComparator somewhere else
# that factors that in?


# NOTE: This particular case is used to determine uncertainty when a new name is introduced to a seemingly solved situation.
# This could also be incredibly helpful as a test case for if a new name is introduced. It's worth considering how we want
# this handled, especially if there are multiple occurences of one of the names (which we would want to prioritize over
# a single anomolous occurence, of course)

unusual_situation_full_name = 'John Jacob Jingleheimer Schmidtt'

intended_final_result_of_unusual_situation = 'John J. Jingleheimer Schmidtt'

returned_unkown_names_for_unusual_situation = ['Jacob', 'Jangle'] # Do we want to include an expected index for all of these to help with this process? This would probably be
                                                                  # fairly situational to something odd like this though

list_of_input_names = ['J J J S', 'John Jacob Jingleheimer Schmidtt', 'John Jangle Jingleheimer Schmidtt']

# NOTE: Fortunately, I think that it would be best to not factor the aboce test case when it comes to a new name being
# added to an already finished FlexibleName. The only exception to that woud be if it would slot into an unkown space in the
# same spot as something else that is unkown, based on the new info from the added name
