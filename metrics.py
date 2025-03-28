def average(data: list) -> float: 
    """
    This function operates to calculate the average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    average = 0

    if data == []:
        return([])
    else:
        x = sum(data)
        y = x/ len(data)
    return round((y), 2)



def maximum(data: list) -> float:
    """   
    This function operates to calculate the maximum heart rate value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """

    if data == []:
        return([])

    else:
        maximum = data[0]
        for item in data:
            if item > maximum:
             maximum = item
        return(maximum)
    



def variance(data: list) -> float:
    """
    This function operates to calculate the variance value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """

    if data == []:
        return([])

    mean = sum(data) / len(data)

    sq_diff = []

    for var in data:
     sq_diff.append((var - mean)**2)
    
    var= sum(sq_diff) / len(data)
    return(var)


def standard_deviation(data: list) -> float:
    """
    This function operates to calculate the standard deviation value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
  
    """
    if data == []:
        return([])
    else:
        stdev = variance (data) **(.5)

        return round((stdev), 2)
    
