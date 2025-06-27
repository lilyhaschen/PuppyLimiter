import os
import sys
import subprocess
import random
import time

# =================== ASCII ART ===================
ART_START = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣄⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⠀⠀⠹⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣴⠾⠛⠉⠉⠉⠀⠀⠀⠀⠀⠉⠉⠉⠛⠷⣶⣼⣿⣉⣁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠛⠉⠛⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡏⠉⠙⠛⢶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣧⠀⠀⠀⠀
⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⢿⡇⠀⠀⠀
⠀⠀⠹⣿⡎⠀⠀⠀⣠⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⢻⡆⠀⠀⣆⣿⡇⠀⠀⠀
⠀⠀⠀⣿⡀⠀⡀⠀⣿⠁⠀⢠⣾⣿⡿⠆⠀⠀⠀⠀⠀⠀⢀⣾⣿⡿⠆⠀⠀⠀⢈⣿⠀⣄⣾⡿⠁⠀⠀⠀
⠀⠀⠀⠘⣿⣧⣇⢀⣇⠀⠀⠘⣿⣿⣷⡆⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⠖⠀⠀⠀⢸⣿⣷⠿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠙⠻⣿⣆⡀⠀⠀⠉⠉⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣸⣿⠁⣀⣀⣀⠀⠀⠀⠀
⠀⢀⣠⡶⠾⠛⠓⠶⣿⡟⠀⠀⠀⠀⠀⠀⠠⣾⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠟⠋⠉⠛⠻⣦⡀⠀
⢀⣾⠋⠀⠀⠀⠀⠀⠘⣿⣠⣄⡀⠀⠀⠀⠀⠛⠿⠟⠁⠀⠀⠀⠀⠀⡀⡀⠀⣴⣾⡏⠀⠀⠀⠀⠀⠈⣿⡄
⢸⣯⠀⢠⠀⠀⢀⣄⣠⣿⠿⢿⣷⣤⣦⣀⣤⣤⣤⣤⣀⣀⣀⣼⣆⣼⣷⣿⡾⠿⢿⣧⣀⣦⠀⠀⣤⠀⣸⡧
⠘⠿⣷⣾⣷⣤⠾⠿⠛⠁⠀⠀⠀⠁⠀⠉⠉⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠉⠛⠻⠷⠾⠿⠟⠛⠁
"""

ART_EXIT = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠤⠤⣤⠀⠀⠀⠀⡼⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⡄⠀⢀⡤⠔⠊⠁⠀⠀⠀⣰⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⠀⠀⠀⠚⠂⠀⠉⠒⠢⠤⠤⠄⠀⡰⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⠟⠛⠛⠋⠉⠉⠉⠉⠉⠉⠛⠛⠛⠷⢷⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠙⠛⠓⠓⠒⠒⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣴⣶⣶⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⠟⠉⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⟟⠀⠀⠀⠉⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⣽⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷⠀⠀⠀⠀⠀
⠀⠀⢰⣿⡏⣤⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡀⠀⠀⢤⢠⣼⡇⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣿⠁⠀⠀⠀⠀⣴⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠈⣇⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠀⡀⣀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⢠⣠⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣷⣇⣽⠀⢈⡏⠀⠀⠀⠀⣀⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣦⣤⠀⠀⠀⠀⠀⣿⣿⣧⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠿⣿⣧⣾⣿⡄⠀⠀⠀⠙⠿⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠋⠀⠀⠀⠀⠀⢸⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣿⡇⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢶⣼⣿⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀
⠀⠀⣠⣶⣾⠿⠛⠛⠻⢷⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡿⠋⠉⠉⠉⠛⢿⣦⡀⠀⠀
⢀⣾⡿⠋⠀⠀⠀⠀⠀⠀⠙⣿⡆⢀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣿⡟⠀⠀⠀⠀⠀⠀⠀⠹⣿⡇⠀
⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣿⣷⣧⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⢠⡾⣠⣇⣠⣿⣿⣿⡇⠀⢀⠀⠀⠀⢀⠀⠀⢹⣷⠀
⣿⣷⡀⠀⣷⠀⠀⠀⣼⣦⣴⣿⠏⠙⠻⠿⣷⡿⠷⣶⣶⡾⠿⠿⠷⢶⣶⣦⣤⣾⣿⣷⣿⣿⠿⠿⠛⠛⠙⠻⣿⣤⣾⣇⠀⢀⣸⡇⠀⠀⠀⠀
⠘⢿⣿⣾⣿⣷⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠋⠀⠀
"""

