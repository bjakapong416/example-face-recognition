# Resnet-Extract-Image-Feature-Pytorch-Python
Extract image features. A script inspired by the blog post: https://becominghuman.ai/extract-a-feature-vector-for-any-image-with-pytorch-9717561d1d4c

Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the main branch. ::


    # clone the repository
    $ git clone https://github.com/bjakapong416/Feature_extraction_image.git
    $ cd Feature_extraction_image
    
    
Create a virtualenv and activate it (for Windows)::

    $ python -m pip install --upgrade pip
    $ pip install virtualenv
    $ virtualenv venv
    $ source .venv\Scripts\activate

or 
Create a virtualenv and activate it (for Ubuntu/Linux)::

    $ python3 -m pip install --upgrade pip
    $ pip install virtualenv 
    $ python3 -m venv venv
    $ source .venv/bin/activate

How to Run
----------

Install Package::
    $ python -m pip install -r requirements.txt

## Usage

* Requires Pytorch

* `image_feature = get_vector(path_to_image="path/image")`

Run::

    $ python extract_image_feature.py
        

