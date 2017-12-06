## Flask-based API for a Simple Mattermost Dice Roller Webhook

This is a simple, lightweight Flask server used to do dice rolls in a public [Mattermost](https://about.mattermost.com/) channel.

This can probably be repurposed to do other things, in this case it just wraps the Python ```random``` library into a JSON-friendly API for Mattermost but could be modified to perform other tasks.

### Components

* ```mattermost-hotdice.py``` Flask app that runs an simple API to query with a
  Mattermost outgoing webhook.

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
   - You should run this as an unprivileged user.

### Mattermost Server Settings

* System Console -> Developer Settings -> Allow untrusted internal connections to: ```localhost```
* System Console -> Custom Integrations -> Enable integrations to override usernames: ```true```
* System Console -> Enable integrations to override profile picture icons: ```true```

### Webhook Settings

* Main Menu -> Integrations -> Outgoing Webhook
  - Add Outgoing Webhook
  - Content-type: ```application/json```
  - Trigger When: ```First word matches a trigger word exactly```
  - Callback URLs:  ```http://localhost:8090/hotdice```

### Action Pic

![hotdice](/image/diceroll.png?raw=true)
