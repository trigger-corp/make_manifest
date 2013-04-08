make_manifest
=============

A script for creating a Reload manifest. Use this as part of the `process to Reload your app with content hosted on a CDN such as Rackspace Cloud Files <http://current-docs.trigger.io/tools/reload.html#reloading-app-content-from-rackspace-cloud-files-or-other-cdn>`_.

Tested with python 2.7

Description
------------

To push a Reload with your app content hosted on a CDN, Trigger.io requires you to have a manifest file which contains meta-data about the files being Reloaded. It associates the file name in your app's `src` directory with a url where the version that you are pushing with Reload is hosted

This script copies your app files to the destination directory renaming them to the hash value. It then creates the manifest file in the same directory and you must upload both the manifest and the renamed files to your CDN at the `server_path` that you specify.


Usage
-----

The script creates a manifest file and copies your app files in the destination directory. The app files are renamed with a hash. You must upload the manifest and the renamed files to your CDN.

   * `python make_manifest.py <server_path> <input_dir> <output_dir>`
   * `server_path` is the url root where your files will be hosted on your CDN
   * `input dir` is the directory containing your app files, usually the `src` subdirectory of your app
   * `output_dir` is the directory you create where the files that you need to upload to the CDN will be generated

Example: 

   python make_manifest.py http://7bda29eaef66b400b7a3-f7a161a32968fd6c090a7ab168500005.r25.cf2.rackcdn.com/ ~/forge-workspace/reload-cloud-files/src ~/forge-workspace/reload-cloud-files/manifest/
	   copied /Users/amirnathoo/forge-workspace/reload-cloud-files/src/config.json to /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/0dc3ebc12e894c77a248a4e5b34e594d9d4493d1
	   copied /Users/amirnathoo/forge-workspace/reload-cloud-files/src/identity.json to /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/80b89540b38441826a6cfae9a1bb3f727f3c702f
	   copied /Users/amirnathoo/forge-workspace/reload-cloud-files/src/index.html to /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/9342ed85c5de32489553002fe15910479cd753aa
	   copied /Users/amirnathoo/forge-workspace/reload-cloud-files/src/css/lungo.css to /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/f5a72b1a010ba40e3bd3920cb0e71e40fbb3ebdf
	   copied /Users/amirnathoo/forge-workspace/reload-cloud-files/src/css/theme.lungo.css to /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/7ee4fada00a6a68c0bb6e53917d9e5a78a23c520
	   copied /Users/amirnathoo/forge-workspace/reload-cloud-files/src/js/jquery-1.7.1.min.js to /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/9eb9ac595e9b5544e2dc79fff7cd2d0b4b5ef71f
	   copied /Users/amirnathoo/forge-workspace/reload-cloud-files/src/js/lungo.js to /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/d73361abf6c7f214bcbf5baaf254a5d1a16a41a4
	   copied /Users/amirnathoo/forge-workspace/reload-cloud-files/src/js/quo.js to /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/15a0a9b20a886a6dfb82b802b15e757dec0bf401
	   copied /Users/amirnathoo/forge-workspace/reload-cloud-files/src/videos/forge.mp4 to /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/8346fe14d556f7b41d3d73aa5c8369e70a3fc48f
	   copied /Users/amirnathoo/forge-workspace/reload-cloud-files/src/videos/reload.mp4 to /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/29e5b4322dcc8e8bb7cddbf8fe68ee0a6edbb256
	   created /Users/amirnathoo/forge-workspace/reload-cloud-files/manifest/6ea4aabd307ab05391d02aa4380ecc3bcccd4802