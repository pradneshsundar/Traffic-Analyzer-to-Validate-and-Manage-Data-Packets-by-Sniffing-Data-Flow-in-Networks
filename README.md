The project is developed mainly using python and Django. 

Python for building the models and Django for UI and Backend DataBase connectivity. 

You must have installed Anaconda Navigator on your system to execute these programs, kindly create a new Runtime environment on your Anaconda Navigator. 

Install the necessary python libraries in your environment The files named GNB.ipynb,ABC.ipynb,CBC.ipynb,DataLoading.ipynb,DataVisualization.ipynb are all coded in Jupyter Notebook hence these are normal python programs and can be run on Jupyter Notebook provided you have all the necessary Python libraries like pandas,seaborn,matplotlib,tensorflow,sklearn etc. 

The CBC.ipynb will take about 30 minutes to run so dont panic its what it is. once CBC.ipynb successfully completes it exports a pkl file named proj.pkl . 

You should locate this file on your system and move this file to your project directory(where all the code is stored) Its easy to find the location of this .pkl file , you can see this file on your Jupyter Notebook home page simply click on that .pkl file and it will show you the path . 

To run this complete project Launch the Visual Studio Code through your Anaconda Environment open the folder(location where the complete project resides) head to views.py file and paste the path of your .pkl file.

 Be Careful while pasting this path as you will be requiring to remove the double quotes, change the existing backward slash to forward slash. 

Finlly run the project by opening a new cmd prompt terminal inside the same VS Code launched throught Anaconda Navigator environment. 

type in the following code- python manage.py runserver on succesful run it will give a URL head to that URL and boom your project fires!!!!
