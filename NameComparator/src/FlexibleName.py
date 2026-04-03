from NameComparator.src.name_extrapolation import clean_name_list
from pydantic import BaseModel

class FlexibleName(BaseModel):
    """ This class represents a name in a way that allows for more
    flexible comparison and for determining the most complete and full
    version of a name when given a list of possible name inputs.

    Attributes:
        original_name_list: The list of possible name variations as
            originally input into the class
        cleaned_name_list: The original name list with irrelevant or
            unlikely names removed from it
        best_name_from_list: The best name that is retrieved from the
            list
        extrapolated_name: The complete name as extrapolated from
            all of the name variations in the name list
    """

    def __init__(self, name_list_input: list[str]):
        self.original_name_list = name_list_input
        self.cleaned_name_list = clean_name_list(name_list_input)
    # TODO: Build functions to allow for all of these different variables and
    # outputs to be determined, probably when the class is constructed. Also
    # allow for different constructor variants if that feels appropriate