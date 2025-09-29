# TASC_Communication-Controls_Task
Giselle's Temperature Publisher and Subscriber Node

The task was to create a simple Publisher and Subscriber node in Python using ROS 2.

I created a temperature publisher and subscriber node that reads a given temperature data
and it gives a warning if the temperature is too high or too cold.

The files draw_circle.py, my_first_node.py, and pose_subscriber.py was my first introduction
while following a tutorial. 

Then, I implemented the temperature publisher and subscriber given the knowledge gained from
the tutorial.

Brief explanation (1–2 paragraphs) describing:

**What type of data did I choose to send?**
- I chose to send random temperature data to the publisher to read.
- Then it would send to the subscriber to determine whether or not the temperature is too high or cold.

**How this type of data would contribute to a robotics system (e.g., navigation, control, sensing)**
- I think this data would be helpful for the robot's safety and contribute to its sensing
- By knowing whether or not the robot itself was too hot or cold, it can then act accordingly to ensure
  that its internal temperature is running at a proper temperature. 

**How would I improve this**
  - Instead of using a given set of temperature data, I would've liked to try using my CPU temperature
    to monitor in real time and see if it is overheating or not.
