# Welcome to the cleanlist package for Python

Package to determine whether a list of strings contains date-time or float types, and to clean the list appropriately.

## Installation

The latest version can be cloned from the GitHub repository and installed as usual with pip:

    git clone https://github.com/alekraus/cleanlist
    
    python -m pip install .

## Descriptions of included functions

`clean_list`:
Cleans input list to desired format assuming items are date-times.

`clean_list_time_float`:
Cleans input list to desired format, depending on whether it is assumed that the items in the list are date-time or float. For date-time, all "'" are removed and all "," are converted to ":" (since time format is %H:%M); for float, all "'" are removed and all "," are converted to "." (to standardize the decimal mark to Pythonic with a period).

`time_or_float_and_clean_list`:
Determines the data type of an input list and cleans the list to the desired format by calling `clean_list_time_float` (see above). The logic is that we first assume that the list contains date-time items, so we store a temporary list cleaning the input list to the time format. We then try to convert each item in the list to the datetime.time format using %H:%M as the time signature. If this test passes, that means that we can (as a first pass) determine the items in the list to be times. On the other hand, if this test fails, it means that at least one of the items in the list could not be converted using the %H:%M time format to a datetime.time object. This makes it likely that we are not dealing with times in this list (e.g., 545 would fail here (as it lacks the ":" string); 102.4 would fail here (as it has three digits for hours and one digit for minutes); 3,34 would pass, since it is interpreted as 3:34 after we cleaned the list, but the occurrences of the non-time items would cause the try block to fail. Since for simplicity we are only differentiating between date-time and float type determination, and the try clause failing upon assuming the date-time type, we conclude that the list contains float items. Note that this is a simplification, since we could further differentiate for other types (e.g., integers).

## Code examples

### For all following examples, run these lines of code first:

    import cleanlist.functions as clp
    Input = ["'10:24","'5:45","'4:56","'3,34","'"]
    Inputstar = ["'102.4","'545","'45.6","'3,34","'","'1.4"]

### Using clp.clean_list to obtain clean output, assuming list items are times:

    print(clp.clean_list(Input))
    print(clp.clean_list(Inputstar))

Output:

    ['10:24', '5:45', '4:56', '3:34']
    ['102.4', '545', '45.6', '3:34', '1.4']

### Using clp.time_or_float_and_clean_list to determine whether list items are times or floats, and to clean the list accordingly:

    print(clp.time_or_float_and_clean_list(Input))
    print(clp.time_or_float_and_clean_list(Inputstar))
    
Output:

    ('date-time', ['10:24', '5:45', '4:56', '3:34'])
    ('float', ['102.4', '545', '45.6', '3.34', '1.4'])