DOG_KAOMOJIS = [
    "૮ • ﻌ - ა", "υ´ᴖ ﻌ ᴖ`υ", "૮ ˶′ ཅ ‵˶ ა","zᶻ ૮˶- ﻌ -˶ა⌒)ᦱ", "૮⍝• ᴥ •⍝ა",
    "૮ฅ・ﻌ・აฅ", "૮ ･ ﻌ･ა", "ฅ՞•ﻌ•՞ฅ", "૮ ˶′ﻌ ‵˶ ა", "｡:ﾟ૮ ˶ˆ ﻌ ˆ˶ ა ﾟ:｡", "υ˶˃ ﻌ ˂˶υ"
]
def random_dog_kaomoji():
    return random.choice(DOG_KAOMOJIS)

CUTE_ACTION_MESSAGES = {
    "scan": [
        "Puppy is sniffing for new friends on the network! 🦴",
        "Sniff sniff... Who's on the LAN today?",
        "Arf! Scanning the park for other doggies...",
        "Nose to the ground—puppy’s searching for every tail!",
        "Looking for new playmates... is that a squirrel or just a device?",
        "Wagging tail... so many new sniffs on the network!",
        "Zooming around the LAN sniffing every corner!",
        "Snuffle snuffle... Puppy is mapping the digital playground.",
        "Any bunnies or kitties out there on the Wi-Fi?",
        "If I find a new device, can I get a treat?"
    ],
    "limit": [
        "Putting a tiny leash on bandwidth! 🦴",
        "No more running wild, says the puppy!",
        "Applying the 'good doggo' limit.",
        "Gentle leash time—no chasing cars, just bytes.",
        "Puppy sits and gently asks the device to slow down!",
        "Puppy says: ‘Please use your paws, not your zoomies!’",
        "Setting the slow-walk mode—no sprinting on the network!",
        "Just a little tug on the collar, for everyone's safety.",
        "Leashing in the bandwidth, but still wagging!",
        "Device, time for a gentle stroll, not a race!"
    ],
    "unlimit": [
        "Taking off the leash—zoomies unlocked!",
        "Limits gone. Who wants to play fetch?",
        "Removing the cone of shame from the bandwidth!",
        "Puppy tosses the leash and shouts: FREEDOM!",
        "All paws on deck! No more limits for this friend.",
        "Puppy unlocks the backyard gate—run wild!",
        "No more fences! Bandwidth is free to roam.",
        "Throwing open the park gates—let's see those zoomies!",
        "Puppy yips with excitement—limits are gone!",
        "Network leash off, tail wags maximum!"
    ],
    "throttle": [
        "Sharing all the bandwidth, wag wag!",
        "Everyone gets a fair biscuit of internet now.",
        "Puppy brings balance to the byte park!",
        "Every pup gets an equal scoop of kibbles!",
        "No one hogs the tennis balls OR the bandwidth.",
        "Biscuit-for-everyone mode: ON!",
        "Fair play in the park! No puppy left behind.",
        "All paws get a turn on the slide—equal bandwidth!",
        "Let’s all chase the same stick—bandwidth for everyone!",
        "Every tail gets a wiggle! Sharing mode engaged."
    ],
    "restore": [
        "Everything is back to normal! Happy tail wiggles!",
        "Limits gone. Maximum tail wag!",
        "Network restored. Can I have a treat now?",
        "The park is tidy, all toys returned—network happy!",
        "Puppy cleaned up all the paw prints—network as good as new!",
        "All fences down, everyone is smiling and sniffing again.",
        "Tails up, noses wet—network feels great now!",
        "All the puppies have their favorite spot back.",
        "Everything is shiny and new, just like a fresh tennis ball.",
        "Belly rubs for the whole network! All restored."
    ],
    "monitor": [
        "Puppy is watching all the bytes go by! 🐾",
        "Monitoring: every bark, every byte.",
        "Network watchdog activated!",
        "Standing guard by the router—no squirrels allowed!",
        "Watching the bytes run like squirrels in the yard.",
        "Puppy perks up ears, watching every single paw step (packet)!",
        "Alert! Puppy is monitoring with big, round eyes.",
        "No biscuit left behind—puppy sees all the data.",
        "Puppy keeps an eye on the ball... and the bandwidth.",
        "If any byte sneaks out, puppy will bark!"
    ],
    "admin": [
        "Puppy is now the admin. Maximum paws!",
        "Secret Windows biscuit jar unlocked!",
        "Root mode: Puppy gets all the belly rubs.",
        "Alpha doggo at the controls now!",
        "Admin hat on—puppy looks very serious (but still cute).",
        "Time to run with the big dogs—admin access granted.",
        "Superpuppy powers activated!",
        "Puppy paws have the magic keys now.",
        "Full access! Puppy promises to be gentle.",
        "Only good doggos can have admin mode!"
    ],
    "physical": [
        "Ultimate access: unplug the Ethernet, but gently.",
        "Physical access: Time to press the Wi-Fi button!",
        "Manual override: pull the plug, fetch the cable.",
        "Sometimes you just gotta chase the cable!",
        "Unplug, replug, and maybe a little chew on the cord?",
        "Puppy can reach the buttons! Physical mode enabled.",
        "Time for the paws-on approach—unplug it, boop it, woof it.",
        "Bork bork! Flipping switches like a real herding dog.",
        "Pulling the plug—don’t worry, puppy will be careful!",
        "Manual methods only! Sometimes the old ways are best."
    ],
    "bark": [
        "Bow wow! Puppy is ready!",
        "Woof woof! All systems barking!",
        "Puppy shakes ears... let's get started!",
        "Loud bark! Time for some puppy action!",
        "Tail wag, big yawn—puppy is ready for anything!",
        "Alert alert! Puppy is on duty!",
        "Give me a command and watch me wag!",
        "Did someone say ‘treat’? Oh, just a command.",
        "Puppy ears perk up. Awaiting your next order!",
        "Tiny paws, big bark—let’s go!"
    ],
    "exit": [
        "Puppy logs off, does a final wag...",
        "Puppy is now off to nap... see you next time!",
        "The puppy curls up and goes to sleep. Good job today!",
        "Tired puppy... time for snuggles and dreams.",
        "Logging out with a tiny yawn and one last tail wag!",
        "Puppy found a sunny spot—logging off for nap time.",
        "Goodbye! Puppy will dream of routers and tennis balls.",
        "The kennel door closes gently—see you soon!",
        "Puppy’s eyes droop... zzz... Network dreams ahead.",
        "Puppy will miss you! Come play again soon."
    ]
}

