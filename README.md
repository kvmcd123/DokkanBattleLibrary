# DokkanBattleLibrary
This repo allows users to import their entire Dokkan Battle Library from pictures into a json file with the card id, title and subtitle. 

## Download Database of Images:
The (most recent) collection of dokkan thumbnail assets can be found at
https://drive.google.com/file/d/1S2PKE_XEqhTnccEcyJL8YDt5keTpjn44/view?usp=drive_link

## Installing DokkanLibrary
DokkanLibrary was designed using Python 3.11.9 and Anaconda. 

First, clone/download the repository.

If you do not have an existing Anaconda installation, go to https://www.anaconda.com/products/individual, click on skip registration, and then click the green download button.

In the windows search bar, type and select Anaconda Prompt. Open the prompt and navigate to `DokkanLibrary/Conda Environment Setup` using `cd` commands. This is where the enviroment `.yml` file is currently stored. Once in the directory run the following command:
``` shell
conda env create -f environment.yml
```
This creates the Python environment named `DokkanLibrary`, with all the packages needed to run the software.

 To activate the environment, run:
``` shell
conda activate DokkanLibrary
```

## Step 1: Taking Pictures in App
In order to import your library, you must take images of your Card list. 

In `Dragon Ball Z: Dokkan Battle` go to 
` Team -> Character List` and take pictures containing 5 complete rows of cards, as shown below
![Alt text](imgs/takingPicture.png?raw=true "Title")



![Alt text](imgs/splitCards.png?raw=true "Title")
![Alt text](imgs/identifyCards.png?raw=true "Title")