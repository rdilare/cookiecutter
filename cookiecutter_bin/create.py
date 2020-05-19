from cookiecutter.main import cookiecutter

from os import remove
from shutil import copy


for i in range(9):

	ec = {"bin_number":"bin"+str(i),"idx":i}
	cookiecutter(
	    '.',
	    no_input=True,
	    extra_context=ec
		)

	src_dir = "./textures/"
	dst_dir = "./bin%s/materials/textures/"%(i)
	img_name = "texture_(%s).png"%(i)
	copy(src_dir+img_name,dst_dir+img_name)