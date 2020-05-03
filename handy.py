import os
os.system("clear")
os.system("tput setaf 1")
print(" Hey Fellas DOCKER HANDY TOOL is here to assist you in Docker Container applications, even if you are a newbie to this technology")
os.system("tput setaf 2")
print(" ---------------------------------------------------------------------------------------------------------------------------------")
os.system("tput setaf 1")
print("Notice:- This program will work in RHEL/CENTOS version 8 only")
os.system("tput setaf 2")
print(" ------------------------------------------------------------------")
os.system("tput setaf 2")
print("You need to install Docker CE for RHEL 8.\nPress Y for confirmation\nPress N for if you have already installed ",end=' ')
ch=input()
if ch=='Y':
	print("please wait while we are installing all the dependencies")
	os.chdir("/etc/yum.repos.d")
	f=open("docker.repo","w+")
	f.write("[docker]\r\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\r\ngpgcheck=0\r\n")
	f.close()
	os.system("yum install docker-ce --nobest")
	os.system("systemctl enable docker")
	os.system("systemctl disable firewalld")
elif ch=='N':               

	while True:
		os.system("clear")
		print("Following are the list of services that I can help you at an ease:") 
		os.system("tput setaf 3")
		print("For launching a container on default network and driver i.e bridge with storage press 1")
		os.system("tput setaf 4")
		print("For showing running containers press 2")
		os.system("tput setaf 5")
		print("For deleting a running container press 3")
		os.system("tput setaf 6")
		print("For cleaning all running/stopped containers press 4")
		os.system("tput setaf 1")
		print("For creating your own image from a container press 5")
		os.system("tput setaf 2")
		print("For full inspection of a container press 6")
		os.system("tput setaf 3")
		print("For getting an IP address of a container press 7")
		os.system("tput setaf 4")	
		print("For launching a container on custom network,driver & a permanent storage press 8")
		os.system("tput setaf 5")		
		print("For saving an image from a running container press 9")
		os.system("tput setaf 1")
		print("For connecting two running containers press 10")
		os.system("tput setaf 2")
		print("For running the WORDPRESS web application on top of docker container press 11")
		os.system("tput setaf 3")
		print("For running the GHOST web application on top of docker container press 12")
		os.system("tput setaf 4")
		print("For stopping the GHOST web application press 13")
		os.system("tput setaf 5")
		print("For stopping the WORDPRESS web application press 14")
		os.system("tput setaf 1")
		print("For establishing a tunnel to generate a public url for your clients press 15")
		print("\n")
		os.system("systemctl disable firewalld")
		os.system("tput setaf 7")
		print("Type exit() to close the program")
		service=input("Input Here from above choices ")
		if int(service)==1:
			os.system("tput setaf 6") 
			print("Do you want to download an image from the docker hub or run a container from existing image?")
			st=input("Press 1 to download or press 2 to show list of existing images ")
			if int(st)==1:
				img=input("Please input the name of the image you want download from the docker hub registry ")
				version=input("Please input the version you want to provide ")
				os.system("docker pull {}:{}".format(img,version))
				os.system("docker images")
				
				k=input("Do you want to launch a container from any above image:version?Press y/N & For going back to main menu press 0 ")
				if k=='y':	
					contname=input("Container name given by you ")
					image=input("Your image name ")
					os.system("docker run -it --name {} {}:{} ".format(contname,image,version))
					next=input("Do you want to continue using more services? Press y/N ")				
					if next=='y':
						True
					else:
							break	
				elif k==0:
					True			
				
			elif int(st)==2:
				os.system("docker images")
				k=input("Do you want to launch a container from any above image:version?Press y/N ")
				print("for main menu press 0")
				if k=='y':	
					contname=input("Container name given by you ")
					image=input("Input The image name from the above list ")
					version=input("Input the version of the image ")
					os.system("docker run -it --name {}  {}:{} ".format(contname,image,version))
					next=input("Do you want to continue using more services? Press y/N ")				
	
					if next=='y':
						True
					else:
						break	
				elif int(k)==0:
					True
		
		elif int(service)==2:
			os.system("tput setaf 6")				
			os.system("docker ps")
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break
		elif int(service)==3:
			os.system("tput setaf 6")
			os.system("docker ps -a")
			contdel=input("Please give the name of the container you want to delete: ")
			os.system("docker rm -f {}".format(contdel) )
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break
						
		elif int(service)==4:
			os.system("tput setaf 6")
			os.system("docker rm -f $(docker ps -aq)")
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break
		
		elif int(service)==5:	
			os.system("tput setaf 6")
			imge=input("Please input the desired name of image you want to create ")
			version=input("Please input the desired version of the image ")
			os.system("docker ps -a")
			osname=input("Also provide the name from above listed containers from which you have to commit: ")
			os.system("docker commit {} {}:{}".format(osname,imge,version))
			os.system("docker images")
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break
			
		elif int(service)==6:
			os.system("tput setaf 6")
			os.system("docker ps -a")
			osname=input("Please provide the name of the container you want to inspect ")
			os.system("docker container inspect {}".format(osname))
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break
		elif int(service)==7:
			os.system("tput setaf 6")
			os.system("docker ps -a")	
			osname=input("Please provide the name of the container you want to inspect ")
			os.system("docker container inspect --format '{{ .NetworkSettings.IPAddress }}' {}".format(osname))
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break
		elif int(service)==8:
			os.system("tput setaf 6")
			env=input("Which container/environment you want to save and share? ")
			name=input("Please input the name you want to give to the environment: ")
			os.system("docker save {} {}.tar".format(env,name))
			next=input("Do you want to continue using more services? Press y/N")				
			if next=='y':
				True
			else:
				break
		
		elif int(service)==9:
			os.system("tput setaf 6")	
			os.system("docker network ls")
			netname=input("Input the network name of your container ")
			os.system("docker volume create apacheserver")
			os.system("docker rm -f apacheserver")
			os.system("docker run -dit --network {} -v apacheserver:/var/www/html  --name apacheserver centos ".format(netname))		
			os.system("docker exec apacheserver yum install httpd -y")
			os.system("docker exec apacheserver /usr/sbin/httpd")	
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break
				
		elif int(service)==10:
			os.system("tput setaf 6")	
			os.system("docker ps -a")
			cont=input("Which of the above listed container you want to link? ")		
			os.system("docker images")
			image=input("Which of the above images you want to use for container ")
			version=input("Please input the version of the image ")
			contname=input("What name you want to give to the container? ")
			os.system("docker network ls")
			net=input("On which of the existing networks you want to run the container ")
			os.system("docker run -it --network {} --name {} --link {} {}:{} ".format(net,contname,cont,image,version))
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break

	
		elif int(service)==11:
			os.system("tput setaf 2")			
			print("Please wait while we are installing the dependencies...")
			os.system("docker pull wordpress:5.1.1-php7.3-apache")
			os.system("docker pull mysql:5.7")					
			os.system("mkdir wordpress_infrastructure")			
			os.system("git init")
			os.system("git clone https://github.com/Moonwalkerr/wordpress_in_container")
			os.chdir("wordpress_in_container/")
			os.system("docker-compose up")
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break	
		elif int(service)==12:
			os.system("tput setaf 2")			
			print("Please wait while we are installing the dependencies...")
			os.system("docker pull ghost:1-alpine")
			os.system("docker pull mysql:5.7")					
			os.system("mkdir ghost_infrastructure")			
			os.system("git init")
			os.system("git clone https://github.com/Moonwalkerr/ghost_webapp_in_container")
			os.chdir("ghost_webapp_in_container/")
			os.system("docker-compose up")
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break	
		elif int(service)==13:
			os.chdir("ghost_webapp_in_container/")
			os.system("docker-compose stop")		
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break
		elif int(service)==14:
			os.chdir("wordpress_in_container/")
			os.system("docker-compose stop")
			next=input("Do you want to continue using more services? Press y/N ")				
			if next=='y':
				True
			else:
				break	
		elif int(service)==15:			
			os.system("yum install ngrok-stable-linux-amd64.zip -y")
			os.system("unzip ngrok-stable-linux-amd64.zip ")	
			print("To set a Tunnel for Ghost web application press 1 ")
			print("To set a Tunnel for Wordpress web application press 2 ")
			print("To set a Tunnel for another port number application press 3 ")
			ip=input()
			if int(ip)==1:
				os.system("tput setaf 1")
				os.system("./ngrok http 8080")
				print("By using the url given in front of forwarding can be given to any of your clients across the internet to get access to your web app ghost!")					
				next=input("Do you want to continue using more services? Press y/N ")				
				if next=='y':
					True
				else:
					break

			elif int(ip)==2:
				os.system("./ngrok http 8081")
				os.system("tput setaf 1")
				print("By using the url given in front of forwarding can be given to any of your clients across the internet to get access to your web app Wordpress!")					
				next=input("Do you want to continue using more services? Press y/N ")				
				if next=='y':
					True
				else:
					break
			elif int(ip)==3:
				port=input("Please input the port number ")
				protocol=input("Please input the protocol ")
				os.system("tput setaf 1")
				os.system("./ngrok {1} {0}".format(port,protocol))
				print("By using the url given in front of forwarding can be given to any of your clients across the internet to get access to your web app ghost!")
				next=input("Do you want to continue using more services? Press y/N ")				
				if next=='y':
					True
				else:
					break					
			else:	
				print("Sorry invalid input!")
				next=input("Do you want to continue using more services? Press y/N ")				
				if next=='y':
					True
				else:
					break			




	exit()
