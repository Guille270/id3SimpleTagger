# ID3 tag script
A simple command line mp3 album tagger


## Getting started
This script was coded because the Toyota Prius + multimedia system is so advanced that can't works with folders in USB media. The right way to work with "folders" is have all songs tagged correctly. But there are a few songs that aren't tagged correctly. And you must go song by song changing the album tag. You can use a tag editor too, but you have to install a software and you have to learn how it works. So, now I have created this python script that alloes change the album metadata in a few seconds. I'm so sure that there are a lot of better software but i did it for me, but i think that maybe any person would want to use it too.

### Prerequisites
You need to install:

* Python 2.7
* [Mutagen library]
````` 
pip install mutagen
`````

## Examples of use

#### To change the album metadata of all folder.

First you need to create a folder like you do it normally in a computer, smartphone... 


To start the script. You can double click to start script too.
``````
python id3SimpleTagger.py

``````

The script will asks you name of folder, and when he ends to edit metadata script wll close automatically.
`````
EN: Write the name of the folder / ES: Escribe el nombre de la carpeta   **Folder Name**
`````

#### In next version I will make an exe to make it easier to use it
