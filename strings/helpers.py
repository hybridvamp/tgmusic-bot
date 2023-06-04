HELP_1 = """🙄 <u>ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</u>

Just add "c" in the starting of the commands to use them for channel.

/pause: Pause the current playing stream.

/resume: Resume the paused stream.

/skip: Skip the current playing stream and start streaming the next track in the queue.

/end or /stop: Clears the queue and ends the current playing stream.

/player: Get an interactive player panel.

/queue: Shows the queued tracks list."""

HELP_2 = """😜 **<u>AUTH USERS:</u>**
Auth users can use admin rights in the bot without admin rights in the chat. [Admins only]

/auth [username]: Add a user to the auth list of the bot.

/unauth [username]: Remove an auth user from the auth users list.

/authusers: Shows the auth users list of the group."""


HELP_3 = """<b>BLACKLIST FEATURE</b> [Only for sudoers]
😒 **<u>BLACKLIST CHAT:</u>**

/blacklistchat [chat ID]: Blacklist a chat from using the bot.

/whitelistchat [chat ID]: Whitelist the blacklisted chat.

/blacklistedchat: Shows the list of blacklisted chats.


😤 **<u>BLOCK USERS:</u>**

/block [username or reply to a user]: Start ignoring the user, so that they can't use bot commands.

/unblock [username or reply to a user]: Unblocks the blocked user.

/blockedusers: Shows the list of blocked users."""


HELP_4 = """🍒 **<u>BROADCAST FEATURE</u>** [Only for sudoers]:

/broadcast [message or reply to a message]: Broadcast a message to served chats of the bot.

<u>Broadcasting modes:</u>
**-pin**: Pins your broadcasted messages in served chats.
**-pinloud**: Pins your broadcasted message in served chats and sends notification to the members.
**-user**: Broadcasts the message to the users who have started your bot.
**-assistant**: Broadcast your message from the assistant account of the bot.
**-nobot**: Forces the bot to not broadcast the message..

**Example:** `/broadcast -user -assistant -pin Testing broadcast`
"""
HELP_5 = """😉 **<u>EXTRAS:</u>**

/loop [disable/enable] or [between 1:10]: When activated, the bot will play the current playing stream in loop for 10 times or the number of requested loops.

/shuffle: Shuffles the queued tracks.

/seek: Seek the stream to the given duration.

/seekback: Backward seek the stream to the the given duration.

/lyrics [song name]: Search lyrics for the requested song and send the results."""

HELP_6 = """🤨 **<u>SERVER PLAYLISTS:</u>**

/playlist: Check your saved playlist on servers.

/deleteplaylist: Delete any saved track in your playlist.

/play: Starts playing from your saved playlist."""

HELP_7 = """🍑 Ping Command:

/ping : show the ping and system stats of the bot.

/stats : get top 10 track global stats, top 10 users of the bot, top 10 chats on the bot, top 10 played in the chat, and many more..."""

HELP_8 = """💞 Play Commands:

c stands for channel play.
v stands for video play.
force stands for force play.

/play or /vplay or /cplay : starts streaming the requested track on videochat.

/playforce or /vplayforce or /cplayforce : force play stops the ongoing stream and starts streaming the requested track.

/channelplay [chat username or ID] or [disable] : connect channel to a group and starts streaming tracks by the help of commands sent in group."""

HELP_9 = """🥀 Sudoers and Owner Commands:

🥺 Add & Remove Sudoers:

/addsudo [username or reply to a user]
/delsudo [username or reply to a chutiya.]

🥶 Heroku:

/usage : shows the dyno usage of the month.

🤯 Config Variables:

/get_var : get a config var from Heroku or .env.
/del_var : delete a config var on Heroku or .env.
/set_var [var name] [value] : set or update a config var on Heroku or .env.

🤓 Bot Commands:

/restart : restarts your bot.

/update : updates the bot from the upstream repo.

/speedtest : check bot's server speed.

/maintenance [enable/disable] : enable or disable maintenance mode of your bot.

/logger [enable/disable] : bot will start logging the activities happen on bot.

/get_log [number of lines] : get logs of your bot [default value is 100 lines]

💔 For Private Bot Only:

/authorize [chat ID] : allows a chat for using the bot.
/unauthorize [chat ID] : disallows the allowed chat.
/authorized : shows the list of allowed chats."""

HELP_10 = """🤑 <u>ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛs :</u>

/activevoice : shows the list of active voicechats on the bot.
/activevideo : shows the list of active videochats on bot.
/autoend [enable|disable] : enable stream auto end if no one is listening."""

HELP_11 = """😅**<u>ɢᴇᴛ sᴛᴀʀᴛᴇᴅ ᴡɪᴛʜ ʙᴏᴛ</u>**
/start : starts the music bot.

/help : get help menu with explanation of commands.

/reboot : reboots the bot for your chat.

/settings : shows the group settings with an interactive inline menu.

/sudolist : shows the sudo users of music bot."""

HELP_12 = """🤬 <u>ɢʙᴀɴ ғᴇᴀᴛᴜʀᴇ</u> [only for sudoers] :

/gban [username or reply to a chutiya] : globally bans the chutiya from all the served chats and blacklist him from using the bot.

/ungban [username or reply to a user] : globally unbans the globally banned user.

/gbannedusers : shows the list of globally banned users."""
