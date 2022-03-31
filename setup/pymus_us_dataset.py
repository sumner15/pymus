import os
import logging
import tools.pymus_utils as pymusutil
import setup.pymus_us_probe as pymusprob
import setup.pymus_us_sequence as pyseq
import numpy as np
import datetime as dt
import h5py

logging.basicConfig(level=logging.DEBUG)

S_TODAY=dt.datetime.now().date().strftime("%Y%m%d")

class IncompatibleDatasetSettings(Exception):
	pass 

class UsDataSet(object):
	''' Ultrasound Dataset object
		probe 	    : probe setting used
		sequence    : illumination sequence
		data        : element output data
		num_samples : number of echo samples in time domain
		sound_speed : sound velocity '''
	def __init__(self,name,probe,sequence):
		self.name=name
		self.date=S_TODAY
		self.probe=probe
		self.sequence = sequence
		self.data=np.array([[],[],[],[]])
		self.num_samples = 0
		self.sound_speed=1500.

	def match(self,data_array):
		n_ang = 2
		n_el = 0
		n_sampl = 0
		if len(data_array.shape) == 2:
			n_ang = 1
			n_el, n_sampl = data_array.shape
		else:
			n_ang, n_el, n_sampl = data_array.shape
		s_ang = len(self.sequence.angles)
		p_el = self.probe.num_channels
		if n_ang != s_ang:
			raise IncompatibleDatasetSettings(" Dataset has %s angles and sequence has %s " % (n_ang,s_ang))
		if n_el != p_el:
			raise IncompatibleDatasetSettings(" Dataset has %s channels, probe has %s " % (n_el,p_el))
		self.data = data_array
		self.num_samples = n_sampl

	def set_data(self,data):
		try:
			self.match(data)
		except IncompatibleDatasetSettings as e:
			logging.error(" Incompatible settings: %s " % e)
			return 1
		return 0

	def __str__(self):
		res = ( "US dataset - {nm} {t0} "
				" {prb} - {seq} - data -> {dt} "
			).format(nm=self.name,t0=self.date,prb=str(self.probe),seq=str(self.sequence),dt=str(self.data.shape))
		return res

	def read_file(self,filename,prefix):
		data_from_file = {'data/real' : None,'sound_speed' : None}
		res = pymusutil.generic_hdf5_read(filename,prefix,data_from_file)
		if data_from_file['data/real'] is None:
			logging.error("data not found in %s:%s " % (filename,prefix))
		else:
			r = self.set_data(data_from_file['data/real'][:])
		if data_from_file['sound_speed'] is None:
			logging.error("sound speed data not found in %s:%s " % (filename,prefix))
		else:
			self.sound_speed = data_from_file['sound_speed'][0]	

	def write_file(self,filename,prefix,overwrite=False):
		data_to_write = { 'data/real'   : self.data,
						  'sound_speed' : self.sound_speed }
		pymusutil.generic_hdf5_write(filename,prefix,overwrite,data_to_write)

def ImportFromCreatis(nbPW=3,pht="in_vitro_type1",format="rf",scheme="1"):
	f_name = "dataset_%s_%s_transmission_%s_nbPW_%s.hdf5" % (format,pht,scheme,nbPW)
	pymusutil.download_dataset(f_name,pymusutil.TO_DATA_TMP)
	probe = pymusprob.UsProbe()
	probe.read_file(pymusutil.TO_DATA_TMP + f_name,"US/US_DATASET0000/","probe_") 
	seq = pyseq.UsPWSequence()
	seq.read_file(pymusutil.TO_DATA_TMP + f_name,"US/US_DATASET0000/",caps_prf=True) 
	dset = UsDataSet("dataset_%s_pw" % nbPW,probe,seq)
	dset.read_file(pymusutil.TO_DATA_TMP + f_name,"US/US_DATASET0000/")
	dset.write_file(pymusutil.TO_DATA + "echo/%s_nb_pw_%s.hdf5" % (pht,nbPW),pht)