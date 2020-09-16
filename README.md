# TaskManager
Time and Task Management Tool

## Proposal
We would like to create a task management tool that allows users to list tasks that need to be done.
At minimum we would like Task Manager to have CRUD capabilities. 
Our tasks would have an optional title, description, optional deadline/ start time, optional priority (Tasks not given a priority will be in average priority), and optional estimated amount of time needed to do the task.

If time permits:
We would also like the option to schedule tasks and integrate an agenda where tasks have to be done in a certain time frame, like a calendar except with the added "hard block of time set or soft" hard and soft meaning whether one can do other stuff during this block of time. Ex: work is a hard block of time because you have to go to work in that set time frame and cannot do other things during work hours, whereas sleep is a softer block of time since you can choose to sleep a little later or wake a little earlier.
All of these can work with the simple "task" object.

<!---
## Basic Features
- Tasks: Ability to create a list of tasks to do with option to add deadlines 
  - Tasks can have different priorities where it can automatically increase in priority (or stay the same) as the deadline approaches
  - Perhaps estimated amount of time needed to do task?
- Schedule: Ability to block out times where one is unavailible to do tasks, like a calendar except with the added "hard block of time set or soft" hard and soft meaning whether one can do other stuff during this block of time. Ex: work is a hard block of time because you have to go to work in that set time frame and cannot do other things during work hours, whereas sleep is a softer block of time since you can choose to sleep a little later or wake a little earlier. Can be implemented using priority??? So maybe these can also be tasks.
- Potentially as deadlines approach, can be reminded about deadline task, as well as warned when you may not have time to do the task due to preexiting schedule. Ex. You have a task to do essay in the next week with estimated time needed of 6 hrs, but you only have 5 hrs of unblocked time, it warns you. 
- Potentially gamify accomplishing tasks????
-->

# Installation 
Install python

Install flask-restx

    pip install flask-restx
 