def cute_print(action="bark"):
    print(random_dog_kaomoji(), end="  ")
    print(random.choice(CUTE_ACTION_MESSAGES.get(action, ["*rolls over*"])))

def pause():
    input("\nPress Enter to return to the menu...")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_art_start():
    clear_screen()
    print(ART_START)
    print("\nThe puppy just woke up and is ready for action!\n")

def print_art_exit():
    clear_screen()
    print(ART_EXIT)
    print("\nThe puppy is going to sleep. See you next time!\n")

# ================== OS & NETWORK SCAN ===================== 99
os_target = None  # global

def scan_network():
    if os_target == "linux":
        return scan_network_linux()
    else:
        return scan_network_windows()

def scan_network_linux():
    cute_print("scan")
    print("🐶 Sniff sniff! Puppy is scanning the network (requires nmap installed, try: sudo apt install nmap)...\n")
    try:
        gateway = subprocess.check_output("ip route | grep default | awk '{print $3}'", shell=True).decode().strip()
        print(f"🐾 Puppy found the gateway: {gateway}")
        subnet = ".".join(gateway.split(".")[:3]) + ".0/24"
        print(f"🐶 Bark! Scanning subnet: {subnet}")
        print("🐕 Please wait while I sniff for devices in the yard...")
        res = subprocess.check_output(f"nmap -sn {subnet}", shell=True).decode()
        lines = [l for l in res.split('\n') if "Nmap scan report" in l]
        devices = []
        for l in lines:
            ip = l.split(" ")[-1]
            devices.append(ip)
        for idx, ip in enumerate(devices):
            print(f"{idx+1}. {ip} (new friend found!)")
        print(f"\n🦴 Puppy found {len(devices)} devices. So many friends in the network park!")
        pause()
        return devices
    except Exception as e:
        print(f"😢 The puppy got distracted by a butterfly and couldn't finish scanning. (Error: {e})")
        pause()
        return []

