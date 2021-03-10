# P2-Beavers Arcade Project

Welcome!

In our project, we will store login information and game data from users signing in to play our web based games that we have created. Each group member made one game each, and we will be able to track users personal highscores and highscores among others. Learn more about our project below!

# Website Instructions
Runtime link: beaversarcade.cf

Simply paste this link into your browser and you will be taken to our website. You can explore the four games we have created and make an account for yourself with the login page

Game Instructions

1. Flappy Beaver: Click the spacebar to make the beaver jump, avoid hitting the barriers and see how far you can go.
2. Crossy Beaver: Use the arrow keys to maneuver the beaver around the different obstacles and make it across as many times as you can, you have 3 chances.
3. 2048: Using the arroqw keys, combine smaller numbered tiles in order to gain a higher numbered tile. Try to score as many points as you can and see if you can reach the 2048 tile!
4. Snake: Using the arrow keys, maneuver the snake around to ea the food which will make you grow. Avoid hitting the walls and your own tail.


Database Instructions

Use the "sign up" button to create your account, choosing a unique username and password. Then, click on the "sign in" button to login to your account using the same login info you used to create your account.

# The Technicals
1. 4 Javascript Games:

   a. Flappy Beaver done by Nolan
   
   b. Crossy Beaver done by Ryan
   
   c. 2048 done by Noah
   
   d. Snake done by Aidan
   
2. 3 RestAPI's (Quote, Word, Joke)
3. Sign up/Sign in system using SQL
4. Games Quiz
5. Leaderboard system/CRUD system to let users enter scores into a database

2048 Link to code: https://github.com/noahahooja/p2beavers/blob/main/templates/2048.html 

Snake Link to code: https://github.com/noahahooja/p2beavers/blob/main/templates/snake2.html

Crossy Beaver Link to code: https://github.com/noahahooja/p2beavers/blob/main/templates/crossybeaver.html

Flappy Bird Link to code: https://github.com/noahahooja/p2beavers/blob/main/templates/flappybeaver.html

# Project Board

Check out our project board where our group kept track of our new tickets and explained each technical used per ticket: https://github.com/noahahooja/p2beavers/projects/1

# College Board Reflections/Incorporations

Big Ideas:

Big Idea 1: Creative Computing: Creativity in visuals and customization in our website shown through games like flappy beaver and crossy beaver. Personalization and free design flow for fundamentals project. Creating navbar with bootstrap template in order for a unique aspect in our project.


Big Idea 2: Data: In our project, we were able to incorporate the “backend” java data in “frontend” to be used with an HTML. This was necessary in our project because we needed those front and end connections in order for our links to run on the web. This is shown through the website as all of our games appear through the navbar.


Big Idea 3: Algorithms and Programming: Lists, iterations, and dictionaries along with other functions were used in our project in order to use all required fundamentals. We used dictionaries as a source for backend data that is connected with templates. We used lists to define buttons on our website in order to connect them with its correlated page. We used jinja templates in the frontend files to organize information in the web page and to also organize variables. HTML was used in almost all of the files


Big Idea 4: Computer Systems and Network: We will be able to incorporate this by hosting a raspberry pi server. We will also have a running website than can be used anywhere. Runtime link: beaversarcade.cf


Big Idea 5: Impact of Computing: We built and developed our website that is available to others outside of our group of 4. In our world today, we see how the internet has changed the world in almost every aspect in life. Our group strongly understands the impact of computing by seeing how we can share information to the world through our web server





# History of big ticket changes:
  12/11 Updated readme to include project plan and scrum board links.
  12/24 Gameplayer format is 90% complete, needs databasing
  1/15 Games are completed/almost done
  2/1 Big Data Tickets

BEAVERS

Scrum Board: https://padlet.com/noland43522/59nicc77kbm7ebt7

Product Backlog: https://docs.google.com/document/d/1xEj5yHHlUAPphvRBRMrszuIpu87dqo8mykamLoRQMAs/edit?usp=sharing

Deployment Link: beaversarcade.cf

Code/GitHub Link: https://github.com/noahahooja/p2beavers.git



Week of 2/16

Aiden and Nolan's Ticket 
[Link to Ticket](https://github.com/noahahooja/p2beavers/projects/1#card-55160808)
[Link to Code](https://github.com/noahahooja/p2beavers/blob/ea179da7790fb6cc17fb2a9b5b881361c94eece6/templates/quiz.html#L1-L198)

Noah and Ryan's Ticket:
[Link to Ticket](https://github.com/noahahooja/p2beavers/projects/1#card-55168621)
[Link to Code](https://github.com/noahahooja/p2beavers/blob/main/templates/leaderboard.html)

Runtime link: beaversarcade.cf 
Leaderboard tab on navbar is Noah and Ryan's Ticket
Quiz tab on navbar is Aiden and Nolan's Ticket




Goals
1) Complete Flappy Beaver game (Nolan)
   - Game is complete, works, is user-friendly.
2) Complete Crossy Beaver game (Ryan)
   - Although Ryan's game is not complete, it is more complicated, with cars, lilipads, and a more intricate system for progressing through the game
   - Ryan has made a lot of progress and probably would have finished already if he had a simpler game.
3) Complete 2048 game (Noah)
   - Incomplete, gridlines are there.
   - The setting for Noah's game is there and works with the gameplayer model, he just needs to learn more javascript in order to create the actual gameplay.
4) Complete Snake game (Aiden, Nolan)
   - Game is complete, works, is user-friendly.
   - Has easter eggs.
(These games are actually coded by ourselves, not ripped from the internet)

Evidence of code completion and review guidance:
https://docs.google.com/document/d/1XIT4tkmv0a9W0HzwQUHU-CpebnF9vkLzT2ZUdbXnGU4/edit?usp=sharing

Week of 2/1: 

Ticket #1
Noah/Aiden: Incorporate a system where users can enter their score on one of our four mini games. We will be able to store this information and users will be able to see other entered information. Add more REST API sections in website. The website will include a random word api which outputs a random word giving its definition and pronunciation. There is also a random joke api which outputs a random joke when clicked.

Direct link to code: https://github.com/noahahooja/p2beavers/blob/main/templates/scorepage.html 
https://github.com/noahahooja/p2beavers/blob/main/main.py
https://github.com/noahahooja/p2beavers/blob/main/templates/home.html

Runtime link: beaversarcade.cf

Ticket #2:

Ryan: Ajax - a process which allows user information and new scores to be updated without the user ever having to reload the page. This will improve website efficiency, user interface, and overall run time. AJAX uses XMLHTTPRequest object to exchange information between a server, and then uses javascript to reupload and display this information.
Nolan: Login systems

Ticket #3
Nolan: Easter Egg- Creating a separate web server and domain to run the easter egg website and creating the user interface for this server as well as a way to get back to the main site.
Easter Egg Location: http://beavers.pii.at


