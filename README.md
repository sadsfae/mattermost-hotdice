## Flask-based API for a Mattermost Dice Roller Webhook/Slash Command

This is a simple, lightweight Flask server used to do dice rolls in [Mattermost](https://about.mattermost.com/) channels.

There is both a custom ```slash command``` version as well as an ```outgoing web hook```

### Components

* ```mattermost-hotdice.py``` Flask app that runs an simple API to query with a
  Mattermost outgoing webhook or slash command.

### Requirements
* python (tested on 2.7.5)
* python-flask
* Mattermost (tested on 4.3.2+)

### Installation

* Clone the repository
```
git clone https://github.com/sadsfae/mattermost-hotdice
cd mattermost-hotdice
```

* Run the Python application via ```python mattermost-hotdice.py```
   - You might want to run this via a systemd service or init script once you're happy with it.
   - You should run this as an unprivileged user, an example ```systemd``` service file is included.

### Mattermost Server Settings

* System Console -> Developer Settings -> Allow untrusted internal connections to: ```localhost```
* System Console -> Custom Integrations -> Enable integrations to override usernames: ```true```
* System Console -> Enable integrations to override profile picture icons: ```true```

### Setup

You only need one of these approaches.  Slash commands are a bit more configurable as they can work in private chat or private channels.

#### Setting up as a Webhook

* Main Menu -> Integrations -> Outgoing Webhook
  - Add Outgoing Webhook
  - Content-type: ```application/json```
  - Trigger Words:   
```
hotdice
Hotdice
```
  - Trigger When: ```First word matches a trigger word exactly```
  - Callback URLs:  ```http://localhost:8090/hotdice```

#### Setting up as a Slash Command

* Main Menu -> Integrations -> Slash Command 
  - Add Slash Command
  - Description: ```/random 1000```
  - Command Trigger Word: ```random```
  - Request URL: ```http://localhost:8090/random```
  - Request Method: ```POST```

### Action Pic

* Webhook

![hotdice](/image/diceroll.png?raw=true)

* Slash Command

![hotdice_slashcmd](/image/diceroll-slashcommand.png?raw=true)