def scan_network_windows():
    cute_print("scan")
    print("🐶 Puppy is sniffing the network (using arp -a)...\n")
    try:
        res = subprocess.check_output("arp -a", shell=True).decode(errors="ignore")
        lines = res.split('\n')
        devices = []
        for line in lines:
            if "-" in line and "." in line:
                ip = line.split()[0]
                devices.append(ip)
        for idx, ip in enumerate(devices):
            print(f"{idx+1}. {ip} (sniff sniff, found!)")
        print(f"\n🦴 Puppy found {len(devices)} devices (some might be asleep or hiding).")
        pause()
        return devices
    except Exception as e:
        print(f"😢 Oh no! The puppy tripped over a cable and couldn't finish scanning. (Error: {e})")
        pause()
        return []

# ================== BANDWIDTH MONITOR =====================

def monitor_bandwidth_linux():
    cute_print("monitor")
    print("🐕 Puppy is monitoring bandwidth (requires ifstat: sudo apt install ifstat).")
    iface = input("Which interface to sniff? (default: eth0): ").strip() or "eth0"
    print("🐶 The puppy is watching live bandwidth usage. Press Ctrl+C to stop.")
    time.sleep(1)
    try:
        os.system(f"ifstat -i {iface}")
    except KeyboardInterrupt:
        print("\n🦴 The puppy stopped watching. Bandwidth monitoring ended!")
    pause()

def monitor_bandwidth_windows():
    cute_print("monitor")
    print("🐶 Puppy is wagging tail while monitoring bandwidth... (using PowerShell Get-NetAdapterStatistics)")
    print("Press Ctrl+C to stop puppy's monitoring patrol.")
    try:
        while True:
            os.system('powershell -Command "Get-NetAdapterStatistics | Format-Table Name,ReceivedBytes,SentBytes -AutoSize"')
            time.sleep(2)
            os.system("cls")
    except KeyboardInterrupt:
        print("\n🦴 Puppy took a break from watching! Monitoring stopped.")
    pause()

# ================== BANDWIDTH LIMITING =====================

def limit_bandwidth_linux(ip, cap_mbps=1):
    cute_print("limit")
    print(f"🐕 Puppy is gently putting a bandwidth leash on {ip} to {cap_mbps} Mbps... (Linux)")
    iface = input("On which interface? (default: eth0): ").strip() or "eth0"
    try:
        os.system(f"sudo tc qdisc add dev {iface} root handle 1: htb default 12")
        os.system(f"sudo tc class add dev {iface} parent 1: classid 1:1 htb rate {cap_mbps}mbit burst 15k")
        os.system(f"sudo tc filter add dev {iface} protocol ip parent 1:0 prio 1 u32 match ip dst {ip} flowid 1:1")
        print("🦴 The leash is on! Limit applied! (Linux, requires sudo and tc/htb). Puppy wags tail!")
    except Exception as e:
        print(f"😢 Puppy got tangled in the leash and couldn't limit the bandwidth! (Failed: {e})")
    pause()

def unlimit_bandwidth_linux(ip):
    cute_print("unlimit")
    print(f"🐾 Puppy is now removing the leash for {ip}... (Linux)")
    iface = input("On which interface? (default: eth0): ").strip() or "eth0"
    try:
        os.system(f"sudo tc qdisc del dev {iface} root")
        print("🦴 Leash removed! {ip} can run free again. (If this was the only limit set.)")
    except Exception as e:
        print(f"😢 Puppy couldn't find the leash to remove! (Failed: {e})")
    pause()

