# aws-alerts-stats

Looking at getting some stats on AWS service alerts.

This is based on a dataset from a slack channel we have subscribed to AWS Service Health alerts.

This data set runs from October 2017 through November 2019.

I'm basically just counting up the alert messages we received with RESOLVED in it, since there seems to only be one RESOLVED message sent for each set of messages relating to a particular event. I then try and extract a region from the message, and add them up.

This is probably not a very robust analysis, but its better than my anecdotal memory I think.

    AP-SOUTH-1           1 
    EU-WEST-3            2 
    GOV-EAST-1           2 
    US-WEST-1            4 
    AP-SOUTHEAST-2       4 
    AP-EAST-1            4 
    EU-CENTRAL-1         5 
    SA-EAST-1            5 
    AP-SOUTHEAST-1       6 
    AP-NORTHEAST-1       6 
    GOV-WEST-1           7 
    AP-NORTHEAST-2       8 
    EU-WEST-2            11
    US-EAST-2            12
    EU-WEST-1            18
    US-WEST-2            30
    None                 42
    US-EAST-1            95