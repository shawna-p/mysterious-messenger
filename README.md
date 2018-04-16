# mysme-generator
A messenger program that mimics the layout of Mystic Messenger
This is an ongoing project intended to give me practice experimenting with the Ren'Py engine and its capabilities. 

## Getting Started

* If you want to run this code, you will need to download the Ren'Py engine: https://www.renpy.org/
* As of 2018-04-16 (the time of this writing) the version of Ren'Py used is 6.99.14.3
* In the Ren'Py launcher, start a new project. Go to the /game folder of the project you just created and place the provided .rpy files in there. Replace the existing screens.rpy options.rpy script.rpy and gui.rpy
* **The images and sound files used in this project are not included in the repository. Please contact me directly if you would like to request the assets.**


### Prerequisites

In your Ren'Py install folder (not the game, but the actual install folder -- it'll be named something like renpy-6.99.14.3-sdk), go to (Install Folder)/renpy/sl2 and find the file "slast.py" (*not* slast.pyo). Open that up in the editor of your choice (e.g. NotePad++) and scroll down to line 1427 or so, which says

```
    ctx.scope[variable] = v
```
Create a new line at the same indent level and type `index = id(v)`
The code from lines 1425 to 1430 or so should look something like the following:
```
    for index, v in enumerate(value):
    
      ctx.scope[variable] = v
      index = id(v)
      
      ctx.old_cache = oldcaches.get(index, None) or { }
```

### Getting the Program Running

If you've set up everything properly, from the Ren'Py Launcher you should be able to select the project you created from the column on the left and hit 'Launch'. If you don't have the images/sound files, you will likely run into a few "not found" errors until you've created your own replacements; otherwise, you should be able to go ahead and type in your desired name for the protagonist and check out the "Example Chatroom", which will walk you through some of the available features in the program.


## Built With

* [Ren'Py](https://www.renpy.org/) - The engine used


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

I'd like to thank the following people for their contribution to this project:
* pokemonxyeevee for contributing many of the assets used in the program
* Cheritz, for making the game that this program is inspired by
* The people of the Lemma Soft forums for many tutorials, answers, and resources
* Sakebobomb for giving me permission to use their art in this program
* [RenpyTom](https://github.com/renpytom) for assistance in fixing some of the errors and animation issues I ran into
