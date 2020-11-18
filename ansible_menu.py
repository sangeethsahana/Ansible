def ansible():

	import os
	
	os.system("tput setaf 3")
	print("\t\t\tWelcome to Ansible menu!!")
	os.system("tput setaf 7")
	print("\t\t\t---------------------")

	while True:
		os.system("clear")
		
		print("""
		\n
		Press 1 : To install Ansible
		Press 2 : To check the version of Ansible
		Press 3 : To create a file and provide your target node details
		Press 4 : To make a ansible directory.. if directory already exits go to option 5
		Press 5 : To create an Inventory and update your file in the inventory
		Press 6 : To install sshpass
		Press 7 : To check connectivity with Target nodes and the list of hosts
		Press 8 : To install httpd service using ansible
		Press 9 : To create a web page 
		Press 10 : To copy your source web page to the target node using ansible
		Press 11 : To execute the httpd service using ansible 
		Press 12 : To take a look at your webpage
		Press 13: Exit
		""")

		ch = input("Enter ur choice:")
		print(ch)
		if int(ch)==1:
			os.system("pip3 install ansible")
			print("ansible installed successfully!!")
		elif int(ch)==2:
			os.system("ansible --version")
			print()
		elif int(ch)==3:
			os.chdir('/root')
			a=input("Press 'i' to create a file and pls follow this format: <target node IP> ansible_user = <username>  ansible_ssh_pass = <password>  ansible_connection = ssh")
			if(a=="i"):
				os.system("vim ip.txt")
				print("You have entered:")
				os.system("cat /root/ip.txt")
				print("File created!!")
			else: 
				print("Going back to ansible menu..")
				os.system("python3 ansible_menu.py")
				break
		elif int(ch)==4:
			
			os.system("mkdir /etc/ansible")
		elif int(ch)==5:
			os.system('echo -e "[defaults]" > /etc/ansible/ansible.cfg')
			os.system('echo -e "\ninventory = /root/ip.txt" >> /etc/ansible/ansible.cfg')
			os.system('echo -e "host_key_checking=false" >> /etc/ansible/ansible.cfg')
			print("Your inventory has been updated!!!")
			
		elif int(ch)==6:
			os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
			os.system("yum install sshpass")
			print("sshpass successfully installed")
		elif int(ch)==7:
			os.system("ansible all -m ping")
			os.system("ansible all --list-hosts")
		elif int(ch)==8:
			os.system('ansible all -m package -a "name=httpd state=present"')
			print("httpd successfully installed in target node")
		elif int(ch)==9:
			os.system("gedit web.html")
		elif int(ch)==10:
			os.system('ansible all -m copy -a "src=web.html dest=/var/www/html"')
			print("file copied to destination folder in target node")
		elif int(ch)==11:
			os.system('ansible all -m service -a "name=httpd state=started"') 
			print("Success! Service has been executed..")
		elif int(ch)==12:
			ip=input("Enter your target node IP")
			os.system('ssh -X {} firefox http://{}/web.html'.format(ip, ip))
		elif int(ch)==13:
			exit()
		else:
			print("not supported")
		input("\nplz enter to continue...")
		
ansible()
		


		

		











