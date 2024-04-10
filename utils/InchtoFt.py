#Converts values given in inches to a more readible string (i.e 71 -> 5'11'')
def convert(inch):
    if(inch % 12 == 0):
        feet = inch/12
        return f"{int(feet)}'"
    else:
        reminch = inch % 12
        feet = (inch-reminch)/12
        return f"{int(feet)}'{reminch}''"
