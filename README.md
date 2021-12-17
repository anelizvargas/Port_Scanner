# Port_Scanner
port scanner


Aneliz Vargas

README

List of files required included in my project:
You need Python script downloaded, as well as use of the command-line for the program. Within Python, I used a couple of extra packages, such as socket, sys, random and time. Additionally, I used pycharm to do command-line usage.

How to run:
In the command-line, you would put: 
“ port_scanner.py [-options] target_ip”
Your options are as follows:
- Order, where the ports are scanned in chronological order
- Random, where the ports are scanned in a random order
- All, all 65,535 ports are scanned
- Known, only some well known 20 ports are scanned

From there, the code should execute itself, and it will show which ports are open, how long it took to execute that command, and then tell you the number of open and closed ports. 

Discussion:
One major challenge that I had while doing this project was definitely having to do this project alone. In addition to that, I just had a great difficulty starting the project, mostly because I didn’t know where to start, but also because I had no partner to be there to help me get started. I guess I was just a bit confused on how a port scanner works, so I watched some Youtube videos that helped me understand. I also used one port scanner code as a base for my project, and in the end, mine looked absolutely different than what I started with. Overall, I believe I overcame this difficulty by using my resources. Unfortunately, I started seriously working on this project a little later than most people, so I didn’t get the chance to go to office hours or TA hours to receive help. However, I think I still managed to do this project in the end, and I am proud of that accomplishment. 

Another quick note! I never figured out how to do the dig glasgow.smith.edu thing so I don't actually know the IP address of that. Therefore I wasn't actually able to test my code. However, I do believe it should work. Another issue I actually had was with the command line usage, but luckily I figured out how to use sys. Lastly, I wasn't sure if we were supposed to be able to scan using two of the options, like scanning with both random and known options, so I only allow one option at a single time. 
