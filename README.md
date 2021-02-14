# Get the Latest Anime Updates, Sometimes.
Bot that scrapes crunchyroll, and relays a summary of the most recent episode of your favorite anime
## Adding to your server
To add to your server, go [here](https://discord.com/api/oauth2/authorize?client_id=810394677705703466&permissions=79936&scope=bot) and give it the necessary permissions. It is setup by default to portray the Dalai Lama's wisdom.

## Running for yourself
The following steps will allow you to run a copy of this bot for yourself.

**On the Discord Applicaiton Page**
1) Create a new discord application [here](https://discord.com/developers/applications).
2) Under the **OAuth2** tab, give the bot permission to:
  * Send Messages
  * Send TTS Messages
  * Manage Messages
  * Read Message History
  * Add Reactions
3)Naviage to the **Bot** tab, regenerate, and copy the token.

**In your local repo**
1) Copy *credentials.config.EXAMPLE* and re-name it *credentials.config*
2) Paste your token (as a string) into the **discord_token** field, in *credentials.config*
3) Run *run.sh* on your system. I think you need to have Git bash installed for this to work. _**Python 3.9** was used to test, but any python 3 version should work_
