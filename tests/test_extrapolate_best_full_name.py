# TODO: NOTE: This file is not yet finished. It is mostly created thus far
# to track a specific test case that will likely be very insightful. This
# will be updated later to be comprehensive and actually include meaningful
# test cases

full_final_name = 'John Jacob Jingleheimer Schmidtt'

list_of_input_names = ['J J J S', 'John Schmidtt', 'J. Jingleheimer', 'John J. J. S.', 'Jacob Jingleheimer Schmidtt']

# TODO: NOTE: What do we want to do with this next one? It won't be possible 
# to get the full final name and it will be difficult to determine where
# the extra J should go. You'll need to think through this

another_full_final_name = 'John Jacob Jingleheimer Schmidtt'

list_of_input_names = ['J J J S', 'John Schmidtt', 'J. Jingleheimer', 'John J. J. S.']

# TODO: NOTE: What do we want to do with this next one? It will be difficult to determine
# which of the similar but conflicting names might be the best for it's position

# TODO: NOTE: This next test case would also be a *GREAT* one to use for the add another
# name function to help clarify more information as part of the flexible name

yet_another_full_final_name = 'John Jacob Jingleheimer Schmidtt'

intended_final_result_if_no_new_info = 'J J Jingleheimer Schmidtt' # This works since we know that Jingleheimer has to be after both John and Jacob to work

returned_still_unknown_names = ['John', 'Jacob'] # We would hold on to these as having an unknown position in case we get more information later, in something
                                                 # like an add name function for FlexibleName

list_of_input_names = ['J J J S', 'John Jingleheimer Schmidtt', 'Jacob Jingleheimer Schmidtt']