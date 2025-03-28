## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?


The presence of missing values or values that state "NO DATA" may be attributed to a connectivity issue where the device fails to record and store data. Additionally it could be due to the participant removing the device interrupting the 5 minute recording cycle the device functions from. The risk of filtering the values out can ultimately create significant gaps in the final analysis. For example, a gap in the sleeping heart rate can result in inaccurate assumptions/findings of the participant's sleep.

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.


The sleep phase appears to occur in Phase 0. It is in this phase where we can observe a steady decrease in heart rate overtime which is typical during sleep. In this phase the average heart rate is about 65 bpm with a lower standard deviation of 8.53 indicating that there is less variability in the fluctuation of bpm patterns, another common trend in sleep.



## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 


The exercise phase appears to occur in Phase 1. Here we observe a heart rate that reaches a maximum of 110 bpm and has an average heart rate of 87 bpm. Also, our figure depicts a trend that is commonly associated with exercising. We notice that overtime, heart rate increases and at the end of the time period the heart rate is still high which could indicate the participant finishing a workout.  


## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

This trend is observed in Phase 2. Here we observe a heart rate that reaches almost about 120 bpm indicating that there is increase in activity and we also have a higher standard deviation, 13.38, which demonstrates a higher variability.

