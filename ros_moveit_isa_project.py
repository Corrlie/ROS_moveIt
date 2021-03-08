import rospy
import sys
import moveit_commander as moveit_namespace  # moveit_commander - namespace to use moveit interfaces
import moveit_msgs.msg
from math import pi

class ROS_isa_moveit_project:
	def __init__(self):
		moveit_namespace.roscpp_initialize(sys.argv)
		robot_info = moveit_namespace.RobotCommander() # kinematic and states
		scene_perception= moveit_namespace.PlanningSceneInterface()
		robot_name = "panda_arm"
		move_robot = moveit_namespace.MoveGroupCommander(robot_name) # planning for panda robot
		self.robot_info = robot_info
		self.scene_perception = scene_perception
		self.robot_name = robot_name
		self.move_robot = move_robot     
		print('Aktualne ustawienie przegubow:') # current joints position
		print(self.move_robot.get_current_joint_values()) # current joints position

	def go_default(self): # go to default configuration
		def_swivel = self.move_robot.get_current_joint_values()
        # positions of newly spawned robot in environment:
		def_swivel[0] = 0 
		def_swivel[1] = -0.785
		def_swivel[2] = 0
		def_swivel[3] = -2.356
		def_swivel[4] = 0
		def_swivel[5] = 1.571
		def_swivel[6] = 0.785
		self.move_robot.go(def_swivel, wait=True)
		self.move_robot.stop()
		current_pos_def_swiv = self.move_robot.get_current_joint_values()
		print('Stan po ruchu: \n') # position after the movement
		print(current_pos_def_swiv)
       
	def go_predefined(self): # go to predefined exemplary configuration
		swivel = self.move_robot.get_current_joint_values()
        # predefined exemplary positions:
		swivel[0] = -pi/6
		swivel[1] = -pi/6
		swivel[2] = -pi/6
		swivel[3] = -pi/2
		swivel[4] = -pi/6
		swivel[5] = pi/4
		swivel[6] = -pi/6
	       
		self.move_robot.go(swivel, wait=True) # planning
		self.move_robot.stop()
		
		current_pos_swiv = self.move_robot.get_current_joint_values()
		print('Stan po ruchu: \n') # Position after the movement
		print(current_pos_swiv)
        
def menu_fun(move_it_obj):
	print("------------------------MENU------------------------")
	print("1. Ruch do konfiguracji domyslnej") # movement to default configuration
	print("2. Ruch do zdefiniowanej konfiguracji") # movement to predefined configuration
	print("3. Zakoncz program") # close program
	option_menu = int(input("Wybierz opcje: ")) # choose menu option
	while option_menu!=0:
		if option_menu == 1: 
			print("Wybrano ruch do konfiguracji domyslnej") # "movement to default configuration was chosen" prompt
			print("...")
			print("Cierplowosci... trwa ruch do domyslnej konfiguracji...") # "Be patient, the movement is being performed" prompt
			move_it_obj.go_default()
			print("Ruch zakonczony") # "Finished movement" prompt
			print("\nPowrot do menu...\n\n") # "Going back to the menu" prompt
		elif option_menu == 2:
			print("Wybrano ruch do zdefiniowanej konfiguracji")
			print("...")
			print("Cierplowosci... trwa ruch do zdefiniowanej konfiguracji...")
			move_it_obj.go_predefined()
			print("Ruch zakonczony")
			print("\nPowrot do menu...\n\n")
		elif option_menu == 3:
			print("Trwa zamykanie programu...") # closing the program
			exit()
		break
def main():
	moveit_robot_ex = ROS_isa_moveit_project()
	print("Hello")
	print('===============ISA - project ROS Moveit=============')
	print("----------------------------------------------------")
	while True:
		menu_fun(moveit_robot_ex)
		
if __name__ == "__main__":
	main()
