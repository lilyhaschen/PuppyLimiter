# PuppyLimiter: The Cutest Bandwidth Capper in the Dog Park૮ • ﻌ - ა

---

## What is this?

PuppyLimiter is a network tool that helps you **monitor, analyze, and limit the bandwidth** (upload/download) of devices on your local network—
all while being as cute as a puppy with zoomies! It works on both **Linux** (with `tc` and `iptables`/`nmap`) and **Windows** (with PowerShell and demo firewall rules).
Choose your access: admin/root (for full power) or just physical (for when you can only unplug things). Every action is announced by adorable dog kaomojis and cute puppy messages.

---

## Features

* ૮ • ﻌ - ა  Scan for devices on your LAN (using nmap or arp)
* υ´ᴖ ﻌ ᴖ`υ  Monitor bandwidth (Linux: `ifstat\`, Windows: PowerShell stats)
* ૮ ˶′ ཅ ‵˶ ა  Limit any device’s bandwidth (Linux: real cap, Windows: demo firewall block)
* zᶻ ૮˶- ﻌ -˶ა⌒)ᦱ  Remove bandwidth limits ("unleash" the device)
* ૮⍝• ᴥ •⍝ა  Throttle everyone fairly (Linux: tbf, Windows: info/demo only)
* ૮ฅ・ﻌ・აฅ  Restore all network limits (let everyone run wild)
* ૮ ･ ﻌ･ა  Cute “bark” alerts on command
* ฅ՞•ﻌ•՞ฅ  Admin/physical access tips for network study
* ｡:ﾟ૮ ˶ˆ ﻌ ˆ˶ ა ﾟ:｡  Puppy kaomojis and unique puppy messages for every action

---

## Requirements

### Linux:
* Python 3
* `nmap` (`sudo apt install nmap`)
* `tc`, `ifstat` (`sudo apt install ifstat`)
* Run as root for bandwidth control features

### Windows:
* Python 3
* PowerShell 5+
* Run as administrator for best results

---

## How To Use
1. Run the script:
   ```
   python3 puppy_limiter.py
   ```
2. Pick your operating system (Linux/Windows)
3. Pick your access level (admin or physical)
4. Choose your action from the menu (scan, limit, unlimit, throttle, restore, bark, study tips, exit)
5. Enjoy the puppy messages and kaomojis!
---
## Limitations
* **Linux:** Real bandwidth limits need root and proper interface selection.
* **Windows:** Bandwidth limits use demo firewall blocks—real throttling needs 3rd party tools.
* Physical access = you really must touch the cable or router! (Manual override.)
---
## Kaomoji Credits
All kaomojis are inspired by doggy cuteness across the internet:
૮ • ﻌ - ა, υ´ᴖ ﻌ ᴖ\`υ, ૮ ˶′ ཅ ‵˶ ა, zᶻ ૮˶- ﻌ -˶ა⌒)ᦱ, ૮⍝• ᴥ •⍝ა,
---
## Disclaimer
PuppyLimiter is for **study and educational purposes only**.
Do not use on networks you do not own or have permission to manage.
The developer is not responsible for any mischief, accidental puppy chewing, or tail chasing.

---

## Have fun and play safe! ૮ ˶ˆ ﻌ ˆ˶ ა

