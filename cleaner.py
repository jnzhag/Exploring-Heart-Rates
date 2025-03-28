def filter_nondigits(data: list) -> list:
    """
    This function will clean up the data filter out all strings that include non-digit characters 

       Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    data_new = []

    for x in data:
        x = x.strip()
        if x.isdigit():
            data_new.append(int(x))
    return (data_new)


    







