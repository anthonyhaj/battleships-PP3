# Battleships Game

**Developer: Anthony Haj Ibrahim**

[Visit live website](https://battleships-game-pp3.herokuapp.com/)

![Mockup image](assets/deployment/mockup-image.png)

## Table of Contents
- [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
- [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
- [Technologies Used](#technology-used)
    - [Language used](#language-used)
    -[Python Libraries used](#python-libraries-used)
    - [Other websites/tools used](#other-websitestools-used)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to be implemented](#features-to-be-implemented)
- [Testing](#testing)
    - [User Stories Testing](#user-stories-testing)
    - [Tested Devices with Browsers](#tested-devices-with-browsers)
    - [Validator Testing](#validator-testing)
    - [Bugs and Fixes](#bugs-and-fixes)
- [Deployment](#deployment)
    - [Deploying in Heroku](#deploying-the-website-in-heroko)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Cloning of Repository in GitHub](#cloning-the-repository-in-github)
- [Credits](#credits)
    - [Credits](#credits)
    - [Code](#code)
- [Acknowledgements](#acknowledgements)

## Project Goals
  - The goal of this project was to create a battleships game where the player plays against the computer

### User Goals
- Play battleships
- Be able to choose if user would like to play
- Be able to see where a user has placed their battleships
- Be able to see opponents board and where the user has targeted

### Site Owner Goals
- To make a game that is easy to understand
- To ask the user if they would like to play the game
- To make sure user can place ships on valid targets
- To make sure user can only attack on valid parts of the game grid
- To give the user a choice to play again

## User Experience

### Target Audience
- No specific target audience
- Anyone who enjoys to play battleships

### User Requirements and Expectations
- No requirements to play
- Expect to see both the player board and computer board 
- Expect to see if player move has hit the desired target
- Expect to see computer move 

### User Manual
<details><summary>Click here to view instructions</summary>

#### Welcome to game

- Once game is started up asks user if they would like to play
- User must enter y/n
- Any other unput prompt user to try again

#### Placing battleships
- Player starts out with 5 ships (Carrier: 5 cells, Battleship: 4 cells, Cruiser: 3 cells, Submarine: 3 cells, Destroyer: 2 cells)
- When game starts it will prompt user to enter a coordinate to place ships
- Once a player has chosen a coordinate, the prompt will ask if player would like placement to be "V" for vertical
or "H" for horizontal.
- Areas where the player battleships are place are marked with 'O'
- Computer battleships will be placed randomly and are hidden from the player

#### Player turn
- Once all player battleships have been placed, the game begins
- Player will be asked to choose a coordinate to attack (e.g A1)
- If the player enters anything other than a coordinate they will prompted to try again
- If a player misses a computer battleship they will see a message saying "Miss!"
- If a player hits a computer battleship they will see a message saying "Hit!"
- Areas where the player has missed will be marked with '-' and hits marked with 'X' on the board
- If a player chooses an already chosen coordinate they will receive a message saying 
"You already targeted this cell." and prompting a user to enter another coordinate

#### Computer turn
- Once a player has chosen a coordinate to attack the computer will also choose a coordinate
- Underneath the computer board the player will see if the computer has missed or hit a target 
- Underneath the computer move showing where the computer has hit on their board
- If a computer has missed a coordinate, it will be marked with '-'
- If a computer has hit a coordinate, it will be marked with 'X' 

#### Win or lose
- Once a player has hit all the computer battleship cells they will recieve the message 
"Congratulations! You sank all the computer's ships."
- If the computer hits all players battleship cells they will revieve the message 
"Game Over! The computer sank all your ships."

#### Restart game
- Once the game is over user is asked whether the would like to play again Y/N
- If user selects "Y" the game will reset the game
- If user selects "N" the game will exit with a goodbye message

</details>

## User Stories

### Users
1. I want to be able to choose if user would like to play
2. I want to be able to see where a user has placed their battleships
3. I want to be able to see the opponents board
4. I want to make sure user can place ships on valid targets

### Site Owner
5. I want users to be able to enter correct coordinates
6. I want users to be able to know when they have used the same coordinate
7. I want users to know if they have hit or missed their target
8. I want to be able to play again

## Technologies Used

### Languages Used
- Python

### Python Libraries used
- random 

### Websites and tools
- [GitHub](https://github.com/)
- [GitPod](https://www.gitpod.io/)
- [Heroku](https://www.heroku.com/)
- [Pycharm](https://www.jetbrains.com/pycharm/)
- [Am I responsive](https://ui.dev/amiresponsive)

## Features

### Welcome to battleships
- Welcome the user to the game
- Promts Y/N to start playing the game

<details>
    <summary>Welcome to game screenshot</summary>
    <img src="assets/screenshots/welcome.png">
</details>  

### Ship placement
- Prompts user to enter a starting coordinate for each ship
- Promts user to choose a vertical or horizontal position
- Player board shows chosen ship placement areas

<details>
    <summary>Game start screenshot</summary>
    <img src="assets/screenshots/game-start.png">
</details>  

<details>
    <summary>Game start chosen cells</summary>
    <img src="assets/screenshots/game-start-2.png">
</details> 

### Game display and moves
- Displays player and computer board showing player ships and hiding computer ships
- Misses are marked with '-' and hits marked with 'X'
- Shows computer move after player has chosen a move

<details>
    <summary>Computer board screenshot</summary>
    <img src="assets/screenshots/computer-board.png">
</details> 

<details>
    <summary>Player board screenshot</summary>
    <img src="assets/screenshots/player-board.png">
</details> 

### Restart Game
- Displays winner after all battleships have sunk
- Prompts user to choose to play again or not

<details>
    <summary>Game ending screenshot</summary>
    <img src="assets/screenshots/game-end.png">
</details> 

## Testing
- Testing of user stories
- Testing validation
- Browser Testing
- Mobile Testing

### Manual User Stories Testing

1. Be able to choose if user would like to play


| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Would you like to play | Type Y/N | Y: Starts game / N: Maybe next time! | Works as expected

<details>
    <summary>Would you like to play screenshot</summary>
    <img src="assets/screenshots/welcome.png">
</details> 

2. Be able to see where a user has placed their battleships


| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Player game board | Type coordinate (e.g A10) | 'O' showing ship placement area | Works as expected

<details>
    <summary>Player board screenshot</summary>
    <img src="assets/screenshots/player-board-2.png">
</details> 


3. I want to be able to see the opponents board

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Computer game board | Type coordinate (e.g A10) | 'X' showing hit / '-' showing miss | Works as expected

<details>
    <summary>Computer board screenshot</summary>
    <img src="assets/screenshots/computer-board-2.png">
</details> 


4. I want to make sure user can place ships on valid targets

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Coordinate validation | Type invalid coordinate (e.g J5, H) | Ship goes out of bounds | Works as expected

<details>
    <summary>Out of bounds screenshot</summary>
    <img src="assets/screenshots/bounds.png">
</details> 


5. I want users to be able to enter correct coordinates

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Coordinate validation | Type coordinate (e.g A10) | Invalid target. Please try again | Works as expected

<details>
    <summary>Invalid target screenshot</summary>
    <img src="assets/screenshots/invalid.png">
</details> 


6. I want users to be able to know when they have used the same coordinate

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Coordinate reuse validation | Type coordinate (e.g A10) | You already targeted this cell | Works as expected

<details>
    <summary>You already targeted this cell screenshot</summary>
    <img src="assets/screenshots/used.png">
</details>  


7. I want users to know if they have hit or missed their target

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Hit! or Miss! | Type coordinate (e.g A10) | "Hit!" or "Miss!" message after player move | Works as expected

<details>
    <summary>Hit screenshot</summary>
    <img src="assets/screenshots/hit.png">
</details>  

<details>
    <summary>Miss screenshot</summary>
    <img src="assets/screenshots/miss.png">
</details>  


8. I want to be able to play again

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Would you like to play again | Type Y/N | Y: resets game / N: Thank you for playing! | Works as expected

<details>
    <summary>Play again screenshot</summary>
    <img src="assets/screenshots/play-again.png">
</details> 

### Tested Devices with Browsers
- iPhone 12 Pro
- iPad Mini
- Lenovo thinkpad (PC)
    - Microsoft edge 
    - Chrome

### Validator Testing

[PEP8 Python Validator](https://pep8ci.herokuapp.com/) was used to validate the code.

- No errors found in code

<details>
    <summary>Validator run.py</summary>
    <img src="assets/screenshots/pep8-validation.png">
</details> 

### Bugs and Fixes

| **Bugs** | **Fixes** |
| ------- | ------- |
| User unable to target certain cells (A10, B10, C10, E10, F10, G10, H10, I10, J10) | Modified the validation function validate_coordinate to handle the special case of coordinates ending with "10" correctly|
| Computer-controlled opponent hits the same target multiple times | Modified the computer_turn function to generate random coordinates until an untargeted cell is found|
| Missing validation for the target coordinate input | Implemented the validate_coordinate function to validate the target coordinate input for both the player and computer-controlled opponent's turns. It ensures that the entered coordinate is in the correct format and within the valid range|

## Deployment

### Deploying in Heroko:
1. Create new app and add an app name
2. Select region then click on "create app"
3. Open settings and scroll to Config vars
4. Add PORT with key of 8000
5. Next scroll down to buildpacks in settings
6. Add python pack first
7. Add Nodejs next

<details>
    <summary>Buildpacks screenshot</summary>
    <img src="assets/deployment/buildpacks.png">
</details> 

8. Open the deploy tab
9. Connect to Github account on the "Deployment method" section
10. On the "Connect to Github" section choose the deployment repo and click connect

<details>
    <summary>Search repo screenshot</summary>
    <img src="assets/deployment/connect.png">
</details> 

11. Choose a method to deploy repo

<details>
    <summary>Deployment method screenshot</summary>
    <img src="assets/deployment/deploy.png">
</details> 

12. Click on "Deploy branch" and wait for a view button to appear
13. Click on view to open deployed webpage

<details>
    <summary>Deployment view screenshot</summary>
    <img src="assets/deployment/deploy-2.png">
</details> 

### Forking Github Repository
1. Go to GitHub repository 
2. Click on Fork button located in the top right corner
3. [GitHub Repository](https://github.com/anthonyhaj/battleships-PP3)

### Local Repository Cloning
1. Go to the GitHub repository
2. Click on Code button above all files
3. Copy HTTPS link to clone
4. On git bash change current directory to desired clone directory
5. Type git clone and paste URL and press enter

## Credits

### Code
- All code in this project was written by me using python

### Acknowledgements
- I would like to thank my mentor Mo Shami for his wonderful support 
- I would like to thank my family for their support through my coding journey