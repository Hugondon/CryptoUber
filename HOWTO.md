## Compilation process How-to (Python)
The RideSharing App is majorly developed in Python. However, additional technologies such as Solidity and Ganache are used to set up the Ethereum environment for the transactions. 

---

### Prerequisites
- Previous installation of Python and a programming environment (ex. VS Code)
	https://code.visualstudio.com/download
	![image](https://user-images.githubusercontent.com/36273088/173963168-464171f9-7205-4d5b-ab98-02f9fc14211e.png)
	
- Previous installation of Ganache Blockchain environment
	https://trufflesuite.com/ganache/
	![image](https://user-images.githubusercontent.com/36273088/173965624-5a1e150e-790d-4216-8049-95d1b5a1a290.png)
	
- Previous installation of Build Tools for Visual Studio
	https://visualstudio.microsoft.com/downloads/  
	![image](https://user-images.githubusercontent.com/36273088/173972615-41942360-769e-4c68-84f1-adaed7985602.png)

---

### Installation
1. Download all the files in this repository
2. Open terminal CMD
3. Verify Python is installed 
	>python --version
	>![image](https://user-images.githubusercontent.com/36273088/173969410-b2ad3071-2d0d-4e0e-9ca2-8f331889ad7c.png)

4. Go to the path to which the files were downloaded by typing
	>cd PATH 
	>
	>Example: "cd C:\Users\student\Documents\ITESM\CryptoProject\RideSharing-main\"
	>
	>![image](https://user-images.githubusercontent.com/36273088/173969897-059f05e1-99c5-4932-b146-44bd08043894.png)

5. Create and run a virtual environment to run the app
	>py -3 -m venv CryptoProject
	>
	>CryptoProject\Scripts\activate
	>
	>![image](https://user-images.githubusercontent.com/36273088/173971589-822bb081-e7ad-4c55-8c33-fb89ad8d7fe1.png)

8. Install required libraries by typing
	>pip install -r requirements.txt
	>
	>![image](https://user-images.githubusercontent.com/36273088/173971645-900d3947-6a59-4d34-a475-d02ba3adc875.png)
	
6. Verify the installation by typing
	>pip freeze 
	>
	>![image](https://user-images.githubusercontent.com/36273088/173971907-5b5a8f55-0c61-4ecf-83f7-ff3bf7c106fd.png)

7. Check if the installed dependencies match the requirements.txt file
	>![image](https://user-images.githubusercontent.com/36273088/173972759-1a478536-d149-4c63-a7b6-23ef5ab641d2.png)

9. Run the file by typing
	>python "RideSharing.py" 
	>![image](https://user-images.githubusercontent.com/36273088/173973085-7bdef341-873d-4a3b-8c5b-d6a862112e30.png)

## The Graphical User Interface will then start.
![image](https://user-images.githubusercontent.com/36273088/173973255-c1e7a533-2e19-4540-8f07-88d582b30fff.png)

---

## IMPORTANT NOTE -
The app will only run properly if a Ganache Workspace has already been created and is running alongside the app.
To create a new workspace: 
1. Open Ganache and click on New Workspace
	>![image](https://user-images.githubusercontent.com/36273088/173965514-3fbb904c-396f-458a-8b2f-74532924da16.png)

2. Give a name to the workspace 
	>![image](https://user-images.githubusercontent.com/36273088/173973598-b89c345d-ff25-4095-a55e-b3b6e733e077.png)

3. Click on the "Save Workspace" Button

## Ganache will be up and running 
![image](https://user-images.githubusercontent.com/36273088/173965624-5a1e150e-790d-4216-8049-95d1b5a1a290.png)


