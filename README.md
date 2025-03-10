# 🤖 Regex Parser Bot: The Regex Wizard 🧙‍♂️

Welcome to the **Regex Parser Bot**, your friendly neighborhood Telegram bot that’s here to make regex magic happen! Built with **Telethon** and powered by **PostgreSQL**, this bot is your go-to tool for parsing messages, managing users and groups, and broadcasting like a pro. Whether you're a regex ninja or just getting started, this bot has got your back!

---

## 🚀 Features That’ll Blow Your Mind

- **Regex Parsing**: Reply to any message with a regex pattern, and watch the bot work its magic! ✨
- **User & Group Management**: Automatically stores user and group IDs in a sleek PostgreSQL database. No duplicates, no drama! 🎯
- **Broadcast Messages**: Send messages to all users, groups, or both with a single command. Spread the word like a boss! 📢
- **Real-Time Stats**: Get instant stats about the number of users and groups in the database. Knowledge is power! 📊
- **Modular Design**: Clean, maintainable, and scalable codebase. Because messy code is a big no-no! �
- **Docker & Heroku Ready**: Deploy like a pro with Docker and Heroku support. Your bot, your rules! 🐳☁️

---

## 🛠️ Command Center

Here’s how you can boss around your bot:

| Command               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `/start`              | Start the bot and get added to the database. Easy peasy! 🎉                |
| `/help`               | Show a list of available commands. Help is just a command away! 🆘         |
| `/stats`              | Display the number of users and groups in the database. Stats don’t lie! 📈|
| `/broadcast -u <msg>` | Broadcast a message to all users. Shout it out! 📣                         |
| `/broadcast -g <msg>` | Broadcast a message to all groups. Group hug! 🤗                           |
| `/broadcast -all <msg>`| Broadcast a message to both users and groups. Go big or go home! 🏠        |
| Reply with regex      | Apply a regex pattern to the replied message. Regex wizardry at its best! �|

---

<h2>🚀 Quick Start: Let’s Get This Bot Rolling!</h2>

<h3>Prerequisites</h3>
<ul>
  <li><strong>Python 3.9+</strong>: Because who uses Python 2 anymore? 🐍</li>
  <li><strong>PostgreSQL</strong>: The database of champions. 🏆</li>
  <li><strong>Telegram API ID and Hash</strong>: Get these from <a href="https://my.telegram.org">my.telegram.org</a>. 🆔</li>
</ul>

<h3>Installation</h3>
<ol>
  <li>Clone the repository (if you haven’t already):
    <pre><code>git clone https://github.com/PN-Projects/regex_parser_bot.git
cd regex_parser_bot</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Set up environment variables:
    Create a <code>.env</code> file and add the following:
    <pre><code>API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
DATABASE_URI=postgresql://user:password@localhost:5432/telegram_bot</code></pre>
  </li>
  <li>Run the bot:
    <pre><code>python3 bot.py</code></pre>
  </li>
</ol>

<h2>🐳 Docker Deployment: Because Containers Are Cool</h2>
<ol>
  <li>Build the Docker image:
    <pre><code>docker build -t regex-parser-bot .</code></pre>
  </li>
  <li>Run the container:
    <pre><code>docker run --env-file .env regex-parser-bot</code></pre>
  </li>
</ol>

<h2>☁️ Heroku Deployment: Take It to the Cloud!</h2>
<ol>
  <li>Install the <a href="https://devcenter.heroku.com/articles/heroku-cli">Heroku CLI</a>. Because clouds are better with tools. ☁️</li>
  <li>Log in to Heroku:
    <pre><code>heroku login</code></pre>
  </li>
  <li>Create a new Heroku app:
    <pre><code>heroku create your-app-name</code></pre>
  </li>
  <li>Set environment variables:
    <pre><code>heroku config:set API_ID=your_api_id API_HASH=your_api_hash BOT_TOKEN=your_bot_token DATABASE_URI=your_database_uri</code></pre>
  </li>
  <li>Deploy the app:
    <pre><code>git push heroku main</code></pre>
  </li>
  <li>Scale the worker:
    <pre><code>heroku ps:scale worker=1</code></pre>
  </li>
</ol>

Or Just Click the button below to deploy this bot to Heroku instantly:

<a href="https://heroku.com/deploy?template=https://github.com/PN-Projects/regex_parser_bot">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku">
</a>



<h2>🌟 Contributors: The Real Heroes</h2>

Thanks to these jacka** i mean amazing people who have contributed to this project:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/satyanandatripathi">
        <img src="https://github.com/satyanandatripathi.png" width="100px;" alt="satyanandatripathi"/>
        <br />
        <sub><b>satyanandatripathi</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/AvikaTrivedi">
        <img src="https://github.com/AvikaTrivedi.png" width="100px;" alt="AvikaTrivedi"/>
        <br />
        <sub><b>AvikaTrivedi</b></sub>
      </a>
    </td>
  </tr>
</table>

<h2>📄 License: Do What You Want (Within Reason)</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details. Basically, do whatever you want, but don’t blame us if it breaks. 😉</p>

<h2>💬 Support: We’re Here for You</h2>
<p>For any questions or issues, please open an issue on <a href="https://github.com/PN-Projects/regex_parser_bot/issues">GitHub</a>. We’ll get back to you faster than a regex match! ⚡</p>

<p>Made with ❤️ by <a href="https://github.com/PN-Projects">PN-Projects</a>. Now go forth and parse like a pro! 🧙‍♂️</p>
