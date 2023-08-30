require('dotenv').config();
const token = process.env.BOT_TOKEN;

const Discord = require('discord.js');
const client = new Discord.Client();
const PREFIX = '!';

client.once('ready', () => {
    console.log('Bot is online!');
});

client.on('message', (message) => {
    if (message.author.bot) return; // Ignore messages from bots
    if (!message.content.startsWith(PREFIX)) return; // Ignore messages without the prefix

    const args = message.content.slice(PREFIX.length).trim().split(/ +/);
    const command = args.shift().toLowerCase();

    if (command === 'hello') {
        message.channel.send('你好！👋');
    }
});

client.login(token);