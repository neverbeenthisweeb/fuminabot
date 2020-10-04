# FuminaBot ホシノ・フミナ

A telegram bot based on the python-telegram-bot [introduction](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot).

### How to start?

1. Copy `.env.example` and make your own `.env`
2. Get your token from [@BotFather](https://telegram.me/botfather)
3. Update the `TOKEN` field in your `.env`
4. Run `pip install -r requirements` to install required modules
5. Run `make start`

### Features
* `start_handler` : Replies with a greeting text on a `/start` command.
* `echo_handler` : Replies with the same message on any non-command incoming messages.
* `img_handler` : Replies with a pict of Fumina on a `/img` command.