def throttle_all_linux():
    cute_print("throttle")
    print("🐶 Puppy is making sure all friends get an equal share of the internet biscuits! (Linux, requires root/sudo & tc)")
    iface = input("Which interface to use? (default: eth0): ").strip() or "eth0"
    rate = input("How many Mbps for everyone? (default 2): ").strip() or "2"
    try:
        os.system(f"sudo tc qdisc add dev {iface} root tbf rate {rate}mbit burst 32k latency 400ms")
        print(f"🦴 All tails wag in harmony! Everyone gets {rate} Mbps.")
    except Exception as e:
        print(f"😢 Puppy spilled the water bowl! Could not throttle all devices. (Failed: {e})")
    pause()

def restore_network_linux():
    cute_print("restore")
    print("🐾 Puppy is restoring all network limits (Linux, requires root/sudo & tc)... Cleaning up the playground!")
    iface = input("Which interface? (default: eth0): ").strip() or "eth0"
    try:
        os.system(f"sudo tc qdisc del dev {iface} root")
        print("🦴 Playground is clean! All limits and throttles are gone.")
    except Exception as e:
        print(f"😢 The puppy couldn't remove all the obstacles! (Failed: {e})")
    pause()

def limit_bandwidth_windows(ip, cap_mbps=1):
    cute_print("limit")
    print(f"🐶 Puppy wants to limit bandwidth for {ip} (Windows):")
    print("🦴 True device-level leashes need admin rights or third-party tools. Puppy can only show you a demo!")
    print("🐕 Demo: Puppy will block all traffic to this IP via Windows Firewall (remove rule to unleash):")
    try:
        ps_command = f'''
        $ip="{ip}"
        Write-Host "Capping bandwidth is tricky in Windows without 3rd-party tools."
        Write-Host "As a demo, I'll block all traffic to $ip via Windows Firewall (remove rule to unblock):"
        New-NetFirewallRule -DisplayName "BlockIP_$ip" -Direction Outbound -RemoteAddress $ip -Action Block
        '''
        subprocess.run(["powershell", "-Command", ps_command], shell=True)
        print("🦴 Block rule applied! The puppy is standing guard (study/demo only)!")
    except Exception as e:
        print(f"😢 Puppy barked, but the firewall gate didn't close! (Failed: {e})")
    pause()

def unlimit_bandwidth_windows(ip):
    cute_print("unlimit")
    print(f"🐕 Puppy is removing the firewall leash for {ip} (Windows)...")
    try:
        ps_command = f'''
        $ip="{ip}"
        Remove-NetFirewallRule -DisplayName "BlockIP_$ip"
        '''
        subprocess.run(["powershell", "-Command", ps_command], shell=True)
        print("🦴 The leash is off! Firewall rule removed, and the puppy is happy!")
    except Exception as e:
        print(f"😢 Puppy couldn't remove the firewall leash! (Failed: {e})")
    pause()

def throttle_all_windows():
    cute_print("throttle")
    print("🐶 Puppy wants to give all Windows friends equal biscuits, but this needs third-party tools!")
    print("You can try demo firewall rules or check third-party suggestions.")
    print("See https://docs.microsoft.com/en-us/windows-server/networking/technologies/qos/qos-policy-management")
    pause()

def restore_network_windows():
    cute_print("restore")
    print("🐕 Restoring all network limits (Windows)... Puppy is fetching back normal settings!")
    try:
        ps_command = '''
        Get-NetFirewallRule | Where-Object {$_.DisplayName -like "BlockIP_*"} | Remove-NetFirewallRule
        '''
        subprocess.run(["powershell", "-Command", ps_command], shell=True)
        print("🦴 All 'BlockIP_' rules removed. Puppy is wagging its tail happily!")
    except Exception as e:
        print(f"😢 Puppy tried, but couldn't remove all the rules! (Failed: {e})")
    pause()

