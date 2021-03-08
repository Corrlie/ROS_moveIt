# ROS_moveIt

ROS distribution: ROS Noetic.
OS: Linux Ubuntu 20.04.1 LTS on Oracle VM VirtualBox 

ROS project - moving panda robot to predefined positions - using Python and moveIt package. It is visualized in RViz environment.

The repo excludes all ROS files (launch files etc.).

Running the python file via terminal command "python3 ros_moveit_isa_project.py". After this command terminal looks like on the image below:

![terminal](https://user-images.githubusercontent.com/63510085/110304267-aa8fc600-7ffb-11eb-8bfd-ebd2cfd1734f.png)

All prompts are in the Polish language and are translated below.
In the terminal there are displayed current joints positions (pol. "Aktualne ustawienie przegubow"), title of the project and short menu. There are three options in the menu: 1. Movement to default configuration (pol. "Ruch do konfiguracji domyslnej"); 2. Movement to predefined configuration (pol. "Ruch do zdefiniowanej konfiguracji"); 3. Close the program (pol. "Zakoncz program"). Below the menu there is request to choose the option (pol. "Wybierz opcje: ").

Choosing the first option of menu:
![option1_menu](https://user-images.githubusercontent.com/63510085/110305217-cba4e680-7ffc-11eb-9b80-7dfd0c2030e1.png)
There is a prompt about chosen option - to default configuration (pol. "Wybrano ruch do konfiguracji domyslnej"). Then "Be patient, the movement is being performed" prompt (pol. "Cierpliwosci... trwa ruch do domyslnej konfiguracji"). In the RViz environment One can see that robot is performing chosen movement at the moment. 
After that there is also the list of joints positions after the movement (pol. "Stan po ruchu: "). In the end there is the text that movement was finished (pol. "Ruch zakonczony") and about going back to the menu (pol. "Powrot do menu"). Image below shows how the robot looks after performing the movement (while there is prompt about ongoing movement in the terminal).
![option1_robot](https://user-images.githubusercontent.com/63510085/110305247-d6f81200-7ffc-11eb-9017-b421379e8289.png)


Choosing the second option of menu - prompts analogous to the prompts from the first option of the menu:
![option2_menu](https://user-images.githubusercontent.com/63510085/110305312-eb3c0f00-7ffc-11eb-8712-a3cce9ea78e6.png)
![option2_robot](https://user-images.githubusercontent.com/63510085/110305422-f42ce080-7ffc-11eb-95ae-c09a3c2b4e00.png)

Choosing the third option of menu:
![option3_menu](https://user-images.githubusercontent.com/63510085/110305489-06a71a00-7ffd-11eb-9b39-3b6473002c3a.png)

Third option closes the program.


