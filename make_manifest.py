#!/usr/bin/env python
import hashlib
import json
import os
import shutil
import sys

def main():
	try:
		server_path, input_dir, output_dir = sys.argv[1:4]
	except ValueError:
		print "usage: {} server_path input_dir output_dir".format(sys.argv[0])
		sys.exit(1)

	manifest = {}
	for root, dirs, files in os.walk(input_dir):
		for index, dir_ in enumerate(dirs):
			# TODO honour .forgeignore?
			if dir_ in ('.hg', '.git'):
				del dirs[index]

		for file_ in files:
			full_path = os.path.join(root, file_)
			relative_path = os.path.relpath(full_path, input_dir)
			with open(full_path) as in_file:
				hash_ = hashlib.sha1()
				while True:
					buf = in_file.read(0x100000)
					if not buf:
						break
					hash_.update(buf)
			hash_value = hash_.hexdigest()

			shutil.copyfile(full_path, os.path.join(output_dir, hash_value))
			manifest[relative_path] = server_path + hash_value
			print "copied", full_path, "to", os.path.join(output_dir, hash_value)

	manifest_str = json.dumps(manifest, indent=4)
	manifest_hash = hashlib.sha1(manifest_str).hexdigest()

	with open(os.path.join(output_dir, manifest_hash), "w") as manifest_file:
		manifest_file.write(manifest_str)
	print "created", os.path.join(output_dir, manifest_hash)

if __name__ == '__main__':
	main()
