import rospy
import sys
import moveit_commander as moveit_namespace  # moveit_commander - namespace to use moveit interfaces
import moveit_msgs.msg
from math import pi

class ROS_isa_moveit_project:
	def __init__(self):
		moveit_namespace.roscpp_initialize(sys.argv)
		# rospy.init_node('move_group', anonymous=True)
		# args init mode: (name of node; anonymous=true - ensures node has unique name)
		robot_info = moveit_namespace.RobotCommander() # kinematic and states
		scene_perception= moveit_namespace.PlanningSceneInterface()
		robot_name = "panda_arm"
		move_robot = moveit_namespace.MoveGroupCommander(robot_name) # planning for panda robot
		self.robot_info = robot_info
		self.scene_perception = scene_perception
		self.robot_name = robot_name
		self.move_robot = move_robot     
		print('Aktualne ustawienie przegubow:')
		print(self.move_robot.get_current_joint_values())

	def go_default(self):
		def_swivel = self.move_robot.get_current_joint_values()
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
		print('Stan po ruchu: \n')
		print(current_pos_def_swiv)
       
	def go_predefined(self):
		swivel = self.move_robot.get_current_joint_values()
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
		print('Stan po ruchu: \n')
		print(current_pos_swiv)
def menu_fun(move_it_obj):
	
	print("------------------------MENU------------------------")
	print("1. Ruch do konfiguracji domyslnej")
	print("2. Ruch do zdefiniowanej konfiguracji")
	print("3. Zakoncz program")
	option_menu = int(input("Wybierz opcje: "))
	while option_menu!=0:
		if option_menu == 1:
			print("Wybrano ruch do konfiguracji domyslnej")
			print("...")
			print("Cierplowosci... trwa ruch do domyslnej konfiguracji...")
			move_it_obj.go_default()
			print("Ruch zakonczony")
			print("\nPowrot do menu...\n\n")
		elif option_menu == 2:
			print("Wybrano ruch do zdefiniowanej konfiguracji")
			print("...")
			print("Cierplowosci... trwa ruch do zdefiniowanej konfiguracji...")
			move_it_obj.go_predefined()
			print("Ruch zakonczony")
			print("\nPowrot do menu...\n\n")
		elif option_menu == 3:
			print("Trwa zamykanie programu...")
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
