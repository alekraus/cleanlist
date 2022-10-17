"""This module contains the package's functions.

Included functions:
    clean_list
    clean_list_time_float
    time_or_float_and_clean_list
    
"""

from datetime import datetime

def clean_list(to_clean):
    """Clean input list to desired format assuming items are times.
    
    Parameters:
    ~~~~~~~~~~~
    to_clean: list
        A list of strings representing times or floats
        
    Returns:
    ~~~~~~~~
    Output: list
        A cleaned list assuming items are times.
    
    """
    Output = [j for j in [i.replace("'","").replace(",",":") for i in to_clean] if j] # for each item in input, remove any "'", replace any "," with ":" (if date-time) or with "." (if float), then discard any empty items
    return Output

def clean_list_time_float(to_clean,isTime):
    """Clean input list to desired format.
    
    Parameters:
    ~~~~~~~~~~~
        to_clean: list
            A list of strings representing times or floats
            
        isTime: boolean
            A boolean representing whether the items in to_clean are assumed to be times (True) or not (False)
            
    Returns:
    ~~~~~~~~
        Output: list
            A cleaned list that replaces commas with colons when assuming items are times, or with periods when assuming floats
    
    """
    if isTime: # if input is type date-time, then replace "," with ":"
        replacer = ":"
    else: # else, assume input is type float, then replace "," with "." for Python float convention
        replacer = "."
    Output = [j for j in [i.replace("'","").replace(",",replacer) for i in to_clean] if j] # for each item in input, remove any "'", replace any "," with ":" (if date-time) or with "." (if float), then discard any empty items
    return Output

def time_or_float_and_clean_list(to_determine):
    """Determine data type in input list and clean the list to desired format.
    
    Parameters:
    ~~~~~~~~~~~
        to_determine: list
            A list of strings representing times or floats
        
    Returns:
    ~~~~~~~~
        whichType: string
            A string describing whether the items in the list are determined to be date-time or float type
            
        timeOutput: list
            A cleaned list that replaces commas with colons when assuming items are times (only returned if try clause succeeds)
            
        floatOutput: list
            A cleaned list that replaces commas with periods when assuming items are floats (only returned if try clause fails)
    
    """
    timeOutput = clean_list_time_float(to_determine,True) # assume it's date-time for now, get cleaned list
    try: # we'll attempt to convert each item in the cleaned list to the %H:%M datetime format; if all items successfully converted, then our input should be a list of date-times
        [datetime.strptime(i,"%H:%M").time() for i in timeOutput]
        whichType = 'date-time'
        return(whichType,timeOutput)
    except ValueError: # if an item fails to convert to the %H:%M datetime format, we will assume we have a list of floats (for simplicity; we could also do further tests to see if the items are of a different type)
        floatOutput = clean_list_time_float(to_determine,False)
        whichType = 'float'
        return(whichType,floatOutput)