# =================== ADMIN/PHYSICAL ACCESS =================

def admin_access_demo():
    cute_print("admin")
    print("🐕 Woof! You have admin/root access! Puppy is SO impressed!")
    print("On Linux: You can set tc/iptables/netfilter QoS, see above.")
    print("On Windows: You can use PowerShell as Administrator for full NetAdapter control, Group Policy, or 3rd-party tools.")
    print("Please use with care! This is for study/lab use. Puppy trusts you with the treats!")
    pause()

def physical_access_demo():
    cute_print("physical")
    print("🐾 No admin? The puppy can always help you:")
    print("- Unplug/replug Ethernet/Wi-Fi cables for that device.")
    print("- Toggle Wi-Fi routers on/off (puppy likes buttons!).")
    print("- Change ports on a switch/router (sniff sniff).")
    print("Manual methods only, but sometimes, that's all you need to herd the network sheep!")
    pause()

def bark_alert():
    cute_print("bark")
    print("🐕 Bark bark! The puppy is on alert and watching over the network! 🐾")
    pause()
# =================== MAIN LOOP =================== 99

def puppy_ascii_start():
    print(ART_START)
    print("The puppy just woke up and is ready to help! ૮ • ﻌ - ა\n")

def puppy_ascii_end():
    print(ART_EXIT)
    print("The puppy is going to sleep now. Thank you for playing! ૮ฅ・ﻌ・აฅ\n")

def main_menu_loop():
    global os_target
    puppy_ascii_start()
    print(random_dog_kaomoji(), "Welcome to PuppyLimiter: the cutest bandwidth cap in the dog park!\n")
    # Select OS
    while True:
        print("Choose your operating system to manage bandwidth limits:")
        print("1. Linux (tc/iptables, sudo required)")
        print("2. Windows (PowerShell, firewall demo only)")
        print("Q. Quit")
        choice = input("> ").strip().lower()
        if choice == "1":
            os_target = "linux"
            break
        elif choice == "2":
            os_target = "windows"
            break
        elif choice == "q":
            puppy_ascii_end()
            return
        else:
            print("Please choose 1, 2, or Q!")

    while True:
        print("\nMenu – choose an action (bark = alert!)")
        print("1. Scan local network for devices")
        print("2. Limit a device's bandwidth")
        print("3. Unlimit a device's bandwidth")
        print("4. Throttle ALL bandwidth")
        print("5. Restore all network limits")
        print("6. Bark! (alert)")
        print("7. Study: Admin access tips")
        print("8. Study: Physical access tips")
        print("9. Monitor bandwidth (live)")
        print("Q. Quit")
        action = input("> ").strip().lower()

        if action == "1":
            scan_network()
        elif action == "2":
            ip = input("Device IP to limit: ").strip()
            cap = input("Limit to (Mbps, default 1): ").strip() or "1"
            if os_target == "linux":
                limit_bandwidth_linux(ip, int(cap))
            else:
                limit_bandwidth_windows(ip, int(cap))
        elif action == "3":
            ip = input("Device IP to unlimit: ").strip()
            if os_target == "linux":
                unlimit_bandwidth_linux(ip)
            else:
                unlimit_bandwidth_windows(ip)
        elif action == "4":
            if os_target == "linux":
                throttle_all_linux()
            else:
                throttle_all_windows()
        elif action == "5":
            if os_target == "linux":
                restore_network_linux()
            else:
                restore_network_windows()
        elif action == "6":
            bark_alert()
        elif action == "7":
            admin_access_demo()
        elif action == "8":
            physical_access_demo()
        elif action == "9":
            if os_target == "linux":
                monitor_bandwidth_linux()
            else:
                monitor_bandwidth_windows()
        elif action == "q":
            puppy_ascii_end()
            break
        else:
            print(random.choice([
                "Oops, paw slipped! Please choose a valid menu option.",
                "That wasn’t a real option, but the puppy still loves you!",
                "The puppy tilts its head in confusion. Try again!",
                "No treat for that input, but you get a tail wag!"
            ]))

if __name__ == "__main__":
    main_menu_loop()
