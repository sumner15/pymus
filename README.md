# PYMUS

A python package for medical ultrasound imaging 

Load experimental setup (probe details, sequence, scanning region) and compute imaging in Plane Wave Compounding mode. See the [wiki](https://github.com/pgarapon/pymus/wiki/Python-in-medical-ultrasounds---wiki)

## You will need:

You will need a distribution of Python (v 3.5+) and several classic python packages, that most likely come with the distribution of Python, or can be easily installed with Pip Install Packages `pip` see [here](https://pip.pypa.io/en/stable/installing/). 

* [Python 3.5+](https://www.python.org/) - A python distribution ([Anaconda](https://www.anaconda.com/download/) comes with the conda package facility and is highly recommended)
* [numpy](http://www.numpy.org/) The classic array library. 
* [scipy](https://www.scipy.org/) Not less classic scientific computation library. 
* [matplotlib](https://matplotlib.org/) A Python plotting/charting library. 
* [click](http://click.pocoo.org/) A powerful command line utility
* [h5py](http://www.h5py.org/) For file I/O we use the hdf5 format

You'll usually want to set up a conda environment, e.g. 
```
conda create --name [env_name] python==3.7
conca activate [env_name]
```

Then, you'll install the packages listed above. Depending on your system, the install should be as easy as:
```
pip install numpy scipy matplotlib click h5py
```

## Installing the pymus modules

Download the repo to a location of your choice `/Users/YourSelf/projects/pymus`. 

In order for python to have access to different modules at startup, one convenient solution is to create a `pymus.pth` file that would be located at a location of the style:
```
/Users/sumner/opt/anaconda3/envs/pymus/lib/python3.7/site-packages/pymus.pth

```
To find out about your specific prefix (`/Users/YourSelf/miniconda2/`), run `python` and then `import sys` and then `sys.prefix`. You'll usually need to append the returned path with [...]`/lib/python3.7/site-packages/`

The `pymus.pth` file should have just one line that is the absolute path to your `pymus` directory. Once you've done this, the command line should return something like:  
```bash
(pymus) sumner@Galileo % cat /path/to/pymus.pth
/Users/sumner/code/pymus
```

### Windows
TBD. Right now, Windows is not supported, and at the very least, the pathing tools will almost certainly fail. User beware. 


## Building an image

The following test should run a Plane-Wave simplified beamforming and display an echogeinicity of a phantom image. 
``` 
python experiment/test_pymus.py
```

## Documentation 

## Authors

* **Pierre Garapon** - *Initial work* - [pgarapon](https://github.com/pgarapon)
* **Sumner Norman** - *Updates 2022+* - [sumner15](https://github.com/sumner15/)

This project is based on porting to python the matlab project [Picmus](https://www.creatis.insa-lyon.fr/Challenge/IEEE_IUS_2016/home). The Plane Wave Imaging Challenge in Medical UltraSound. See the following paper:

Liebgott, H., Rodriguez-Molares, A., Jensen, J.A., Bernard, O., "Plane-Wave Imaging Challenge in Medical Ultrasound", in IEEE International Ultrasonics Symposium, Tours, France., 2016, p. accepted

See also the list of [contributors](https://github.com/pymus/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The Medical ultrasound community and the folks at INSA Lyon for exposing some datasets. [Creatis](https://www.creatis.insa-lyon.fr/site7/fr)
* The Python community for an ever growing suite of efficient tools. 

