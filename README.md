# cstrike-fastdl
## Introduction
Basic script that should assist those running servers from source engine games to allow users to download the custom content on the server.
Essentially, it will setup and run a fastdl server, handling map compression and what directories it will serve on its own.

**DO NOTE THAT YOU MUST RUN THIS SCRIPT EVERYTIME YOU RUN YOUR SERVER**

## Requirements
- Port forwarding
- Python's requests library
 ```
pip install requests
```

## Setup
1. Place the script file on your server's map directory
2. Make sure whatever port the server is running on is forwarded
3. After running the script, you should get the host address and port that the files are being served on, make sure your server's cfg has the _sv_downloadurl_ cvar set correctly to that value
4. (optional) If you did not previously have the _sv_downloadurl_ cvar set on your server's cfg, restart your server
