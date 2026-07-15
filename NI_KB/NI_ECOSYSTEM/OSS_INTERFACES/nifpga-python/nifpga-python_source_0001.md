# NI OSS SOURCE SNAPSHOT: nifpga-python

<!--NI_OSS_SNAPSHOT repo=ni/nifpga-python commit=6a878b3c124af06e77f9d95cf7c5f8b4a57054d9 -->

<!--NI_OSS_SOURCE repo=nifpga-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=6fca2a789270c7665bb0e87ca376dd51330991c168833441face0ce796d5bdb9 bytes=644 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/nifpga-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `6fca2a789270c7665bb0e87ca376dd51330991c168833441face0ce796d5bdb9`
- bytes: 644

````markdown
[ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/nifpga-python/blob/master/CONTRIBUTING.md).

TODO: Check the above box with an 'x' indicating you've read and followed [CONTRIBUTING.md](https://github.com/ni/nifpga-python/blob/master/CONTRIBUTING.md).

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=nifpga-python path=.gitignore sha256=27dc312e2fcd9123a5347e8bf2269bc21d91a251e1b8a8978019f78fed085ea8 bytes=32 -->
## FILE: .gitignore

- repository: `ni/nifpga-python`
- source_path: `.gitignore`
- sha256: `27dc312e2fcd9123a5347e8bf2269bc21d91a251e1b8a8978019f78fed085ea8`
- bytes: 32

````text
*.pyc
.cache
.venv
*.egg-info
````

<!--NI_OSS_SOURCE repo=nifpga-python path=.travis.yml sha256=aafa655a29821c858317dd5296d37757dfe1f4b0cad4c2560045ded825772723 bytes=244 -->
## FILE: .travis.yml

- repository: `ni/nifpga-python`
- source_path: `.travis.yml`
- sha256: `aafa655a29821c858317dd5296d37757dfe1f4b0cad4c2560045ded825772723`
- bytes: 244

````yaml
language: python
python:
  - "2.7"
  - "3.4"
  - "3.5"
  - "3.6"
install:
  - "pip install flake8"
  - "pip install -r requirements.txt"
before_script:
  - "flake8 nifpga --ignore=E501,W503 "
script:
  - "nosetests --with-doctest"
````

<!--NI_OSS_SOURCE repo=nifpga-python path=CONTRIBUTING.md sha256=e71769b6d17c22c45d019d2df41e0d61ed80b9b378930e3f880d43c6d7f68907 bytes=2217 -->
## FILE: CONTRIBUTING.md

- repository: `ni/nifpga-python`
- source_path: `CONTRIBUTING.md`
- sha256: `e71769b6d17c22c45d019d2df41e0d61ed80b9b378930e3f880d43c6d7f68907`
- bytes: 2217

````markdown
# Contributing to nifpga-python

Contributions to nifpga-python are welcome from all!

nifpga-python is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](http://github.com/).

nifpga-python follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project, push a
branch with your changes to your project, and then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

# Testing

This project uses [Travis CI](https://travis-ci.org/ni/nifpga-python/).  Use it
to test your branch ahead of time and it will also be run on all pull-requests.

# Developer Certificate of Origin (DCO)

   Developer's Certificate of Origin 1.1

   By making a contribution to this project, I certify that:

   (a) The contribution was created in whole or in part by me and I
       have the right to submit it under the open source license
       indicated in the file; or

   (b) The contribution is based upon previous work that, to the best
       of my knowledge, is covered under an appropriate open source
       license and I have the right under that license to submit that
       work with modifications, whether created in whole or in part
       by me, under the same open source license (unless I am
       permitted to submit under a different license), as indicated
       in the file; or

   (c) The contribution was provided directly to me by some other
       person who certified (a), (b) or (c) and I have not modified
       it.

   (d) I understand and agree that this project and the contribution
       are public and that a record of the contribution (including all
       personal information I submit with it, including my sign-off) is
       maintained indefinitely and may be redistributed consistent with
       this project or the open source license(s) involved.

(taken from [developercertificate.org](http://developercertificate.org/))

See [LICENSE](https://github.com/ni/nifpga-python/blob/master/LICENSE)
for details about how nifpga-python is licensed.
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/api_reference.rst sha256=9fc713d67f73128ce82b8209cc2bcd1f1f7b5c58f0615e59f5c26e2b195eb7f7 bytes=301 -->
## FILE: docs/api_reference.rst

- repository: `ni/nifpga-python`
- source_path: `docs/api_reference.rst`
- sha256: `9fc713d67f73128ce82b8209cc2bcd1f1f7b5c58f0615e59f5c26e2b195eb7f7`
- bytes: 301

````rst
.. _api_references_page:

==============
API References
==============

.. toctree::
   :maxdepth: 4
   :caption: Table of Contents:

   api_references/session_ref
   api_references/register_ref
   api_references/array_register_ref
   api_references/fifo_ref
   api_references/status_ref
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/api_references/array_register_ref.rst sha256=7e1874f7a079e5f36d572b7be85d5f4f32d72a93c3d5aaadf337774be3e94ad8 bytes=248 -->
## FILE: docs/api_references/array_register_ref.rst

- repository: `ni/nifpga-python`
- source_path: `docs/api_references/array_register_ref.rst`
- sha256: `7e1874f7a079e5f36d572b7be85d5f4f32d72a93c3d5aaadf337774be3e94ad8`
- bytes: 248

````rst
.. _api_array_registers_page:

===============
Array Registers
===============

.. autoclass:: nifpga.session._ArrayRegister
    :members:
    :special-members: __len__
    :undoc-members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/api_references/fifo_ref.rst sha256=b5b916bba09f07c726c71c95a6ae196e44ad27580a2f29f295e531478a14501f bytes=143 -->
## FILE: docs/api_references/fifo_ref.rst

- repository: `ni/nifpga-python`
- source_path: `docs/api_references/fifo_ref.rst`
- sha256: `b5b916bba09f07c726c71c95a6ae196e44ad27580a2f29f295e531478a14501f`
- bytes: 143

````rst
.. _api_fifos_page:

=====
FIFOs
=====

.. autoclass:: nifpga.session._FIFO
    :members:
    :undoc-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/api_references/register_ref.rst sha256=4f43057096a8c0f733937be51b075d99da56ed439aebe4b9713dfa6d50457422 bytes=194 -->
## FILE: docs/api_references/register_ref.rst

- repository: `ni/nifpga-python`
- source_path: `docs/api_references/register_ref.rst`
- sha256: `4f43057096a8c0f733937be51b075d99da56ed439aebe4b9713dfa6d50457422`
- bytes: 194

````rst
.. _api_registers_page:

=========
Registers
=========

.. autoclass:: nifpga.session._Register
    :members:
    :special-members: __len__
    :undoc-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/api_references/session_ref.rst sha256=c048850ddc0dcc53b99143d152e27650b7bfc53aef387785c0a34f1c4f8822a2 bytes=163 -->
## FILE: docs/api_references/session_ref.rst

- repository: `ni/nifpga-python`
- source_path: `docs/api_references/session_ref.rst`
- sha256: `c048850ddc0dcc53b99143d152e27650b7bfc53aef387785c0a34f1c4f8822a2`
- bytes: 163

````rst
.. _api_sessions_page:

========
Sessions
========

.. autoclass:: nifpga.session.Session
    :special-members: __init__
    :members:
    :undoc-members:
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/api_references/status_ref.rst sha256=37d6a50655feca967b8cc73f6def1d57f7e32055314c826a4382d548cf6e7c6f bytes=326 -->
## FILE: docs/api_references/status_ref.rst

- repository: `ni/nifpga-python`
- source_path: `docs/api_references/status_ref.rst`
- sha256: `37d6a50655feca967b8cc73f6def1d57f7e32055314c826a4382d548cf6e7c6f`
- bytes: 326

````rst
.. _api_status_page:

======
Status
======

.. autoclass:: nifpga.status.Status
   :special-members: __init__, __str__
   :members:
   :show-inheritance:

.. autoclass:: nifpga.status.WarningStatus
   :members:
   :show-inheritance:

.. autoclass:: nifpga.status.ErrorStatus
   :members:
   :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/conf.py sha256=72f16af3b02a5f120542460a244af4bf6e123154a29663e02d3aa8fd5c35972f bytes=11089 -->
## FILE: docs/conf.py

- repository: `ni/nifpga-python`
- source_path: `docs/conf.py`
- sha256: `72f16af3b02a5f120542460a244af4bf6e123154a29663e02d3aa8fd5c35972f`
- bytes: 11089

````python
# -*- coding: utf-8 -*-
#
# NiFpga Example documentation build configuration file, created by
# sphinx-quickstart on Thu Dec 29 12:51:21 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'FPGA Interface Python API'
copyright = u'2017, National Instruments'
author = u'National Instruments'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#


def get_version():
    """
    Gets the version stored in the VERSION file updated by the build.

    Returns:
        str: The version stored in the packages VERSION file.
    """
    version = None
    script_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    script_dir = os.path.join(script_dir, 'nifpga')
    print script_dir
    with open(os.path.join(script_dir, "VERSION"), "r") as version_file:
        version = version_file.read().rstrip()
    return version


def get_short_version():
    """
    Gets the short version (X.Y) for this package.

    Returns:
        str: The short version of this package.
    """
    version = get_version()
    m = re.search(r"(^\d+\.\d+)", version)
    return m.groups(1)[0]


# The short X.Y version.
version = get_short_version()
# The full version, including alpha/beta/rc tags.
release = get_version()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = u'NiFpga Example v1.0.0'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
# html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'NiFpgaExampledoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NiFpgaExample.tex', u'NiFpga Example Documentation',
     u'National Instruments', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# It false, will not define \strong, \code, 	itleref, \crossref ... but only
# \sphinxstrong, ..., \sphinxtitleref, ... To help avoid clash with user added
# packages.
#
# latex_keep_old_macro_names = True

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'NiFpgaexample', u'NiFpga Example Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NiFpgaExample', u'NiFpga Example Documentation',
     author, 'NiFpgaExample', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/examples/basic_examples.rst sha256=2a07d9566002ec4d390bed8ce4e645ef047ddb8b697b9bcadb035dbd4437e26d bytes=6171 -->
## FILE: docs/examples/basic_examples.rst

- repository: `ni/nifpga-python`
- source_path: `docs/examples/basic_examples.rst`
- sha256: `2a07d9566002ec4d390bed8ce4e645ef047ddb8b697b9bcadb035dbd4437e26d`
- bytes: 6171

````rst
.. _basic_examples_page:

==============
Basic Examples
==============

Opening a Session
-----------------
The FPGA Interface Python API is session based. LabVIEW FPGA will generate bitfiles (.lvbitx) that can be used to program the hardware. For additional information on sessions view the API Page :ref:`api_sessions_page`.

Recommended usage is to open a Session as follows:

.. code-block:: python

   from nifpga import Session

   with Session(bitfile="MyBitfile.lvbitx", resource="RIO0") as session:
       # Reset stops the logic on the FPGA and puts it in the default state.
       # May substitute reset with download if your bitfile doesn't support it.
       session.reset()  
       
       # Add Initialization code here!
       # Write initial values to controls while the FPGA logic is stopped.
       
       # Start the logic on the FPGA
       session.run()
       
       # Add code that interacts with the FPGA while it is running here!

Using Controls and Indicators
-----------------------------
Controls and indicators are used to transmit small amounts of data to and from the FPGA.  The controls and indicators accessible by the FPGA Interface Python API are from the front panel of the top level VI from the LabVIEW FPGA code that was built into the bitfile. Accessing a control or indicator is done via its unique name from :ref:`api_sessions_page`'s register property. For additional information on controls and indicators view the API page :ref:`api_registers_page`.

The following example uses this FPGA VI:

.. image:: controlsAndIndicators1.png

This VI will take in a value from MyControl, square it, and output it to MyIndicator.

Example Usage:

.. code-block:: python

   from nifpga import Session

   with Session("MyBitfile.lvbitx", "RIO0") as session:
       my_control = session.registers['My Control']
       my_indicator = session.registers['My Indicator']
       my_control.write(4)
       data = my_indicator.read()
       print(data)  # prints 16

Using Array Controls and Indicators
-----------------------------------
Controls and indicators can also be an array type. They work like the a non-array registers, except use a `python list <https://docs.python.org/2/tutorial/datastructures.html>`_ for reading and writing. Accessing an array control or indicator is done via its unique name from :ref:`api_sessions_page`'s register property, all controls and indicators exist in this dictionary. For additional information on array controls and indicators view the API page :ref:`api_array_registers_page`.


For the following example, we have added two arrays to our FPGA VI:

.. image:: controlsAndIndicators2.png

Example Usage:

.. code-block:: python

   from nifpga import Session

   with Session("MyBitfile.lvbitx", "RIO0") as session:
       my_array_control = session.registers['My Array Control']
       my_array_indicator = session.registers['My Array Indicator']

       data = [0, 1, 2, 3, 4]
       my_array_control.write(data)
       print(my_array_indicator.read())  # prints [0, 1, 4, 9, 16]

Using FIFOs
-----------
FIFOs are used for streaming data to and from the FPGA. A FIFO is accessible by the FPGA Interface Python API via the top level VI from LabVIEW FPGA code. For additional information on FIFOs view the API page :ref:`api_fifos_page`.

For the following example, we have made a VI with two FIFOs.  One FIFO is a host to target FIFO and the other is target to host FIFO.  This VI uses the FIFOs to stream data from the processor, to the FPGA and then back to the processor.

.. image:: fifos.png


Example Usage:

.. code-block:: python

   from nifpga import Session

   # create a list of 100 incrementing values
   data = list(range(0, 100))

   with Session("MyBitfile.lvbitx", "RIO0") as session:
       host_to_target = session.fifos['Host To Target Fifo']
       target_to_host = session.fifos['Target To Host Fifo']
       host_to_target.start()
       target_to_host.start()

       # stream the data to the FPGA
       host_to_target.write(data, timeout_ms=100)
       # steam the data back to the processor
       read_value = target_to_host.read(100, timeout_ms=100)
       # read_value is a tuple containing the data and elements remaining
       print(read_value.elements_remaining)  # prints 0

       # loop over both lists and print if the data doesn't match
       for input_data, output_data in zip(data, read_value.data):
           if input_data != output_data:
               print("data error")


Using IRQs
----------

IRQs are used to generate and handle user interrupts occurring on the FPGA. IRQs are accessible through the :ref:`api_sessions_page` class. IRQs have two methods :meth:`Session.wait_on_irqs(irqs, timeout_ms)` and :meth:`Session.acknowledge_irqs(irqs)`.

For the following example, we have made a VI with an IRQ in a loop.  This will fire IRQ 1 continuously and block the loop until the user acknowledges the IRQ.

.. image:: irqs.png


Example Usage:

.. code-block:: python

   from nifpga import Session

   timeout_ms = 300
   irq_1 = 1

   with Session("MyBitfile.lvbitx", "RIO0") as session:
       loop_count = session.registers["IRQ Loop Count"]

       # Wait on irq_1
       irq_status = session.wait_on_irqs(irq_1, timeout_ms)
       if irq_status.timed_out is True:
           print("timeout out while waiting for the interrupt")

       # Check to see if irq 1 asserted
       if irq_1 in irq_status.irqs_asserted:
           print("1 was asserted")
       else:
           print("1 was not asserted")

       # Print the loop count before and after acknowledging the irq
       print("Initial loop count:")
       print(loop_count.read())
       # Acknowledge the IRQ(s) when we're done
       session.acknowledge_irqs(irq_status.irqs_asserted)

       # Wait for the IRQ to fire again
       session.wait_on_irqs(irq_1, timeout_ms)
       # Print the loop count again to see its been incremented once
       print("Loop count after acknowledge:")
       print(loop_count.read())
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/examples.rst sha256=e742525ea37af91e956a3658d33dc9985119a846009b9edac83df857e14d54a8 bytes=325 -->
## FILE: docs/examples.rst

- repository: `ni/nifpga-python`
- source_path: `docs/examples.rst`
- sha256: `e742525ea37af91e956a3658d33dc9985119a846009b9edac83df857e14d54a8`
- bytes: 325

````rst
.. _examples_page:

========
Examples
========
This Section will go different snippets of example code using the FPGA Interface python API to accomplish different tasks. Use the following links to navigate to the examples.

.. toctree::
   :maxdepth: 3
   :caption: Table of Contents:

   examples/basic_examples
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/getting_started.rst sha256=d54f87fafbd2879aa4816d6138d00f6d1588b6faa3a9a1f2da420aafce24792e bytes=286 -->
## FILE: docs/getting_started.rst

- repository: `ni/nifpga-python`
- source_path: `docs/getting_started.rst`
- sha256: `d54f87fafbd2879aa4816d6138d00f6d1588b6faa3a9a1f2da420aafce24792e`
- bytes: 286

````rst
.. _getting_started_page:
===============
Getting Started
===============

This document will show you how to get up and running with the NI FPGA Interface
Python API.

.. toctree::
   :maxdepth: 2
   :caption: User Documentation

   installation
   examples/basic_examples
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/index.rst sha256=b45156189c5abe68232a2cc31765ac538f7caf295c6d7f86f606ab62bd079a9a bytes=1028 -->
## FILE: docs/index.rst

- repository: `ni/nifpga-python`
- source_path: `docs/index.rst`
- sha256: `b45156189c5abe68232a2cc31765ac538f7caf295c6d7f86f606ab62bd079a9a`
- bytes: 1028

````rst
.. _welcome_page:
=========================================================
Welcome to the FPGA Interface Python API's documentation!
=========================================================

The National Instruments FPGA Interface Python API is used for communication between processor and FPGA within NI reconfigurable I/O (RIO) hardware such as NI CompactRIO, NI Single-Board RIO, NI FlexRIO, and NI R Series multifunction RIO.

With the FPGA Interface Python API, developers can use LabVIEW FPGA to program the FPGA within NI hardware and communicate to it from Python running on a host computer.  This gives engineers and scientists with Python expertise the ability to take advantage of compiled LabVIEW FPGA bitfiles, also the option to reuse existing Python code.

.. include:: readme.rst

.. toctree::
   :maxdepth: 3
   :caption: User Documentation

   getting_started
   api_reference
   examples

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/installation.rst sha256=b123788d006d4e0411326379cf487eb1bec3b3352690c49db9213b773b189302 bytes=1263 -->
## FILE: docs/installation.rst

- repository: `ni/nifpga-python`
- source_path: `docs/installation.rst`
- sha256: `b123788d006d4e0411326379cf487eb1bec3b3352690c49db9213b773b189302`
- bytes: 1263

````rst
.. _installation_page:

============
Installation
============
The NI FPGA Interface Python API can be installed through pip, see below
for more detailed instructions.

Windows
-------
#. Install the correct driver for your RIO device

   * You can find drivers at http://www.ni.com/downloads/ni-drivers/

#. Install Python https://www.python.org/downloads/
#. Install nifpga using pip (pip will be installed under "Scripts" in your python installation location.

   .. code-block:: sh

      pip install nifpga

Desktop Linux
-------------
#. Install the correct driver for your RIO device

   * You can find drivers at http://www.ni.com/downloads/ni-drivers/

#. Use your package manager to install the "python-pip" package
#. Install nifpga using pip

.. code-block:: sh

   pip install nifpga

NI Linux RT
-----------
#. Install the driver for your device using NI MAX
#. Enable SSH or the serial console from NI MAX
#. Connect to SSH or the serial console and login as admin
#. Run the following commands

.. code-block:: sh

   opkg update
   opkg install python3 python3-misc
   # follow the latest instructions to install pip:
   # https://pip.pypa.io/en/stable/installing/
   python3 -m pip install nifpga
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/make.bat sha256=356a2f79be1ecc4aa7d4a2f2476f2ea586b55315b2ee4bb2c523925c4064ac48 bytes=7754 -->
## FILE: docs/make.bat

- repository: `ni/nifpga-python`
- source_path: `docs/make.bat`
- sha256: `356a2f79be1ecc4aa7d4a2f2476f2ea586b55315b2ee4bb2c523925c4064ac48`
- bytes: 7754

````batch
@ECHO OFF

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set BUILDDIR=_build
set ALLSPHINXOPTS=-d %BUILDDIR%/doctrees %SPHINXOPTS% .
set I18NSPHINXOPTS=%SPHINXOPTS% .
if NOT "%PAPER%" == "" (
	set ALLSPHINXOPTS=-D latex_paper_size=%PAPER% %ALLSPHINXOPTS%
	set I18NSPHINXOPTS=-D latex_paper_size=%PAPER% %I18NSPHINXOPTS%
)

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  html       to make standalone HTML files
	echo.  dirhtml    to make HTML files named index.html in directories
	echo.  singlehtml to make a single large HTML file
	echo.  pickle     to make pickle files
	echo.  json       to make JSON files
	echo.  htmlhelp   to make HTML files and a HTML help project
	echo.  qthelp     to make HTML files and a qthelp project
	echo.  devhelp    to make HTML files and a Devhelp project
	echo.  epub       to make an epub
	echo.  epub3      to make an epub3
	echo.  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter
	echo.  text       to make text files
	echo.  man        to make manual pages
	echo.  texinfo    to make Texinfo files
	echo.  gettext    to make PO message catalogs
	echo.  changes    to make an overview over all changed/added/deprecated items
	echo.  xml        to make Docutils-native XML files
	echo.  pseudoxml  to make pseudoxml-XML files for display purposes
	echo.  linkcheck  to check all external links for integrity
	echo.  doctest    to run all doctests embedded in the documentation if enabled
	echo.  coverage   to run coverage check of the documentation if enabled
	echo.  dummy      to check syntax errors of document sources
	goto end
)

if "%1" == "clean" (
	for /d %%i in (%BUILDDIR%\*) do rmdir /q /s %%i
	del /q /s %BUILDDIR%\*
	goto end
)


REM Check if sphinx-build is available and fallback to Python version if any
%SPHINXBUILD% 1>NUL 2>NUL
if errorlevel 9009 goto sphinx_python
goto sphinx_ok

:sphinx_python

set SPHINXBUILD=python -m sphinx.__init__
%SPHINXBUILD% 2> nul
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

:sphinx_ok


if "%1" == "html" (
	%SPHINXBUILD% -b html %ALLSPHINXOPTS% %BUILDDIR%/html
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/html.
	goto end
)

if "%1" == "dirhtml" (
	%SPHINXBUILD% -b dirhtml %ALLSPHINXOPTS% %BUILDDIR%/dirhtml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/dirhtml.
	goto end
)

if "%1" == "singlehtml" (
	%SPHINXBUILD% -b singlehtml %ALLSPHINXOPTS% %BUILDDIR%/singlehtml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/singlehtml.
	goto end
)

if "%1" == "pickle" (
	%SPHINXBUILD% -b pickle %ALLSPHINXOPTS% %BUILDDIR%/pickle
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can process the pickle files.
	goto end
)

if "%1" == "json" (
	%SPHINXBUILD% -b json %ALLSPHINXOPTS% %BUILDDIR%/json
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can process the JSON files.
	goto end
)

if "%1" == "htmlhelp" (
	%SPHINXBUILD% -b htmlhelp %ALLSPHINXOPTS% %BUILDDIR%/htmlhelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can run HTML Help Workshop with the ^
.hhp project file in %BUILDDIR%/htmlhelp.
	goto end
)

if "%1" == "qthelp" (
	%SPHINXBUILD% -b qthelp %ALLSPHINXOPTS% %BUILDDIR%/qthelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can run "qcollectiongenerator" with the ^
.qhcp project file in %BUILDDIR%/qthelp, like this:
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\DAQImationExample.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\DAQImationExample.ghc
	goto end
)

if "%1" == "devhelp" (
	%SPHINXBUILD% -b devhelp %ALLSPHINXOPTS% %BUILDDIR%/devhelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished.
	goto end
)

if "%1" == "epub" (
	%SPHINXBUILD% -b epub %ALLSPHINXOPTS% %BUILDDIR%/epub
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The epub file is in %BUILDDIR%/epub.
	goto end
)

if "%1" == "epub3" (
	%SPHINXBUILD% -b epub3 %ALLSPHINXOPTS% %BUILDDIR%/epub3
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The epub3 file is in %BUILDDIR%/epub3.
	goto end
)

if "%1" == "latex" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; the LaTeX files are in %BUILDDIR%/latex.
	goto end
)

if "%1" == "latexpdf" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	cd %BUILDDIR%/latex
	make all-pdf
	cd %~dp0
	echo.
	echo.Build finished; the PDF files are in %BUILDDIR%/latex.
	goto end
)

if "%1" == "latexpdfja" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	cd %BUILDDIR%/latex
	make all-pdf-ja
	cd %~dp0
	echo.
	echo.Build finished; the PDF files are in %BUILDDIR%/latex.
	goto end
)

if "%1" == "text" (
	%SPHINXBUILD% -b text %ALLSPHINXOPTS% %BUILDDIR%/text
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The text files are in %BUILDDIR%/text.
	goto end
)

if "%1" == "man" (
	%SPHINXBUILD% -b man %ALLSPHINXOPTS% %BUILDDIR%/man
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The manual pages are in %BUILDDIR%/man.
	goto end
)

if "%1" == "texinfo" (
	%SPHINXBUILD% -b texinfo %ALLSPHINXOPTS% %BUILDDIR%/texinfo
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The Texinfo files are in %BUILDDIR%/texinfo.
	goto end
)

if "%1" == "gettext" (
	%SPHINXBUILD% -b gettext %I18NSPHINXOPTS% %BUILDDIR%/locale
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The message catalogs are in %BUILDDIR%/locale.
	goto end
)

if "%1" == "changes" (
	%SPHINXBUILD% -b changes %ALLSPHINXOPTS% %BUILDDIR%/changes
	if errorlevel 1 exit /b 1
	echo.
	echo.The overview file is in %BUILDDIR%/changes.
	goto end
)

if "%1" == "linkcheck" (
	%SPHINXBUILD% -b linkcheck %ALLSPHINXOPTS% %BUILDDIR%/linkcheck
	if errorlevel 1 exit /b 1
	echo.
	echo.Link check complete; look for any errors in the above output ^
or in %BUILDDIR%/linkcheck/output.txt.
	goto end
)

if "%1" == "doctest" (
	%SPHINXBUILD% -b doctest %ALLSPHINXOPTS% %BUILDDIR%/doctest
	if errorlevel 1 exit /b 1
	echo.
	echo.Testing of doctests in the sources finished, look at the ^
results in %BUILDDIR%/doctest/output.txt.
	goto end
)

if "%1" == "coverage" (
	%SPHINXBUILD% -b coverage %ALLSPHINXOPTS% %BUILDDIR%/coverage
	if errorlevel 1 exit /b 1
	echo.
	echo.Testing of coverage in the sources finished, look at the ^
results in %BUILDDIR%/coverage/python.txt.
	goto end
)

if "%1" == "xml" (
	%SPHINXBUILD% -b xml %ALLSPHINXOPTS% %BUILDDIR%/xml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The XML files are in %BUILDDIR%/xml.
	goto end
)

if "%1" == "pseudoxml" (
	%SPHINXBUILD% -b pseudoxml %ALLSPHINXOPTS% %BUILDDIR%/pseudoxml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The pseudo-XML files are in %BUILDDIR%/pseudoxml.
	goto end
)

if "%1" == "dummy" (
	%SPHINXBUILD% -b dummy %ALLSPHINXOPTS% %BUILDDIR%/dummy
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. Dummy builder generates no files.
	goto end
)

:end
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/Makefile sha256=55ba3966633e61387c9aa80880e41af4332d60bc026c1be0b9442f461b322ea6 bytes=7875 -->
## FILE: docs/Makefile

- repository: `ni/nifpga-python`
- source_path: `docs/Makefile`
- sha256: `55ba3966633e61387c9aa80880e41af4332d60bc026c1be0b9442f461b322ea6`
- bytes: 7875

````text
# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  applehelp  to make an Apple Help Book"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  epub3      to make an epub3"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  latexpdfja to make LaTeX files and run them through platex/dvipdfmx"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  xml        to make Docutils-native XML files"
	@echo "  pseudoxml  to make pseudoxml-XML files for display purposes"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"
	@echo "  coverage   to run coverage check of the documentation (if enabled)"
	@echo "  dummy      to check syntax errors of document sources"

.PHONY: clean
clean:
	rm -rf $(BUILDDIR)/*

.PHONY: html
html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

.PHONY: dirhtml
dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

.PHONY: singlehtml
singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

.PHONY: pickle
pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

.PHONY: json
json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

.PHONY: htmlhelp
htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

.PHONY: qthelp
qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/DAQImationExample.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/DAQImationExample.qhc"

.PHONY: applehelp
applehelp:
	$(SPHINXBUILD) -b applehelp $(ALLSPHINXOPTS) $(BUILDDIR)/applehelp
	@echo
	@echo "Build finished. The help book is in $(BUILDDIR)/applehelp."
	@echo "N.B. You won't be able to view it unless you put it in" \
	      "~/Library/Documentation/Help or install it in your application" \
	      "bundle."

.PHONY: devhelp
devhelp:
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/DAQImationExample"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/DAQImationExample"
	@echo "# devhelp"

.PHONY: epub
epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

.PHONY: epub3
epub3:
	$(SPHINXBUILD) -b epub3 $(ALLSPHINXOPTS) $(BUILDDIR)/epub3
	@echo
	@echo "Build finished. The epub3 file is in $(BUILDDIR)/epub3."

.PHONY: latex
latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

.PHONY: latexpdf
latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

.PHONY: latexpdfja
latexpdfja:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through platex and dvipdfmx..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf-ja
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

.PHONY: text
text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

.PHONY: man
man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

.PHONY: texinfo
texinfo:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo
	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."
	@echo "Run \`make' in that directory to run these through makeinfo" \
	      "(use \`make info' here to do that automatically)."

.PHONY: info
info:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo "Running Texinfo files through makeinfo..."
	make -C $(BUILDDIR)/texinfo info
	@echo "makeinfo finished; the Info files are in $(BUILDDIR)/texinfo."

.PHONY: gettext
gettext:
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

.PHONY: changes
changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

.PHONY: linkcheck
linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

.PHONY: doctest
doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

.PHONY: coverage
coverage:
	$(SPHINXBUILD) -b coverage $(ALLSPHINXOPTS) $(BUILDDIR)/coverage
	@echo "Testing of coverage in the sources finished, look at the " \
	      "results in $(BUILDDIR)/coverage/python.txt."

.PHONY: xml
xml:
	$(SPHINXBUILD) -b xml $(ALLSPHINXOPTS) $(BUILDDIR)/xml
	@echo
	@echo "Build finished. The XML files are in $(BUILDDIR)/xml."

.PHONY: pseudoxml
pseudoxml:
	$(SPHINXBUILD) -b pseudoxml $(ALLSPHINXOPTS) $(BUILDDIR)/pseudoxml
	@echo
	@echo "Build finished. The pseudo-XML files are in $(BUILDDIR)/pseudoxml."

.PHONY: dummy
dummy:
	$(SPHINXBUILD) -b dummy $(ALLSPHINXOPTS) $(BUILDDIR)/dummy
	@echo
	@echo "Build finished. Dummy builder generates no files."
````

<!--NI_OSS_SOURCE repo=nifpga-python path=docs/readme.rst sha256=670b300de855c26e5c35d7c5df9d1db7eeb12a5dcb1602cfe81ffe7a2b517956 bytes=2630 -->
## FILE: docs/readme.rst

- repository: `ni/nifpga-python`
- source_path: `docs/readme.rst`
- sha256: `670b300de855c26e5c35d7c5df9d1db7eeb12a5dcb1602cfe81ffe7a2b517956`
- bytes: 2630

````rst
===========  =================================================================================================================================
Info         Python API for interacting with LabVIEW FPGA Devices. See our `GitHub <https://github.com/ni/nifpga-python/>`_.
Author       National Instruments
Maintainers  Michael Strain <Michael.Strain@ni.com>
===========  =================================================================================================================================

About
=====

The ``nifpga`` package contains an API for interacting with National Instrument's
LabVIEW FPGA Devices - from Python. This package was created and is officially
supported by National Instruments.

**nifpga**  supports versions 16.0 and later of the RIO driver.

Some functions in the **nifpga** package may be unavailable with earlier
versions of your RIO driver. Visit the
`National Instruments downloads page <http://www.ni.com/downloads/>`_ to
upgrade the appropriate RIO device driver for your hardware.

**nifpga** supports Windows and Linux operating systems.

**nifpga** supports Python  3.5+ . **nifpga** will likely work on other Python implementations.  Feel free to open a issue on github for supporting a new implementation.

Bugs / Feature Requests
=======================

To report a bug or submit a feature request, please use our
`GitHub issues page <https://github.com/ni/nifpga-python/issues>`_ to open a
new issue.

Information to Include When Asking For Help
-------------------------------------------

Please include **all** of the following information when opening an issue:

- Detailed steps on how to reproduce the problem, and full traceback (if
  applicable).
- The exact python version used::

  $ python -c "import sys; print(sys.version)"

- The exact versions of packages used::

  $ python -m pip list

- The exact version of the RIO driver used. Follow
  `this KB article <http://digital.ni.com/public.nsf/allkb/2266B58A5061E86A8625758C007A4FE3>`_
  to determine the RIO driver you have installed.
- The operating system and version (e.g. Windows 7, CentOS 7.2, ...)

Additional Documentation
========================

If you are unfamiliar with LabVIEW FPGA module, perusing the
`LabVIEW FPGA Module <http://www.ni.com/labview/fpga/>`_
resource is a great way to get started. This documentation is API-agnostic.

License
=======
**nifpga** is licensed under an MIT-style license (see LICENSE). Other
incorporated projects may be licensed under different licenses. All licenses
allow for non-commercial and commercial use.
````

<!--NI_OSS_SOURCE repo=nifpga-python path=examples/Example.lvproj sha256=49d81a6a4ba30bbddb659885822134f562d9b2739c1a2238cf2396f5aa8fe32a bytes=23410 -->
## FILE: examples/Example.lvproj

- repository: `ni/nifpga-python`
- source_path: `examples/Example.lvproj`
- sha256: `49d81a6a4ba30bbddb659885822134f562d9b2739c1a2238cf2396f5aa8fe32a`
- bytes: 23410

````xml
<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="16008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Dependencies" Type="Dependencies"/>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
	<Item Name="RT CompactRIO Target" Type="RT CompactRIO">
		<Property Name="alias.name" Type="Str">RT CompactRIO Target</Property>
		<Property Name="alias.value" Type="Str">0.0.0.0</Property>
		<Property Name="CCSymbols" Type="Str">TARGET_TYPE,RT;OS,Linux;CPU,ARM;DeviceCode,76D6;</Property>
		<Property Name="crio.ControllerPID" Type="Str">76D6</Property>
		<Property Name="host.ResponsivenessCheckEnabled" Type="Bool">true</Property>
		<Property Name="host.ResponsivenessCheckPingDelay" Type="UInt">5000</Property>
		<Property Name="host.ResponsivenessCheckPingTimeout" Type="UInt">1000</Property>
		<Property Name="host.TargetCPUID" Type="UInt">8</Property>
		<Property Name="host.TargetOSID" Type="UInt">8</Property>
		<Property Name="target.cleanupVisa" Type="Bool">false</Property>
		<Property Name="target.FPProtocolGlobals_ControlTimeLimit" Type="Int">300</Property>
		<Property Name="target.getDefault-&gt;WebServer.Port" Type="Int">80</Property>
		<Property Name="target.getDefault-&gt;WebServer.Timeout" Type="Int">60</Property>
		<Property Name="target.IOScan.Faults" Type="Str"></Property>
		<Property Name="target.IOScan.NetVarPeriod" Type="UInt">100</Property>
		<Property Name="target.IOScan.NetWatchdogEnabled" Type="Bool">false</Property>
		<Property Name="target.IOScan.Period" Type="UInt">10000</Property>
		<Property Name="target.IOScan.PowerupMode" Type="UInt">0</Property>
		<Property Name="target.IOScan.Priority" Type="UInt">0</Property>
		<Property Name="target.IOScan.ReportModeConflict" Type="Bool">true</Property>
		<Property Name="target.IsRemotePanelSupported" Type="Bool">true</Property>
		<Property Name="target.RTCPULoadMonitoringEnabled" Type="Bool">true</Property>
		<Property Name="target.RTDebugWebServerHTTPPort" Type="Int">8001</Property>
		<Property Name="target.RTTarget.ApplicationPath" Type="Path">/c/ni-rt/startup/startup.rtexe</Property>
		<Property Name="target.RTTarget.EnableFileSharing" Type="Bool">true</Property>
		<Property Name="target.RTTarget.IPAccess" Type="Str">+*</Property>
		<Property Name="target.RTTarget.LaunchAppAtBoot" Type="Bool">false</Property>
		<Property Name="target.RTTarget.VIPath" Type="Path">/home/lvuser/natinst/bin</Property>
		<Property Name="target.server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="target.server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="target.server.tcp.access" Type="Str">+*</Property>
		<Property Name="target.server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="target.server.tcp.paranoid" Type="Bool">true</Property>
		<Property Name="target.server.tcp.port" Type="Int">3363</Property>
		<Property Name="target.server.tcp.serviceName" Type="Str">Main Application Instance/VI Server</Property>
		<Property Name="target.server.tcp.serviceName.default" Type="Str">Main Application Instance/VI Server</Property>
		<Property Name="target.server.vi.access" Type="Str">+*</Property>
		<Property Name="target.server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="target.server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="target.WebServer.Enabled" Type="Bool">false</Property>
		<Property Name="target.WebServer.LogEnabled" Type="Bool">false</Property>
		<Property Name="target.WebServer.LogPath" Type="Path">/c/ni-rt/system/www/www.log</Property>
		<Property Name="target.WebServer.Port" Type="Int">80</Property>
		<Property Name="target.WebServer.RootPath" Type="Path">/c/ni-rt/system/www</Property>
		<Property Name="target.WebServer.TcpAccess" Type="Str">c+*</Property>
		<Property Name="target.WebServer.Timeout" Type="Int">60</Property>
		<Property Name="target.WebServer.ViAccess" Type="Str">+*</Property>
		<Property Name="target.webservices.SecurityAPIKey" Type="Str">PqVr/ifkAQh+lVrdPIykXlFvg12GhhQFR8H9cUhphgg=:pTe9HRlQuMfJxAG6QCGq7UvoUpJzAzWGKy5SbZ+roSU=</Property>
		<Property Name="target.webservices.ValidTimestampWindow" Type="Int">15</Property>
		<Item Name="Chassis" Type="cRIO Chassis">
			<Property Name="crio.ProgrammingMode" Type="Str">fpga</Property>
			<Property Name="crio.ResourceID" Type="Str">RIO0</Property>
			<Property Name="crio.Type" Type="Str">cRIO-9068</Property>
			<Item Name="FPGA Target" Type="FPGA Target">
				<Property Name="AutoRun" Type="Bool">false</Property>
				<Property Name="configString.guid" Type="Str">{1611F439-B8CF-419E-A299-F1E677C2F2AE}"ControlLogic=0;NumberOfElements=1029;Type=1;ReadArbs=Arbitrate if Multiple Requestors Only;ElementsPerRead=1;WriteArbs=Arbitrate if Multiple Requestors Only;ElementsPerWrite=1;Implementation=2;Host To Target Fifo;DataType=1000800000000001000940070003553332000100000000000000000000;DisableOnOverflowUnderflow=FALSE"{28617CB2-1F4A-48DF-BB4F-057E64260813}resource=/Chassis Temperature;0;ReadMethodType=i16{39B0297E-9A29-4E66-BA35-59F4C7946E0C}resource=/Scan Clock;0;ReadMethodType=bool{400E4CED-8AE1-4D58-8C93-2200B8161C54}"ControlLogic=0;NumberOfElements=1023;Type=2;ReadArbs=Arbitrate if Multiple Requestors Only;ElementsPerRead=1;WriteArbs=Arbitrate if Multiple Requestors Only;ElementsPerWrite=1;Implementation=2;TargetToHostFifo;DataType=1000800000000001000940070003553332000100000000000000000000;DisableOnOverflowUnderflow=FALSE"{7FB77B42-EC21-4671-AA12-748428E3DA33}resource=/Sleep;0;ReadMethodType=bool;WriteMethodType=bool{876494C1-6B68-4C2B-98DF-76C2959B0550}resource=/System Reset;0;ReadMethodType=bool;WriteMethodType=bool{99BF64DA-9F17-439E-9143-B4625CA9B47C}resource=/USER FPGA LED;0;ReadMethodType=u8;WriteMethodType=u8{D7439DE9-90E5-49CE-8E7A-27B143D7A77D}ResourceName=40 MHz Onboard Clock;TopSignalConnect=Clk40;ClockSignalName=Clk40;MinFreq=40000000.000000;MaxFreq=40000000.000000;VariableFreq=0;NomFreq=40000000.000000;PeakPeriodJitter=250.000000;MinDutyCycle=50.000000;MaxDutyCycle=50.000000;Accuracy=100.000000;RunTime=0;SpreadSpectrum=0;GenericDataHash=D41D8CD98F00B204E9800998ECF8427E;cRIO-9068/Clk40/falsefalseFPGA_EXECUTION_MODEFPGA_TARGETFPGA_TARGET_CLASSCRIO_9068FPGA_TARGET_FAMILYZYNQTARGET_TYPEFPGA</Property>
				<Property Name="configString.name" Type="Str">40 MHz Onboard ClockResourceName=40 MHz Onboard Clock;TopSignalConnect=Clk40;ClockSignalName=Clk40;MinFreq=40000000.000000;MaxFreq=40000000.000000;VariableFreq=0;NomFreq=40000000.000000;PeakPeriodJitter=250.000000;MinDutyCycle=50.000000;MaxDutyCycle=50.000000;Accuracy=100.000000;RunTime=0;SpreadSpectrum=0;GenericDataHash=D41D8CD98F00B204E9800998ECF8427E;Chassis Temperatureresource=/Chassis Temperature;0;ReadMethodType=i16cRIO-9068/Clk40/falsefalseFPGA_EXECUTION_MODEFPGA_TARGETFPGA_TARGET_CLASSCRIO_9068FPGA_TARGET_FAMILYZYNQTARGET_TYPEFPGAHost To Target Fifo"ControlLogic=0;NumberOfElements=1029;Type=1;ReadArbs=Arbitrate if Multiple Requestors Only;ElementsPerRead=1;WriteArbs=Arbitrate if Multiple Requestors Only;ElementsPerWrite=1;Implementation=2;Host To Target Fifo;DataType=1000800000000001000940070003553332000100000000000000000000;DisableOnOverflowUnderflow=FALSE"Scan Clockresource=/Scan Clock;0;ReadMethodType=boolSleepresource=/Sleep;0;ReadMethodType=bool;WriteMethodType=boolSystem Resetresource=/System Reset;0;ReadMethodType=bool;WriteMethodType=boolTarget To Host Fifo"ControlLogic=0;NumberOfElements=1023;Type=2;ReadArbs=Arbitrate if Multiple Requestors Only;ElementsPerRead=1;WriteArbs=Arbitrate if Multiple Requestors Only;ElementsPerWrite=1;Implementation=2;TargetToHostFifo;DataType=1000800000000001000940070003553332000100000000000000000000;DisableOnOverflowUnderflow=FALSE"USER FPGA LEDresource=/USER FPGA LED;0;ReadMethodType=u8;WriteMethodType=u8</Property>
				<Property Name="NI.LV.FPGA.CompileConfigString" Type="Str">cRIO-9068/Clk40/falsefalseFPGA_EXECUTION_MODEFPGA_TARGETFPGA_TARGET_CLASSCRIO_9068FPGA_TARGET_FAMILYZYNQTARGET_TYPEFPGA</Property>
				<Property Name="NI.LV.FPGA.Version" Type="Int">6</Property>
				<Property Name="niFpga_TopLevelVIID" Type="Path">/C/Users/Administrator/Desktop/PythonExample/FPGAExample.vi</Property>
				<Property Name="Resource Name" Type="Str">RIO0</Property>
				<Property Name="Target Class" Type="Str">cRIO-9068</Property>
				<Property Name="Top-Level Timing Source" Type="Str">40 MHz Onboard Clock</Property>
				<Property Name="Top-Level Timing Source Is Default" Type="Bool">true</Property>
				<Item Name="Chassis I/O" Type="Folder">
					<Item Name="Chassis Temperature" Type="Elemental IO">
						<Property Name="eioAttrBag" Type="Xml"><AttributeSet name="">
   <Attribute name="resource">
   <Value>/Chassis Temperature</Value>
   </Attribute>
</AttributeSet>
</Property>
						<Property Name="FPGA.PersistentID" Type="Str">{28617CB2-1F4A-48DF-BB4F-057E64260813}</Property>
					</Item>
					<Item Name="Scan Clock" Type="Elemental IO">
						<Property Name="eioAttrBag" Type="Xml"><AttributeSet name="">
   <Attribute name="resource">
   <Value>/Scan Clock</Value>
   </Attribute>
</AttributeSet>
</Property>
						<Property Name="FPGA.PersistentID" Type="Str">{39B0297E-9A29-4E66-BA35-59F4C7946E0C}</Property>
					</Item>
					<Item Name="Sleep" Type="Elemental IO">
						<Property Name="eioAttrBag" Type="Xml"><AttributeSet name="">
   <Attribute name="resource">
   <Value>/Sleep</Value>
   </Attribute>
</AttributeSet>
</Property>
						<Property Name="FPGA.PersistentID" Type="Str">{7FB77B42-EC21-4671-AA12-748428E3DA33}</Property>
					</Item>
					<Item Name="System Reset" Type="Elemental IO">
						<Property Name="eioAttrBag" Type="Xml"><AttributeSet name="">
   <Attribute name="resource">
   <Value>/System Reset</Value>
   </Attribute>
</AttributeSet>
</Property>
						<Property Name="FPGA.PersistentID" Type="Str">{876494C1-6B68-4C2B-98DF-76C2959B0550}</Property>
					</Item>
					<Item Name="USER FPGA LED" Type="Elemental IO">
						<Property Name="eioAttrBag" Type="Xml"><AttributeSet name="">
   <Attribute name="resource">
   <Value>/USER FPGA LED</Value>
   </Attribute>
</AttributeSet>
</Property>
						<Property Name="FPGA.PersistentID" Type="Str">{99BF64DA-9F17-439E-9143-B4625CA9B47C}</Property>
					</Item>
				</Item>
				<Item Name="40 MHz Onboard Clock" Type="FPGA Base Clock">
					<Property Name="FPGA.PersistentID" Type="Str">{D7439DE9-90E5-49CE-8E7A-27B143D7A77D}</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig" Type="Str">ResourceName=40 MHz Onboard Clock;TopSignalConnect=Clk40;ClockSignalName=Clk40;MinFreq=40000000.000000;MaxFreq=40000000.000000;VariableFreq=0;NomFreq=40000000.000000;PeakPeriodJitter=250.000000;MinDutyCycle=50.000000;MaxDutyCycle=50.000000;Accuracy=100.000000;RunTime=0;SpreadSpectrum=0;GenericDataHash=D41D8CD98F00B204E9800998ECF8427E;</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.Accuracy" Type="Dbl">100</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.ClockSignalName" Type="Str">Clk40</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.MaxDutyCycle" Type="Dbl">50</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.MaxFrequency" Type="Dbl">40000000</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.MinDutyCycle" Type="Dbl">50</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.MinFrequency" Type="Dbl">40000000</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.NominalFrequency" Type="Dbl">40000000</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.PeakPeriodJitter" Type="Dbl">250</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.ResourceName" Type="Str">40 MHz Onboard Clock</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.SupportAndRequireRuntimeEnableDisable" Type="Bool">false</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.TopSignalConnect" Type="Str">Clk40</Property>
					<Property Name="NI.LV.FPGA.BaseTSConfig.VariableFrequency" Type="Bool">false</Property>
					<Property Name="NI.LV.FPGA.Valid" Type="Bool">true</Property>
					<Property Name="NI.LV.FPGA.Version" Type="Int">5</Property>
				</Item>
				<Item Name="FPGAExample.vi" Type="VI" URL="../FPGAExample.vi">
					<Property Name="BuildSpec" Type="Str">{DFE57F2A-7572-4948-A08F-1F422B287DB0}</Property>
					<Property Name="configString.guid" Type="Str">{1611F439-B8CF-419E-A299-F1E677C2F2AE}"ControlLogic=0;NumberOfElements=1029;Type=1;ReadArbs=Arbitrate if Multiple Requestors Only;ElementsPerRead=1;WriteArbs=Arbitrate if Multiple Requestors Only;ElementsPerWrite=1;Implementation=2;Host To Target Fifo;DataType=1000800000000001000940070003553332000100000000000000000000;DisableOnOverflowUnderflow=FALSE"{28617CB2-1F4A-48DF-BB4F-057E64260813}resource=/Chassis Temperature;0;ReadMethodType=i16{39B0297E-9A29-4E66-BA35-59F4C7946E0C}resource=/Scan Clock;0;ReadMethodType=bool{400E4CED-8AE1-4D58-8C93-2200B8161C54}"ControlLogic=0;NumberOfElements=1023;Type=2;ReadArbs=Arbitrate if Multiple Requestors Only;ElementsPerRead=1;WriteArbs=Arbitrate if Multiple Requestors Only;ElementsPerWrite=1;Implementation=2;TargetToHostFifo;DataType=1000800000000001000940070003553332000100000000000000000000;DisableOnOverflowUnderflow=FALSE"{7FB77B42-EC21-4671-AA12-748428E3DA33}resource=/Sleep;0;ReadMethodType=bool;WriteMethodType=bool{876494C1-6B68-4C2B-98DF-76C2959B0550}resource=/System Reset;0;ReadMethodType=bool;WriteMethodType=bool{99BF64DA-9F17-439E-9143-B4625CA9B47C}resource=/USER FPGA LED;0;ReadMethodType=u8;WriteMethodType=u8{D7439DE9-90E5-49CE-8E7A-27B143D7A77D}ResourceName=40 MHz Onboard Clock;TopSignalConnect=Clk40;ClockSignalName=Clk40;MinFreq=40000000.000000;MaxFreq=40000000.000000;VariableFreq=0;NomFreq=40000000.000000;PeakPeriodJitter=250.000000;MinDutyCycle=50.000000;MaxDutyCycle=50.000000;Accuracy=100.000000;RunTime=0;SpreadSpectrum=0;GenericDataHash=D41D8CD98F00B204E9800998ECF8427E;cRIO-9068/Clk40/falsefalseFPGA_EXECUTION_MODEFPGA_TARGETFPGA_TARGET_CLASSCRIO_9068FPGA_TARGET_FAMILYZYNQTARGET_TYPEFPGA</Property>
					<Property Name="configString.name" Type="Str">40 MHz Onboard ClockResourceName=40 MHz Onboard Clock;TopSignalConnect=Clk40;ClockSignalName=Clk40;MinFreq=40000000.000000;MaxFreq=40000000.000000;VariableFreq=0;NomFreq=40000000.000000;PeakPeriodJitter=250.000000;MinDutyCycle=50.000000;MaxDutyCycle=50.000000;Accuracy=100.000000;RunTime=0;SpreadSpectrum=0;GenericDataHash=D41D8CD98F00B204E9800998ECF8427E;Chassis Temperatureresource=/Chassis Temperature;0;ReadMethodType=i16cRIO-9068/Clk40/falsefalseFPGA_EXECUTION_MODEFPGA_TARGETFPGA_TARGET_CLASSCRIO_9068FPGA_TARGET_FAMILYZYNQTARGET_TYPEFPGAHost To Target Fifo"ControlLogic=0;NumberOfElements=1029;Type=1;ReadArbs=Arbitrate if Multiple Requestors Only;ElementsPerRead=1;WriteArbs=Arbitrate if Multiple Requestors Only;ElementsPerWrite=1;Implementation=2;Host To Target Fifo;DataType=1000800000000001000940070003553332000100000000000000000000;DisableOnOverflowUnderflow=FALSE"Scan Clockresource=/Scan Clock;0;ReadMethodType=boolSleepresource=/Sleep;0;ReadMethodType=bool;WriteMethodType=boolSystem Resetresource=/System Reset;0;ReadMethodType=bool;WriteMethodType=boolTarget To Host Fifo"ControlLogic=0;NumberOfElements=1023;Type=2;ReadArbs=Arbitrate if Multiple Requestors Only;ElementsPerRead=1;WriteArbs=Arbitrate if Multiple Requestors Only;ElementsPerWrite=1;Implementation=2;TargetToHostFifo;DataType=1000800000000001000940070003553332000100000000000000000000;DisableOnOverflowUnderflow=FALSE"USER FPGA LEDresource=/USER FPGA LED;0;ReadMethodType=u8;WriteMethodType=u8</Property>
					<Property Name="NI.LV.FPGA.InterfaceBitfile" Type="Str">C:\Users\Administrator\Desktop\PythonExample\FPGA Bitfiles\MyBitfile.lvbitx</Property>
				</Item>
				<Item Name="Host To Target Fifo" Type="FPGA FIFO">
					<Property Name="Actual Number of Elements" Type="UInt">1029</Property>
					<Property Name="Arbitration for Read" Type="UInt">1</Property>
					<Property Name="Arbitration for Write" Type="UInt">1</Property>
					<Property Name="Control Logic" Type="UInt">0</Property>
					<Property Name="Data Type" Type="UInt">7</Property>
					<Property Name="Disable on Overflow/Underflow" Type="Bool">false</Property>
					<Property Name="fifo.configuration" Type="Str">"ControlLogic=0;NumberOfElements=1029;Type=1;ReadArbs=Arbitrate if Multiple Requestors Only;ElementsPerRead=1;WriteArbs=Arbitrate if Multiple Requestors Only;ElementsPerWrite=1;Implementation=2;Host To Target Fifo;DataType=1000800000000001000940070003553332000100000000000000000000;DisableOnOverflowUnderflow=FALSE"</Property>
					<Property Name="fifo.configured" Type="Bool">true</Property>
					<Property Name="fifo.projectItemValid" Type="Bool">true</Property>
					<Property Name="fifo.valid" Type="Bool">true</Property>
					<Property Name="fifo.version" Type="Int">12</Property>
					<Property Name="FPGA.PersistentID" Type="Str">{1611F439-B8CF-419E-A299-F1E677C2F2AE}</Property>
					<Property Name="Local" Type="Bool">false</Property>
					<Property Name="Memory Type" Type="UInt">2</Property>
					<Property Name="Number Of Elements Per Read" Type="UInt">1</Property>
					<Property Name="Number Of Elements Per Write" Type="UInt">1</Property>
					<Property Name="Requested Number of Elements" Type="UInt">1023</Property>
					<Property Name="Type" Type="UInt">1</Property>
					<Property Name="Type Descriptor" Type="Str">1000800000000001000940070003553332000100000000000000000000</Property>
				</Item>
				<Item Name="IP Builder" Type="IP Builder Target">
					<Item Name="Dependencies" Type="Dependencies"/>
					<Item Name="Build Specifications" Type="Build"/>
				</Item>
				<Item Name="Target To Host Fifo" Type="FPGA FIFO">
					<Property Name="Actual Number of Elements" Type="UInt">1023</Property>
					<Property Name="Arbitration for Read" Type="UInt">1</Property>
					<Property Name="Arbitration for Write" Type="UInt">1</Property>
					<Property Name="Control Logic" Type="UInt">0</Property>
					<Property Name="Data Type" Type="UInt">7</Property>
					<Property Name="Disable on Overflow/Underflow" Type="Bool">false</Property>
					<Property Name="fifo.configuration" Type="Str">"ControlLogic=0;NumberOfElements=1023;Type=2;ReadArbs=Arbitrate if Multiple Requestors Only;ElementsPerRead=1;WriteArbs=Arbitrate if Multiple Requestors Only;ElementsPerWrite=1;Implementation=2;TargetToHostFifo;DataType=1000800000000001000940070003553332000100000000000000000000;DisableOnOverflowUnderflow=FALSE"</Property>
					<Property Name="fifo.configured" Type="Bool">true</Property>
					<Property Name="fifo.projectItemValid" Type="Bool">true</Property>
					<Property Name="fifo.valid" Type="Bool">true</Property>
					<Property Name="fifo.version" Type="Int">12</Property>
					<Property Name="FPGA.PersistentID" Type="Str">{400E4CED-8AE1-4D58-8C93-2200B8161C54}</Property>
					<Property Name="Local" Type="Bool">false</Property>
					<Property Name="Memory Type" Type="UInt">2</Property>
					<Property Name="Number Of Elements Per Read" Type="UInt">1</Property>
					<Property Name="Number Of Elements Per Write" Type="UInt">1</Property>
					<Property Name="Requested Number of Elements" Type="UInt">1023</Property>
					<Property Name="Type" Type="UInt">2</Property>
					<Property Name="Type Descriptor" Type="Str">1000800000000001000940070003553332000100000000000000000000</Property>
				</Item>
				<Item Name="Dependencies" Type="Dependencies"/>
				<Item Name="Build Specifications" Type="Build">
					<Item Name="PythonExample" Type="{F4C5E96F-7410-48A5-BB87-3559BC9B167F}">
						<Property Name="AllowEnableRemoval" Type="Bool">false</Property>
						<Property Name="BuildSpecDecription" Type="Str"></Property>
						<Property Name="BuildSpecName" Type="Str">PythonExample</Property>
						<Property Name="Comp.BitfileName" Type="Str">MyBitfile.lvbitx</Property>
						<Property Name="Comp.CustomXilinxParameters" Type="Str"></Property>
						<Property Name="Comp.MaxFanout" Type="Int">-1</Property>
						<Property Name="Comp.RandomSeed" Type="Bool">false</Property>
						<Property Name="Comp.Version.Build" Type="Int">0</Property>
						<Property Name="Comp.Version.Fix" Type="Int">0</Property>
						<Property Name="Comp.Version.Major" Type="Int">1</Property>
						<Property Name="Comp.Version.Minor" Type="Int">0</Property>
						<Property Name="Comp.VersionAutoIncrement" Type="Bool">false</Property>
						<Property Name="Comp.Vivado.EnableMultiThreading" Type="Bool">true</Property>
						<Property Name="Comp.Vivado.OptDirective" Type="Str"></Property>
						<Property Name="Comp.Vivado.PhysOptDirective" Type="Str"></Property>
						<Property Name="Comp.Vivado.PlaceDirective" Type="Str"></Property>
						<Property Name="Comp.Vivado.RouteDirective" Type="Str"></Property>
						<Property Name="Comp.Vivado.RunPowerOpt" Type="Bool">false</Property>
						<Property Name="Comp.Vivado.Strategy" Type="Str">Default</Property>
						<Property Name="Comp.Xilinx.DesignStrategy" Type="Str">balanced</Property>
						<Property Name="Comp.Xilinx.MapEffort" Type="Str">default(noTiming)</Property>
						<Property Name="Comp.Xilinx.ParEffort" Type="Str">standard</Property>
						<Property Name="Comp.Xilinx.SynthEffort" Type="Str">normal</Property>
						<Property Name="Comp.Xilinx.SynthGoal" Type="Str">speed</Property>
						<Property Name="Comp.Xilinx.UseRecommended" Type="Bool">true</Property>
						<Property Name="DefaultBuildSpec" Type="Bool">true</Property>
						<Property Name="DestinationDirectory" Type="Path">FPGA Bitfiles</Property>
						<Property Name="NI.LV.FPGA.LastCompiledBitfilePath" Type="Path">/C/Users/Administrator/Desktop/PythonExample/FPGA Bitfiles/MyBitfile.lvbitx</Property>
						<Property Name="NI.LV.FPGA.LastCompiledBitfilePathRelativeToProject" Type="Path">FPGA Bitfiles/MyBitfile.lvbitx</Property>
						<Property Name="ProjectPath" Type="Path">/C/Users/Administrator/Desktop/PythonExample/Example.lvproj</Property>
						<Property Name="RelativePath" Type="Bool">true</Property>
						<Property Name="RunWhenLoaded" Type="Bool">false</Property>
						<Property Name="SupportDownload" Type="Bool">true</Property>
						<Property Name="SupportResourceEstimation" Type="Bool">false</Property>
						<Property Name="TargetName" Type="Str">FPGA Target</Property>
						<Property Name="TopLevelVI" Type="Ref">/RT CompactRIO Target/Chassis/FPGA Target/FPGAExample.vi</Property>
					</Item>
				</Item>
			</Item>
		</Item>
		<Item Name="Dependencies" Type="Dependencies"/>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
````

<!--NI_OSS_SOURCE repo=nifpga-python path=LICENSE sha256=72a8fa56334d91433970e8f7a7a7e2fabbb97a9249df7752b100d0cb1aa768cb bytes=1081 -->
## FILE: LICENSE

- repository: `ni/nifpga-python`
- source_path: `LICENSE`
- sha256: `72a8fa56334d91433970e8f7a7a7e2fabbb97a9249df7752b100d0cb1aa768cb`
- bytes: 1081

````text
Copyright (c) 2017 National Instruments

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/__init__.py sha256=94c6cdf080f47440850d6cef6a1fb244c01f23fb6dfa9544f28c2c726c08e797 bytes=194 -->
## FILE: nifpga/__init__.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/__init__.py`
- sha256: `94c6cdf080f47440850d6cef6a1fb244c01f23fb6dfa9544f28c2c726c08e797`
- bytes: 194

````python
from .status import *
from .statuscheckedlibrary import FunctionInfo, StatusCheckedLibrary
from .nifpga import *
from .session import Session
from .bitfile import Bitfile

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/bitfile.py sha256=4ecfea1f31ec41a709ee1d44106c0d5681ad5cf0495cd6d614689fd5d6b798bc bytes=27436 -->
## FILE: nifpga/bitfile.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/bitfile.py`
- sha256: `4ecfea1f31ec41a709ee1d44106c0d5681ad5cf0495cd6d614689fd5d6b798bc`
- bytes: 27436

````python
import os
import xml.etree.ElementTree as ElementTree
from collections import OrderedDict
from decimal import Decimal
from nifpga import DataType
from numbers import Number
from warnings import warn
import ctypes


class Bitfile(object):
    """ Class that represents the contents of the .lvbitx file.

    Bitfile is a class that parses and contains the data from the XML based
    .lvbitx file.  This class can be used to lookup registers and FIFOs and
    is mostly intended to be used by Session.
    """
    def __init__(self, filepath, parse_contents=False):
        if parse_contents:
            self._filepath = None
            tree = ElementTree.fromstring(filepath)
        else:
            self._filepath = os.path.abspath(filepath)
            tree = ElementTree.ElementTree().parse(self._filepath)

        self._signature = tree.find("SignatureRegister").text.upper()

        documentation = tree.find("Documentation")
        if documentation is not None:
            build_spec_version_xml = documentation.find("BuildSpecVersion")
            self._build_spec_version = build_spec_version_xml.text if build_spec_version_xml is not None and build_spec_version_xml.text else None
            build_spec_description_xml = documentation.find("BuildSpecDescription")
            self._build_spec_description = build_spec_description_xml.text if build_spec_description_xml is not None and build_spec_description_xml.text else None
        else:
            self._build_spec_version = None
            self._build_spec_description = None

        project = tree.find("Project")
        nifpga = project.find("CompilationResultsTree") \
                        .find("CompilationResults") \
                        .find("NiFpga")
        self._base_address_on_device = int(nifpga.find("BaseAddressOnDevice").text)
        self._registers = {}
        for reg_xml in tree.find("VI").find("RegisterList"):
            try:
                reg = Register(reg_xml)
                assert reg.name not in self._registers, \
                    "One or more registers have the same name '%s', this is not supported" % reg.name
                self._registers[reg.name] = reg
            except UnsupportedTypeError as e:
                warn("Skipping Register: %s, %s" % (reg_xml.find("Name").text, str(e)))
            except ClusterMustContainUniqueNames as e:
                warn("Skipping Register: %s, %s" % (reg_xml.find("Name").text, str(e)))

        self._fifos = {}
        for channel_xml in nifpga.find("DmaChannelAllocationList"):
            try:
                fifo = Fifo(channel_xml)
                self._fifos[fifo.name] = fifo
            except UnsupportedTypeError as e:
                warn("Skipping FIFO: %s, %s" % (fifo.name, str(e)))
            except ClusterMustContainUniqueNames as e:
                warn("Skipping FIFO: %s, %s" % (fifo.name, str(e)))

    @property
    def filepath(self):
        """ Returns the filepath used to create this bitfile. """
        return self._filepath

    @property
    def signature(self):
        """ Returns the signature of the bitfile. """
        return self._signature

    @property
    def build_spec_version(self):
        """ Returns the build spec version from the bitfile Documentation, or
        None if not present or empty.
        """
        return self._build_spec_version

    @property
    def build_spec_description(self):
        """ Returns the build spec description from the bitfile Documentation,
        or None if not present or empty.
        """
        return self._build_spec_description

    @property
    def registers(self):
        """ Returns a dictionary of Registers (Controls and Indicators) that
        the bitfile contained.  The dictionary is indexed by the name of the
        register.
        """
        return self._registers

    @property
    def fifos(self):
        """ Returns a dictionary of FIFOs that the bitfile contained.
        The dictionary is indexed by the name of the FIFO.
        """
        return self._fifos

    def base_address_on_device(self):
        """ Returns the base address on the device.  This is the offset on the
        device that Registers are located at.  So a Registers offset is
        base_address_on_device + register_offset
        """
        return self._base_address_on_device


class UnsupportedTypeError(RuntimeError):
    pass


def _parse_type(type_xml):
    """ Parses the XML given and creates the appropriate type class for it.

    Type XML comes in 2 flavors and we need to handle both.
    We will sometimes (for FIFOs) get a non-recursive "SubType" that just
    provides the type and does not name it.  We will never see Clusters or
    Arrays as the "SubType".
    For registers and sometimes FIFOs, we will always get a recursive type
    containing names for all members.
    """
    type = type_xml.find("SubType")
    if type is not None:
        type_name = type.text
        name = ""
    else:
        type_name = type_xml.tag
        name = type_xml.find("Name").text
    if type_name == "Boolean":
        return _Bool(name)
    if type_name == "Cluster":
        return _Cluster(name, type_xml)
    if type_name == "FXP":
        return _FXP(name, type_xml)
    if type_name == "Array":
        return _Array(name, type_xml)
    if type_name == "SGL" or type_name == "DBL":
        return _Float(name, type_name)
    if type_name == "String":
        # Strings are not supported on the FPGA, but show up in error clusters
        return _String(name)
    if type_name == "CFXP":
        raise UnsupportedTypeError("The FPGA Interface Python API does not yet support Complex Fixed Point")
    return _Numeric(name, type_name)


class _BaseType(object):
    def __init__(self, name):
        if name is None:
            self._name = ""
        else:
            self._name = name

    @property
    def name(self):
        return self._name


class _String(_BaseType):
    """ Handles ignoring string types on the FPGA.  Strings are not supported
    on the FPGA, but sometimes show up in error clusters. """
    def __init__(self, name):
        super(_String, self).__init__(name)

    @property
    def datatype(self):
        return DataType.Cluster  # lie and claim we are a cluster so callers don't make assumptions about our contents

    @property
    def size_in_bits(self):
        return 0

    @property
    def is_c_api_type(self):
        return False

    def unpack_data(self, data):
        return ""

    def pack_data(self, data_to_pack, packed_data):
        return packed_data  # don't pack anything for a string


class _Numeric(_BaseType):
    """ Handles packing and unpacking Numerics such as U8, I8, EnumU8, etc"""
    def __init__(self, name, type_name):
        super(_Numeric, self).__init__(name)
        type_name = type_name.replace("Enum", "")
        for datatype in DataType:
            if str(datatype).lower() in type_name.lower():
                self._datatype = datatype
                break
        else:
            raise UnsupportedTypeError("Unrecognized type encountered: %s.  Consider opening an issue on github.com/ni/nifpga" % type_name)
        self._signed = type_name[0].lower() == 'i'
        self._size_in_bits = int(type_name[1:])
        self._data_mask = (1 << self._size_in_bits) - 1
        self._signed_bit_mask = 1 << (self._size_in_bits - 1)
        self._unpack = self._unpack_numeric_signed if self._signed else self._unpack_numeric_unsigned

    def _unpack_numeric_unsigned(self, bits_from_fpga):
        data = bits_from_fpga & self._data_mask
        return data

    def _unpack_numeric_signed(self, bits_from_fpga):
        data = bits_from_fpga & self._data_mask
        if data & self._signed_bit_mask:
            data = data ^ self._data_mask
            data += 1
            data *= -1
        return data

    @property
    def datatype(self):
        return self._datatype

    @property
    def size_in_bits(self):
        return self._size_in_bits

    @property
    def is_c_api_type(self):
        return True

    def unpack_data(self, data):
        return self._unpack(data)

    def pack_data(self, data_to_pack, packed_data):
        packed_data = packed_data << self._size_in_bits
        return packed_data | (data_to_pack & self._data_mask)


class _Float(_BaseType):
    """ Handles packing and unpacking floating point values from the FPGA. """
    def __init__(self, name, type_name):
        super(_Float, self).__init__(name)
        if "SGL" == type_name:
            self._size_in_bits = 32
            self._datatype = DataType.Sgl
        elif "DBL" == type_name:
            self._size_in_bits = 64
            self._datatype = DataType.Dbl
        self._data_mask = (1 << self._size_in_bits) - 1

    @property
    def datatype(self):
        return self._datatype

    @property
    def size_in_bits(self):
        return self._size_in_bits

    @property
    def is_c_api_type(self):
        return True

    def unpack_data(self, data):
        data = data & self._data_mask
        if self._datatype == DataType.Sgl:
            return ctypes.c_float.from_buffer(ctypes.c_uint(data)).value
        if self._datatype == DataType.Dbl:
            return ctypes.c_double.from_buffer(ctypes.c_ulonglong(data)).value

    def pack_data(self, data_to_pack, packed_data):
        if self._datatype == DataType.Sgl:
            bits_to_pack = ctypes.c_uint.from_buffer(ctypes.c_float(data_to_pack)).value
        if self._datatype == DataType.Dbl:
            bits_to_pack = ctypes.c_ulonglong.from_buffer(ctypes.c_double(data_to_pack)).value
        return (packed_data << self._size_in_bits) | bits_to_pack


class _Bool(_BaseType):
    """ Handles packing and unpacking bools. """
    def __init__(self, name):
        super(_Bool, self).__init__(name)

    @property
    def datatype(self):
        return DataType.Bool

    @property
    def size_in_bits(self):
        return 1

    @property
    def is_c_api_type(self):
        return True

    def unpack_data(self, data):
        return bool(data & 1)

    def pack_data(self, data_to_pack, packed_data):
        bit_to_pack = 1 if data_to_pack else 0
        return (packed_data << 1) | bit_to_pack


class ClusterMustContainUniqueNames(RuntimeError):
    """ For the FPGA Interface Python API, we have chosen to represent clusters
    as dictionaries.  This has a relatively straight forward conversion, but
    requires that all members of the cluster have a unique label."""
    pass


class _Cluster(_BaseType):
    """ Handles packing and unpacking clusters. """
    def __init__(self, name, type_xml):
        super(_Cluster, self).__init__(name)
        self._datatype = DataType.Cluster
        member_types = type_xml.find("TypeList")
        self._children = []
        names = set()
        for child in list(member_types):
            child_type = _parse_type(child)
            if child_type.name in names:
                raise ClusterMustContainUniqueNames("Cluster: '%s', contains multiple members with the name: '%s'" % (self._name, child_type.name))
            names.add(child_type.name)
            self._children.append(_parse_type(child))
        self._size_in_bits = sum(child.size_in_bits for child in self._children)

    @property
    def datatype(self):
        return DataType.Cluster

    @property
    def size_in_bits(self):
        return self._size_in_bits

    @property
    def is_c_api_type(self):
        return False

    def _unpack_data_recursive(self, data, result, child_iter):
        """ Clusters are stored in the correct order in the blob, but since we
        parse the blob from least significant to most, we are parsing the clusters
        out backwards. So parse out the data backwards going down the stack and
        add it to the dict going back up the stack. This way we insert into the
        OrderedDict in the correct order"""
        child = next(child_iter, None)
        if child is None:
            return
        current_result = child.unpack_data(data)
        data >>= child.size_in_bits
        self._unpack_data_recursive(data, result, child_iter)
        result[child.name] = current_result

    def unpack_data(self, data):
        result = OrderedDict()
        self._unpack_data_recursive(data, result, reversed(self._children))
        return result

    def pack_data(self, data_to_pack, packed_data):
        i = 0
        for child in self._children:
            packed_data = child.pack_data(data_to_pack[child.name], packed_data)
            i += 1
        return packed_data


class _Array(_BaseType):
    """ Handles packing and unpacking arrays. """
    def __init__(self, name, type_xml):
        super(_Array, self).__init__(name)
        self._subtype = _parse_type(list(type_xml.find("Type"))[0])
        self._size = int(type_xml.find("Size").text)
        self._size_in_bits = self._subtype.size_in_bits * self._size

    @property
    def datatype(self):
        return self._subtype.datatype

    @property
    def size(self):
        return self._size

    @property
    def size_in_bits(self):
        return self._size_in_bits

    @property
    def is_c_api_type(self):
        return self._subtype.is_c_api_type

    def unpack_data(self, data):
        results = [0] * self._size
        for i in range(0, self._size):
            results[i] = self._subtype.unpack_data(data)
            data = data >> self._subtype.size_in_bits
        # Arrays are packed in order, which means that as we are grabbing out values
        # and shifting data, we are grabbing from the back of the array.  So reverse it.
        results.reverse()
        return results

    def pack_data(self, data_to_pack, packed_data):
        for i in range(0, self._size):
            packed_data = self._subtype.pack_data(data_to_pack[i], packed_data)
        return packed_data


class _FXP(_BaseType):
    """ Handles packing and unpacking FXP values from the FPGA. """
    def __init__(self, name, type_xml):
        super(_FXP, self).__init__(name)
        self._datatype = DataType.Fxp
        signed_tag = type_xml.find("Signed")
        if signed_tag is None:
            raise UnsupportedTypeError("Unsupported FXP type encountered. This bitfile "
                                       "was likely compiled with LabVIEW Communications 2.0. "
                                       "Recompile with LabVIEW Communications 2.1 or later.")
        self._signed = True if signed_tag.text.lower() == 'true' else False
        overflow_enabled_xml = type_xml.find("IncludeOverflowStatus")
        if overflow_enabled_xml is not None:
            self._overflow_enabled = True if overflow_enabled_xml.text.lower() == 'true' else False
        else:
            self._overflow_enabled = False
        self._word_length = int(type_xml.find("WordLength").text)
        self._integer_word_length = int(type_xml.find("IntegerWordLength").text)
        # Delta, min, and max exist in the XML, but are incorrect...
        # So we calculate them here instead.
        self._delta = self._calculate_delta()
        self._minimum = self._calculate_minimum()
        self._maximum = self._calculate_maximum()
        self._size_in_bits = self._calculate_size_in_bits()
        self._data_mask = (1 << self._size_in_bits) - 1
        self._word_length_mask = (1 << self._word_length) - 1
        if self._signed:
            self._signed_bit_mask = 1 << (self._word_length - 1)

    @property
    def datatype(self):
        return self._datatype

    @property
    def size_in_bits(self):
        return self._size_in_bits

    @property
    def is_c_api_type(self):
        return False

    def _calculate_delta(self):
        """ Determines the fixed point delta value, the value of the register
        is only allowed to be an integer multiple of the delta. For example if
        delta is 1, then it is impossible to represent a fraction.
        The value persisted in the bitfile for delta is not always correct,
        therefore we must calculate it manually.
        """
        return Decimal(2**(self._integer_word_length - self._word_length))

    def _calculate_minimum(self):
        """ Determines the minimum possible value that can be represented with
        the given fixed point register. The value persisted in the bitfile for
        the minimum value is not always accurate, therefore we must calculate
        it manually.
        """
        if self._signed:
            magnitude_bits = self._word_length - 1
            return -1 * (2**(magnitude_bits) * self._delta)
        else:
            return 0

    def _calculate_maximum(self):
        """ Determines the minimum possible value that can be represented with
        the given fixed point register.The value persisted in the bitfile for
        the maximum value is not always accurate, therefore we must calculate
        it manually.
        """
        if self._signed:
            magnitude_bits = self._word_length - 1
        else:
            magnitude_bits = self._word_length
        return (2**(magnitude_bits) - 1) * self._delta

    def _calculate_size_in_bits(self):
        """ Fixed point values are transfered to the driver as an array of U32
        The length is between 1 and 3 determined by the word length (includes
        the signed bit) plus the include_overflow_status_enable bit.
        """
        bits_required = self._word_length
        if self._overflow_enabled:
            """ If overflow status is enabled we need an extra bit. """
            bits_required += 1
        return bits_required

    def unpack_data(self, data):
        """ This method converts value from hardware and returns the respective
        decimal value or a tuple with the overflow status and the decimal
        value.
        """
        data = data & self._data_mask
        overflow = None
        if self._overflow_enabled:
            overflow = self._get_overflow_value(data)
            data = self._remove_overflow_bit(data)

        if self._signed:
            data = self._integer_twos_comp(data)
        decimal_value = data * self._delta
        if self._overflow_enabled:
            return (overflow, decimal_value)
        else:
            return decimal_value

    def _get_overflow_value(self, data):
        """ Mask out all the data within the word length, leaving the overflow
        bit. If the result after masking the the word portion of the fixed
        point is nonzero that indicates the data read has overflowed. """
        mask = 2**(self._word_length)
        if data & mask > 0:
            return True
        return False

    def _remove_overflow_bit(self, data):
        """ This helper method masks out all bits not inside the word length,
        ultimately returning a value of data without the overflow bit. """
        return data & self._word_length_mask

    def _integer_twos_comp(self, data):
        """ Checks the signed bit and determines if the value is negative, If
        so take the twos complement of the input."""
        if data & self._signed_bit_mask > 0:
            data = data ^ self._word_length_mask
            data += 1
            data *= -1
        return data

    def pack_data(self, data_to_pack, packed_data):
        (overflow, data) = self._validate_and_parse_user_input(data_to_pack)

        fxp_representation = 0
        if data < self._minimum:
            fxp_representation = self._convert_value_to_fxp(self._minimum)
            self.warn_coerced_data()
        elif data > self._maximum:
            fxp_representation = self._convert_value_to_fxp(self._maximum)
            self.warn_coerced_data()
        else:
            fxp_representation = self._convert_value_to_fxp(data)

        if self._signed and data < 0:
            fxp_representation = self._integer_twos_comp(fxp_representation)

        if overflow:
            fxp_representation += 2**(self._word_length)

        packed_data <<= self._size_in_bits
        packed_data |= fxp_representation
        return packed_data

    def _validate_and_parse_user_input(self, user_input):
        overflow = None
        data = None
        if self._overflow_enabled:
            try:
                (overflow, data) = user_input
            except TypeError:
                """ If the user does not input any overflow status, eat the
                exception and use default value of False. """
                overflow = False
                data = user_input
            assert isinstance(overflow, bool)
        else:
            data = user_input
        assert isinstance(data, Number)
        return (overflow, data)

    def _convert_value_to_fxp(self, data):
        calculated_fxp = Decimal(data) / Decimal(self._delta)
        fxp_representation = int(calculated_fxp)
        """ If the result of the division is not an integer, we lost some of
        the input data. In this case we warn the user that we had to coerce the
        value to the nearest fixed point representation. """
        if fxp_representation != calculated_fxp:
            self.warn_coerced_data()
        return fxp_representation

    def warn_coerced_data(self):
        warn("The inputed value was not able to be converted to FXP, without coercion. ")


class Register(object):
    def __init__(self, reg_xml):
        """
        A control or indicator from the front panel of the top level FPGA VI

        reg_xml: the <Register> XML element, e.g. one of these:
            <Register>
                <Name>Output Array Bool 17</Name>
                <Indicator>true</Indicator>
                <Datatype>
                    <Array>
                        <Name>Output Array Bool 17</Name>
                        <Size>17</Size>
                        <Type>
                            <Boolean>
                            </Boolean>
                        </Type>
                    </Array>
                </Datatype>
                <Offset>98364</Offset>
                <Internal>false</Internal>
                <AccessMayTimeout>false</AccessMayTimeout>
            </Register>

            Or

            <Register>
                <Name>Input U64</Name>
                <Indicator>false</Indicator>
                <Datatype>
                    <U64>
                    </U64>
                </Datatype>
                <Offset>98464</Offset>
                <Internal>false</Internal>
                <AccessMayTimeout>false</AccessMayTimeout>
            </Register>
        """
        self._name = reg_xml.find("Name").text
        self._offset = int(reg_xml.find("Offset").text)
        self._indicator = True if reg_xml.find("Indicator").text.lower() == "true" else False
        self._access_may_timeout = True if reg_xml.find("AccessMayTimeout").text.lower() == 'true' else False
        self._internal = True if reg_xml.find("Internal").text.lower() == 'true' else False
        datatype = reg_xml.find("Datatype")
        self._type = _parse_type(list(datatype)[0])
        if self.is_array():
            self._num_elements = self._type.size
        else:
            self._num_elements = 1

    def __len__(self):
        """ Returns the number of elements in this register. """
        return self._num_elements

    @property
    def name(self):
        """ Returns the name of the Register. """
        return self._name

    @property
    def datatype(self):
        """ Returns a string containing the datatype of the Register. """
        return self._type.datatype

    @property
    def type(self):
        return self._type

    def is_array(self):
        """ Returns whether or not this Register is an array """
        return isinstance(self._type, _Array)

    @property
    def is_indicator(self):
        """ Returns whether or not this Register is an Indicator """
        return self._indicator

    @property
    def offset(self):
        """ Returns the offset of this register from the base address. """
        return self._offset

    def access_may_timeout(self):
        """ Returns Whether or not this register access could timeout.
        This could happen if the register is in an external clock domain.
        """
        return self._access_may_timeout

    def is_internal(self):
        """ Returns whether or not this register is for internal use. """
        return self._internal

    def __str__(self):
        return ("Register '%s'\n" % self._name
                + "\tType: %s\n" % self._datatype
                + "\tNum Elements: %d\n" % len(self)
                + "\tOffset: %d\n" % self._offset)


def _is_not_power_of_2(value):
    return value & (value - 1) != 0


class Fifo(object):
    def __init__(self, channel_xml):
        self._name = channel_xml.attrib["name"]
        self._number = int(channel_xml.find("Number").text)
        datatype_xml = channel_xml.find("DataType")
        if datatype_xml.find("SubType") is not None:
            self._type = _parse_type(datatype_xml)
        else:
            self._type = _parse_type(list(datatype_xml)[0])
        transfer_size_bytes_xml = channel_xml.find("TransferSizeBytes")
        # only newer XML that supports composite types will have TransferSizeBytes
        if transfer_size_bytes_xml is not None:
            self._transfer_size_bytes = int(transfer_size_bytes_xml.text)
            # As of 2018 transfer size must be a power of two.
            if _is_not_power_of_2(self._transfer_size_bytes):
                raise UnsupportedTypeError("This FIFO is incompatible with this version of 'nifpga'.  Upgrade to the latest version or open an issue on github.")
        else:
            if self._type.datatype is DataType.Fxp:
                self._transfer_size_bytes = 8
            else:
                self._transfer_size_bytes = ctypes.sizeof(self._type.datatype._return_ctype())

    @property
    def datatype(self):
        """ Returns the datatype string of the FIFO. """
        return self._type.datatype

    @property
    def number(self):
        """ Returns the FIFO number.
        This number is the unique identifier for the FIFO in this bitfile.
        """
        return self._number

    @property
    def name(self):
        """ Returns the name of the FIFO. """
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def transfer_size_bytes(self):
        """ The size of one FIFO element in bytes. """
        return self._transfer_size_bytes

    def is_fxp(self):
        return isinstance(self._type, _FXP)

    def is_composite(self):
        return isinstance(self._type, _Cluster) or isinstance(self._type, _Array)
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/nifpga.py sha256=1d78c406bbf6778d822d366fae85fa02d6bea1bb48686f518f9bf1cc89caf053 bytes=30680 -->
## FILE: nifpga/nifpga.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/nifpga.py`
- sha256: `1d78c406bbf6778d822d366fae85fa02d6bea1bb48686f518f9bf1cc89caf053`
- bytes: 30680

````python
"""
NiFpga, a thin wrapper around the FPGA Interface C API

Copyright (c) 2015 National Instruments
"""
from .statuscheckedlibrary import (NamedArgtype,
                                   LibraryFunctionInfo,
                                   StatusCheckedLibrary,
                                   LibraryNotFoundError)
import ctypes
from enum import Enum


class DataType(Enum):
    """ DataType is an enumerator, with the intention of abstracting the
    association between datatypes and ctypes within the Python API.
    """
    Bool = 1
    I8 = 2
    U8 = 3
    I16 = 4
    U16 = 5
    I32 = 6
    U32 = 7
    I64 = 8
    U64 = 9
    Sgl = 10
    Dbl = 11
    Fxp = 12
    Cluster = 13

    def __str__(self):
        return self.name

    def _return_ctype(self):
        """ Returns the associated ctype of a given datatype. """
        _datatype_ctype = {
            DataType.Bool: ctypes.c_uint8,
            DataType.I8: ctypes.c_int8,
            DataType.U8: ctypes.c_uint8,
            DataType.I16: ctypes.c_int16,
            DataType.U16: ctypes.c_uint16,
            DataType.I32: ctypes.c_int32,
            DataType.U32: ctypes.c_uint32,
            DataType.I64: ctypes.c_int64,
            DataType.U64: ctypes.c_uint64,
            DataType.Sgl: ctypes.c_float,
            DataType.Dbl: ctypes.c_double,
            DataType.Fxp: ctypes.c_uint32,
            DataType.Cluster: ctypes.c_uint32,
        }
        return _datatype_ctype[self]

    def isSigned(self):
        if self == DataType.I8 \
           or self == DataType.I16 \
           or self == DataType.I32 \
           or self == DataType.I64 \
           or self == DataType.Sgl \
           or self == DataType.Dbl:
            return True
        return False


class FifoPropertyType(Enum):
    """ Types of FIFO Properties, intended to abstract away the C Type. """
    I32 = 1
    U32 = 2
    I64 = 3
    U64 = 4
    Ptr = 5

    def __str__(self):
        return self.name

    def _return_ctype(self):
        """ Returns the associated ctype of a given property type. """
        _propertyType_ctype = {
            FifoPropertyType.I32: ctypes.c_int32,
            FifoPropertyType.U32: ctypes.c_uint32,
            FifoPropertyType.I64: ctypes.c_int64,
            FifoPropertyType.U64: ctypes.c_uint64,
            FifoPropertyType.Ptr: ctypes.c_void_p
        }
        return _propertyType_ctype[self]


class FifoProperty(Enum):
    BytesPerElement = 1  # U32
    BufferAllocationGranularityElements = 2  # U32
    BufferSizeElements = 3  # U64
    MirroredElements = 4  # U64
    DmaBufferType = 5  # I32
    DmaBuffer = 6  # Ptr
    FlowControl = 7  # I32
    ElementsCurrentlyAcquired = 8  # U64
    PreferredNumaNode = 9  # I32

    def __str__(self):
        return self.name


class FlowControl(Enum):
    """ When flow control is disabled, the FIFO no longer acts like a FIFO.
    The FIFO will overwrite data in this mode. The FPGA fully controls when
    data transfers. This can be useful when regenerating a waveform or when
    you only care about the most recent data.
    For Host to Target FIFOs, this only disables flow control when the entire FIFO
    has been written once.
    For Target to Host FIFOs, flow control is disabled on start and the FPGA can
    begin writing then.
    """
    DisableFlowControl = 1
    """ Default FIFO behavior. No data is lost, data only moves when there is
    room for it.
    """
    EnableFlowControl = 2


class DmaBufferType(Enum):
    """ Allocated by RIO means the driver take the other properties and create
    a buffer that meets their requirements.
    """
    AllocatedByRIO = 1
    """ Allocated by User means you will allocate a buffer and set the DMA Buffer
    property with your buffer. The driver will then use this buffer as the
    underlying host memory in the FIFO.
    """
    AllocatedByUser = 2


_fifo_properties_to_types = {
    FifoProperty.BytesPerElement: FifoPropertyType.U32,
    FifoProperty.BufferAllocationGranularityElements: FifoPropertyType.U32,
    FifoProperty.BufferSizeElements: FifoPropertyType.U64,
    FifoProperty.MirroredElements: FifoPropertyType.U64,
    FifoProperty.DmaBufferType: FifoPropertyType.I32,
    FifoProperty.DmaBuffer: FifoPropertyType.Ptr,
    FifoProperty.FlowControl: FifoPropertyType.I32,
    FifoProperty.ElementsCurrentlyAcquired: FifoPropertyType.U64,
    FifoProperty.PreferredNumaNode: FifoPropertyType.I32,
}


class FpgaViState(Enum):
    """ The FPGA VI has either been downloaded and not run, or the VI was aborted
    or reset. """
    NotRunning = 0
    """ An error has occurred. """
    Invalid = 1
    """ The FPGA VI is currently executing. """
    Running = 2
    """ The FPGA VI stopped normally.  This indicates it was not aborted or reset,
    but instead reached the end of any loops it was executing and ended. """
    NaturallyStopped = 3


_SessionType = ctypes.c_uint32
_IrqContextType = ctypes.c_void_p

OPEN_ATTRIBUTE_NO_RUN = 1
OPEN_ATTRIBUTE_BITFILE_PATH_IS_UTF8 = 2
RUN_ATTRIBUTE_WAIT_UNTIL_DONE = 1
CLOSE_ATTRIBUTE_NO_RESET_IF_LAST_SESSION = 1
INFINITE_TIMEOUT = 0xffffffff


class _NiFpga(StatusCheckedLibrary):
    """
    _NiFpga, a thin wrapper around the FPGA Interface C API

    Defines FPGA Interface C API types, and provides the _NiFpga class
    which loads C API symbols and allows them to be called, e.g.
    nifpga.Open(<args>) or nifpga["ReadU32](<args>). If any NiFpga function
    return status is non-zero, the appropriate exception derived from either
    WarningStatus or ErrorStatus is raised.

    While _NiFpga can be used directly, Session provides a higher-level and
    more convenient API that is better-suited for most users.
    """

    def __init__(self):
        library_function_infos = [
            LibraryFunctionInfo(
                pretty_name="Open",
                name_in_library="NiFpgaDll_Open",
                named_argtypes=[
                    NamedArgtype("bitfile path", ctypes.c_char_p),
                    NamedArgtype("signature", ctypes.c_char_p),
                    NamedArgtype("resource", ctypes.c_char_p),
                    NamedArgtype("attribute", ctypes.c_uint32),
                    NamedArgtype("session", ctypes.POINTER(_SessionType)),
                ]),
            LibraryFunctionInfo(
                pretty_name="Run",
                name_in_library="NiFpgaDll_Run",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("attribute", ctypes.c_uint32),
                ]),
            LibraryFunctionInfo(
                pretty_name="Close",
                name_in_library="NiFpgaDll_Close",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("attribute", ctypes.c_uint32),
                ]),
            LibraryFunctionInfo(
                pretty_name="OpenResource",
                name_in_library="NiFpgaDll_OpenResource",
                named_argtypes=[
                    NamedArgtype("parentSession", _SessionType),
                    NamedArgtype("parentIndex", ctypes.c_uint32),
                    NamedArgtype("globalIndex", ctypes.c_uint32),
                    NamedArgtype("childSession", ctypes.POINTER(_SessionType)),
                ]),
            LibraryFunctionInfo(
                pretty_name="AddResources",
                name_in_library="NiFpgaDll_AddResources",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("resourceNames", ctypes.POINTER(ctypes.c_char_p)),
                    NamedArgtype("resourceValues", ctypes.POINTER(ctypes.c_uint32)),
                    NamedArgtype("externalRegisters", ctypes.POINTER(ctypes.c_uint32)),
                    NamedArgtype("numberOfResources", ctypes.c_size_t),
                ]),
            LibraryFunctionInfo(
                pretty_name="GetResourceIndex",
                name_in_library="NiFpgaDll_GetResourceIndex",
                named_argtypes=[
                    NamedArgtype("resourceName", ctypes.c_char_p),
                    NamedArgtype("resourceIndex", ctypes.POINTER(ctypes.c_uint32)),
                ]),
            LibraryFunctionInfo(
                pretty_name="ReleaseResourceIndex",
                name_in_library="NiFpgaDll_ReleaseResourceIndex",
                named_argtypes=[
                    NamedArgtype("resourceName", ctypes.c_char_p),
                ]),
            LibraryFunctionInfo(
                pretty_name="GetResourceName",
                name_in_library="NiFpgaDll_GetResourceName",
                named_argtypes=[
                    NamedArgtype("resourceIndex", ctypes.c_uint32),
                    NamedArgtype("resourceName", ctypes.POINTER(ctypes.c_char_p)),
                ]),
            LibraryFunctionInfo(
                pretty_name="Reset",
                name_in_library="NiFpgaDll_Reset",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                ]),
            LibraryFunctionInfo(
                pretty_name="Abort",
                name_in_library="NiFpgaDll_Abort",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                ]),
            LibraryFunctionInfo(
                pretty_name="Download",
                name_in_library="NiFpgaDll_Download",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                ]),
            LibraryFunctionInfo(
                pretty_name="ReserveIrqContext",
                name_in_library="NiFpgaDll_ReserveIrqContext",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("context", ctypes.POINTER(_IrqContextType)),
                ]),
            LibraryFunctionInfo(
                pretty_name="UnreserveIrqContext",
                name_in_library="NiFpgaDll_UnreserveIrqContext",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("context", _IrqContextType),
                ]),
            LibraryFunctionInfo(
                pretty_name="WaitOnIrqs",
                name_in_library="NiFpgaDll_WaitOnIrqs",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("context", _IrqContextType),
                    NamedArgtype("irqs", ctypes.c_uint32),
                    NamedArgtype("timeout ms", ctypes.c_uint32),
                    NamedArgtype("irqs asserted", ctypes.POINTER(ctypes.c_uint32)),
                    NamedArgtype("timed out", ctypes.POINTER(DataType.Bool._return_ctype())),
                ]),
            LibraryFunctionInfo(
                pretty_name="AcknowledgeIrqs",
                name_in_library="NiFpgaDll_AcknowledgeIrqs",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("irqs", ctypes.c_uint32),
                ]),
            LibraryFunctionInfo(
                pretty_name="AddFifo",
                name_in_library="NiFpgaDll_AddFifo",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("baseAddress", ctypes.c_uint32),
                    NamedArgtype("direction", ctypes.c_uint32),
                    NamedArgtype("bytesPerElement", ctypes.c_uint32),
                ]),
            LibraryFunctionInfo(
                pretty_name="ConfigureFifo",
                name_in_library="NiFpgaDll_ConfigureFifo",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("depth", ctypes.c_size_t),
                ]),
            LibraryFunctionInfo(
                pretty_name="ConfigureFifo2",
                name_in_library="NiFpgaDll_ConfigureFifo2",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("requested depth", ctypes.c_size_t),
                    NamedArgtype("actual depth", ctypes.POINTER(ctypes.c_size_t))
                ]),
            LibraryFunctionInfo(
                pretty_name="StartFifo",
                name_in_library="NiFpgaDll_StartFifo",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                ]),
            LibraryFunctionInfo(
                pretty_name="StopFifo",
                name_in_library="NiFpgaDll_StopFifo",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                ]),
            LibraryFunctionInfo(
                pretty_name="UnreserveFifo",
                name_in_library="NiFpgaDll_UnreserveFifo",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                ]),
            LibraryFunctionInfo(
                pretty_name="ReleaseFifoElements",
                name_in_library="NiFpgaDll_ReleaseFifoElements",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("elements", ctypes.c_size_t),
                ]),
            LibraryFunctionInfo(
                pretty_name="GetPeerToPeerFifoEndpoint",
                name_in_library="NiFpgaDll_GetPeerToPeerFifoEndpoint",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("endpoint", ctypes.POINTER(ctypes.c_uint32)),
                ]),
            LibraryFunctionInfo(
                pretty_name="ClientFunctionCall",
                name_in_library="NiFpgaDll_ClientFunctionCall",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("group", ctypes.c_uint32),
                    NamedArgtype("functionId", ctypes.c_uint32),
                    NamedArgtype("inBuffer", ctypes.c_void_p),
                    NamedArgtype("inBufferSize", ctypes.c_size_t),
                    NamedArgtype("outBuffer", ctypes.c_void_p),
                    NamedArgtype("outBufferSize", ctypes.c_size_t),
                ]),
            LibraryFunctionInfo(
                pretty_name="FindRegisterPrivate",
                name_in_library="NiFpgaDll_FindRegisterPrivate",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("name", ctypes.c_char_p),
                    NamedArgtype("expectedType", ctypes.c_uint32),
                    NamedArgtype("offset", ctypes.POINTER(ctypes.c_uint32)),
                ]),
            LibraryFunctionInfo(
                pretty_name="FindFifoPrivate",
                name_in_library="NiFpgaDll_FindFifoPrivate",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("name", ctypes.c_char_p),
                    NamedArgtype("expectedType", ctypes.c_uint32),
                    NamedArgtype("fifoNumber", ctypes.POINTER(ctypes.c_uint32)),
                ]),
            LibraryFunctionInfo(
                pretty_name="GetFpgaViState",
                name_in_library="NiFpgaDll_GetFpgaViState",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("state", ctypes.POINTER(ctypes.c_uint32)),
                ]),
            LibraryFunctionInfo(
                pretty_name="CommitFifoConfiguration",
                name_in_library="NiFpgaDll_CommitFifoConfiguration",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                ])
        ]  # list of function_infos

        for datatype in DataType:
            if datatype == DataType.Fxp or datatype == DataType.Cluster:
                continue  # Fxp and Cluster do not have named read write entry points.
            type_ctype = datatype._return_ctype()
            library_function_infos.extend([
                LibraryFunctionInfo(
                    pretty_name="Read%s" % datatype,
                    name_in_library="NiFpgaDll_Read%s" % datatype,
                    named_argtypes=[
                        NamedArgtype("session", _SessionType),
                        NamedArgtype("indicator", ctypes.c_uint32),
                        NamedArgtype("value", ctypes.POINTER(type_ctype)),
                    ]),
                LibraryFunctionInfo(
                    pretty_name="Write%s" % datatype,
                    name_in_library="NiFpgaDll_Write%s" % datatype,
                    named_argtypes=[
                        NamedArgtype("session", _SessionType),
                        NamedArgtype("control", ctypes.c_uint32),
                        NamedArgtype("value", type_ctype),
                    ]),
                LibraryFunctionInfo(
                    pretty_name="ReadArray%s" % datatype,
                    name_in_library="NiFpgaDll_ReadArray%s" % datatype,
                    named_argtypes=[
                        NamedArgtype("session", _SessionType),
                        NamedArgtype("indicator", ctypes.c_uint32),
                        NamedArgtype("array", ctypes.POINTER(type_ctype)),
                        NamedArgtype("size", ctypes.c_size_t),
                    ]),
                LibraryFunctionInfo(
                    pretty_name="WriteArray%s" % datatype,
                    name_in_library="NiFpgaDll_WriteArray%s" % datatype,
                    named_argtypes=[
                        NamedArgtype("session", _SessionType),
                        NamedArgtype("control", ctypes.c_uint32),
                        NamedArgtype("array", ctypes.POINTER(type_ctype)),
                        NamedArgtype("size", ctypes.c_size_t),
                    ]),
                LibraryFunctionInfo(
                    pretty_name="ReadFifo%s" % datatype,
                    name_in_library="NiFpgaDll_ReadFifo%s" % datatype,
                    named_argtypes=[
                        NamedArgtype("session", _SessionType),
                        NamedArgtype("fifo", ctypes.c_uint32),
                        NamedArgtype("data", ctypes.POINTER(type_ctype)),
                        NamedArgtype("number of elements", ctypes.c_size_t),
                        NamedArgtype("timeout ms", ctypes.c_uint32),
                        NamedArgtype("elements remaining", ctypes.POINTER(ctypes.c_size_t)),
                    ]),
                LibraryFunctionInfo(
                    pretty_name="WriteFifo%s" % datatype,
                    name_in_library="NiFpgaDll_WriteFifo%s" % datatype,
                    named_argtypes=[
                        NamedArgtype("session", _SessionType),
                        NamedArgtype("fifo", ctypes.c_uint32),
                        NamedArgtype("data", ctypes.POINTER(type_ctype)),
                        NamedArgtype("number of elements", ctypes.c_size_t),
                        NamedArgtype("timeout ms", ctypes.c_uint32),
                        NamedArgtype("empty elements remaining", ctypes.POINTER(ctypes.c_size_t)),
                    ]),
                LibraryFunctionInfo(
                    pretty_name="AcquireFifoReadElements%s" % datatype,
                    name_in_library="NiFpgaDll_AcquireFifoReadElements%s" % datatype,
                    named_argtypes=[
                        NamedArgtype("session", _SessionType),
                        NamedArgtype("fifo", ctypes.c_uint32),
                        NamedArgtype("elements", ctypes.POINTER(ctypes.POINTER(type_ctype))),
                        NamedArgtype("elements requested ", ctypes.c_size_t),
                        NamedArgtype("timeout ms", ctypes.c_uint32),
                        NamedArgtype("elements acquired", ctypes.POINTER(ctypes.c_size_t)),
                        NamedArgtype("elements remaining", ctypes.POINTER(ctypes.c_size_t)),
                    ]),
                LibraryFunctionInfo(
                    pretty_name="AcquireFifoWriteElements%s" % datatype,
                    name_in_library="NiFpgaDll_AcquireFifoWriteElements%s" % datatype,
                    named_argtypes=[
                        NamedArgtype("session", _SessionType),
                        NamedArgtype("fifo", ctypes.c_uint32),
                        NamedArgtype("elements", ctypes.POINTER(ctypes.POINTER(type_ctype))),
                        NamedArgtype("elements requested ", ctypes.c_size_t),
                        NamedArgtype("timeout ms", ctypes.c_uint32),
                        NamedArgtype("elements acquired", ctypes.POINTER(ctypes.c_size_t)),
                        NamedArgtype("elements remaining", ctypes.POINTER(ctypes.c_size_t)),
                    ]),
            ])  # end of library_function_infos.extend() call
        for fifoPropertyType in FifoPropertyType:
            type_ctype = fifoPropertyType._return_ctype()
            library_function_infos.extend([
                LibraryFunctionInfo(
                    pretty_name="GetFifoProperty%s" % fifoPropertyType,
                    name_in_library="NiFpgaDll_GetFifoProperty%s" % fifoPropertyType,
                    named_argtypes=[
                        NamedArgtype("session", _SessionType),
                        NamedArgtype("fifo", ctypes.c_uint32),
                        NamedArgtype("property", ctypes.c_uint32),
                        NamedArgtype("value", ctypes.POINTER(type_ctype)),
                    ]),
                LibraryFunctionInfo(
                    pretty_name="SetFifoProperty%s" % fifoPropertyType,
                    name_in_library="NiFpgaDll_SetFifoProperty%s" % fifoPropertyType,
                    named_argtypes=[
                        NamedArgtype("session", _SessionType),
                        NamedArgtype("fifo", ctypes.c_uint32),
                        NamedArgtype("property", ctypes.c_uint32),
                        NamedArgtype("value", type_ctype),
                    ]),
            ])
        # Add Composite FIFO Functions
        library_function_infos.extend([
            LibraryFunctionInfo(
                pretty_name="ReadFifoComposite",
                name_in_library="NiFpgaDll_ReadFifoComposite",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("data", ctypes.POINTER(ctypes.c_uint8)),
                    NamedArgtype("bytes per element", ctypes.c_uint32),
                    NamedArgtype("number of elements", ctypes.c_size_t),
                    NamedArgtype("timeout ms", ctypes.c_uint32),
                    NamedArgtype("elements remaining", ctypes.POINTER(ctypes.c_size_t)),
                ]),
            LibraryFunctionInfo(
                pretty_name="WriteFifoComposite",
                name_in_library="NiFpgaDll_WriteFifoComposite",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("data", ctypes.POINTER(ctypes.c_uint8)),
                    NamedArgtype("bytes per element", ctypes.c_uint32),
                    NamedArgtype("number of elements", ctypes.c_size_t),
                    NamedArgtype("timeout ms", ctypes.c_uint32),
                    NamedArgtype("empty elements remaining", ctypes.POINTER(ctypes.c_size_t)),
                ]),
            LibraryFunctionInfo(
                pretty_name="AcquireFifoReadElementsComposite",
                name_in_library="NiFpgaDll_AcquireFifoReadElementsComposite",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("elements", ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8))),
                    NamedArgtype("bytes per element", ctypes.c_uint32),
                    NamedArgtype("elements requested ", ctypes.c_size_t),
                    NamedArgtype("timeout ms", ctypes.c_uint32),
                    NamedArgtype("elements acquired", ctypes.POINTER(ctypes.c_size_t)),
                    NamedArgtype("elements remaining", ctypes.POINTER(ctypes.c_size_t)),
                ]),
            LibraryFunctionInfo(
                pretty_name="AcquireFifoWriteElementsComposite",
                name_in_library="NiFpgaDll_AcquireFifoWriteElementsComposite",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("elements", ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8))),
                    NamedArgtype("bytes per element", ctypes.c_uint32),
                    NamedArgtype("elements requested ", ctypes.c_size_t),
                    NamedArgtype("timeout ms", ctypes.c_uint32),
                    NamedArgtype("elements acquired", ctypes.POINTER(ctypes.c_size_t)),
                    NamedArgtype("elements remaining", ctypes.POINTER(ctypes.c_size_t)),
                ]),
        ])
        # Add Acquire FIFO Region functions
        library_function_infos.extend([
            LibraryFunctionInfo(
                pretty_name="AcquireFifoReadRegion",
                name_in_library="NiFpgaDll_AcquireFifoReadRegion",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("region", ctypes.POINTER(ctypes.c_void_p)),
                    NamedArgtype("elements", ctypes.POINTER(ctypes.c_void_p)),
                    NamedArgtype("is signed", ctypes.c_bool),
                    NamedArgtype("bytes per element", ctypes.c_uint32),
                    NamedArgtype("elements requested ", ctypes.c_size_t),
                    NamedArgtype("timeout ms", ctypes.c_uint32),
                    NamedArgtype("elements acquired", ctypes.POINTER(ctypes.c_size_t)),
                    NamedArgtype("elements remaining", ctypes.POINTER(ctypes.c_size_t)),
                ]),
            LibraryFunctionInfo(
                pretty_name="AcquireFifoWriteRegion",
                name_in_library="NiFpgaDll_AcquireFifoWriteRegion",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("region", ctypes.POINTER(ctypes.c_void_p)),
                    NamedArgtype("elements", ctypes.POINTER(ctypes.c_void_p)),
                    NamedArgtype("is signed", ctypes.c_bool),
                    NamedArgtype("bytes per element", ctypes.c_uint32),
                    NamedArgtype("elements requested ", ctypes.c_size_t),
                    NamedArgtype("timeout ms", ctypes.c_uint32),
                    NamedArgtype("elements acquired", ctypes.POINTER(ctypes.c_size_t)),
                    NamedArgtype("elements remaining", ctypes.POINTER(ctypes.c_size_t)),
                ]),
            LibraryFunctionInfo(
                pretty_name="ReleaseFifoRegion",
                name_in_library="NiFpgaDll_ReleaseFifoRegion",
                named_argtypes=[
                    NamedArgtype("session", _SessionType),
                    NamedArgtype("fifo", ctypes.c_uint32),
                    NamedArgtype("region", ctypes.c_void_p)
                ]),
        ])
        try:
            super(_NiFpga, self).__init__(library_name="NiFpga",
                                          library_function_infos=library_function_infos)
        except LibraryNotFoundError as e:
            import platform
            system = platform.system().lower()
            if system == 'windows':
                raise LibraryNotFoundError(
                    "Unable to find NiFpga.dll on your system, "
                    "ensure you have installed the relevent RIO distribution for your device. "
                    "Search for your product here: http://www.ni.com/downloads/ni-drivers/ "
                    "Original Exception: " + str(e))
            if system == 'linux':
                raise LibraryNotFoundError(
                    "Unable to find libNiFpga.so on your system, "
                    "If you are on desktop linux, ensure you have installed the latest "
                    "RIO Linux distribution for your product, such as https://www.ni.com/en-us/support/downloads/drivers/download.ni-linux-device-drivers.html "
                    "If you are on a Linux RT embedded target (cRIO, sbRIO, FlexRIO, Industrial Controller, etc) install NI-RIO to your target "
                    "though MAX following these instructions: https://www.ni.com/getting-started/set-up-hardware/compactrio/controller-software "
                    "Original Exception: " + str(e))
            if system == 'darwin':
                raise LibraryNotFoundError(
                    "Unable to find NiFpga.Framework on your system, "
                    "Sorry we don't yet support using RIO Devices on OSX, contact your sales person "
                    "for the latest information on OSX support. "
                    "Original Exception: " + str(e))
            raise
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/session.py sha256=c3954448a977c124de0c4f79201b280684411511534de0f741a54f3c74688f84 bytes=53896 -->
## FILE: nifpga/session.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/session.py`
- sha256: `c3954448a977c124de0c4f79201b280684411511534de0f741a54f3c74688f84`
- bytes: 53896

````python
"""
Session, a convenient wrapper around the low-level _NiFpga class.

Copyright (c) 2017 National Instruments
"""

from .nifpga import (_SessionType, _IrqContextType, _NiFpga, DataType,
                     OPEN_ATTRIBUTE_NO_RUN, RUN_ATTRIBUTE_WAIT_UNTIL_DONE,
                     CLOSE_ATTRIBUTE_NO_RESET_IF_LAST_SESSION, FifoProperty,
                     _fifo_properties_to_types, FlowControl, DmaBufferType,
                     FpgaViState, OPEN_ATTRIBUTE_BITFILE_PATH_IS_UTF8)
from .bitfile import Bitfile
from .status import ErrorStatus, InvalidSessionError
from collections import namedtuple
import ctypes
from builtins import bytes
from math import ceil
import locale
try:
    # Python 2
    xrange
except NameError:
    # Python 3
    xrange = range


class Session(object):
    """
    Session, a convenient wrapper around the low-level _NiFpga class.

    The Session class uses regular python types, provides convenient default
    arguments to C API functions, and makes controls, indicators, and FIFOs
    available by name. If any NiFpga function return status is non-zero, the
    appropriate exception derived from either WarningStatus or ErrorStatus is
    raised.
    Example usage of FPGA configuration functions::

        with Session(bitfile="myBitfilePath.lvbitx", resource="RIO0") as session:
            session.run()
            session.download()
            session.abort()
            session.reset()

    Note:
        It is always recommended that you use a Session with a context manager
        (with). Opening a Session without a context manager could cause you to
        leak the session if :meth:`Session.close` is not called.

    Controls and indicators are accessed directly via a _Register object
    obtained from the session::

        my_control = session.registers["MyControl"]
        my_control.write(data=4)
        data = my_control.read()

    FIFOs are accessed directly via a _FIFO object obtained from the session::

        myHostToFpgaFifo = session.fifos["MyHostToFpgaFifo"]
        myHostToFpgaFifo.stop()
        actual_depth = myHostToFpgaFifo.configure(requested_depth=4096)
        myHostToFpgaFifo.start()
        empty_elements_remaining = myHostToFpgaFifo.write(data=[1, 2, 3, 4],
                                                          timeout_ms=2)

        myFpgaToHostFifo = session.fifos["MyHostToFpgaFifo"]
        read_values = myFpgaToHostFifo.read(number_of_elements=4,
                                            timeout_ms=0)
        print(read_values.data)
    """

    def __init__(self,
                 bitfile,
                 resource,
                 no_run=False,
                 reset_if_last_session_on_exit=False,
                 **kwargs):
        """Creates a session to the specified resource with the specified
        bitfile.

        Args:
            bitfile (str)(Bitfile): A bitfile.Bitfile() instance or a string
                                    filepath to a bitfile.
            resource (str): e.g. "RIO0", "PXI1Slot2", or "rio://hostname/RIO0"
                            or an already open session
            no_run (bool): If true, don't run the bitfile, just open the
                session.
            reset_if_last_session_on_exit (bool): Passed into Close on
                exit. Unused if not using this session as a context guard.
            **kwargs: Additional arguments that edit the session.
        """
        if not isinstance(bitfile, Bitfile):
            """ The bitfile we were passed is a path to an lvbitx."""
            bitfile = Bitfile(bitfile)
        self._nifpga = _NiFpga()
        self._session = _SessionType()

        open_attribute = 0
        for key, value in kwargs.items():
            if key == '_open_attribute':
                open_attribute = value

        if no_run:
            open_attribute = open_attribute | OPEN_ATTRIBUTE_NO_RUN

        if isinstance(resource, _SessionType):
            self._session = resource
        else:
            # Newer versions of the driver support utf-8 paths, but the python API
            # supports old drivers too, so see if codepage will work and if not use UTF-8
            try:
                bitfile_path = bytes(bitfile.filepath, locale.getpreferredencoding())
            except UnicodeEncodeError:
                bitfile_path = bytes(bitfile.filepath, 'utf-8')
                open_attribute = open_attribute | OPEN_ATTRIBUTE_BITFILE_PATH_IS_UTF8
            bitfile_signature = bytes(bitfile.signature, 'ascii')
            resource = bytes(resource, 'ascii')
            self._nifpga.Open(bitfile_path,
                              bitfile_signature,
                              resource,
                              open_attribute,
                              self._session)

        self._reset_if_last_session_on_exit = reset_if_last_session_on_exit
        self._registers = {}
        self._internal_registers_dict = {}
        base_address_on_device = bitfile.base_address_on_device()
        for name, bitfile_register in bitfile.registers.items():
            assert name not in self._registers, \
                "One or more registers have the same name '%s', this is not supported" % name
            register = self._create_register(bitfile_register,
                                             base_address_on_device)
            if bitfile_register.is_internal():
                self._internal_registers_dict[name] = register
            else:
                self._registers[name] = register

        self._fifos = {}
        for name, bitfile_fifo in bitfile.fifos.items():
            assert name not in self._fifos, \
                "One or more FIFOs have the same name '%s', this is not supported" % name
            self._fifos[name] = self._create_fifo(bitfile_fifo)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.close(reset_if_last_session=self._reset_if_last_session_on_exit)
        except InvalidSessionError:
            pass
        except ErrorStatus:
            if exception_type is None:
                raise

    def close(self, reset_if_last_session=False):
        """ Closes the FPGA Session.

        Args:
            reset_if_last_session (bool): If True, resets the FPGA on the
                last close. If true, does not reset the FPGA on the last
                session close.
        """
        close_attr = CLOSE_ATTRIBUTE_NO_RESET_IF_LAST_SESSION if reset_if_last_session is False else 0
        self._nifpga.Close(self._session, close_attr)

    def run(self, wait_until_done=False):
        """ Runs the FPGA VI on the target.

        Args:
            wait_until_done (bool): If true, this functions blocks until the
                                    FPGA VI stops running
        """
        run_attr = RUN_ATTRIBUTE_WAIT_UNTIL_DONE if wait_until_done else 0
        self._nifpga.Run(self._session, run_attr)

    def abort(self):
        """ Aborts the FPGA VI. """
        self._nifpga.Abort(self._session)

    def download(self):
        """ Re-downloads the FPGA bitstream to the target. """
        self._nifpga.Download(self._session)

    def reset(self):
        """ Resets the FPGA VI. """
        self._nifpga.Reset(self._session)

    @property
    def fpga_vi_state(self):
        """ Returns the current state of the FPGA VI. """
        state = ctypes.c_uint32()
        self._nifpga.GetFpgaViState(self._session, state)
        return FpgaViState(state.value)

    def _irq_ordinals_to_bitmask(self, ordinals):
        bitmask = 0
        for ordinal in ordinals:
            assert 0 <= ordinal and ordinal <= 31, "Valid IRQs are 0-31: %d is invalid" % ordinal
            bitmask |= (1 << ordinal)
        return bitmask

    WaitOnIrqsReturnValues = namedtuple('WaitOnIrqsReturnValues',
                                        ["irqs_asserted", "timed_out"])

    def wait_on_irqs(self, irqs, timeout_ms):
        """ Stops the calling thread until the FPGA asserts any IRQ in the irqs
        parameter or until the function call times out.

        Args:
            irqs: A list of irq ordinals 0-31, e.g. [0, 6, 31].
            timeout_ms: The timeout to wait in milliseconds.

        Returns:
            session_wait_on_irqs (namedtuple)::

                session_wait_on_irqs.irqs_asserted (list): is a list of the
                    asserted IRQs.
                session_wait_on_irqs.timed_out (bool): Outputs whether or not
                    the time out expired before all irqs were asserted.

        """
        if type(irqs) != list:
            irqs = [irqs]
        irqs_bitmask = self._irq_ordinals_to_bitmask(irqs)

        context = _IrqContextType()
        self._nifpga.ReserveIrqContext(self._session, context)

        irqs_asserted_bitmask = ctypes.c_uint32(0)
        timed_out = DataType.Bool._return_ctype()()
        try:
            self._nifpga.WaitOnIrqs(self._session,
                                    context,
                                    irqs_bitmask,
                                    timeout_ms,
                                    irqs_asserted_bitmask,
                                    timed_out)
        finally:
            self._nifpga.UnreserveIrqContext(self._session, context)
        irqs_asserted = [i for i in range(32) if irqs_asserted_bitmask.value & (1 << i)]
        return self.WaitOnIrqsReturnValues(irqs_asserted=irqs_asserted,
                                           timed_out=bool(timed_out.value))

    def acknowledge_irqs(self, irqs):
        """ Acknowledges an IRQ or set of IRQs.

        Args:
            irqs (list): A list of irq ordinals 0-31, e.g. [0, 6, 31].
        """
        self._nifpga.AcknowledgeIrqs(self._session,
                                     self._irq_ordinals_to_bitmask(irqs))

    def _get_unique_register_or_fifo(self, name):
        assert not (name in self._registers and name in self._fifos), \
            "Ambiguous: '%s' is both a register and a FIFO" % name
        assert name in self._registers or name in self._fifos, \
            "Unknown register or FIFO '%s'" % name
        try:
            return self._registers[name]
        except KeyError:
            return self._fifos[name]

    @property
    def registers(self):
        """ This property returns a dictionary containing all registers that
        are associated with the bitfile opened with the session. A register can
        be accessed by its unique name.
        """
        return self._registers

    @property
    def _internal_registers(self):
        """ This property contains internal registers"""
        return self._internal_registers_dict

    @property
    def fifos(self):
        """ This property returns a dictionary containing all FIFOs that are
        associated with the bitfile opened with the session. A FIFO can be
        accessed by its unique name.
        """
        return self._fifos

    def _create_register(self, bitfile_register, base_address_on_device):
        # simple C type registers use the same entrypoint as the C API
        if bitfile_register.type.is_c_api_type:
            if bitfile_register.is_array():
                return _ArrayRegister(self._session,
                                      self._nifpga,
                                      bitfile_register,
                                      base_address_on_device)
            else:
                return _Register(self._session,
                                 self._nifpga,
                                 bitfile_register,
                                 base_address_on_device)
        else:  # register that handles conversion for more complex types
            return _DataConvertingRegister(self._session,
                                           self._nifpga,
                                           bitfile_register,
                                           base_address_on_device)

    def _create_fifo(self, bitfile_fifo):
        if bitfile_fifo.is_fxp():
            return _FxpFIFO(self._session, self._nifpga, bitfile_fifo)
        elif bitfile_fifo.is_composite():
            return _DataConvertingFifo(self._session, self._nifpga, bitfile_fifo)
        else:
            return _FIFO(self._session, self._nifpga, bitfile_fifo)


class _Register(object):
    """ _Register is a private class that is a wrapper of logic that is
    associated with controls and indicators.

    All Registers will exists in a sessions session.registers property. This
    means that all possible registers for a given session are created during
    session initialization; a user should never need to create a new instance
    of this class.

    """
    def __init__(self,
                 session,
                 nifpga,
                 bitfile_register,
                 base_address_on_device,
                 read_func=None,
                 write_func=None):
        self._datatype = bitfile_register.datatype
        self._name = bitfile_register.name
        self._session = session
        if read_func is None:
            self._read_func = nifpga["Read%s" % self.datatype]
        else:
            self._read_func = read_func
        if write_func is None:
            self._write_func = nifpga["Write%s" % self.datatype]
        else:
            self._write_func = write_func
        self._ctype_type = self._datatype._return_ctype()
        self._type = bitfile_register.type
        self._resource = bitfile_register.offset + base_address_on_device
        if bitfile_register.access_may_timeout():
            self._resource = self._resource | 0x80000000

    def __len__(self):
        """ A single register will always have one and only one element.

        Returns:
            (int): Always a constant 1.
        """
        return 1

    def write(self, data):
        """ Writes the specified data to the control or indicator

        Args:
            data (DataType.value): The data to be written into the register
        """
        self._write_func(self._session, self._resource, data)

    def read(self):
        """ Reads a single element from the control or indicator

        Returns:
            data (DataType.value): The data inside the register.
        """
        data = self._ctype_type()
        self._read_func(self._session, self._resource, data)
        if self._datatype is DataType.Bool:
            return bool(data.value)
        return data.value

    @property
    def name(self):
        """ Property of a register that returns the name of the control or
        indicator. """
        return self._name

    @property
    def datatype(self):
        """ Property of a register that returns the datatype of the control or
        indicator. """
        return self._datatype


class _ArrayRegister(_Register):
    """
    _ArryRegister is a private class that inherits from _Register with
    additional interfaces unique to the logic of array controls and indicators.
    """
    def __init__(self,
                 session,
                 nifpga,
                 bitfile_register,
                 base_address_on_device):
        super(_ArrayRegister, self).__init__(session,
                                             nifpga,
                                             bitfile_register,
                                             base_address_on_device,
                                             read_func=nifpga["ReadArray%s" % bitfile_register.datatype],
                                             write_func=nifpga["WriteArray%s" % bitfile_register.datatype])
        self._num_elements = len(bitfile_register)
        self._ctype_type = self._ctype_type * self._num_elements

    def __len__(self):
        """ Returns the length of the array.

        Returns:
            (int): The number of elements in the array.
        """
        return self._num_elements

    def write(self, data):
        """ Writes the specified array of data to the control or indicator

            Args:
                data (list): The data "array" to be written into the registers
                wrapped into a python list.
        """
        # if data is not iterable make it iterable
        try:
            iter(data)
        except TypeError:
            data = [data]
        assert len(data) == len(self), \
            "Bad data length %d for register '%s', expected %s" \
            % (len(data), self._name, len(self))
        buf = self._ctype_type(*data)
        self._write_func(self._session, self._resource, buf, len(self))

    def read(self):
        """ Reads the entire array from the control or indicator.

        Returns:
            (list): The data in the register in a python list.
        """
        buf = self._ctype_type()
        self._read_func(self._session, self._resource, buf, len(self))
        val = [bool(elem) if self._datatype is DataType.Bool else elem for elem in buf]
        return val


class _DataConvertingRegister(_Register):
    """
    _DataConvertingRegister does all the work of converting the LabVIEW Cluster
    and fixed point types into something more native to python. As a
    user you will read and write to this register just as you would any other
    register. Given the nature of fixed point there are a few caveats.

    Just like the other registers, we do not support users creating their
    instances of _FxpRegister, but after opening a session to a valid bitfile
    the session.registers property will contain all registers fixed point
    included.

    Fixed point registers should be easily used from python with a few caveats:
        1. Trying to write a value that does not conform to boundaries of the
        defined register, will be coerced just as it would in labVIEW. Input
        a value that needs to be coerced will result in a warning to the user.
        A value is to be coerced if it is not a multiple of the delta value, or
        if it exceeds the minimum or maximum values.
    """
    def __init__(self,
                 session,
                 nifpga,
                 bitfile_register,
                 base_address_on_device):
        super(_DataConvertingRegister, self).__init__(
            session,
            nifpga,
            bitfile_register,
            base_address_on_device,
            read_func=nifpga["ReadArray%s" % DataType.U32],
            write_func=nifpga["WriteArray%s" % DataType.U32])
        self._transfer_len = int(ceil(self._type.size_in_bits / 32.0))
        self._ctype_type = self._ctype_type * self._transfer_len

    def read(self):
        """ Reads the value from the control or indicator

        Returns:
            data (value_type): The data inside the register.
        """
        buf = self._ctype_type()
        self._read_func(self._session, self._resource, buf, self._transfer_len)
        read_array = [elem for elem in buf]
        fpga_representation = self._combine_array_of_u32_into_one_value(read_array)
        return self._type.unpack_data(fpga_representation)

    def _combine_array_of_u32_into_one_value(self, data):
        """ This method is a helper to convert the array read from hardware
        and return a single value removing any excessive bits. Whenever
        the array is longer than 1 element, the data is left justified, we need
        to shift the combined data to the right before doing the conversion.
        For example, if the register had a word length of 54, the 54 MSB would
        be the fixed point bits. The 10 LSB of the combinedData must be shifted
        off in order to not mess up further calculations.

        """
        combinedData = 0
        for index in range(0, self._transfer_len):
            combinedData = (combinedData << 32) + data[index]
        if self._transfer_len > 1:
            combinedData = combinedData >> (32 * self._transfer_len - self._type.size_in_bits)
        return combinedData

    def write(self, user_input):
        """ Writes the user's the users input into the register as a fixed
        point number. Any inputs outside the bounds of this fixed point
        register will be coerced and the user will be warned. The user input's
        supported include any python Number.

            Args:
                Number: user numerical input to be converted to fixed point.
                (bool, Number): Tuple with the members : Boolean for overflow,
                                user numerical input to be converted to fixed
                                point.
        """
        fpga_representation = self._type.pack_data(user_input, 0)
        arrayData = self._convert_to_u32_array(fpga_representation)
        buf = self._ctype_type(*arrayData)
        self._write_func(self._session, self._resource, buf, self._transfer_len)

    def _convert_to_u32_array(self, data):
        if self._transfer_len > 1:
            data = data << (32 * self._transfer_len - self._type.size_in_bits)

        mask_32bit = (2**32) - 1
        extracted_array = []
        for index in range(0, self._transfer_len):
            extracted_array.append(data & mask_32bit)
            data = data >> 32
        extracted_array.reverse()
        return extracted_array


class _FIFO(object):
    """ _FIFO is a private class that is a wrapper for the logic that
    associated with a FIFO.

    All FIFOs will exists in a sessions session.fifos property. This means that
    all possible FIFOs for a given session are created during session
    initialization; a user should never need to create a new instance of this
    class.
    """
    def __init__(self,
                 session,
                 nifpga,
                 bitfile_fifo,
                 datatype=None):
        self._datatype = datatype
        if self._datatype is None:
            self._datatype = bitfile_fifo.datatype
        self._number = bitfile_fifo.number
        self._session = session
        self._transfer_size_bytes = bitfile_fifo.transfer_size_bytes
        self._write_func = nifpga["WriteFifo%s" % self._datatype]
        self._read_func = nifpga["ReadFifo%s" % self._datatype]
        self._acquire_read_func = nifpga["AcquireFifoReadElements%s" % self._datatype]
        self._acquire_write_func = nifpga["AcquireFifoWriteElements%s" % self._datatype]
        self._release_elements_func = nifpga["ReleaseFifoElements"]
        self._nifpga = nifpga
        self._ctype_type = self._datatype._return_ctype()
        self._name = bitfile_fifo.name
        self._type = bitfile_fifo.type

    def configure(self, requested_depth):
        """ Specifies the depth of the host memory part of the DMA FIFO.

        Args:
            requested_depth (int): The depth of the host memory part of the DMA
                                   FIFO in number of elements.

        Returns:
            actual_depth (int): The actual number of elements in the host
            memory part of the DMA FIFO, which may be more than the
            requested number.
        """
        actual_depth = ctypes.c_size_t()
        self._nifpga.ConfigureFifo2(self._session, self._number,
                                    requested_depth, actual_depth)
        return actual_depth.value

    def start(self):
        """ Starts the FIFO. """
        self._nifpga.StartFifo(self._session, self._number)

    def stop(self):
        """ Stops the FIFO. """
        self._nifpga.StopFifo(self._session, self._number)

    def unreserve(self):
        """ Unreserves the FIFO.

        FIFOs are reserved by the first process that uses them.  This call will
        unreserve them from the calling process so a different process may use
        the FIFO.
        """
        self._nifpga.UnreserveFifo(self._session, self._number)

    def write(self, data, timeout_ms=0):
        """ Writes the specified data to the FIFO.

        NOTE:
            If the FIFO has not been started before calling
            :meth:`_FIFO.write()`, then it will automatically start and
            continue to work as expected.

        Args:
            data (list): Data to be written to the FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            elements_remaining (int): The number of elements remaining in the
            host memory part of the DMA FIFO.
        """
        # if data is not iterable make it iterable
        try:
            iter(data)
        except TypeError:
            data = [data]
        buf_type = self._ctype_type * len(data)
        buf = buf_type(*data)
        empty_elements_remaining = ctypes.c_size_t()
        self._write_func(self._session,
                         self._number,
                         buf,
                         len(data),
                         timeout_ms,
                         empty_elements_remaining)
        return empty_elements_remaining.value

    ReadValues = namedtuple("ReadValues", ["data", "elements_remaining"])

    def read(self, number_of_elements, timeout_ms=0):
        """ Read the specified number of elements from the FIFO.

        NOTE:
            If the FIFO has not been started before calling
            :meth:`_FIFO.read()`, then it will automatically start and continue
            to work as expected.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            ReadValues (namedtuple)::

                ReadValues.data (list): containing the data from
                    the FIFO.
                ReadValues.elements_remaining (int): The amount of elements
                    remaining in the FIFO.
        """
        buf_type = self._ctype_type * number_of_elements
        buf = buf_type()
        elements_remaining = ctypes.c_size_t()
        self._read_func(self._session,
                        self._number,
                        buf,
                        number_of_elements,
                        timeout_ms,
                        elements_remaining)
        if self._datatype is DataType.Bool:
            data = [bool(elem) for elem in buf]
        else:
            data = [elem for elem in buf]
        return self.ReadValues(data=data,
                               elements_remaining=elements_remaining.value)

    AcquireWriteValues = namedtuple("AcquireWriteValues",
                                    ["data", "elements_acquired",
                                     "elements_remaining"])

    def _acquire_write(self, number_of_elements, timeout_ms=0):
        """ Write the specified number of elements from the FIFO.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            AcquireWriteValues(namedtuple)::

                AcquireWriteValues.data (ctypes.pointer): Contains the data
                    from the FIFO.
                AcquireWriteValues.elements_acquired (int): The number of
                    elements that were actually acquired.
                AcquireWriteValues.elements_remaining (int): The amount of
                    elements remaining in the FIFO.
        """
        block_out = ctypes.POINTER(self._ctype_type)()
        elements_acquired = ctypes.c_size_t()
        elements_remaining = ctypes.c_size_t()
        self._acquire_write_func(self._session,
                                 self._number,
                                 block_out,
                                 number_of_elements,
                                 timeout_ms,
                                 elements_acquired,
                                 elements_remaining)
        return self.AcquireWriteValues(data=block_out,
                                       elements_acquired=elements_acquired.value,
                                       elements_remaining=elements_remaining.value)

    AcquireReadValues = namedtuple("AcquireReadValues",
                                   ["data", "elements_acquired",
                                    "elements_remaining"])

    def _acquire_read(self, number_of_elements, timeout_ms=0):
        """ Read the specified number of elements from the FIFO.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            AcquireReadValues(namedtuple): has the following members::

                AcquireReadValues.data (ctypes.pointer): Contains the data
                    from the FIFO.
                AcquireReadValues.elements_acquired (int): The number of
                    elements that were actually acquired.
                AcquireReadValues.elements_remaining (int): The amount of
                    elements remaining in the FIFO.
        """
        buf = self._ctype_type()
        buf_ptr = ctypes.pointer(buf)
        elements_acquired = ctypes.c_size_t()
        elements_remaining = ctypes.c_size_t()
        self._acquire_read_func(self._session,
                                self._number,
                                buf_ptr,
                                number_of_elements,
                                timeout_ms,
                                elements_acquired,
                                elements_remaining)
        return self.AcquireReadValues(data=buf_ptr,
                                      elements_acquired=elements_acquired.value,
                                      elements_remaining=elements_remaining.value)

    def _release_elements(self, number_of_elements):
        """ Releases the FIFOs elements. """
        self._release_elements_func(self._session, self._number, number_of_elements)

    AcquireRegionValues = namedtuple("AcquireRegionValues",
                                     ["region", "elements_acquired",
                                      "elements_remaining"])

    def acquire_read_region(self, number_of_elements, timeout_ms=0):
        """ Acquire regions of the FIFO's buffer directly.

        This function can be useful if you are going to access large sections of
        FIFO buffer at one time and don't want a copy of it in memory.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            AcquireRegionValues(namedtuple): has the following members::

                AcquireRegionValues.region (_FIFODataRegion): A region that can
                    be used with a content manager to access elements in the FIFO.
                AcquireRegionValues.elements_acquired (int): The number of
                    elements that were actually acquired.
                AcquireRegionValues.elements_remaining (int): The amount of
                    elements remaining in the FIFO.
        """
        buf = ctypes.c_void_p()
        buf_ptr = ctypes.pointer(buf)
        region = ctypes.c_void_p()
        region_ptr = ctypes.pointer(region)
        elements_acquired = ctypes.c_size_t()
        elements_remaining = ctypes.c_size_t()
        signed = self._datatype.isSigned()
        self._nifpga["AcquireFifoReadRegion"](self._session,
                                              self._number,
                                              region_ptr,
                                              buf_ptr,
                                              signed,
                                              self._transfer_size_bytes,
                                              number_of_elements,
                                              timeout_ms,
                                              elements_acquired,
                                              elements_remaining)
        casted_buffer = ctypes.cast(buf_ptr[0], ctypes.POINTER(self._ctype_type))
        region = ctypes.cast(region_ptr[0], ctypes.c_void_p)
        accessor = _FIFODataAccessor(casted_buffer, self._type, self._transfer_size_bytes, elements_acquired.value)
        fifo_region = _FIFODataRegion(accessor, region, self)
        return self.AcquireRegionValues(region=fifo_region,
                                        elements_acquired=elements_acquired.value,
                                        elements_remaining=elements_remaining.value)

    def acquire_write_region(self, number_of_elements, timeout_ms=0):
        """ Acquire regions of the FIFO's buffer directly.

        This function can be useful if you are going to access large sections of
        FIFO buffer at one time and don't want a copy of it in memory.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            AcquireRegionValues(namedtuple): has the following members::

                AcquireRegionValues.region (_FIFODataRegion): A region that can
                    be used with a content manager to access elements in the FIFO.
                AcquireRegionValues.elements_acquired (int): The number of
                    elements that were actually acquired.
                AcquireRegionValues.elements_remaining (int): The amount of
                    elements remaining in the FIFO.
        """
        buf = ctypes.c_void_p()
        buf_ptr = ctypes.pointer(buf)
        region = ctypes.c_void_p()
        region_ptr = ctypes.pointer(region)
        elements_acquired = ctypes.c_size_t()
        elements_remaining = ctypes.c_size_t()
        signed = self._datatype.isSigned()
        self._nifpga["AcquireFifoWriteRegion"](self._session,
                                               self._number,
                                               region_ptr,
                                               buf_ptr,
                                               signed,
                                               self._transfer_size_bytes,
                                               number_of_elements,
                                               timeout_ms,
                                               elements_acquired,
                                               elements_remaining)
        casted_buffer = ctypes.cast(buf_ptr[0], ctypes.POINTER(self._ctype_type))
        region = ctypes.cast(region_ptr[0], ctypes.c_void_p)
        accessor = _FIFODataAccessor(casted_buffer, self._type, self._transfer_size_bytes, elements_acquired.value)
        fifo_region = _FIFODataRegion(accessor, region, self)
        return self.AcquireRegionValues(region=fifo_region,
                                        elements_acquired=elements_acquired.value,
                                        elements_remaining=elements_remaining.value)

    def release_region(self, accessor):
        """ Releases a region.

        Args:
            accessor (_FIFODataAccessor): the accessor from the acquired region
        """
        self._nifpga["ReleaseFifoRegion"](self._session, self._number, accessor._region)

    def get_peer_to_peer_endpoint(self):
        """ Gets an endpoint reference to a peer-to-peer FIFO. """
        endpoint = ctypes.c_uint32(0)
        self._nifpga.GetPeerToPeerFifoEndpoint(self._session, self._number, endpoint)
        return endpoint.value

    def commit_configuration(self):
        """ Resolves and Commits property changes made to the FIFO. """
        self._nifpga.CommitFifoConfiguration(self._session, self._number)

    @property
    def name(self):
        """ Property of a Fifo that contains its name. """
        return self._name

    @property
    def datatype(self):
        """ Property of a Fifo that contains its datatype. """
        return self._datatype

    def _get_fifo_property(self, prop):
        prop_type = _fifo_properties_to_types[prop]
        value = (prop_type._return_ctype())(0)
        value_pointer = ctypes.pointer(value)
        self._nifpga['GetFifoProperty%s' % prop_type](self._session, self._number, prop.value, value_pointer)
        return value.value

    def _set_fifo_property(self, prop, value):
        prop_type = _fifo_properties_to_types[prop]
        self._nifpga['SetFifoProperty%s' % prop_type](self._session, self._number, prop.value, value)

    @property
    def buffer_allocation_granularity(self):
        """ The allocation granularity of the host memory part of a DMA FIFO.

        By default this will usually be a page size, which is optimal for most
        devices.  This property can be used to customize it.
        """
        return self._get_fifo_property(FifoProperty.BufferAllocationGranularityElements)

    @buffer_allocation_granularity.setter
    def buffer_allocation_granularity(self, value):
        self._set_fifo_property(FifoProperty.BufferAllocationGranularityElements, value)

    @property
    def buffer_size(self):
        """ The size in elements of the Host Memory part of a DMA FIFO. """
        return self._get_fifo_property(FifoProperty.BufferSizeElements)

    @buffer_size.setter
    def buffer_size(self, value):
        self._set_fifo_property(FifoProperty.BufferSizeElements, value)

    @property
    def _mirror_size(self):
        """ The amount of elements in the Host Memory part of the DMA FIFO that
        mirror elements at the beginning.

        The Host Memory part of a DMA FIFO is a circular buffer.  This means that
        when we hit the end of the buffer we have to deal with the logic of wrapping
        around the buffer.  Mirrored elements are elements at the beginning of
        the buffer that are mapped twice in memory to the end of the buffer.
        Settings this value can allow us to avoid wrap arounds.

        This is mostly useful when using our Zero Copy API.  Its not yet
        supported in Python though, so this property is private.
        """
        return self._get_fifo_property(FifoProperty.MirroredElements)

    @_mirror_size.setter
    def _mirror_size(self, value):
        self._set_fifo_property(FifoProperty.MirroredElements, value)

    @property
    def _dma_buffer_type(self):
        return self._get_fifo_property(FifoProperty.DmaBufferType)

    @_dma_buffer_type.setter
    def _dma_buffer_type(self, value):
        if not isinstance(value, DmaBufferType):
            raise TypeError("_dma_buffer_type must be set to a nifpga.DmaBufferType")
        self._set_fifo_property(FifoProperty.DmaBufferType, value.value)

    @property
    def _dma_buffer(self):
        return self._get_fifo_property(FifoProperty.DmaBuffer)

    @_dma_buffer.setter
    def _dma_buffer(self, value):
        self._set_fifo_property(FifoProperty.DmaBuffer, value)

    @property
    def flow_control(self):
        """ Controls whether the FPGA will wait for the host when using FIFOs.

        If flow control is disabled, the FPGA will have free reign to read or
        write elements before the host is ready.  This means the FIFO no longer
        acts in a First In First Out manner.

        For Host To Target FIFOs, this feature is useful when you want to put
        something like a waveform in a FIFO and let the FPGA continue reading
        that waveform over and over without any involvement from the host.

        For Target To Host FIFOs, this feature is useful when you only care
        about the latest data and don't care about old data.
        """
        return self._get_fifo_property(FifoProperty.FlowControl)

    @flow_control.setter
    def flow_control(self, value):
        if not isinstance(value, FlowControl):
            raise TypeError("flow_control must be set to an nifpga.FlowControl")
        self._set_fifo_property(FifoProperty.FlowControl, value.value)

    @property
    def elements_currently_acquired(self):
        return self._get_fifo_property(FifoProperty.ElementsCurrentlyAcquired)

    @property
    def preferred_numa_node(self):
        return self._get_fifo_property(FifoProperty.PreferredNumaNode)

    @preferred_numa_node.setter
    def preferred_numa_node(self, value):
        self._set_fifo_property(FifoProperty.PreferredNumaNode, value)


class _FxpFIFO(_FIFO):
    """
    FXP FIFOs are packed up to 64bits
    """
    def __init__(self,
                 session,
                 nifpga,
                 bitfile_fifo):
        super(_FxpFIFO, self).__init__(session,
                                       nifpga,
                                       bitfile_fifo,
                                       datatype=DataType.U64)

    @property
    def datatype(self):
        return DataType.Fxp

    def write(self, data, timeout_ms=0):
        """ Writes the specified data to the FIFO.

        NOTE:
            If the FIFO has not been started before calling
            :meth:`_FIFO.write()`, then it will automatically start and
            continue to work as expected.

        Args:
            data (list): Data to be written to the FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            elements_remaining (int): The number of elements remaining in the
            host memory part of the DMA FIFO.
        """
        # if data is not iterable make it iterable
        try:
            iter(data)
        except TypeError:
            data = [data]
        buf_type = self._ctype_type * len(data)
        buf = buf_type()
        for i, item in enumerate(data):
            buf[i] = self._type.pack_data(item, 0)
        empty_elements_remaining = ctypes.c_size_t()
        self._write_func(self._session,
                         self._number,
                         buf,
                         len(data),
                         timeout_ms,
                         empty_elements_remaining)
        return empty_elements_remaining.value

    def read(self, number_of_elements, timeout_ms=0):
        """ Read the specified number of elements from the FIFO.

        NOTE:
            If the FIFO has not been started before calling
            :meth:`_FIFO.read()`, then it will automatically start and continue
            to work as expected.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            ReadValues (namedtuple)::

                ReadValues.data (list): containing the data from
                    the FIFO.
                ReadValues.elements_remaining (int): The amount of elements
                    remaining in the FIFO.
        """
        buf_type = self._ctype_type * number_of_elements
        buf = buf_type()
        elements_remaining = ctypes.c_size_t()
        self._read_func(self._session,
                        self._number,
                        buf,
                        number_of_elements,
                        timeout_ms,
                        elements_remaining)
        data = _FIFODataAccessor(buf, self._type, 8, number_of_elements)
        return self.ReadValues(data=data,
                               elements_remaining=elements_remaining.value)


def _combine_array_of_u8_into_one_value(data, element_index, transfer_size_bytes, size_in_bits):
    """ This method is a helper to convert the array read from hardware
    and return a single element removing any excessive bits.

    First we combine the data into a single number while swapping the
    endianness.

    Whenever the array is longer than 1 word, the data is left justified, we
    need to shift the combined data to the right before doing the
    conversion.
    For example, if the element had a size in bits of 54, the 54 MSB would
    be the data bits. The 10 LSB of the combinedData must be shifted
    off in order to not mess up further calculations.
    """
    combinedData = 0
    if transfer_size_bytes >= 4:
        index = element_index
        element_end = element_index + transfer_size_bytes
        while index < element_end:
            combinedData = (combinedData << 8) + data[index + 3]
            combinedData = (combinedData << 8) + data[index + 2]
            combinedData = (combinedData << 8) + data[index + 1]
            combinedData = (combinedData << 8) + data[index]
            index += 4
    elif transfer_size_bytes == 2:
        combinedData = data[element_index + 1]
        combinedData = (combinedData << 8) + data[element_index]
    else:
        combinedData = data[element_index]
    if transfer_size_bytes > 4:
        combinedData = combinedData >> (8 * transfer_size_bytes - size_in_bits)
    return combinedData


def _convert_to_u8_array(u8_array, element_index, data, transfer_size_bytes, size_in_bits):
    """ Converts the data into the format expected by the FPGA FIFO and inserts it
    into the given u8_array at the provided element_index.
    """
    # if the element is > 4 bytes, shift the data over
    if transfer_size_bytes > 4:
        data = data << (8 * transfer_size_bytes - size_in_bits)
    if transfer_size_bytes == 1:
        u8_array[element_index] = data & 0xFF
    elif transfer_size_bytes == 2:
        u8_array[element_index] = data & 0xFF
        data = data >> 8
        u8_array[element_index + 1] = data & 0xFF
    else:  # >= 4
        # Insert the data such that the Most Significant Words are at the lower
        # indexes while each word's endianness is swapped
        for index in reversed(range(0, transfer_size_bytes, 4)):
            local_index = element_index + index
            u8_array[local_index] = data & 0xFF
            data = data >> 8
            u8_array[local_index + 1] = data & 0xFF
            data = data >> 8
            u8_array[local_index + 2] = data & 0xFF
            data = data >> 8
            u8_array[local_index + 3] = data & 0xFF
            data = data >> 8


class _DataConvertingFifo(_FIFO):
    """
    Converts FIFOs that transfer data that is packed in the FPGA representation
    into Python types.  In this case, it converts a FIFO of clusters into lists
    of OrderedDicts and back.
    """
    def __init__(self,
                 session,
                 nifpga,
                 bitfile_fifo):
        super(_DataConvertingFifo, self).__init__(session,
                                                  nifpga,
                                                  bitfile_fifo,
                                                  datatype=DataType.U8)
        self._write_func = nifpga["WriteFifoComposite"]
        self._read_func = nifpga["ReadFifoComposite"]
        self._acquire_read_func = nifpga["AcquireFifoReadElementsComposite"]
        self._acquire_write_func = nifpga["AcquireFifoWriteElementsComposite"]

    @property
    def datatype(self):
        return DataType.Cluster

    def write(self, data, timeout_ms=0):
        # If data is a dict, then the customer passed us a single cluster
        # put it into a list before using it.
        if isinstance(data, dict):
            data = [data]
        buf_type = self._ctype_type * (self._transfer_size_bytes * len(data))
        buf = buf_type()
        # for each element, pack the data, reverse the bytes, and swap the
        # endianness
        for index, item in enumerate(data):
            packed_element = self._type.pack_data(item, 0)
            element_index = index * self._transfer_size_bytes
            _convert_to_u8_array(buf, element_index, packed_element, self._transfer_size_bytes, self._type.size_in_bits)
        empty_elements_remaining = ctypes.c_size_t()
        self._write_func(self._session,
                         self._number,
                         buf,
                         self._transfer_size_bytes,
                         len(data),
                         timeout_ms,
                         empty_elements_remaining)
        return empty_elements_remaining.value

    def read(self, number_of_elements, timeout_ms=0):
        buf_type = self._ctype_type * (self._transfer_size_bytes * number_of_elements)
        buf = buf_type()
        elements_remaining = ctypes.c_size_t()
        self._read_func(self._session,
                        self._number,
                        buf,
                        self._transfer_size_bytes,
                        number_of_elements,
                        timeout_ms,
                        elements_remaining)
        data = _FIFODataAccessor(buf, self._type, self._transfer_size_bytes, number_of_elements)
        return self.ReadValues(data=data,
                               elements_remaining=elements_remaining.value)


class _FIFODataAccessor(object):
    """
        Accesses FIFO Data element by element.
    """
    def __init__(self, buffer, type, bytes_per_element, number_of_elements):
        self._buffer = buffer
        self._type = type
        self._bytes_per_element = bytes_per_element
        self._number_of_elements = number_of_elements

    def __iter__(self):
        if self._type.datatype is DataType.Cluster:
            for index in xrange(self._number_of_elements):
                element_index = index * self._bytes_per_element
                packed_data = _combine_array_of_u8_into_one_value(self._buffer, element_index, self._bytes_per_element, self._type.size_in_bits)
                yield self._type.unpack_data(packed_data)
        elif self._type.datatype is DataType.Fxp:
            for index in xrange(self._number_of_elements):
                yield self._type.unpack_data(self._buffer[index])
        elif self._type.datatype is DataType.Bool:
            for index in xrange(self._number_of_elements):
                yield bool(self._buffer[index])
        else:
            for index in xrange(self._number_of_elements):
                yield self._buffer[index]

    def __getitem__(self, index):
        if index < 0 or index > self._number_of_elements:
            raise KeyError()
        if self._type.datatype is DataType.Cluster:
            element_index = index * self._bytes_per_element
            packed_data = _combine_array_of_u8_into_one_value(self._buffer, element_index, self._bytes_per_element, self._type.size_in_bits)
            return self._type.unpack_data(packed_data)
        elif self._type.datatype is DataType.Fxp:
            return self._type.unpack_data(self._buffer[index])
        elif self._type.datatype is DataType.Bool:
            return bool(self._buffer[index])
        else:
            return self._buffer[index]

    def __setitem__(self, index, value):
        if index < 0 or index > self._number_of_elements:
            raise KeyError()
        if self._type.datatype is DataType.Cluster:
            element_index = index * self._bytes_per_element
            packed_element = self._type.pack_data(value, 0)
            _convert_to_u8_array(self._buffer, element_index, packed_element, self._bytes_per_element, self._type.size_in_bits)
        elif self._type.datatype is DataType.Fxp:
            self._buffer[index] = self._type.pack_data(value, 0)
        else:
            self._buffer[index] = value

    def __len__(self):
        return self._number_of_elements

    def __eq__(self, other):
        if len(other) != self._number_of_elements:
            return False
        for index in xrange(0, self._number_of_elements):
            if self[index] != other[index]:
                return False
        return True

    def __str__(self):
        string_value = "["
        for index in xrange(0, self._number_of_elements):
            string_value += str(self[index])
            if (index + 1) < self._number_of_elements:
                string_value += ", "
        return string_value + "]"

    def __repr__(self):
        return str(self)


class _FIFODataRegion(object):
    def __init__(self, accessor, region, fifo):
        self._accessor = accessor
        self._region = region
        self._fifo = fifo
        self._released = False

    def __enter__(self):
        return self._accessor

    def __exit__(self, exception_type, exception_val, trace):
        self.release()

    @property
    def accessor(self):
        return self.accessor

    def release(self):
        if not self._released:
            self._accessor = None
            self._fifo.release_region(self)
            self._released = True
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/status.py sha256=1345291fc80a4827f513ba17e12a1bce1eda4fd6fd4b0a16899485d221b403f3 bytes=15005 -->
## FILE: nifpga/status.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/status.py`
- sha256: `1345291fc80a4827f513ba17e12a1bce1eda4fd6fd4b0a16899485d221b403f3`
- bytes: 15005

````python
"""
An set of status exception classes to be used when an NiFpga
function returns either a warning or error status.

Use check_status() to raise an appropriate exception if necessary.

Error and Warning exception class names are auto-generated from the
strings in 'codeToString' in this file.
For example, handle a fatal error like this:

    >>> @check_status('frob', ['foo', 'bar', 'baz'])
    ... def frob(foo, bar, baz):
    ...     return -61141
    ...
    >>> try:
    ...     frob(0, 1, 2)
    ... except FpgaBusyError as e:
    ...     print(e)  # doctest: +NORMALIZE_WHITESPACE
    Error: FpgaBusy (-61141) when calling 'frob' with arguments:
        foo: 0x0
        bar: 0x1
        baz: 0x2

Or handle a warning like this:

    >>> @check_status('frob', ['foo', 'bar', 'baz'])
    ... def frob(foo, bar, baz):
    ...     return 61003
    ...
    >>> with warnings.catch_warnings(record=True) as w:
    ...     frob(0, 1, 2)
    ...     print(w[0].message)  # doctest: +NORMALIZE_WHITESPACE
    Warning: FpgaAlreadyRunning (61003) when calling 'frob' with arguments:
        foo: 0x0
        bar: 0x1
        baz: 0x2

Copyright (c) 2017 National Instruments
"""
import functools
import warnings


def _raise_or_warn_if_nonzero_status(status, function_name, argument_names, *args):
    """
    Helper for the 'check_status' decorator.

    Raises the proper ErrorStatus subclass or warns the proper WarnStatus
    subclass if status is not 0 (success).

    function_name: the name of the function, e.g. "NiFpga_ConfigureFifo"
        Used to make the exception message more useful.
    argument_names: list of names of the arguments to the function
        e.g. ["session", "fifo"]
    args: the arguments that were passed to the function

    'argument_names' and 'args' are used to make the exception message
    more useful, and to find the arguments after catching an exception if
    the function fails (e.g. 'e.get_args()["session"]').
    """
    if status == 0:
        return

    if status in codes_to_exception_classes:
        if status < 0:
            raise codes_to_exception_classes[status](function_name, argument_names, *args)
        else:
            warning = codes_to_exception_classes[status](function_name, argument_names, *args)
            warnings.warn(warning)
    else:
        if status < 0:
            raise UnknownError(status, function_name, argument_names, *args)
        else:
            warnings.warn(UnknownWarning(status, function_name, argument_names, *args))


def check_status(function_name, argument_names):
    """
    Decorator (that takes arguments) to call a function and raise
    an appropriate subclass of Status if the
    returned status is not zero.
    Also validates that the number of parameters passed to the
    function is correct.

    function_name: the name of the function, e.g. "NiFpga_ConfigureFifo"
        Used to make the exception message more useful.
    argument_names: list of names of the arguments to the function
        e.g. ["session", "fifo"]
        Used to make the exception message more useful, and to find the
        arguments after catching an exception if the function fails
        (e.g. 'e.get_args()["session"]').
    """
    def decorator(function):
        @functools.wraps(function)
        def internal(*args):
            if hasattr(function, "argtypes") and len(args) != len(function.argtypes):
                raise TypeError("%s takes exactly %u arguments (%u given)"
                                % (function_name, len(function.argtypes), len(args)))
            status = function(*args)
            _raise_or_warn_if_nonzero_status(status, function_name, argument_names, args)
        return internal
    return decorator


class Status(BaseException):
    def __init__(self, code, code_string, function_name, argument_names,
                 function_args):
        """ Base exception class for when an NiFpga function returns a non-zero
        status.

        Args:
            code (int): e.g. -52000
            code_string (str) : e.g. 'MemoryFull'
            function_name (string): the function that returned the error or
                warning status. e.g. 'NiFpga_ConfigureFifo'
            argument_names (list): a list of the names of the arguments to the
                function. e.g. ["session", "fifo", "requested depth"]
            function_args (tuple) : a tuple of the arguments passed to the
                function. The order of argument_names should correspond to the
                order of function_args. e.g. '(session, fifo, depth)'
        """
        self._code = code
        self._code_string = code_string
        self._function_name = function_name

        self._named_args = []
        for i, arg in enumerate(function_args):
            self._named_args.append(
                {
                    "name": argument_names[i],
                    "value": arg
                })
        # this is also necessary to properly reconstruct the object when
        # passing it between processes
        super(Status, self).__init__(self._code,
                                     self._code_string,
                                     self._function_name,
                                     self._named_args)

    def get_code(self):
        return self._code

    def get_code_string(self):
        return self._code_string

    def get_function_name(self):
        """ Returns a string for the functions name, """
        return self._function_name

    def get_args(self):
        """
        Returns a dictionary of argument names to argument values of
        the function that caused the exception to be raised.

        Returns:
        arg_dict (dictionary): Converts ctypes args to their actual values
        instead of the  ctypes instance. e.g.

        .. code-block:: python

            {
            "session":0x10000L,
            "fifo" : 0x0,
            ...}



        """
        arg_dict = {}
        for arg in self._named_args:
            # ctypes types all have a member named 'value'.
            value = arg["value"].value if hasattr(arg["value"], "value") else arg["value"]
            arg_dict[arg["name"]] = value
        return arg_dict

    def _stringify_arg(self, arg):
        """
        Converts a function argument to a readable string for debugging.

        Stringify ctypes values, instead of the ctypes instance itself.
        Adds single quotes around strings (so it's obvious they are strings).
        Stringify numbers as hex to make it easier to decode
        bit packed sessions, attributes, etc.
        """
        # ctypes types all have a member named 'value'.
        if hasattr(arg, "value"):
            return self._stringify_arg(arg.value)

        if isinstance(arg, str):
            return "'%s'" % arg

        try:
            return hex(arg)
        except TypeError:
            return str(arg)

    def __str__(self):
        """
        Returns the function name, status code, and arguments used.
        Example:

        .. code-block:: python

            Error: FifoTimeout (-50400) when calling 'Dummy Function Name' with
            arguments:
                session: 0xbeef
                fifo: 0xf1f0L
                data: 0xda7aL
                number of elements: 0x100L
                timeout ms: 0x200L
                elements remaining: 0x300L
                a bogus string argument: 'I am a string'
        """
        arg_string = ""
        for arg in self._named_args:
            arg_string += "\n\t%s: %s" % (arg["name"], self._stringify_arg(arg["value"]))
        return "%s: %s (%d) when calling '%s' with arguments:%s" \
            % ("Error" if self._code < 0 else "Warning",
               self._code_string,
               self._code,
               self._function_name,
               arg_string)


class WarningStatus(Status, RuntimeWarning):
    """
    Base warning class for when an NiFpga function returns a warning (> 0)
    status.

    Useful if trying to catch warning and error status exceptions separately
    """
    def __init__(self, code, code_string, function_name, argument_names,
                 function_args):
        super(WarningStatus, self).__init__(code, code_string, function_name,
                                            argument_names, function_args)


class ErrorStatus(Status, RuntimeError):
    """
    Base Error class for when an NiFpga function returns an error (< 0)
    status.

    Useful if trying to catch warning and error status exceptions separately
    """
    def __init__(self, code, code_string, function_name, argument_names,
                 function_args):
        super(ErrorStatus, self).__init__(code, code_string, function_name,
                                          argument_names, function_args)


class UnknownWarning(WarningStatus):
    def __init__(self, code, function_name, argument_names, function_args):
        super(UnknownWarning, self).__init__(code=code,
                                             code_string="Unknown code",
                                             function_name=function_name,
                                             argument_names=argument_names,
                                             function_args=function_args)


class UnknownError(ErrorStatus):
    def __init__(self, code, function_name, argument_names, function_args):
        super(UnknownError, self).__init__(code=code,
                                           code_string="Unknown code",
                                           function_name=function_name,
                                           argument_names=argument_names,
                                           function_args=function_args)


# Define error codes and their names.
# Each code in this list will be codegened into two classes, e.g.:
#   FifoTimeoutError (for code -50400)
#   FifoTimeoutWarning (for code 50400)
error_codes = [
    (-50400, "FifoTimeout"),
    (-50405, "TransferAborted"),
    (-52000, "MemoryFull"),
    (-52003, "SoftwareFault"),
    (-52005, "InvalidParameter"),
    (-52006, "ResourceNotFound"),
    (-52007, "OperationTimedOut"),
    (-52008, "OSFault"),
    (-52010, "ResourceNotInitialized"),
    (-52012, "EndOfData"),
    (-52013, "ObjectNameCollision"),
    (-61003, "FpgaAlreadyRunning"),
    (-61018, "DownloadError"),
    (-61024, "DeviceTypeMismatch"),
    (-61046, "CommunicationTimeout"),
    (-61060, "IrqTimeout"),
    (-61070, "CorruptBitfile"),
    (-61072, "BadDepth"),
    (-61073, "BadReadWriteCount"),
    (-61083, "ClockLostLock"),
    (-61141, "FpgaBusy"),
    (-61200, "FpgaBusyFpgaInterfaceCApi"),
    (-61201, "FpgaBusyScanInterface"),
    (-61202, "FpgaBusyFpgaInterface"),
    (-61203, "FpgaBusyInteractive"),
    (-61204, "FpgaBusyEmulation"),
    (-61211, "ResetCalledWithImplicitEnableRemoval"),
    (-61212, "AbortCalledWithImplicitEnableRemoval"),
    (-61213, "CloseAndResetCalledWithImplicitEnableRemoval"),
    (-61214, "ImplicitEnableRemovalButNotYetRun"),
    (-61215, "RunAfterStoppedCalledWithImplicitEnableRemoval"),
    (-61216, "GatedClockHandshakingViolation"),
    (-61217, "RegionsOutstandingForSession"),
    (-61219, "ElementsNotPermissibleToBeAcquired"),
    (-61252, "FpgaBusyConfiguration"),
    (-61253, "CloseCalledWithResetNotSupported"),
    (-61254, "RunAfterStoppedNotSupported"),
    (-61499, "InternalError"),
    (-63003, "TotalDmaFifoDepthExceeded"),
    (-63033, "AccessDenied"),
    (-63038, "HostVersionMismatch"),
    (-63040, "RpcConnectionError"),
    (-63041, "RpcServerError"),
    (-63042, "NetworkFault"),
    (-63043, "RpcSessionError"),
    (-63044, "RpcServerMissing"),
    (-63045, "FeatureNotSupportedOverRpc"),
    (-63046, "UsingRemoteSessionForLocalTarget"),
    (-63050, "TriggerReserved"),
    (-63051, "TriggerNotReserved"),
    (-63080, "BufferInvalidSize"),
    (-63081, "BufferNotAllocated"),
    (-63082, "FifoReserved"),
    (-63083, "FifoElementsCurrentlyAcquired"),
    (-63084, "MisalignedAccess"),
    (-63085, "ControlOrIndicatorTooLarge"),
    (-63086, "OperationNotSupportedWhileStarted"),
    (-63087, "TypesDoNotMatch"),
    (-63088, "OutOfFifoRegions"),
    (-63101, "BitfileReadError"),
    (-63106, "SignatureMismatch"),
    (-63107, "IncompatibleBitfile"),
    (-63150, "HardwareFault"),
    (-63170, "PowerShutdown"),
    (-63171, "ThermalShutdown"),
    (-63180, "InvalidAliasName"),
    (-63181, "AliasNotFound"),
    (-63182, "InvalidDeviceAccess"),
    (-63183, "InvalidPort"),
    (-63184, "ChildDeviceNotInserted"),
    (-63192, "InvalidResourceName"),
    (-63193, "FeatureNotSupported"),
    (-63194, "VersionMismatch"),
    (-63195, "InvalidSession"),
    (-63196, "InvalidAttribute"),
    (-63198, "OutOfHandles"),
]

# create an exception class for each error code and add to dictionary
# ie FifoTimeoutWarning, FifoTimeoutError
codes_to_exception_classes = {}
_g = globals()
for code, code_string in error_codes:
    # we need introduce a scope, otherwise code, and code_string
    # will all reference the same value.
    def add_classes(code, code_string):
        classname = code_string + 'Error'

        def __init__(self, function_name, argument_names, function_args):
            ErrorStatus.__init__(self,
                                 code=code,
                                 code_string=code_string,
                                 function_name=function_name,
                                 argument_names=argument_names,
                                 function_args=function_args)
        error_class = type(classname, (ErrorStatus,),
                           {'__init__': __init__, 'CODE': code})
        codes_to_exception_classes[code] = error_class
        # copy the exception type into module globals
        _g[error_class.__name__] = error_class

        classname = code_string + 'Warning'

        def __init__(self, function_name, argument_names, function_args):
            WarningStatus.__init__(self,
                                   code=-code,
                                   code_string=code_string,
                                   function_name=function_name,
                                   argument_names=argument_names,
                                   function_args=function_args)
        warning_class = type(classname, (WarningStatus,),
                             {'__init__': __init__, 'CODE': -code})
        codes_to_exception_classes[-code] = warning_class
        # copy the warning type into module globals
        _g[warning_class.__name__] = warning_class

    add_classes(code, code_string)
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/statuscheckedlibrary.py sha256=3a100a9cf0f546cb8bd526f75e1235d524de6eccd014514294bb4e398dffa007 bytes=8555 -->
## FILE: nifpga/statuscheckedlibrary.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/statuscheckedlibrary.py`
- sha256: `3a100a9cf0f546cb8bd526f75e1235d524de6eccd014514294bb4e398dffa007`
- bytes: 8555

````python
from .status import check_status, VersionMismatchError
import ctypes
import ctypes.util

StatusType = ctypes.c_int32


class FunctionInfo(object):
    def __init__(self, function, name, argument_names):
        """
        A struct describing a function to be used in StatusCheckedFunctions.
        Args:
            function (str): the callable function itself
            name (str): A name used to call 'function'
                e.g. "ReadFifoU32".
                See 'StatusCheckedFunctions' to see this parameter's usage
                and how functions are called with this name.
            argument_names (list): a list of the strings of the arguments to
            'function'
                e.g. ["session",
                        "fifo",
                        "data",
                        "number of elements",
                        "timeout ms",
                        "elements remaining"]
                Used for printing helpful messages if the function fails,
                and to get arguments after catching an exception if
                the function fails (e.g. 'e.get_args()["session"]').
        """
        self.function = function
        self.name = name
        self.argument_names = argument_names

    def __str__(self):
        return ("FunctionInfo"
                + "\n\tFunction: %s" % self.function
                + "\n\tName: %s" % self.name
                + "\n\tArguments:"
                + "\n\t\t%s" % "\n\t\t".join(self.argument_names))


class StatusCheckedFunctions(object):
    def __init__(self, function_infos):
        """
        A class to wrap functions that return an Status error code. Each
        function is wrapped with a closure that raises an appropriate derived
        class of Status if the returned error code is non-zero.

        Args:
            function_infos (list): A list of FunctionInfo objects

        The name from each FunctionInfo can be used to call its associated
        function, e.g.::

            def my_raw_func(code)
                return code

            checked_functions = \
                    StatusCheckedFunctions(
                        function_infos=[\
                            FunctionInfo(
                                function=my_raw_func,
                                name="MyFunc",
                                argument_names="code to return")
                        ])

            # This raises FifoTimeoutError with a useful error message
            # mentioning all arguments, such as 'code to return'.
            checked_functions.MyFunc(-50400)

            # Returns with no exceptions thrown
            checked_functions.MyFunc(0)

            # You can also call functions using the bracket operator.
            # This raises FifoTimeoutWarning.
            checked_functions["MyFunc"](50400)
        """
        # dictionary of function names to a closure that wraps a
        # function with a status check
        self._wrapped_functions = {}
        for function_info in function_infos:
            decorator = check_status(function_info.function.__name__,
                                     function_info.argument_names)
            closure = decorator(function_info.function)

            # e.g. "self.Open = closure"
            # So now "<this object>.Open(...)" works
            setattr(self, function_info.name, closure)

            # Store closure this so __getitem__ can provide more convenience
            self._wrapped_functions[function_info.name] = closure

    def __getitem__(self, key):
        """
        Override bracket operator to call wrapped functions.

        For convenience when function names are dynamically built, e.g.,
        makes this work:
            datatype = "U64"
            <this object>['ReadArray%s' % datatype](session, ...)
        """
        return self._wrapped_functions[key]


class NamedArgtype(object):
    def __init__(self, name, argtype):
        """
        A struct of a name and ctypes argtype for a function argument
        to be used in a LibraryFunctionInfo.
        name: e.g. "session"
            Used for printing helpful messages if the function fails,
            and to get arguments after catching an exception if
            the function fails (e.g. 'e.get_args()["session"]').
        argtype: e.g. "ctypes.c_uint32", the ctypes type of the argument
        """
        self.name = name
        self.argtype = argtype


class LibraryFunctionInfo(object):
    def __init__(self, pretty_name, name_in_library, named_argtypes):
        """
        A struct describing a library entry point function to be used
        in StatusCheckedLibrary.
        pretty_name: e.g. "Run"
            A "pretty" name by which a StatusCheckedLibrary object will
            call the function.
        name_in_library: e.g. "NiFpgaDll_Run"
            The name of the actual DLL entry point used to call the function.
        named_argtypes: e.g. [NamedArgtype("session", _SessionType),
                                NamedArgtype("fifo", ctypes.c_uint32)]
            A list of NamedArgtype structs used to call the function.
        """
        self.pretty_name = pretty_name
        self.name_in_library = name_in_library
        self.named_argtypes = named_argtypes


class LibraryNotFoundError(RuntimeError):
    pass


class StatusCheckedLibrary(StatusCheckedFunctions):
    def __init__(self, library_name, library_function_infos):
        """
        Raises exceptions from entry points that return NiFpga_Status codes.

        library_name: e.g. "NiFpga" (libNiFpga.so, NiFpga.dll)
        library_function_infos: a list of library_function_info objects

        Automatically wraps each entry point named in library_function_infos
        with a closure that raises an appropriate derived class of
        Status if the returned error code is non-zero.

        The pretty_name from the LibraryFunctionInfo's passed to the
        constructor can be used to call functions in the library, e.g.:
            cool_library = \
                StatusCheckedLibrary(
                    library_name="CoolLibrary",  # CoolLibrary.dll, libCoolLibrary.so
                    library_function_infos=[\
                        LibraryFunctionInfo(
                            pretty_name="AwesomeFunction",
                            name_in_library="CoolLibraryEntrypoint_AwesomeFunction",
                            named_argtypes=[NamedArgtype("session", ctypes.c_uint32)])
                    ])

            # Both lines below call "CoolLibraryEntrypoint_AwesomeFunction()"
            # from CoolLibrary.dll (or libCoolLibrary.so) with '7' as a uint32_t
            # argument.
            cool_library.AwesomeFunction(7)
            cool_library["AwesomeFunction"](7)
        """
        library = ctypes.util.find_library(library_name)
        if library is None:
            raise LibraryNotFoundError(library_name)
        library = ctypes.cdll.LoadLibrary(library)
        function_infos = []
        for lfi in library_function_infos:
            try:
                func = getattr(library, lfi.name_in_library)  # i.e., dlsym()
                # ctypes functions have special 'argtypes' and 'restype' fields
                # that we set, so ctypes can automatically convert types and knows
                # how to call into the library.
                func.argtypes = [named_argtype.argtype for named_argtype in lfi.named_argtypes]
                # Assume that everything returns an NiFpga_Status
                func.restype = StatusType
            except AttributeError:
                # if we can't find the symbol, instead insert a function that
                # always returns the VersionMismatch error, that way they can
                # use the rest of the API
                def returnsVersionMismatchError(*args, **kwargs):
                    """ Always returns the version mismatch error code. """
                    return VersionMismatchError.CODE
                func = returnsVersionMismatchError
            function_infos.append(
                FunctionInfo(function=func,
                             name=lfi.pretty_name,
                             argument_names=[named_argtype.name for named_argtype in lfi.named_argtypes]))
        super(StatusCheckedLibrary, self).__init__(function_infos)
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/tests/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: nifpga/tests/__init__.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/tests/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/tests/allregistertypes.lvbitx sha256=b79f4ecd829ce8de9122bd246d0fb4bcc31b000a31afc9c2215d96c296e6bc7e bytes=194985 -->
## FILE: nifpga/tests/allregistertypes.lvbitx

- repository: `ni/nifpga-python`
- source_path: `nifpga/tests/allregistertypes.lvbitx`
- sha256: `b79f4ecd829ce8de9122bd246d0fb4bcc31b000a31afc9c2215d96c296e6bc7e`
- bytes: 194985

````text
<?xml version="1.0" encoding="UTF-8"                 ?>
<Bitfile>
	<BitfileVersion>4.0</BitfileVersion>
	<Documentation>
		  <BuildSpecVersion>1.0.0</BuildSpecVersion>
		  <BuildSpecDescription>Test Bitfile Description</BuildSpecDescription>
	</Documentation>
	<SignatureRegister>11D7986409F418C50DCF65F91C759A9D</SignatureRegister>
	<SignatureGuids>57582923F80D3869DB116511EF8DBC8C</SignatureGuids>
	<SignatureNames>2F736CF3BB1BBB8755B585BC9527A2C2</SignatureNames>
	<TimeStamp/>
	<CompilationStatus/>
	<BitstreamVersion>2</BitstreamVersion>
	<VI>
		  <Name>FPGA.vi</Name>
		  <RegisterList>
			  <Register>
				    <Name>Input Array Bool</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array Bool</Name>
						      <Size>33</Size>
						      <Type>
							      <Boolean>
								        <Name>OutputBool 3</Name>
							</Boolean>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>1300800000000002001240210C4F7574707574426F6F6C203300001E4040000180000021000010496E70757420417272617920426F6F6C00000100010000002100000000000000000000000000000000000000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98304</Offset>
				    <SizeInBits>33</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>0</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array Bool</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array Bool</Name>
						      <Size>33</Size>
						      <Type>
							      <Boolean>
								        <Name>OutputBool 3</Name>
							</Boolean>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>1300800000000002001240210C4F7574707574426F6F6C203300001E40400001800000210000114F757470757420417272617920426F6F6C000100010000002100000000000000000000000000000000000000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98308</Offset>
				    <SizeInBits>33</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>1</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array I8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array I8</Name>
						      <Size>5</Size>
						      <Type>
							      <I8>
								        <Name>OutputI8 3</Name>
							</I8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114001000A4F75747075744938203300001C404000018000000500000E496E707574204172726179204938000001000100000005000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98312</Offset>
				    <SizeInBits>40</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>2</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array I8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array I8</Name>
						      <Size>5</Size>
						      <Type>
							      <I8>
								        <Name>OutputI8 3</Name>
							</I8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114001000A4F75747075744938203300001C404000018000000500000F4F75747075742041727261792049380001000100000005000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98316</Offset>
				    <SizeInBits>40</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>3</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array U8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array U8</Name>
						      <Size>6</Size>
						      <Type>
							      <U8>
								        <Name>OutputI8 3</Name>
							</U8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114005000A4F75747075744938203300001C404000018000000600000E496E70757420417272617920553800000100010000000600000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98320</Offset>
				    <SizeInBits>48</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>4</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array U8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array U8</Name>
						      <Size>6</Size>
						      <Type>
							      <U8>
								        <Name>OutputI8 3</Name>
							</U8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114005000A4F75747075744938203300001C404000018000000600000F4F7574707574204172726179205538000100010000000600000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98324</Offset>
				    <SizeInBits>48</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>5</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array I16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array I16</Name>
						      <Size>3</Size>
						      <Type>
							      <I16>
								        <Name>OutputI8 3</Name>
							</I16>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114002000A4F75747075744938203300001C404000018000000300000F496E70757420417272617920493136000100010000000300000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98328</Offset>
				    <SizeInBits>48</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>6</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array I16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array I16</Name>
						      <Size>3</Size>
						      <Type>
							      <I16>
								        <Name>OutputI8 3</Name>
							</I16>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114002000A4F75747075744938203300001E40400001800000030000104F75747075742041727261792049313600000100010000000300000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98332</Offset>
				    <SizeInBits>48</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>7</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array U16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array U16</Name>
						      <Size>4</Size>
						      <Type>
							      <U16>
								        <Name>OutputI8 3</Name>
							</U16>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114006000A4F75747075744938203300001C404000018000000400000F496E707574204172726179205531360001000100000004000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98336</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>8</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array U16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array U16</Name>
						      <Size>4</Size>
						      <Type>
							      <U16>
								        <Name>OutputI8 3</Name>
							</U16>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114006000A4F75747075744938203300001E40400001800000040000104F757470757420417272617920553136000001000100000004000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98340</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>9</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array I32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array I32</Name>
						      <Size>2</Size>
						      <Type>
							      <I32>
								        <Name>OutputI8 3</Name>
							</I32>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114003000A4F75747075744938203300001C404000018000000200000F496E707574204172726179204933320001000100000002000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98344</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>10</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array I32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array I32</Name>
						      <Size>2</Size>
						      <Type>
							      <I32>
								        <Name>OutputI8 3</Name>
							</I32>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114003000A4F75747075744938203300001E40400001800000020000104F757470757420417272617920493332000001000100000002000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98348</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>11</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array U32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array U32</Name>
						      <Size>3</Size>
						      <Type>
							      <U32>
								        <Name>OutputI8 3</Name>
							</U32>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114007000A4F75747075744938203300001C404000018000000300000F496E70757420417272617920553332000100010000000300000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98352</Offset>
				    <SizeInBits>96</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>12</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array U32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array U32</Name>
						      <Size>3</Size>
						      <Type>
							      <U32>
								        <Name>OutputI8 3</Name>
							</U32>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114007000A4F75747075744938203300001E40400001800000030000104F75747075742041727261792055333200000100010000000300000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98356</Offset>
				    <SizeInBits>96</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>13</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array I64</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array I64</Name>
						      <Size>2</Size>
						      <Type>
							      <I64>
								        <Name>OutputI8 3</Name>
							</I64>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114004000A4F75747075744938203300001C404000018000000200000F496E7075742041727261792049363400010001000000020000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98360</Offset>
				    <SizeInBits>128</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>14</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array I64</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array I64</Name>
						      <Size>2</Size>
						      <Type>
							      <I64>
								        <Name>OutputI8 3</Name>
							</I64>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114004000A4F75747075744938203300001E40400001800000020000104F7574707574204172726179204936340000010001000000020000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98364</Offset>
				    <SizeInBits>128</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>15</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array U64</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array U64</Name>
						      <Size>3</Size>
						      <Type>
							      <U64>
								        <Name>OutputI8 3</Name>
							</U64>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114008000A4F75747075744938203300001C404000018000000300000F496E70757420417272617920553634000100010000000300000000000000000000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98368</Offset>
				    <SizeInBits>192</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>16</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array U64</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array U64</Name>
						      <Size>3</Size>
						      <Type>
							      <U64>
								        <Name>OutputI8 3</Name>
							</U64>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114008000A4F75747075744938203300001E40400001800000030000104F75747075742041727261792055363400000100010000000300000000000000000000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98372</Offset>
				    <SizeInBits>192</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>17</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array U64 1</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array U64 1</Name>
						      <Size>1</Size>
						      <Type>
							      <U64>
								        <Name>OutputI8 3</Name>
							</U64>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114008000A4F75747075744938203300001E4040000180000001000011496E7075742041727261792055363420310001000100000001000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98376</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>18</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array U64 1</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array U64 1</Name>
						      <Size>1</Size>
						      <Type>
							      <U64>
								        <Name>OutputI8 3</Name>
							</U64>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114008000A4F75747075744938203300002040400001800000010000124F7574707574204172726179205536342031000001000100000001000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98380</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>19</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array Bool 16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array Bool 16</Name>
						      <Size>16</Size>
						      <Type>
							      <Boolean>
								        <Name>OutputBool 3</Name>
							</Boolean>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>1300800000000002001240210C4F7574707574426F6F6C20330000204040000180000010000013496E70757420417272617920426F6F6C20313600010001000000100000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98386</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>20</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array Bool 16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array Bool 16</Name>
						      <Size>16</Size>
						      <Type>
							      <Boolean>
								        <Name>OutputBool 3</Name>
							</Boolean>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>1300800000000002001240210C4F7574707574426F6F6C203300002240400001800000100000144F757470757420417272617920426F6F6C2031360000010001000000100000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98390</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>21</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array Bool 17</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array Bool 17</Name>
						      <Size>17</Size>
						      <Type>
							      <Boolean>
								        <Name>OutputBool 3</Name>
							</Boolean>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>1300800000000002001240210C4F7574707574426F6F6C20330000204040000180000011000013496E70757420417272617920426F6F6C2031370001000100000011000000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98392</Offset>
				    <SizeInBits>17</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>22</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array Bool 17</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array Bool 17</Name>
						      <Size>17</Size>
						      <Type>
							      <Boolean>
								        <Name>OutputBool 3</Name>
							</Boolean>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>1300800000000002001240210C4F7574707574426F6F6C203300002240400001800000110000144F757470757420417272617920426F6F6C203137000001000100000011000000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98396</Offset>
				    <SizeInBits>17</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>23</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array I8 1</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array I8 1</Name>
						      <Size>1</Size>
						      <Type>
							      <I8>
								        <Name>OutputI8 3</Name>
							</I8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114001000A4F75747075744938203300001E4040000180000001000010496E70757420417272617920493820310000010001000000010000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98402</Offset>
				    <SizeInBits>8</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>24</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array I8 1</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array I8 1</Name>
						      <Size>1</Size>
						      <Type>
							      <I8>
								        <Name>OutputI8 3</Name>
							</I8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114001000A4F75747075744938203300001E40400001800000010000114F7574707574204172726179204938203100010001000000010000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98406</Offset>
				    <SizeInBits>8</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>25</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array U8 2</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array U8 2</Name>
						      <Size>2</Size>
						      <Type>
							      <U8>
								        <Name>OutputI8 3</Name>
							</U8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114005000A4F75747075744938203300001E4040000180000002000010496E7075742041727261792055382032000001000100000002000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98410</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>26</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array U8 2</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array U8 2</Name>
						      <Size>2</Size>
						      <Type>
							      <U8>
								        <Name>OutputI8 3</Name>
							</U8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114005000A4F75747075744938203300001E40400001800000020000114F757470757420417272617920553820320001000100000002000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98414</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>27</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array I8 3</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array I8 3</Name>
						      <Size>3</Size>
						      <Type>
							      <I8>
								        <Name>OutputI8 3</Name>
							</I8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114001000A4F75747075744938203300001E4040000180000003000010496E707574204172726179204938203300000100010000000300000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98416</Offset>
				    <SizeInBits>24</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>28</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array I8 3</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array I8 3</Name>
						      <Size>3</Size>
						      <Type>
							      <I8>
								        <Name>OutputI8 3</Name>
							</I8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114001000A4F75747075744938203300001E40400001800000030000114F75747075742041727261792049382033000100010000000300000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98420</Offset>
				    <SizeInBits>24</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>29</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array U8 4</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array U8 4</Name>
						      <Size>4</Size>
						      <Type>
							      <U8>
								        <Name>OutputI8 3</Name>
							</U8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114005000A4F75747075744938203300001E4040000180000004000010496E70757420417272617920553820340000010001000000040000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98424</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>30</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array U8 4</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array U8 4</Name>
						      <Size>4</Size>
						      <Type>
							      <U8>
								        <Name>OutputI8 3</Name>
							</U8>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114005000A4F75747075744938203300001E40400001800000040000114F7574707574204172726179205538203400010001000000040000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98428</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>31</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array I16 1</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array I16 1</Name>
						      <Size>1</Size>
						      <Type>
							      <I16>
								        <Name>OutputI8 3</Name>
							</I16>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114002000A4F75747075744938203300001E4040000180000001000011496E7075742041727261792049313620310001000100000001000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98434</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>32</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array I16 1</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array I16 1</Name>
						      <Size>1</Size>
						      <Type>
							      <I16>
								        <Name>OutputI8 3</Name>
							</I16>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114002000A4F75747075744938203300002040400001800000010000124F7574707574204172726179204931362031000001000100000001000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98438</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>33</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array SGL 1</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array SGL 1</Name>
						      <Size>1</Size>
						      <Type>
							      <SGL>
								        <Name>OutputI8 3</Name>
							</SGL>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114009000A4F75747075744938203300002040400001800000010000124F75747075742041727261792053474C20310000010001000000010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98440</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>34</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array SGL 1</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array SGL 1</Name>
						      <Size>1</Size>
						      <Type>
							      <SGL>
								        <Name>OutputI8 3</Name>
							</SGL>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114009000A4F75747075744938203300001E4040000180000001000011496E7075742041727261792053474C203100010001000000010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98444</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>35</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array SGL</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array SGL</Name>
						      <Size>3</Size>
						      <Type>
							      <SGL>
								        <Name>OutputI8 3</Name>
							</SGL>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114009000A4F75747075744938203300001E40400001800000030000104F75747075742041727261792053474C00000100010000000300000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98448</Offset>
				    <SizeInBits>96</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>36</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array SGL</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array SGL</Name>
						      <Size>3</Size>
						      <Type>
							      <SGL>
								        <Name>OutputI8 3</Name>
							</SGL>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114009000A4F75747075744938203300001C404000018000000300000F496E7075742041727261792053474C000100010000000300000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98452</Offset>
				    <SizeInBits>96</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>37</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input I8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <I8>
						      <Name>Input I8</Name>
					</I8>
				</Datatype>
				    <FlattenedType>1300800000000001000F40010008496E70757420493800000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98458</Offset>
				    <SizeInBits>8</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>38</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output I8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <I8>
						      <Name>Output I8</Name>
					</I8>
				</Datatype>
				    <FlattenedType>1300800000000001000F400100094F7574707574204938000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98462</Offset>
				    <SizeInBits>8</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>39</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input U8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U8>
						      <Name>Input U8</Name>
					</U8>
				</Datatype>
				    <FlattenedType>1300800000000001000F40050008496E70757420553800000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98466</Offset>
				    <SizeInBits>8</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>40</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output U8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <U8>
						      <Name>Output U8</Name>
					</U8>
				</Datatype>
				    <FlattenedType>1300800000000001000F400500094F7574707574205538000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98470</Offset>
				    <SizeInBits>8</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>41</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input I16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <I16>
						      <Name>Input I16</Name>
					</I16>
				</Datatype>
				    <FlattenedType>1300800000000001000F40020009496E7075742049313600010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98474</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>42</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output I16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <I16>
						      <Name>Output I16</Name>
					</I16>
				</Datatype>
				    <FlattenedType>130080000000000100114002000A4F7574707574204931360000010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98478</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>43</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input U16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U16>
						      <Name>Input U16</Name>
					</U16>
				</Datatype>
				    <FlattenedType>1300800000000001000F40060009496E7075742055313600010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98482</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>44</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output U16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <U16>
						      <Name>Output U16</Name>
					</U16>
				</Datatype>
				    <FlattenedType>130080000000000100114006000A4F7574707574205531360000010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98486</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>45</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input I32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <I32>
						      <Name>Input I32</Name>
					</I32>
				</Datatype>
				    <FlattenedType>1300800000000001000F40030009496E70757420493332000100000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98488</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>46</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output I32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <I32>
						      <Name>Output I32</Name>
					</I32>
				</Datatype>
				    <FlattenedType>130080000000000100114003000A4F75747075742049333200000100000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98492</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>47</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input U32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U32>
						      <Name>Input U32</Name>
					</U32>
				</Datatype>
				    <FlattenedType>1300800000000001000F40070009496E70757420553332000100000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98496</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>48</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output U32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <U32>
						      <Name>Output U32</Name>
					</U32>
				</Datatype>
				    <FlattenedType>130080000000000100114007000A4F75747075742055333200000100000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98500</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>49</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input U64</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U64>
						      <Name>Input U64</Name>
					</U64>
				</Datatype>
				    <FlattenedType>1300800000000001000F40080009496E7075742055363400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98504</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>50</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output U64</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <U64>
						      <Name>Output U64</Name>
					</U64>
				</Datatype>
				    <FlattenedType>130080000000000100114008000A4F7574707574205536340000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98508</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>51</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output SGL</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <SGL>
						      <Name>Output SGL</Name>
					</SGL>
				</Datatype>
				    <FlattenedType>130080000000000100114009000A4F75747075742053474C00000100000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98512</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>52</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input SGL</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <SGL>
						      <Name>Input SGL</Name>
					</SGL>
				</Datatype>
				    <FlattenedType>1300800000000001000F40090009496E7075742053474C000100000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98516</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>53</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Bool</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Boolean>
						      <Name>Input Bool</Name>
					</Boolean>
				</Datatype>
				    <FlattenedType>1300800000000001001040210A496E70757420426F6F6C00000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98522</Offset>
				    <SizeInBits>1</SizeInBits>
				    <Class>8</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>54</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Bool</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Boolean>
						      <Name>Output Bool</Name>
					</Boolean>
				</Datatype>
				    <FlattenedType>1300800000000001001040210B4F757470757420426F6F6C000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98526</Offset>
				    <SizeInBits>1</SizeInBits>
				    <Class>8</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>55</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array U16 2</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array U16 2</Name>
						      <Size>2</Size>
						      <Type>
							      <U16>
								        <Name>OutputI8 3</Name>
							</U16>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114006000A4F75747075744938203300001E4040000180000002000011496E70757420417272617920553136203200010001000000020000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98528</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>56</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array U16 2</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array U16 2</Name>
						      <Size>2</Size>
						      <Type>
							      <U16>
								        <Name>OutputI8 3</Name>
							</U16>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114006000A4F75747075744938203300002040400001800000020000124F75747075742041727261792055313620320000010001000000020000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98532</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>57</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Array I32 1</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Input Array I32 1</Name>
						      <Size>1</Size>
						      <Type>
							      <I32>
								        <Name>OutputI8 3</Name>
							</I32>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114003000A4F75747075744938203300001E4040000180000001000011496E70757420417272617920493332203100010001000000010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98536</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>58</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Array I32 1</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>Output Array I32 1</Name>
						      <Size>1</Size>
						      <Type>
							      <I32>
								        <Name>OutputI8 3</Name>
							</I32>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>130080000000000200114003000A4F75747075744938203300002040400001800000010000124F75747075742041727261792049333220310000010001000000010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98540</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>59</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input I64</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <I64>
						      <Name>Input I64</Name>
					</I64>
				</Datatype>
				    <FlattenedType>1300800000000001000F40040009496E7075742049363400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98544</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>60</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output I64</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <I64>
						      <Name>Output I64</Name>
					</I64>
				</Datatype>
				    <FlattenedType>130080000000000100114004000A4F7574707574204936340000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98548</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>61</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Stop</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Boolean>
						      <Name>Stop</Name>
					</Boolean>
				</Datatype>
				    <FlattenedType>1300800000000001000A40210453746F7000000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98554</Offset>
				    <SizeInBits>1</SizeInBits>
				    <Class>8</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>62</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 63-bit Unsigned</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 63-bit Unsigned</Name>
						      <Signed>false</Signed>
						      <WordLength>63</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>4294967296.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010058405F0311003F00000020000000010000000100000000000000000000003F000000207FFFFFFFFFFFFFFF00000001FFFFFFE200000000000000011A4F7574707574204658502036332D62697420556E7369676E65640000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98556</Offset>
				    <SizeInBits>63</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>63</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Comms 2.0 FXP</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Comms 2.0 FXP</Name>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010058405F0311003F00000020000000010000000100000000000000000000003F000000207FFFFFFFFFFFFFFF00000001FFFFFFE200000000000000011A4F7574707574204658502036332D62697420556E7369676E65640000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98556</Offset>
				    <SizeInBits>63</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>63</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 63-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 63-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>63</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>-2147483648.000000</Minimum>
						      <Maximum>2147483648.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010056405F0351003F000000200001000100000020FFFFFFFFFFFFFFFF0000003E0000001F3FFFFFFFFFFFFFFF00000001FFFFFFE20000000000000001184F7574707574204658502036332D626974205369676E65640000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98560</Offset>
				    <SizeInBits>63</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>64</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 63-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 63-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>63</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>-2147483648.000000</Minimum>
						      <Maximum>2147483648.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010054405F0351003F000000200001000100000020FFFFFFFFFFFFFFFF0000003E0000001F3FFFFFFFFFFFFFFF00000001FFFFFFE2000000000000000117496E707574204658502036332D626974205369676E656400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98564</Offset>
				    <SizeInBits>63</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>65</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 63-bit Unsigned</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 63-bit Unsigned</Name>
						      <Signed>false</Signed>
						      <WordLength>63</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>4294967296.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010056405F0311003F00000020000000010000000100000000000000000000003F000000207FFFFFFFFFFFFFFF00000001FFFFFFE2000000000000000119496E707574204658502036332D62697420556E7369676E656400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98568</Offset>
				    <SizeInBits>63</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>66</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 64-bit Unsigned Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 64-bit Unsigned Overflow</Name>
						      <Signed>false</Signed>
						      <WordLength>64</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>4294967296.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010060405F0B11004000000020000000010000000100000000000000000000004000000020FFFFFFFFFFFFFFFF00000001FFFFFFE10000000000000001234F7574707574204658502036342D62697420556E7369676E6564204F766572666C6F770001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98572</Offset>
				    <SizeInBits>65</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>67</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 64-bit Signed Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 64-bit Signed Overflow</Name>
						      <Signed>true</Signed>
						      <WordLength>64</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>-2147483648.000000</Minimum>
						      <Maximum>2147483648.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005E405F0B510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE10000000000000001214F7574707574204658502036342D626974205369676E6564204F766572666C6F770001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98576</Offset>
				    <SizeInBits>65</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>68</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 64-bit Unsigned</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 64-bit Unsigned</Name>
						      <Signed>false</Signed>
						      <WordLength>64</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>4294967296.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010058405F0311004000000020000000010000000100000000000000000000004000000020FFFFFFFFFFFFFFFF00000001FFFFFFE100000000000000011A4F7574707574204658502036342D62697420556E7369676E65640000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98580</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>69</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 64-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 64-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>64</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>-2147483648.000000</Minimum>
						      <Maximum>2147483648.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010056405F03510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE10000000000000001184F7574707574204658502036342D626974205369676E65640000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98584</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>70</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 64-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 64-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>64</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>-2147483648.000000</Minimum>
						      <Maximum>2147483648.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010054405F03510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE1000000000000000117496E707574204658502036342D626974205369676E656400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98588</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>71</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 64-bit Unsigned Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 64-bit Unsigned Overflow</Name>
						      <Signed>false</Signed>
						      <WordLength>64</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>4294967296.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010060405F0B11004000000020000000010000000100000000000000000000004000000020FFFFFFFFFFFFFFFF00000001FFFFFFE1000000000000000122496E707574204658502036342D62697420556E7369676E6564204F766572666C6F77000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98592</Offset>
				    <SizeInBits>65</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>72</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 64-bit Signed Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 64-bit Signed Overflow</Name>
						      <Signed>true</Signed>
						      <WordLength>64</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>-2147483648.000000</Minimum>
						      <Maximum>2147483648.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005E405F0B510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE1000000000000000120496E707574204658502036342D626974205369676E6564204F766572666C6F77000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98596</Offset>
				    <SizeInBits>65</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>73</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 64-bit Unsigned</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 64-bit Unsigned</Name>
						      <Signed>false</Signed>
						      <WordLength>64</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>4294967296.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010056405F0311004000000020000000010000000100000000000000000000004000000020FFFFFFFFFFFFFFFF00000001FFFFFFE1000000000000000119496E707574204658502036342D62697420556E7369676E656400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98600</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>74</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 63-bit Unsigned Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 63-bit Unsigned Overflow</Name>
						      <Signed>false</Signed>
						      <WordLength>63</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>4294967296.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010060405F0B11003F00000020000000010000000100000000000000000000003F000000207FFFFFFFFFFFFFFF00000001FFFFFFE20000000000000001234F7574707574204658502036332D62697420556E7369676E6564204F766572666C6F770001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98604</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>75</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 63-bit Signed Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 63-bit Signed Overflow</Name>
						      <Signed>true</Signed>
						      <WordLength>63</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>-2147483648.000000</Minimum>
						      <Maximum>2147483648.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005E405F0B51003F000000200001000100000020FFFFFFFFFFFFFFFF0000003E0000001F3FFFFFFFFFFFFFFF00000001FFFFFFE20000000000000001214F7574707574204658502036332D626974205369676E6564204F766572666C6F770001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98608</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>76</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 63-bit Unsigned Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 63-bit Unsigned Overflow</Name>
						      <Signed>false</Signed>
						      <WordLength>63</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>4294967296.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010060405F0B11003F00000020000000010000000100000000000000000000003F000000207FFFFFFFFFFFFFFF00000001FFFFFFE2000000000000000122496E707574204658502036332D62697420556E7369676E6564204F766572666C6F77000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98612</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>77</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 63-bit Signed Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 63-bit Signed Overflow</Name>
						      <Signed>true</Signed>
						      <WordLength>63</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>-2147483648.000000</Minimum>
						      <Maximum>2147483648.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005E405F0B51003F000000200001000100000020FFFFFFFFFFFFFFFF0000003E0000001F3FFFFFFFFFFFFFFF00000001FFFFFFE2000000000000000120496E707574204658502036332D626974205369676E6564204F766572666C6F77000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98616</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>78</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 32-bit Unsigned Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 32-bit Unsigned Overflow</Name>
						      <Signed>false</Signed>
						      <WordLength>32</WordLength>
						      <IntegerWordLength>16</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>65535.999985</Maximum>
						      <Delta>0.000015</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010060405F0B1100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF10000000000000001234F7574707574204658502033322D62697420556E7369676E6564204F766572666C6F770001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98620</Offset>
				    <SizeInBits>33</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>79</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 32-bit Signed Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 32-bit Signed Overflow</Name>
						      <Signed>true</Signed>
						      <WordLength>32</WordLength>
						      <IntegerWordLength>16</IntegerWordLength>
						      <Minimum>-32768.000000</Minimum>
						      <Maximum>32767.999985</Maximum>
						      <Delta>0.000015</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005E405F0B510020000000100001000100000010FFFFFFFFFFFFFFFF0000001F0000000F000000007FFFFFFF00000001FFFFFFF10000000000000001214F7574707574204658502033322D626974205369676E6564204F766572666C6F770001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98624</Offset>
				    <SizeInBits>33</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>80</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 32-bit Unsigned</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 32-bit Unsigned</Name>
						      <Signed>false</Signed>
						      <WordLength>32</WordLength>
						      <IntegerWordLength>16</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>65535.999985</Maximum>
						      <Delta>0.000015</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010058405F031100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF100000000000000011A4F7574707574204658502033322D62697420556E7369676E65640000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98628</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>81</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 32-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 32-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>32</WordLength>
						      <IntegerWordLength>16</IntegerWordLength>
						      <Minimum>-32768.000000</Minimum>
						      <Maximum>32767.999985</Maximum>
						      <Delta>0.000015</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010056405F03510020000000100001000100000010FFFFFFFFFFFFFFFF0000001F0000000F000000007FFFFFFF00000001FFFFFFF10000000000000001184F7574707574204658502033322D626974205369676E65640000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98632</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>82</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 32-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 32-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>32</WordLength>
						      <IntegerWordLength>16</IntegerWordLength>
						      <Minimum>-32768.000000</Minimum>
						      <Maximum>32767.999985</Maximum>
						      <Delta>0.000015</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010054405F03510020000000100001000100000010FFFFFFFFFFFFFFFF0000001F0000000F000000007FFFFFFF00000001FFFFFFF1000000000000000117496E707574204658502033322D626974205369676E656400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98636</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>83</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 32-bit Unsigned Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 32-bit Unsigned Overflow</Name>
						      <Signed>false</Signed>
						      <WordLength>32</WordLength>
						      <IntegerWordLength>16</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>65535.999985</Maximum>
						      <Delta>0.000015</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010060405F0B1100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF1000000000000000122496E707574204658502033322D62697420556E7369676E6564204F766572666C6F77000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98640</Offset>
				    <SizeInBits>33</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>84</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 32-bit Signed Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 32-bit Signed Overflow</Name>
						      <Signed>true</Signed>
						      <WordLength>32</WordLength>
						      <IntegerWordLength>16</IntegerWordLength>
						      <Minimum>-32768.000000</Minimum>
						      <Maximum>32767.999985</Maximum>
						      <Delta>0.000015</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005E405F0B510020000000100001000100000010FFFFFFFFFFFFFFFF0000001F0000000F000000007FFFFFFF00000001FFFFFFF1000000000000000120496E707574204658502033322D626974205369676E6564204F766572666C6F77000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98644</Offset>
				    <SizeInBits>33</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>85</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 32-bit Unsigned</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 32-bit Unsigned</Name>
						      <Signed>false</Signed>
						      <WordLength>32</WordLength>
						      <IntegerWordLength>16</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>65535.999985</Maximum>
						      <Delta>0.000015</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010056405F031100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF1000000000000000119496E707574204658502033322D62697420556E7369676E656400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98648</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>86</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 16-bit Unsigned Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 16-bit Unsigned Overflow</Name>
						      <Signed>false</Signed>
						      <WordLength>16</WordLength>
						      <IntegerWordLength>8</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>255.996094</Maximum>
						      <Delta>0.003906</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010060405F0B11001000000008000000010000000100000000000000000000001000000008000000000000FFFF00000001FFFFFFF90000000000000001234F7574707574204658502031362D62697420556E7369676E6564204F766572666C6F770001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98652</Offset>
				    <SizeInBits>17</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>87</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 16-bit Signed Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 16-bit Signed Overflow</Name>
						      <Signed>true</Signed>
						      <WordLength>16</WordLength>
						      <IntegerWordLength>8</IntegerWordLength>
						      <Minimum>-128.000000</Minimum>
						      <Maximum>127.996094</Maximum>
						      <Delta>0.003906</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005E405F0B510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF90000000000000001214F7574707574204658502031362D626974205369676E6564204F766572666C6F770001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98656</Offset>
				    <SizeInBits>17</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>88</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 16-bit Unsigned</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 16-bit Unsigned</Name>
						      <Signed>false</Signed>
						      <WordLength>16</WordLength>
						      <IntegerWordLength>8</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>255.996094</Maximum>
						      <Delta>0.003906</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010058405F0311001000000008000000010000000100000000000000000000001000000008000000000000FFFF00000001FFFFFFF900000000000000011A4F7574707574204658502031362D62697420556E7369676E65640000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98662</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>89</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output FXP 16-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output FXP 16-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>16</WordLength>
						      <IntegerWordLength>8</IntegerWordLength>
						      <Minimum>-128.000000</Minimum>
						      <Maximum>127.996094</Maximum>
						      <Delta>0.003906</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010056405F03510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF90000000000000001184F7574707574204658502031362D626974205369676E65640000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98666</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>90</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 16-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 16-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>16</WordLength>
						      <IntegerWordLength>8</IntegerWordLength>
						      <Minimum>-128.000000</Minimum>
						      <Maximum>127.996094</Maximum>
						      <Delta>0.003906</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010054405F03510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF9000000000000000117496E707574204658502031362D626974205369676E656400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98670</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>91</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 16-bit Unsigned Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 16-bit Unsigned Overflow</Name>
						      <Signed>false</Signed>
						      <WordLength>16</WordLength>
						      <IntegerWordLength>8</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>255.996094</Maximum>
						      <Delta>0.003906</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010060405F0B11001000000008000000010000000100000000000000000000001000000008000000000000FFFF00000001FFFFFFF9000000000000000122496E707574204658502031362D62697420556E7369676E6564204F766572666C6F77000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98672</Offset>
				    <SizeInBits>17</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>92</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 16-bit Signed Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 16-bit Signed Overflow</Name>
						      <Signed>true</Signed>
						      <WordLength>16</WordLength>
						      <IntegerWordLength>8</IntegerWordLength>
						      <Minimum>-128.000000</Minimum>
						      <Maximum>127.996094</Maximum>
						      <Delta>0.003906</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005E405F0B510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF9000000000000000120496E707574204658502031362D626974205369676E6564204F766572666C6F77000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98676</Offset>
				    <SizeInBits>17</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>93</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input FXP 16-bit Unsigned</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input FXP 16-bit Unsigned</Name>
						      <Signed>false</Signed>
						      <WordLength>16</WordLength>
						      <IntegerWordLength>8</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>255.996094</Maximum>
						      <Delta>0.003906</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010056405F0311001000000008000000010000000100000000000000000000001000000008000000000000FFFF00000001FFFFFFF9000000000000000119496E707574204658502031362D62697420556E7369676E656400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98682</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>94</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster U32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U32>
						      <Name>Input Cluster U32</Name>
					</U32>
				</Datatype>
				    <FlattenedType>1300800000000001001740070011496E70757420436C757374657220553332000100000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98684</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>95</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster I32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <I32>
						      <Name>Input Cluster I32</Name>
					</I32>
				</Datatype>
				    <FlattenedType>1300800000000001001740030011496E70757420436C757374657220493332000100000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98688</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>96</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster U16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U16>
						      <Name>Input Cluster U16</Name>
					</U16>
				</Datatype>
				    <FlattenedType>1300800000000001001740060011496E70757420436C75737465722055313600010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98694</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>97</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster I16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <I16>
						      <Name>Input Cluster I16</Name>
					</I16>
				</Datatype>
				    <FlattenedType>1300800000000001001740020011496E70757420436C75737465722049313600010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98698</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>98</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster I8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <I8>
						      <Name>Input Cluster I8</Name>
					</I8>
				</Datatype>
				    <FlattenedType>1300800000000001001740010010496E70757420436C757374657220493800000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98702</Offset>
				    <SizeInBits>8</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>99</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster U64</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U64>
						      <Name>Input Cluster U64</Name>
					</U64>
				</Datatype>
				    <FlattenedType>1300800000000001001740080011496E70757420436C75737465722055363400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98704</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>100</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster  U8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U8>
						      <Name>Input Cluster  U8</Name>
					</U8>
				</Datatype>
				    <FlattenedType>1300800000000001001740050011496E70757420436C757374657220205538000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98710</Offset>
				    <SizeInBits>8</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>101</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster Bool</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Boolean>
						      <Name>Input Cluster Bool</Name>
					</Boolean>
				</Datatype>
				    <FlattenedType>13008000000000010018402112496E70757420436C757374657220426F6F6C00000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98714</Offset>
				    <SizeInBits>1</SizeInBits>
				    <Class>8</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>102</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster EnumU8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <EnumU16>
						      <Name>Input Cluster EnumU8</Name>
						      <StringList>
							      <String>G</String>
							      <String>F</String>
							      <String>E</String>
							      <String>D</String>
							      <String>C</String>
							      <String>B</String>
							      <String>A</String>
						</StringList>
					</EnumU16>
				</Datatype>
				    <FlattenedType>1300800000000001002B4016000701470146014501440143014201410014496E70757420436C757374657220456E756D55380000010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98718</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>35</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>103</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster FXP 13-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input Cluster FXP 13-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>16</WordLength>
						      <IntegerWordLength>8</IntegerWordLength>
						      <Minimum>-128.000000</Minimum>
						      <Maximum>127.996094</Maximum>
						      <Delta>0.003906</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005C405F03510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF900000000000000011F496E70757420436C7573746572204658502031332D626974205369676E656400010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98722</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>104</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster FXP 32-bit Unsigned Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input Cluster FXP 32-bit Unsigned Overflow</Name>
						      <Signed>false</Signed>
						      <WordLength>32</WordLength>
						      <IntegerWordLength>16</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>65535.999985</Maximum>
						      <Delta>0.000015</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010068405F0B1100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF100000000000000012A496E70757420436C7573746572204658502033322D62697420556E7369676E6564204F766572666C6F77000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98724</Offset>
				    <SizeInBits>33</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>105</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster FXP 64-bit Signed Overflow</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input Cluster FXP 64-bit Signed Overflow</Name>
						      <Signed>true</Signed>
						      <WordLength>64</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>-2147483648.000000</Minimum>
						      <Maximum>2147483648.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010066405F0B510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE1000000000000000128496E70757420436C7573746572204658502036342D626974205369676E6564204F766572666C6F77000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98728</Offset>
				    <SizeInBits>65</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>106</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster FXP 4-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input Cluster FXP 4-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>4</WordLength>
						      <IntegerWordLength>2</IntegerWordLength>
						      <Minimum>-2.000000</Minimum>
						      <Maximum>1.750000</Maximum>
						      <Delta>0.250000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005C405F0B510004000000020001000100000002FFFFFFFFFFFFFFFF0000000300000001000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E6564000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98734</Offset>
				    <SizeInBits>5</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>107</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster Bool 2</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Boolean>
						      <Name>Input Cluster Bool 2</Name>
					</Boolean>
				</Datatype>
				    <FlattenedType>1300800000000001001A402114496E70757420436C757374657220426F6F6C203200000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98738</Offset>
				    <SizeInBits>1</SizeInBits>
				    <Class>8</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>108</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster I16 2</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <I16>
						      <Name>Input Cluster I16 2</Name>
					</I16>
				</Datatype>
				    <FlattenedType>1300800000000001001940020013496E70757420436C757374657220493136203200010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98742</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>109</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster FXP 32-bit Unsigned Overflow 2</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input Cluster FXP 32-bit Unsigned Overflow 2</Name>
						      <Signed>false</Signed>
						      <WordLength>32</WordLength>
						      <IntegerWordLength>16</IntegerWordLength>
						      <Minimum>0.000000</Minimum>
						      <Maximum>65535.999985</Maximum>
						      <Delta>0.000015</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001006A405F0B1100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF100000000000000012C496E70757420436C7573746572204658502033322D62697420556E7369676E6564204F766572666C6F772032000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98744</Offset>
				    <SizeInBits>33</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>110</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster FXP 64-bit Signed Overflow 2</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input Cluster FXP 64-bit Signed Overflow 2</Name>
						      <Signed>true</Signed>
						      <WordLength>64</WordLength>
						      <IntegerWordLength>32</IntegerWordLength>
						      <Minimum>-2147483648.000000</Minimum>
						      <Maximum>2147483648.000000</Maximum>
						      <Delta>0.000000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>13008000000000010068405F0B510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE100000000000000012A496E70757420436C7573746572204658502036342D626974205369676E6564204F766572666C6F772032000001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98748</Offset>
				    <SizeInBits>65</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>111</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Input Cluster FXP 13-bit Signed 2</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Input Cluster FXP 13-bit Signed 2</Name>
						      <Signed>true</Signed>
						      <WordLength>16</WordLength>
						      <IntegerWordLength>8</IntegerWordLength>
						      <Minimum>-128.000000</Minimum>
						      <Maximum>127.996094</Maximum>
						      <Delta>0.003906</Delta>
						      <IncludeOverflowStatus>false</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005E405F03510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF9000000000000000121496E70757420436C7573746572204658502031332D626974205369676E6564203200010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98754</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>112</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>output small cluster</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Cluster>
						      <Name>output small cluster</Name>
						      <TypeList>
							      <FXP>
								        <Name>Input Cluster FXP 4-bit Signed</Name>
								        <Signed>true</Signed>
								        <WordLength>4</WordLength>
								        <IntegerWordLength>2</IntegerWordLength>
								        <Minimum>-2.000000</Minimum>
								        <Maximum>1.750000</Maximum>
								        <Delta>0.250000</Delta>
								        <IncludeOverflowStatus>true</IncludeOverflowStatus>
							</FXP>
						</TypeList>
					</Cluster>
				</Datatype>
				    <FlattenedType>1300800000000002005C405F0B510004000000020001000100000002FFFFFFFFFFFFFFFF0000000300000001000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E656400001E405000010000146F757470757420736D616C6C20636C7573746572000001000100000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98758</Offset>
				    <SizeInBits>5</SizeInBits>
				    <Class>30</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>113</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList>
					    <SubControl>
						      <Name>Input Cluster FXP 4-bit Signed</Name>
						      <FlattenedType>1800800000000001005C405F0B510004000000020001000400000002FFFFFFFFFFFFFFF80001000400000002000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E6564000001000000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output small cluster</Name>
								        <Name>Input Cluster FXP 4-bit Signed</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>113</Item>
								        <Item>0</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
				</SubControlList>
			</Register>
			  <Register>
				    <Name>output cluster</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Cluster>
						      <Name>output cluster</Name>
						      <TypeList>
							      <FXP>
								        <Name>Input Cluster FXP 4-bit Signed</Name>
								        <Signed>true</Signed>
								        <WordLength>4</WordLength>
								        <IntegerWordLength>2</IntegerWordLength>
								        <Minimum>-2.000000</Minimum>
								        <Maximum>1.750000</Maximum>
								        <Delta>0.250000</Delta>
								        <IncludeOverflowStatus>true</IncludeOverflowStatus>
							</FXP>
							      <U8>
								        <Name>Input Cluster  U8</Name>
							</U8>
							      <U64>
								        <Name>Input Cluster U64</Name>
							</U64>
							      <I8>
								        <Name>Input Cluster I8</Name>
							</I8>
						</TypeList>
					</Cluster>
				</Datatype>
				    <FlattenedType>1300800000000005005C405F0B510004000000020001000100000002FFFFFFFFFFFFFFFF0000000300000001000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E656400001740050011496E70757420436C757374657220205538001740080011496E70757420436C757374657220553634001740010010496E70757420436C757374657220493800001E4050000400000001000200030E6F757470757420636C757374657200000100040000000000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98760</Offset>
				    <SizeInBits>85</SizeInBits>
				    <Class>30</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>114</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList>
					    <SubControl>
						      <Name>Input Cluster FXP 4-bit Signed</Name>
						      <FlattenedType>1800800000000001005C405F0B510004000000020001000400000002FFFFFFFFFFFFFFF80001000400000002000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E6564000001000000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster</Name>
								        <Name>Input Cluster FXP 4-bit Signed</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>114</Item>
								        <Item>0</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster  U8</Name>
						      <FlattenedType>1800800000000001001740050011496E70757420436C757374657220205538000100000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster</Name>
								        <Name>Input Cluster  U8</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>114</Item>
								        <Item>1</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster U64</Name>
						      <FlattenedType>1800800000000001001740080011496E70757420436C75737465722055363400010000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster</Name>
								        <Name>Input Cluster U64</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>114</Item>
								        <Item>2</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster I8</Name>
						      <FlattenedType>1800800000000001001740010010496E70757420436C757374657220493800000100000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster</Name>
								        <Name>Input Cluster I8</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>114</Item>
								        <Item>3</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
				</SubControlList>
			</Register>
			  <Register>
				    <Name>output cluster 2</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Cluster>
						      <Name>output cluster 2</Name>
						      <TypeList>
							      <U16>
								        <Name>Input Cluster U16</Name>
							</U16>
							      <Cluster>
								        <Name>output cluster 2</Name>
								        <TypeList>
									        <FXP>
										          <Name>Input Cluster FXP 4-bit Signed</Name>
										          <Signed>true</Signed>
										          <WordLength>4</WordLength>
										          <IntegerWordLength>2</IntegerWordLength>
										          <Minimum>-2.000000</Minimum>
										          <Maximum>1.750000</Maximum>
										          <Delta>0.250000</Delta>
										          <IncludeOverflowStatus>true</IncludeOverflowStatus>
									</FXP>
									        <U8>
										          <Name>Input Cluster  U8</Name>
									</U8>
									        <U64>
										          <Name>Input Cluster U64</Name>
									</U64>
									        <I8>
										          <Name>Input Cluster I8</Name>
									</I8>
								</TypeList>
							</Cluster>
							      <Array>
								        <Name>output cluster array</Name>
								        <Size>2</Size>
								        <Type>
									        <Cluster>
										          <Name/>
										          <TypeList>
											          <FXP>
												            <Name>Input Cluster FXP 64-bit Signed Overflow 2</Name>
												            <Signed>true</Signed>
												            <WordLength>64</WordLength>
												            <IntegerWordLength>32</IntegerWordLength>
												            <Minimum>-2147483648.000000</Minimum>
												            <Maximum>2147483648.000000</Maximum>
												            <Delta>0.000000</Delta>
												            <IncludeOverflowStatus>true</IncludeOverflowStatus>
											</FXP>
											          <I16>
												            <Name>Input Cluster I16 2</Name>
											</I16>
											          <FXP>
												            <Name>Input Cluster FXP 32-bit Unsigned Overflow 2</Name>
												            <Signed>false</Signed>
												            <WordLength>32</WordLength>
												            <IntegerWordLength>16</IntegerWordLength>
												            <Minimum>0.000000</Minimum>
												            <Maximum>65535.999985</Maximum>
												            <Delta>0.000015</Delta>
												            <IncludeOverflowStatus>true</IncludeOverflowStatus>
											</FXP>
											          <Boolean>
												            <Name>Input Cluster Bool 2</Name>
											</Boolean>
										</TypeList>
									</Cluster>
								</Type>
							</Array>
							      <I32>
								        <Name>Input Cluster I32</Name>
							</I32>
							      <EnumU16>
								        <Name>Input Cluster EnumU8</Name>
								        <StringList>
									        <String>G</String>
									        <String>F</String>
									        <String>E</String>
									        <String>D</String>
									        <String>C</String>
									        <String>B</String>
									        <String>A</String>
								</StringList>
							</EnumU16>
							      <U32>
								        <Name>Input Cluster U32</Name>
							</U32>
							      <Array>
								        <Name>output fxp array</Name>
								        <Size>2</Size>
								        <Type>
									        <FXP>
										          <Name>Input Cluster FXP 13-bit Signed 2</Name>
										          <Signed>true</Signed>
										          <WordLength>16</WordLength>
										          <IntegerWordLength>8</IntegerWordLength>
										          <Minimum>-128.000000</Minimum>
										          <Maximum>127.996094</Maximum>
										          <Delta>0.003906</Delta>
										          <IncludeOverflowStatus>false</IncludeOverflowStatus>
									</FXP>
								</Type>
							</Array>
						</TypeList>
					</Cluster>
				</Datatype>
				    <FlattenedType>1300800000000012001740060011496E70757420436C757374657220553136005C405F0B510004000000020001000100000002FFFFFFFFFFFFFFFF0000000300000001000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E656400001740050011496E70757420436C757374657220205538001740080011496E70757420436C757374657220553634001740010010496E70757420436C7573746572204938000020405000040001000200030004106F757470757420636C75737465722032000068405F0B510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE100000000000000012A496E70757420436C7573746572204658502036342D626974205369676E6564204F766572666C6F77203200001940020013496E70757420436C7573746572204931362032006A405F0B1100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF100000000000000012C496E70757420436C7573746572204658502033322D62697420556E7369676E6564204F766572666C6F77203200001A402114496E70757420436C757374657220426F6F6C203200000E00500004000600070008000900224040000180000002000A146F757470757420636C757374657220617272617900001740030011496E70757420436C757374657220493332002B4016000701470146014501440143014201410014496E70757420436C757374657220456E756D553800001740070011496E70757420436C757374657220553332005E405F03510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF9000000000000000121496E70757420436C7573746572204658502031332D626974205369676E65642032001E4040000180000002000F106F7574707574206678702061727261790000264050000700000005000B000C000D000E0010106F757470757420636C7573746572203200000100110000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98764</Offset>
				    <SizeInBits>443</SizeInBits>
				    <Class>30</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>115</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList>
					    <SubControl>
						      <Name>Input Cluster U16</Name>
						      <FlattenedType>1800800000000001001740060011496E70757420436C75737465722055313600010000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster U16</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>0</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>output cluster 2</Name>
						      <FlattenedType>1800800000000005005C405F0B510004000000020001000400000002FFFFFFFFFFFFFFF80001000400000002000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E656400001740050011496E70757420436C757374657220205538001740080011496E70757420436C757374657220553634001740010010496E70757420436C7573746572204938000020405000040000000100020003106F757470757420636C7573746572203200000100040000000000000000000000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>output cluster 2</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>1</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster FXP 4-bit Signed</Name>
						      <FlattenedType>1800800000000001005C405F0B510004000000020001000400000002FFFFFFFFFFFFFFF80001000400000002000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E6564000001000000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster FXP 4-bit Signed</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>1</Item>
								        <Item>0</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster  U8</Name>
						      <FlattenedType>1800800000000001001740050011496E70757420436C757374657220205538000100000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster  U8</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>1</Item>
								        <Item>1</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster U64</Name>
						      <FlattenedType>1800800000000001001740080011496E70757420436C75737465722055363400010000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster U64</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>1</Item>
								        <Item>2</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster I8</Name>
						      <FlattenedType>1800800000000001001740010010496E70757420436C757374657220493800000100000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster I8</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>1</Item>
								        <Item>3</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>output cluster array</Name>
						      <FlattenedType>18008000000000060068405F0B510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE100000000000000012A496E70757420436C7573746572204658502036342D626974205369676E6564204F766572666C6F77203200001940020013496E70757420436C7573746572204931362032006A405F0B1100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF100000000000000012C496E70757420436C7573746572204658502033322D62697420556E7369676E6564204F766572666C6F77203200001A402114496E70757420436C757374657220426F6F6C203200000E005000040000000100020003002240400001800000020004146F757470757420636C757374657220617272617900000100050000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>output cluster array</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>2</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster I32</Name>
						      <FlattenedType>1800800000000001001740030011496E70757420436C757374657220493332000100000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster I32</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>3</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster EnumU8</Name>
						      <FlattenedType>1800800000000001002B4016000701470146014501440143014201410014496E70757420436C757374657220456E756D55380000010000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster EnumU8</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>4</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster U32</Name>
						      <FlattenedType>1800800000000001001740070011496E70757420436C757374657220553332000100000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster U32</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>5</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>output fxp array</Name>
						      <FlattenedType>1800800000000002005E405F03510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF9000000000000000121496E70757420436C7573746572204658502031332D626974205369676E65642032001E40400001800000020000106F7574707574206678702061727261790000010001000000020000000000000000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>output cluster 2</Name>
								        <Name>output fxp array</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>115</Item>
								        <Item>6</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
				</SubControlList>
			</Register>
			  <Register>
				    <Name>input cluster</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Cluster>
						      <Name>input cluster</Name>
						      <TypeList>
							      <U16>
								        <Name>Input Cluster U16</Name>
							</U16>
							      <Cluster>
								        <Name>output cluster 2</Name>
								        <TypeList>
									        <FXP>
										          <Name>Input Cluster FXP 4-bit Signed</Name>
										          <Signed>true</Signed>
										          <WordLength>4</WordLength>
										          <IntegerWordLength>2</IntegerWordLength>
										          <Minimum>-2.000000</Minimum>
										          <Maximum>1.750000</Maximum>
										          <Delta>0.250000</Delta>
										          <IncludeOverflowStatus>true</IncludeOverflowStatus>
									</FXP>
									        <U8>
										          <Name>Input Cluster  U8</Name>
									</U8>
									        <U64>
										          <Name>Input Cluster U64</Name>
									</U64>
									        <I8>
										          <Name>Input Cluster I8</Name>
									</I8>
								</TypeList>
							</Cluster>
							      <Array>
								        <Name>output cluster array</Name>
								        <Size>2</Size>
								        <Type>
									        <Cluster>
										          <Name/>
										          <TypeList>
											          <FXP>
												            <Name>Input Cluster FXP 64-bit Signed Overflow 2</Name>
												            <Signed>true</Signed>
												            <WordLength>64</WordLength>
												            <IntegerWordLength>32</IntegerWordLength>
												            <Minimum>-2147483648.000000</Minimum>
												            <Maximum>2147483648.000000</Maximum>
												            <Delta>0.000000</Delta>
												            <IncludeOverflowStatus>true</IncludeOverflowStatus>
											</FXP>
											          <I16>
												            <Name>Input Cluster I16 2</Name>
											</I16>
											          <FXP>
												            <Name>Input Cluster FXP 32-bit Unsigned Overflow 2</Name>
												            <Signed>false</Signed>
												            <WordLength>32</WordLength>
												            <IntegerWordLength>16</IntegerWordLength>
												            <Minimum>0.000000</Minimum>
												            <Maximum>65535.999985</Maximum>
												            <Delta>0.000015</Delta>
												            <IncludeOverflowStatus>true</IncludeOverflowStatus>
											</FXP>
											          <Boolean>
												            <Name>Input Cluster Bool 2</Name>
											</Boolean>
										</TypeList>
									</Cluster>
								</Type>
							</Array>
							      <I32>
								        <Name>Input Cluster I32</Name>
							</I32>
							      <EnumU16>
								        <Name>Input Cluster EnumU8</Name>
								        <StringList>
									        <String>G</String>
									        <String>F</String>
									        <String>E</String>
									        <String>D</String>
									        <String>C</String>
									        <String>B</String>
									        <String>A</String>
								</StringList>
							</EnumU16>
							      <U32>
								        <Name>Input Cluster U32</Name>
							</U32>
							      <Array>
								        <Name>output fxp array</Name>
								        <Size>2</Size>
								        <Type>
									        <FXP>
										          <Name>Input Cluster FXP 13-bit Signed 2</Name>
										          <Signed>true</Signed>
										          <WordLength>16</WordLength>
										          <IntegerWordLength>8</IntegerWordLength>
										          <Minimum>-128.000000</Minimum>
										          <Maximum>127.996094</Maximum>
										          <Delta>0.003906</Delta>
										          <IncludeOverflowStatus>false</IncludeOverflowStatus>
									</FXP>
								</Type>
							</Array>
						</TypeList>
					</Cluster>
				</Datatype>
				    <FlattenedType>1300800000000012001740060011496E70757420436C757374657220553136005C405F0B510004000000020001000100000002FFFFFFFFFFFFFFFF0000000300000001000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E656400001740050011496E70757420436C757374657220205538001740080011496E70757420436C757374657220553634001740010010496E70757420436C7573746572204938000020405000040001000200030004106F757470757420636C75737465722032000068405F0B510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE100000000000000012A496E70757420436C7573746572204658502036342D626974205369676E6564204F766572666C6F77203200001940020013496E70757420436C7573746572204931362032006A405F0B1100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF100000000000000012C496E70757420436C7573746572204658502033322D62697420556E7369676E6564204F766572666C6F77203200001A402114496E70757420436C757374657220426F6F6C203200000E00500004000600070008000900224040000180000002000A146F757470757420636C757374657220617272617900001740030011496E70757420436C757374657220493332002B4016000701470146014501440143014201410014496E70757420436C757374657220456E756D553800001740070011496E70757420436C757374657220553332005E405F03510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF9000000000000000121496E70757420436C7573746572204658502031332D626974205369676E65642032001E4040000180000002000F106F7574707574206678702061727261790000224050000700000005000B000C000D000E00100D696E70757420636C7573746572000100110000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98768</Offset>
				    <SizeInBits>443</SizeInBits>
				    <Class>30</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>116</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList>
					    <SubControl>
						      <Name>Input Cluster U16</Name>
						      <FlattenedType>1800800000000001001740060011496E70757420436C75737465722055313600010000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>Input Cluster U16</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>0</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>output cluster 2</Name>
						      <FlattenedType>1800800000000005005C405F0B510004000000020001000400000002FFFFFFFFFFFFFFF80001000400000002000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E656400001740050011496E70757420436C757374657220205538001740080011496E70757420436C757374657220553634001740010010496E70757420436C7573746572204938000020405000040000000100020003106F757470757420636C7573746572203200000100040000000000000000000000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>output cluster 2</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>1</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster FXP 4-bit Signed</Name>
						      <FlattenedType>1800800000000001005C405F0B510004000000020001000400000002FFFFFFFFFFFFFFF80001000400000002000000000000000700000001FFFFFFFF00000000000000011E496E70757420436C75737465722046585020342D626974205369676E6564000001000000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster FXP 4-bit Signed</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>1</Item>
								        <Item>0</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster  U8</Name>
						      <FlattenedType>1800800000000001001740050011496E70757420436C757374657220205538000100000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster  U8</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>1</Item>
								        <Item>1</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster U64</Name>
						      <FlattenedType>1800800000000001001740080011496E70757420436C75737465722055363400010000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster U64</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>1</Item>
								        <Item>2</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster I8</Name>
						      <FlattenedType>1800800000000001001740010010496E70757420436C757374657220493800000100000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>output cluster 2</Name>
								        <Name>Input Cluster I8</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>1</Item>
								        <Item>3</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>output cluster array</Name>
						      <FlattenedType>18008000000000060068405F0B510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE100000000000000012A496E70757420436C7573746572204658502036342D626974205369676E6564204F766572666C6F77203200001940020013496E70757420436C7573746572204931362032006A405F0B1100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF100000000000000012C496E70757420436C7573746572204658502033322D62697420556E7369676E6564204F766572666C6F77203200001A402114496E70757420436C757374657220426F6F6C203200000E005000040000000100020003002240400001800000020004146F757470757420636C757374657220617272617900000100050000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>output cluster array</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>2</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster I32</Name>
						      <FlattenedType>1800800000000001001740030011496E70757420436C757374657220493332000100000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>Input Cluster I32</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>3</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster EnumU8</Name>
						      <FlattenedType>1800800000000001002B4016000701470146014501440143014201410014496E70757420436C757374657220456E756D55380000010000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>Input Cluster EnumU8</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>4</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>Input Cluster U32</Name>
						      <FlattenedType>1800800000000001001740070011496E70757420436C757374657220553332000100000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>Input Cluster U32</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>5</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>output fxp array</Name>
						      <FlattenedType>1800800000000002005E405F03510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF9000000000000000121496E70757420436C7573746572204658502031332D626974205369676E65642032001E40400001800000020000106F7574707574206678702061727261790000010001000000020000000000000000000000000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>input cluster</Name>
								        <Name>output fxp array</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>116</Item>
								        <Item>6</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
				</SubControlList>
			</Register>
			  <Register>
				    <Name>Output Cluster U16</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <U16>
						      <Name>Output Cluster U16</Name>
					</U16>
				</Datatype>
				    <FlattenedType>13008000000000010019400600124F757470757420436C7573746572205531360000010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98774</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>117</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Cluster FXP 4-bit Signed</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <FXP>
						      <Name>Output Cluster FXP 4-bit Signed</Name>
						      <Signed>true</Signed>
						      <WordLength>4</WordLength>
						      <IntegerWordLength>2</IntegerWordLength>
						      <Minimum>-2.000000</Minimum>
						      <Maximum>1.750000</Maximum>
						      <Delta>0.250000</Delta>
						      <IncludeOverflowStatus>true</IncludeOverflowStatus>
					</FXP>
				</Datatype>
				    <FlattenedType>1300800000000001005C405F0B510004000000020001000100000002FFFFFFFFFFFFFFFF0000000300000001000000000000000700000001FFFFFFFF00000000000000011F4F757470757420436C75737465722046585020342D626974205369676E65640001000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98778</Offset>
				    <SizeInBits>5</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>118</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Cluster  U8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <U8>
						      <Name>Output Cluster  U8</Name>
					</U8>
				</Datatype>
				    <FlattenedType>13008000000000010019400500124F757470757420436C75737465722020553800000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98782</Offset>
				    <SizeInBits>8</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>119</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Cluster U64</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <U64>
						      <Name>Output Cluster U64</Name>
					</U64>
				</Datatype>
				    <FlattenedType>13008000000000010019400800124F757470757420436C7573746572205536340000010000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98784</Offset>
				    <SizeInBits>64</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>120</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Cluster I8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <I8>
						      <Name>Output Cluster I8</Name>
					</I8>
				</Datatype>
				    <FlattenedType>13008000000000010017400100114F757470757420436C7573746572204938000100000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98790</Offset>
				    <SizeInBits>8</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>121</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Cluster I32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <I32>
						      <Name>Output Cluster I32</Name>
					</I32>
				</Datatype>
				    <FlattenedType>13008000000000010019400300124F757470757420436C75737465722049333200000100000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98792</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>122</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Cluster EnumU8</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <EnumU16>
						      <Name>Output Cluster EnumU8</Name>
						      <StringList>
							      <String>G</String>
							      <String>F</String>
							      <String>E</String>
							      <String>D</String>
							      <String>C</String>
							      <String>B</String>
							      <String>A</String>
						</StringList>
					</EnumU16>
				</Datatype>
				    <FlattenedType>1300800000000001002B40160007014701460145014401430142014100154F757470757420436C757374657220456E756D553800010000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98798</Offset>
				    <SizeInBits>16</SizeInBits>
				    <Class>35</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>123</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>Output Cluster U32</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <U32>
						      <Name>Output Cluster U32</Name>
					</U32>
				</Datatype>
				    <FlattenedType>13008000000000010019400700124F757470757420436C75737465722055333200000100000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98800</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>18</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>124</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>output fxp array</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>output fxp array</Name>
						      <Size>2</Size>
						      <Type>
							      <FXP>
								        <Name>Input Cluster FXP 13-bit Signed 2</Name>
								        <Signed>true</Signed>
								        <WordLength>16</WordLength>
								        <IntegerWordLength>8</IntegerWordLength>
								        <Minimum>-128.000000</Minimum>
								        <Maximum>127.996094</Maximum>
								        <Delta>0.003906</Delta>
								        <IncludeOverflowStatus>false</IncludeOverflowStatus>
							</FXP>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>1300800000000002005E405F03510010000000080001000100000008FFFFFFFFFFFFFFFF0000000F000000070000000000007FFF00000001FFFFFFF9000000000000000121496E70757420436C7573746572204658502031332D626974205369676E65642032001E40400001800000020000106F7574707574206678702061727261790000010001000000020000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98804</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>125</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>output cluster array</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name>output cluster array</Name>
						      <Size>2</Size>
						      <Type>
							      <Cluster>
								        <Name/>
								        <TypeList>
									        <FXP>
										          <Name>Input Cluster FXP 64-bit Signed Overflow 2</Name>
										          <Signed>true</Signed>
										          <WordLength>64</WordLength>
										          <IntegerWordLength>32</IntegerWordLength>
										          <Minimum>-2147483648.000000</Minimum>
										          <Maximum>2147483648.000000</Maximum>
										          <Delta>0.000000</Delta>
										          <IncludeOverflowStatus>true</IncludeOverflowStatus>
									</FXP>
									        <I16>
										          <Name>Input Cluster I16 2</Name>
									</I16>
									        <FXP>
										          <Name>Input Cluster FXP 32-bit Unsigned Overflow 2</Name>
										          <Signed>false</Signed>
										          <WordLength>32</WordLength>
										          <IntegerWordLength>16</IntegerWordLength>
										          <Minimum>0.000000</Minimum>
										          <Maximum>65535.999985</Maximum>
										          <Delta>0.000015</Delta>
										          <IncludeOverflowStatus>true</IncludeOverflowStatus>
									</FXP>
									        <Boolean>
										          <Name>Input Cluster Bool 2</Name>
									</Boolean>
								</TypeList>
							</Cluster>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType>13008000000000060068405F0B510040000000200001000100000020FFFFFFFFFFFFFFFF0000003F0000001F7FFFFFFFFFFFFFFF00000001FFFFFFE100000000000000012A496E70757420436C7573746572204658502036342D626974205369676E6564204F766572666C6F77203200001940020013496E70757420436C7573746572204931362032006A405F0B1100200000001000000001000000010000000000000000000000200000001000000000FFFFFFFF00000001FFFFFFF100000000000000012C496E70757420436C7573746572204658502033322D62697420556E7369676E6564204F766572666C6F77203200001A402114496E70757420436C757374657220426F6F6C203200000E005000040000000100020003002240400001800000020004146F757470757420636C757374657220617272617900000100050000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98808</Offset>
				    <SizeInBits>230</SizeInBits>
				    <Class>14</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>126</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>ViControl</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U32>
						      <Name/>
					</U32>
				</Datatype>
				    <FlattenedType/>
				    <Grouping/>
				    <Offset>94208</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>0</Class>
				    <Internal>true</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>0</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>DiagramReset</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U32>
						      <Name/>
					</U32>
				</Datatype>
				    <FlattenedType/>
				    <Grouping/>
				    <Offset>94216</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>0</Class>
				    <Internal>true</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>0</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>ViSignature</Name>
				    <Hidden>true</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Array>
						      <Name/>
						      <Size>4</Size>
						      <Type>
							      <U32>
								        <Name/>
							</U32>
						</Type>
					</Array>
				</Datatype>
				    <FlattenedType/>
				    <Grouping/>
				    <Offset>94212</Offset>
				    <SizeInBits>128</SizeInBits>
				    <Class>0</Class>
				    <Internal>true</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>0</ID>
				    <Bidirectional>false</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>InterruptEnable</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U32>
						      <Name/>
					</U32>
				</Datatype>
				    <FlattenedType/>
				    <Grouping/>
				    <Offset>90112</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>0</Class>
				    <Internal>true</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>0</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>InterruptMask</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U32>
						      <Name/>
					</U32>
				</Datatype>
				    <FlattenedType/>
				    <Grouping/>
				    <Offset>90120</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>0</Class>
				    <Internal>true</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>0</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
			  <Register>
				    <Name>InterruptStatus</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <U32>
						      <Name/>
					</U32>
				</Datatype>
				    <FlattenedType/>
				    <Grouping/>
				    <Offset>90124</Offset>
				    <SizeInBits>32</SizeInBits>
				    <Class>0</Class>
				    <Internal>true</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>0</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList/>
			</Register>
         <Register>
				    <Name>Output Error Cluster</Name>
				    <Hidden>false</Hidden>
				    <Indicator>true</Indicator>
				    <Datatype>
					    <Cluster>
						      <Name>Output Error Cluster</Name>
						      <TypeList>
							      <Boolean>
								        <Name>status</Name>
							</Boolean>
							      <I32>
								        <Name>code</Name>
							</I32>
							      <String>
								        <Name>source</Name>
							</String>
						</TypeList>
					</Cluster>
				</Datatype>
				    <FlattenedType>1300800000000004000C40210673746174757300000B40030004636F64650000104030FFFFFFFF06736F7572636500002240500003000000010002144F7574707574204572726F7220436C7573746572000001000300000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98724</Offset>
				    <SizeInBits>33</SizeInBits>
				    <Class>30</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>105</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList>
					    <SubControl>
						      <Name>status</Name>
						      <FlattenedType>1800800000000001000C40210673746174757300000100000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>Output Error Cluster</Name>
								        <Name>status</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>105</Item>
								        <Item>0</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>code</Name>
						      <FlattenedType>1800800000000001000B40030004636F646500000100000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>Output Error Cluster</Name>
								        <Name>code</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>105</Item>
								        <Item>1</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>source</Name>
						      <FlattenedType>180080000000000100104030FFFFFFFF06736F7572636500000100000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>Output Error Cluster</Name>
								        <Name>source</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>105</Item>
								        <Item>2</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
				</SubControlList>
			</Register>
			<Register>
				    <Name>Input Error Cluster</Name>
				    <Hidden>false</Hidden>
				    <Indicator>false</Indicator>
				    <Datatype>
					    <Cluster>
						      <Name>Input Error Cluster</Name>
						      <TypeList>
							      <Boolean>
								        <Name>status</Name>
							</Boolean>
							      <I32>
								        <Name>code</Name>
							</I32>
							      <String>
								        <Name>source</Name>
							</String>
						</TypeList>
					</Cluster>
				</Datatype>
				    <FlattenedType>1300800000000004000C40210673746174757300000B40030004636F64650000104030FFFFFFFF06736F757263650000204050000300000001000213496E707574204572726F7220436C75737465720001000300000000000000000000000000</FlattenedType>
				    <Grouping/>
				    <Offset>98728</Offset>
				    <SizeInBits>33</SizeInBits>
				    <Class>30</Class>
				    <Internal>false</Internal>
				    <TypedefPath/>
				    <TypedefRelativePath/>
				    <ID>106</ID>
				    <Bidirectional>true</Bidirectional>
				    <Synchronous>false</Synchronous>
				    <MechanicalAction>Switch When Pressed</MechanicalAction>
				    <AccessMayTimeout>false</AccessMayTimeout>
				    <RegisterNode>false</RegisterNode>
				    <SubControlList>
					    <SubControl>
						      <Name>status</Name>
						      <FlattenedType>1800800000000001000C40210673746174757300000100000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>Input Error Cluster</Name>
								        <Name>status</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>106</Item>
								        <Item>0</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>code</Name>
						      <FlattenedType>1800800000000001000B40030004636F646500000100000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>Input Error Cluster</Name>
								        <Name>code</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>106</Item>
								        <Item>1</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
					    <SubControl>
						      <Name>source</Name>
						      <FlattenedType>180080000000000100104030FFFFFFFF06736F7572636500000100000000000000000000</FlattenedType>
						      <ClusterInformation>
							      <NameHierarchy>
								        <Name>Input Error Cluster</Name>
								        <Name>source</Name>
							</NameHierarchy>
							      <ItemOrder>
								        <Item>106</Item>
								        <Item>2</Item>
							</ItemOrder>
						</ClusterInformation>
						      <TypedefPath/>
						      <TypedefRelativePath/>
					</SubControl>
				</SubControlList>
			</Register>
		</RegisterList>
		  <Icon>
			  <ImageType>0</ImageType>
			  <ImageDepth>8</ImageDepth>
			  <Image>////////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//wAA/////////////////////////wAAAAAAAAAAAP//AAD/+fn5+fn5+fn5+fn59/ks+SzgAAAAAAAAAAAA//8AAP/5///////////////3+Sz5LP8AAAAAAAAAAAD//wAA//n/6OTo////6OTo//f8K/ws/wAAAAAAAAAAAP//AAD/+f/k/+T////k/+T/9ywsLCzgAAAAAAAAAAAA//8AAP/56OT/5Oj/6OT/5Oj3K/wrLP8AAAAAAAAAAAD//wAA//nk6P/o5P/k6P/o5Pf8CPws/wAAAAAAAAAAAP//AAD/+eT////k/+T////k9/wI/Cz/AAAAAAAAAAAA//8AAP/5/////+jk6P/////3K/wrLP8AAAAAAAAAAAD//wAA//n///////////////csLCws/wAAAAAAAAAAAP//AAD/9/f39/f39/f39/f39ywsg4P/AAAAAAAAAAAA//8AAP8sLCwsLCwsLCwsLCwsLCyDBYODAAAAAAAAAAD//wAA/yz8LCwsLCz8LCwsLCMjI4MFBQWDgwAAAAAAAP//AAD//PD8LCws/CP8LCMjLCwsgwUF/wUFg4MAAAAA//8AAP8s7ywsLCwjLCwjLCwsLCyDBf///wUFBYMjIwD//wAA///w////I///I////////4MFBf8FBYODAAAAAP//AAAAAO8AAAAjAAAjAADw7+/wgwUFBYODAAAAAAAA//8AAAAAAPAAAAAjIwAA7wAAAACDBYODAAAAAAAAAAD//wAAAAAAAO/vAAAAAPAAAAAAAIODAAAAAAAAAAAAAP//AAAAAAAAAADw7/DvAAAAAAAAAAAAAAAAAP8AAAAA//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//wAAAAD//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/AAAAAP//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP8AAAAA//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAAAAD//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/AAAAAP//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP8AAAAA//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////w==</Image>
			  <Mask>//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8=</Mask>
			  <Colors>AP///wD//8wA//+ZAP//ZgD//zMA//8AAP/M/wD/zMwA/8yZAP/MZgD/zDMA/8wAAP+Z/wD/mcwA/5mZAP+ZZgD/mTMA/5kAAP9m/wD/ZswA/2aZAP9mZgD/ZjMA/2YAAP8z/wD/M8wA/zOZAP8zZgD/MzMA/zMAAP8A/wD/AMwA/wCZAP8AZgD/ADMA/wAAAMz//wDM/8wAzP+ZAMz/ZgDM/zMAzP8AAMzM/wDMzMwAzMyZAMzMZgDMzDMAzMwAAMyZ/wDMmcwAzJmZAMyZZgDMmTMAzJkAAMxm/wDMZswAzGaZAMxmZgDMZjMAzGYAAMwz/wDMM8wAzDOZAMwzZgDMMzMAzDMAAMwA/wDMAMwAzACZAMwAZgDMADMAzAAAAJn//wCZ/8wAmf+ZAJn/ZgCZ/zMAmf8AAJnM/wCZzMwAmcyZAJnMZgCZzDMAmcwAAJmZ/wCZmcwAmZmZAJmZZgCZmTMAmZkAAJlm/wCZZswAmWaZAJlmZgCZZjMAmWYAAJkz/wCZM8wAmTOZAJkzZgCZMzMAmTMAAJkA/wCZAMwAmQCZAJkAZgCZADMAmQAAAGb//wBm/8wAZv+ZAGb/ZgBm/zMAZv8AAGbM/wBmzMwAZsyZAGbMZgBmzDMAZswAAGaZ/wBmmcwAZpmZAGaZZgBmmTMAZpkAAGZm/wBmZswAZmaZAGZmZgBmZjMAZmYAAGYz/wBmM8wAZjOZAGYzZgBmMzMAZjMAAGYA/wBmAMwAZgCZAGYAZgBmADMAZgAAADP//wAz/8wAM/+ZADP/ZgAz/zMAM/8AADPM/wAzzMwAM8yZADPMZgAzzDMAM8wAADOZ/wAzmcwAM5mZADOZZgAzmTMAM5kAADNm/wAzZswAM2aZADNmZgAzZjMAM2YAADMz/wAzM8wAMzOZADMzZgAzMzMAMzMAADMA/wAzAMwAMwCZADMAZgAzADMAMwAAAAD//wAA/8wAAP+ZAAD/ZgAA/zMAAP8AAADM/wAAzMwAAMyZAADMZgAAzDMAAMwAAACZ/wAAmcwAAJmZAACZZgAAmTMAAJkAAABm/wAAZswAAGaZAABmZgAAZjMAAGYAAAAz/wAAM8wAADOZAAAzZgAAMzMAADMAAAAA/wAAAMwAAACZAAAAZgAAADMA7gAAAN0AAAC7AAAAqgAAAIgAAAB3AAAAVQAAAEQAAAAiAAAAEQAAAADuAAAA3QAAALsAAACqAAAAiAAAAHcAAABVAAAARAAAACIAAAARAAAAAO4AAADdAAAAuwAAAKoAAACIAAAAdwAAAFUAAABEAAAAIgAAABEA7u7uAN3d3QC7u7sAqqqqAIiIiAB3d3cAVVVVAERERAAiIiIAERERAAAAAA==</Colors>
			  <Rectangle>
				    <Left>0</Left>
				    <Top>0</Top>
				    <Right>32</Right>
				    <Bottom>32</Bottom>
			</Rectangle>
		</Icon>
	</VI>
	<Project>
		  <TargetClass>cRIO-9068</TargetClass>
		  <AutoRunWhenDownloaded>false</AutoRunWhenDownloaded>
		  <CompilationResultsTree>
      <CompilationResults>
       <NiFpga>
          <BaseAddressOnDevice>0</BaseAddressOnDevice>
           <DmaChannelAllocationList>
              <Channel name="FXP FIFO">
                 <BaseAddressTag>NiLvFpgaFXP FIFO</BaseAddressTag>
                 <ControlSet>0</ControlSet>
                 <DataType>
                  <Delta>1.000000000000000000000000000000000000000000000000000000</Delta>
                  <IntegerWordLength>16</IntegerWordLength>
                  <Maximum>32767.00000000000000000000000000000000000000000000000000</Maximum>
                  <Minimum>-32768.00000000000000000000000000000000000000000000000000</Minimum>
                  <Signed>true</Signed>
                  <SubType>FXP</SubType>
                  <WordLength>16</WordLength>
               </DataType>
                 <Direction>TargetToHost</Direction>
                 <Implementation>niFpgaTargetToHost</Implementation>
                 <Number>0</Number>
                 <NumberOfElements>1023</NumberOfElements>
                 <UserVisible>true</UserVisible>
            </Channel>
         </DmaChannelAllocationList>
          <RegisterBlockList>
           <RegisterBlock name="NiLvFpgaFXP FIFO">
              <Offset>0xFFC0</Offset>
           </RegisterBlock>
          </RegisterBlockList>
          <UsedBaseClockList>
           <BaseClock name="DmaClk">
         </BaseClock>
           <BaseClock name="BusClk">
         </BaseClock>
           <BaseClock name="40 MHz Onboard Clock">
         </BaseClock>
      </UsedBaseClockList>
          <version>1</version>
   </NiFpga>
       <NiRio>
          <Version>1</Version>
          <ZynqBsEnablePatch>True</ZynqBsEnablePatch>
   </NiRio>
</CompilationResults> </CompilationResultsTree>
		  <MultipleUserClocks>false</MultipleUserClocks>
		  <AllowImplicitEnableRemoval>false</AllowImplicitEnableRemoval>
	</Project>
	<ClientData/>
	<BitstreamMD5>ab62625ba4cb0a125dbbc1abfa773571</BitstreamMD5>
	<Bitstream>Removed to save space</Bitstream>
</Bitfile>
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/tests/test_bitfile.py sha256=02e91f9df6c2d84224a0af1e6a0431b61e4372a90987d9159e1f22aca3bceab3 bytes=2223 -->
## FILE: nifpga/tests/test_bitfile.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/tests/test_bitfile.py`
- sha256: `02e91f9df6c2d84224a0af1e6a0431b61e4372a90987d9159e1f22aca3bceab3`
- bytes: 2223

````python
import unittest
import os
import nifpga

BITFILE_ALL_REGISTERS = 'nifpga/tests/allregistertypes.lvbitx'


class BitfileTest(unittest.TestCase):
    def test_parse_from_path(self):
        bitfile = nifpga.Bitfile(BITFILE_ALL_REGISTERS)
        self.assertEqual(bitfile.filepath, os.path.abspath(BITFILE_ALL_REGISTERS))

    def test_parse_from_contents(self):
        with open(BITFILE_ALL_REGISTERS, 'r') as f:
            bitfile = nifpga.Bitfile(f.read(), parse_contents=True)
            self.assertTrue(bitfile.filepath is None)

    def test_parse_bitfile_with_fxp_fifo(self):
        with open(BITFILE_ALL_REGISTERS, 'r') as f:
            bitfile = nifpga.Bitfile(f.read(), parse_contents=True)
            bitfile.fifos["FXP FIFO"]

    def test_parse_bitfile_with_fxp_register_array(self):
        with open(BITFILE_ALL_REGISTERS, 'r') as f:
            bitfile = nifpga.Bitfile(f.read(), parse_contents=True)
            print(bitfile.registers)
            bitfile.registers["output fxp array"]

    def test_build_spec_version(self):
        bitfile = nifpga.Bitfile(BITFILE_ALL_REGISTERS)
        self.assertEqual(bitfile.build_spec_version, "1.0.0")

    def test_build_spec_description(self):
        bitfile = nifpga.Bitfile(BITFILE_ALL_REGISTERS)
        self.assertEqual(bitfile.build_spec_description, "Test Bitfile Description")

    def test_build_spec_version_none_when_empty(self):
        xml = """<?xml version="1.0" encoding="UTF-8"?>
<Bitfile>
  <BitfileVersion>4.0</BitfileVersion>
  <Documentation>
    <BuildSpecVersion/>
    <BuildSpecDescription/>
  </Documentation>
  <SignatureRegister>AABBCCDD00112233AABBCCDD00112233</SignatureRegister>
  <Project>
    <CompilationResultsTree>
      <CompilationResults>
        <NiFpga>
          <BaseAddressOnDevice>0</BaseAddressOnDevice>
          <DmaChannelAllocationList/>
        </NiFpga>
      </CompilationResults>
    </CompilationResultsTree>
  </Project>
  <VI>
    <RegisterList/>
  </VI>
</Bitfile>"""
        bitfile = nifpga.Bitfile(xml, parse_contents=True)
        self.assertIsNone(bitfile.build_spec_version)
        self.assertIsNone(bitfile.build_spec_description)
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/tests/test_Cluster.py sha256=81af066045db39c355d82b3c0f53c0de1453ee87ac219abfe22b18a59e1b04d8 bytes=9971 -->
## FILE: nifpga/tests/test_Cluster.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/tests/test_Cluster.py`
- sha256: `81af066045db39c355d82b3c0f53c0de1453ee87ac219abfe22b18a59e1b04d8`
- bytes: 9971

````python
from nifpga.bitfile import (_parse_type,
                            UnsupportedTypeError,
                            ClusterMustContainUniqueNames)
import unittest
import xml.etree.ElementTree as ElementTree

cluster_xml = """
<Cluster>
    <Name>input cluster</Name>
    <TypeList>
        <U16>
            <Name>Input Cluster U16</Name>
        </U16>
        <Cluster>
            <Name>output cluster 2</Name>
            <TypeList>
                <FXP>
                    <Name>Input Cluster FXP 4-bit Signed</Name>
                    <Signed>true</Signed>
                    <WordLength>4</WordLength>
                    <IntegerWordLength>2</IntegerWordLength>
                    <Minimum>-2.000000</Minimum>
                    <Maximum>1.750000</Maximum>
                    <Delta>0.250000</Delta>
                    <IncludeOverflowStatus>true</IncludeOverflowStatus>
                </FXP>
                <U8>
                      <Name>Input Cluster  U8</Name>
                </U8>
                <U64>
                      <Name>Input Cluster U64</Name>
                </U64>
                <I8>
                      <Name>Input Cluster I8</Name>
                </I8>
            </TypeList>
        </Cluster>
        <Array>
            <Name>output cluster array</Name>
            <Size>2</Size>
            <Type>
                <Cluster>
                    <Name/>
                    <TypeList>
                        <FXP>
                            <Name>Input Cluster FXP 64-bit Signed Overflow 2</Name>
                            <Signed>true</Signed>
                            <WordLength>64</WordLength>
                            <IntegerWordLength>32</IntegerWordLength>
                            <Minimum>-2147483648.000000</Minimum>
                            <Maximum>2147483648.000000</Maximum>
                            <Delta>0.000000</Delta>
                            <IncludeOverflowStatus>true</IncludeOverflowStatus>
                        </FXP>
                        <I16>
                            <Name>Input Cluster I16 2</Name>
                        </I16>
                        <FXP>
                            <Name>Input Cluster FXP 32-bit Unsigned Overflow 2</Name>
                            <Signed>false</Signed>
                            <WordLength>32</WordLength>
                            <IntegerWordLength>16</IntegerWordLength>
                            <Minimum>0.000000</Minimum>
                            <Maximum>65535.999985</Maximum>
                            <Delta>0.000015</Delta>
                            <IncludeOverflowStatus>true</IncludeOverflowStatus>
                        </FXP>
                        <Boolean>
                            <Name>Input Cluster Bool 2</Name>
                        </Boolean>
                    </TypeList>
                </Cluster>
            </Type>
        </Array>
        <I32>
            <Name>Input Cluster I32</Name>
        </I32>
        <EnumU16>
            <Name>Input Cluster EnumU8</Name>
            <StringList>
                <String>G</String>
                <String>F</String>
                <String>E</String>
                <String>D</String>
                <String>C</String>
                <String>B</String>
                <String>A</String>
            </StringList>
        </EnumU16>
        <U32>
            <Name>Input Cluster U32</Name>
        </U32>
        <Array>
            <Name>output fxp array</Name>
            <Size>2</Size>
            <Type>
                <FXP>
                    <Name>Input Cluster FXP 13-bit Signed 2</Name>
                    <Signed>true</Signed>
                    <WordLength>16</WordLength>
                    <IntegerWordLength>8</IntegerWordLength>
                    <Minimum>-128.000000</Minimum>
                    <Maximum>127.996094</Maximum>
                    <Delta>0.003906</Delta>
                    <IncludeOverflowStatus>false</IncludeOverflowStatus>
                </FXP>
            </Type>
        </Array>
    </TypeList>
</Cluster>
"""

cluster_with_cfxp_xml = """
<Cluster>
    <Name>input cluster</Name>
    <TypeList>
        <U16>
            <Name>Input Cluster U16</Name>
        </U16>
        <CFXP>
          <Name>Some CFXP Register</Name>
        </CFXP>
    </TypeList>
</Cluster>
"""

cluster_with_multiple_members_with_the_same_name = """
<Cluster>
    <Name>input cluster</Name>
    <TypeList>
        <U16>
            <Name>Name</Name>
        </U16>
        <U32>
          <Name>Name</Name>
        </U32>
    </TypeList>
</Cluster>
"""


class ClusterTests(unittest.TestCase):
    def setUp(self):
        tree = ElementTree.fromstring(cluster_xml)
        self.testRegister = _parse_type(tree)

    def test_cluster_zero_data(self):
        data = self.testRegister.unpack_data(0)
        expected_data = \
            {'Input Cluster U16': 0,
             'output cluster 2': {'Input Cluster FXP 4-bit Signed': (False, 0),
                                  'Input Cluster  U8': 0,
                                  'Input Cluster U64': 0,
                                  'Input Cluster I8': 0},
             'output cluster array': [{'Input Cluster FXP 64-bit Signed Overflow 2': (False, 0),
                                       'Input Cluster I16 2': 0,
                                       'Input Cluster FXP 32-bit Unsigned Overflow 2': (False, 0),
                                       'Input Cluster Bool 2': False},
                                      {'Input Cluster FXP 64-bit Signed Overflow 2': (False, 0),
                                       'Input Cluster I16 2': 0,
                                       'Input Cluster FXP 32-bit Unsigned Overflow 2': (False, 0),
                                       'Input Cluster Bool 2': False}],
             'Input Cluster I32': 0,
             'Input Cluster EnumU8': 0,
             'Input Cluster U32': 0,
             'output fxp array': [0, 0]}
        assert data == expected_data
        packed_data = self.testRegister.pack_data(expected_data, 0)
        assert packed_data == 0

    def test_cluster_values_set_to_1(self):
        actual_data = 389948983317742165538549719682430202967988854558358925786670372898282524917257258819755320125926426630253986178278732200331444480
        data = self.testRegister.unpack_data(actual_data)
        expected_data = \
            {'Input Cluster U16': 1,
             'output cluster 2': {'Input Cluster FXP 4-bit Signed': (False, 1),
                                  'Input Cluster  U8': 1,
                                  'Input Cluster U64': 1,
                                  'Input Cluster I8': 1},
             'output cluster array': [{'Input Cluster FXP 64-bit Signed Overflow 2': (False, 1),
                                       'Input Cluster I16 2': 1,
                                       'Input Cluster FXP 32-bit Unsigned Overflow 2': (False, 1),
                                       'Input Cluster Bool 2': True},
                                      {'Input Cluster FXP 64-bit Signed Overflow 2': (False, 1),
                                       'Input Cluster I16 2': 1,
                                       'Input Cluster FXP 32-bit Unsigned Overflow 2': (False, 1),
                                       'Input Cluster Bool 2': True}],
             'Input Cluster I32': 1,
             'Input Cluster EnumU8': 1,
             'Input Cluster U32': 1,
             'output fxp array': [1, 1]}
        assert data == expected_data
        packed_data = self.testRegister.pack_data(expected_data, 0)
        assert packed_data == actual_data

    def test_cluster_random_data(self):
        actual_data = 650140623102406731927256098101662313669128987008919352549838047850309849438881231947219947572849073945363668902620592607917571840
        data = self.testRegister.unpack_data(actual_data)
        expected_cluster = \
            {'Input Cluster U16': 1,
             'output cluster 2': {'Input Cluster FXP 4-bit Signed': (True, -1),
                                  'Input Cluster  U8': 7,
                                  'Input Cluster U64': 4564564654564654,
                                  'Input Cluster I8': -32},
             'output cluster array': [{'Input Cluster FXP 64-bit Signed Overflow 2': (False, -11111),
                                       'Input Cluster I16 2': -1,
                                       'Input Cluster FXP 32-bit Unsigned Overflow 2': (True, 17.5),
                                       'Input Cluster Bool 2': False},
                                      {'Input Cluster FXP 64-bit Signed Overflow 2': (True, 797979),
                                       'Input Cluster I16 2': 0,
                                       'Input Cluster FXP 32-bit Unsigned Overflow 2': (False, 1000.75),
                                       'Input Cluster Bool 2': True}],
             'Input Cluster I32': 1919919,
             'Input Cluster EnumU8': 0,
             'Input Cluster U32': 4294967295,
             'output fxp array': [0, -1]}
        assert data == expected_cluster
        packed_data = self.testRegister.pack_data(expected_cluster, 0)
        assert packed_data == actual_data

    def test_unsupported_type(self):
        tree = ElementTree.fromstring(cluster_with_cfxp_xml)
        with self.assertRaises(UnsupportedTypeError):
            self.testRegister = _parse_type(tree)

    def test_error_when_multiple_members(self):
        tree = ElementTree.fromstring(cluster_with_multiple_members_with_the_same_name)
        with self.assertRaises(ClusterMustContainUniqueNames):
            self.testRegister = _parse_type(tree)
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/tests/test_FXP.py sha256=f9fed4657a76b4b1c21d8ffdc50f6c2e0838097a98438a772bad8a3ad6a1298e bytes=13445 -->
## FILE: nifpga/tests/test_FXP.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/tests/test_FXP.py`
- sha256: `f9fed4657a76b4b1c21d8ffdc50f6c2e0838097a98438a772bad8a3ad6a1298e`
- bytes: 13445

````python
from decimal import Decimal, getcontext
from nifpga import DataType
from nifpga.bitfile import _FXP
from nifpga.tests.test_nifpga import assert_warns
import unittest

getcontext().prec = 100


class MockFxp(_FXP):
    def __init__(self,
                 signed,
                 enableOverflowStatus,
                 word_length,
                 integer_word_length):
        self._signed = signed
        self._word_length = word_length
        self._integer_word_length = integer_word_length
        self._delta = self._calculate_delta()
        self._minimum = self._calculate_minimum()
        self._maximum = self._calculate_maximum()
        self._overflow_enabled = enableOverflowStatus
        self._size_in_bits = self._calculate_size_in_bits()
        self._data_mask = (1 << self._size_in_bits) - 1
        self._word_length_mask = (1 << self._word_length) - 1
        self._signed_bit_mask = 1 << (self._word_length - 1)
        self.set_register_attributes()

    def set_register_attributes(self):
        self._name = "MockFxp"
        self._offset = 0  # Not needed for mock
        self._datatype = DataType.Fxp  # FXP is always DataType.Fxp
        self._ctype_type = self._datatype._return_ctype()
        self._access_may_timeout = False  # Does not affect FXP any different
        self._internal = False  # Cant be internal
        self._is_array = False  # This mock is always a single FXP


class FXPRegisterAsserts(object):
    def __init__(self, test):
        self._test = test

    def assert_fxp_value_converted_to_decimal(self,
                                              register,
                                              read_value,
                                              expected_value):
        actual = register.unpack_data(read_value)
        self._test.assertEqual(actual, expected_value)

    def assert_user_input_converted_to_fxp(self,
                                           register,
                                           user_input,
                                           expected_value):
        actual = register.pack_data(user_input, 0)
        self._test.assertEqual(actual, expected_value)


def _calculate_minimum_fxp_value(register):
    if register._signed:
        return 2**(register._word_length - 1)
    else:
        return 0


def _calculate_maximum_fxp_value(register):
    if register._signed:
        magnitude_bits = register._word_length - 1
    else:
        magnitude_bits = register._word_length
    return (2**(magnitude_bits) - 1)


""" These are a couple of arbitrary binary strings that the following unit
to test a non random value.
"""
binary_string_16bit = '1110010010010110'  # 2's comp = 0001101101101010
binary_string_32bit = '01000101100100100011000100001100'

positive_integer = 42  # Arbitrary constant used in some tests


class FXPRegisterSharedTests(unittest.TestCase):
    def setUp(self):
        self.testRegister = MockFxp(signed=False,
                                    enableOverflowStatus=False,
                                    word_length=1,
                                    integer_word_length=1)
        self.FxpAssert = FXPRegisterAsserts(self)
        self.fxp_value = int('1', 2)
        self.user_value = Decimal(1)

    def test_converting_fxp_to_decimal_value(self):
        self.FxpAssert.assert_fxp_value_converted_to_decimal(self.testRegister,
                                                             self.fxp_value,
                                                             self.user_value)

    def test_converting_user_data_into_binary(self):
        self.FxpAssert.assert_user_input_converted_to_fxp(self.testRegister,
                                                          self.user_value,
                                                          self.fxp_value)

    def test_user_input_less_than_minimum(self):
        less_than_minimum = self.testRegister._minimum - positive_integer
        expected_value = _calculate_minimum_fxp_value(self.testRegister)
        with assert_warns(UserWarning):
            if self.testRegister._overflow_enabled:
                overflow = False
                self.FxpAssert.assert_user_input_converted_to_fxp(self.testRegister,
                                                                  (overflow, less_than_minimum),
                                                                  expected_value)
            else:
                self.FxpAssert.assert_user_input_converted_to_fxp(self.testRegister,
                                                                  less_than_minimum,
                                                                  expected_value)

    def test_user_input_greater_than_maximum(self):
        greater_than_max = self.testRegister._maximum + positive_integer
        expected_value = _calculate_maximum_fxp_value(self.testRegister)
        with assert_warns(UserWarning):
            if self.testRegister._overflow_enabled:
                overflow = False
                self.FxpAssert.assert_user_input_converted_to_fxp(self.testRegister,
                                                                  (overflow, greater_than_max),
                                                                  expected_value)
            else:
                self.FxpAssert.assert_user_input_converted_to_fxp(self.testRegister,
                                                                  greater_than_max,
                                                                  expected_value)


class FXPRegister16bitWord16bitInteger(FXPRegisterSharedTests):
    def setUp(self):
        self.testRegister = MockFxp(signed=False,
                                    enableOverflowStatus=False,
                                    word_length=16,
                                    integer_word_length=16)
        self.FxpAssert = FXPRegisterAsserts(self)
        self.fxp_value = int(binary_string_16bit, 2)
        self.user_value = Decimal(2**(15) + 2**(14) + 2**(13) + 2**(10)
                                  + 2**(7) + 2**(4) + 2**(2) + 2**(1))


class FXPRegister16bitWord16bitIntegerSigned(FXPRegisterSharedTests):
    def setUp(self):
        self.testRegister = MockFxp(signed=True,
                                    enableOverflowStatus=False,
                                    word_length=16,
                                    integer_word_length=16)
        self.FxpAssert = FXPRegisterAsserts(self)
        self.fxp_value = int(binary_string_16bit, 2)
        self.user_value = Decimal((-1) * (2**(12) + 2**(11) + 2**(9) + 2**(8)
                                          + 2**(6) + 2**(5) + 2**(3) + 2**(1)))


class FXPRegister15bitWord15bitIntegerOverflow(FXPRegisterSharedTests):

    def setUp(self):
        self.testRegister = MockFxp(signed=False,
                                    enableOverflowStatus=True,
                                    word_length=15,
                                    integer_word_length=15)
        self.FxpAssert = FXPRegisterAsserts(self)
        self.fxp_value = int(binary_string_16bit, 2)
        self.user_value = (True, Decimal(2**(14) + 2**(13) + 2**(10) + 2**(7)
                                         + 2**(4) + 2**(2) + 2**(1)))

    def test_converting_user_data_without_overflow_use_false(self):
        fxp_with_false_overflow = self.fxp_value - 2**self.testRegister._word_length
        self.FxpAssert.assert_user_input_converted_to_fxp(self.testRegister,
                                                          self.user_value[1],
                                                          fxp_with_false_overflow)


class FXPRegister15bitWord15bitIntegerSignedOverflow(FXPRegisterSharedTests):
    def setUp(self):
        self.testRegister = MockFxp(signed=True,
                                    enableOverflowStatus=True,
                                    word_length=15,
                                    integer_word_length=15)
        self.FxpAssert = FXPRegisterAsserts(self)
        self.fxp_value = int(binary_string_16bit, 2)
        self.user_value = (True, Decimal((-1) * (2**(12) + 2**(11) + 2**(9)
                                                 + 2**(8) + 2**(6) + 2**(5)
                                                 + 2**(3) + 2**(1))))

    def test_overflow_bit_is_not_calculated_in_twos_compliment(self):
        # Create a 15 bit word that is all 1's
        value = int('1' * (self.testRegister._word_length + 1), 2)
        result = self.testRegister.unpack_data(value)
        """ The expected value of overflow(1) 111 1111 1111 1111, would
        expect -1 and an overflow. as the twos complement of the non-overflow
        bits would be 000 0000 0000 0001"""
        self.assertTrue(result[0])
        self.assertEqual(-1, result[1])


class FXPRegister16bitWord0bitInteger(FXPRegisterSharedTests):
    def setUp(self):
        self.testRegister = MockFxp(signed=False,
                                    enableOverflowStatus=False,
                                    word_length=16,
                                    integer_word_length=0)
        self.FxpAssert = FXPRegisterAsserts(self)
        self.fxp_value = int(binary_string_16bit, 2)
        self.user_value = Decimal(2**(-1) + 2**(-2) + 2**(-3) + 2**(-6)
                                  + 2**(-9) + 2**(-12) + 2**(-14) + 2**(-15))


class FXPRegister15bitWord0bitIntegerOverflow(FXPRegisterSharedTests):
    def setUp(self):
        self.testRegister = MockFxp(signed=False,
                                    enableOverflowStatus=True,
                                    word_length=15,
                                    integer_word_length=0)
        self.FxpAssert = FXPRegisterAsserts(self)
        self.fxp_value = int(binary_string_16bit, 2)
        self.user_value = (True, Decimal(2**(-1) + 2**(-2) + 2**(-5) + 2**(-8)
                                         + 2**(-11) + 2**(-13) + 2**(-14)))


class FXPRegister15bitWord0bitIntegerSignedOverflow(FXPRegisterSharedTests):
    def setUp(self):
        self.testRegister = MockFxp(signed=True,
                                    enableOverflowStatus=True,
                                    word_length=15,
                                    integer_word_length=0)
        self.FxpAssert = FXPRegisterAsserts(self)
        self.fxp_value = int(binary_string_16bit, 2)
        self.user_value = (True, Decimal((-1) * (2**(-3) + 2**(-4) + 2**(-6)
                                                 + 2**(-7) + 2**(-9) + 2**(-10)
                                                 + 2**(-12) + 2**(-14))))


class FXPRegister32bitWord16bitIntegerOverflow(FXPRegisterSharedTests):
    def setUp(self):
        self.testRegister = MockFxp(signed=False,
                                    enableOverflowStatus=True,
                                    word_length=32,
                                    integer_word_length=16)
        self.FxpAssert = FXPRegisterAsserts(self)
        """ binary String '(0) 0100010110010010.0011000100001100' """
        self.fxp_value = int('0' + binary_string_32bit, 2)
        self.user_value = (False, Decimal(2**(1) + 2**(4) + 2**(7) + 2**(8)
                                          + 2**(10) + 2**(14) + 2**(-3)
                                          + 2**(-4) + 2**(-8) + 2**(-13)
                                          + 2**(-14)))


class FXPRegister16bitWord100bitInteger(FXPRegisterSharedTests):
    def setUp(self):
        self.testRegister = MockFxp(signed=False,
                                    enableOverflowStatus=False,
                                    word_length=16,
                                    integer_word_length=100)
        self.FxpAssert = FXPRegisterAsserts(self)
        self.fxp_value = int(binary_string_16bit, 2)
        self.user_value = Decimal(2**(99) + 2**(98) + 2**(97) + 2**(94)
                                  + 2**(91) + 2**(88) + 2**(86) + 2**(85))


class FXPRegister16bitWordNegative100bitInteger(FXPRegisterSharedTests):
    def setUp(self):
        self.testRegister = MockFxp(signed=False,
                                    enableOverflowStatus=False,
                                    word_length=16,
                                    integer_word_length=-100)
        self.FxpAssert = FXPRegisterAsserts(self)
        self.fxp_value = int(binary_string_16bit, 2)
        self.user_value = Decimal(2**(-101) + 2**(-102) + 2**(-103) + 2**(-106)
                                  + 2**(-109) + 2**(-112) + 2**(-114)
                                  + 2**(-115))


class FXPRegister64bitWord64bitIntegerOverflow(FXPRegisterSharedTests):
    def setUp(self):
        self.testRegister = MockFxp(signed=False,
                                    enableOverflowStatus=True,
                                    word_length=64,
                                    integer_word_length=64)
        self.FxpAssert = FXPRegisterAsserts(self)
        """(1) 0100 0101 1001 0010 0011 0001 0000 1100 0100 0101 1001 0010 0011 0001 0000 1100 """
        self.fxp_value = int('1' + binary_string_32bit + binary_string_32bit, 2)
        self.user_value = (True, Decimal(5013123263993360652))
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/tests/test_nifpga.py sha256=4705e1d9755361fb92db05faeac9c9ee55c3961192b13389151019d814303e83 bytes=11971 -->
## FILE: nifpga/tests/test_nifpga.py

- repository: `ni/nifpga-python`
- source_path: `nifpga/tests/test_nifpga.py`
- sha256: `4705e1d9755361fb92db05faeac9c9ee55c3961192b13389151019d814303e83`
- bytes: 11971

````python
import ctypes
import mock
import unittest
import sys
import warnings
from contextlib import contextmanager
from nose import SkipTest

import nifpga
from nifpga.statuscheckedlibrary import (check_status,
                                         NamedArgtype,
                                         LibraryFunctionInfo,
                                         LibraryNotFoundError,
                                         StatusCheckedLibrary)

python_version = 3 if sys.version_info >= (3, 0) else 2


def raise_an_exception():
    """
    A helper for NiFpgaStatusExceptionTest
    """
    session = ctypes.c_int32(0x0000beef)
    fifo = ctypes.c_uint32(0x0000f1f0)
    data = ctypes.c_uint64(0x0000da7a)
    number_of_elements = ctypes.c_size_t(0x100)
    timeout_ms = ctypes.c_size_t(0x200)
    elements_remaining = ctypes.c_size_t(0x300)
    bogus_string_argument = ctypes.c_char_p(b"I am a string")
    exception = nifpga.FifoTimeoutError(
        function_name="Dummy Function Name",
        argument_names=["session",
                        "fifo",
                        "data",
                        "number of elements",
                        "timeout ms",
                        "elements remaining",
                        "a bogus string argument"],
        function_args=(session,
                       fifo,
                       data,
                       number_of_elements,
                       timeout_ms,
                       elements_remaining,
                       bogus_string_argument))
    raise exception


class NiFpgaStatusExceptionTest(unittest.TestCase):
    def test_autogenerated_status_warning_and_error_classes_exist(self):
        nifpga.FifoTimeoutWarning
        nifpga.FifoTimeoutError

    def test_can_get_arguments_from_exception(self):
        try:
            raise_an_exception()
            self.fail("An exception should have been raised")
        except nifpga.FifoTimeoutError as e:
            self.assertEqual(-50400, e.get_code())
            self.assertEqual("FifoTimeout", e.get_code_string())
            self.assertEqual("Dummy Function Name", e.get_function_name())

            args = e.get_args()
            self.assertEqual(args["session"], 0x0000beef)
            self.assertEqual(args["fifo"], 0x0000f1f0)
            self.assertEqual(args["data"], 0x0000da7a)
            self.assertEqual(args["number of elements"], 0x100)
            self.assertEqual(args["timeout ms"], 0x200)
            self.assertEqual(args["elements remaining"], 0x300)
            self.assertEqual(args["a bogus string argument"], b"I am a string")

            # Spot check a couple different types of args in the
            # printed string that should be helpful for readability
            exception_str = str(e)
            # numbers in hex!
            self.assertIn("session: 0xbeef", exception_str)
            # strings have single quotes around them
            if python_version == 2:
                self.assertIn("a bogus string argument: 'I am a string'", exception_str)
            else:
                self.assertIn("a bogus string argument: b'I am a string'", exception_str)

    def test_status_exceptions_can_be_pickled_across_processes(self):
        try:
            import jobrunner
        except ImportError:
            raise SkipTest("jobrunner not installed, skipping")
        runner = jobrunner.JobRunner(jobrunner.JobRunner.RUN_MODE_MULTIPROCESS,
                                     runnables=[raise_an_exception],
                                     auto_assert=False)
        result = runner.run()[0]
        self.assertTrue(result.exception_occured())
        self.assertEqual(str(result.err_type), str(nifpga.FifoTimeoutError))
        self.assertIn("session: 0xbeef", result.err_class)
        if python_version == 2:
            self.assertIn("a bogus string argument: 'I am a string'", result.err_class)
        else:
            self.assertIn("a bogus string argument: b'I am a string'", result.err_class)


@check_status(function_name="Fake Function Name", argument_names=["code"])
def return_a_checked_status(code):
    """
    A helper for CheckStatusTest
    """
    return code


@contextmanager
def assert_warns(warning):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        yield
        # verify the warning occured
        assert len(w) == 1
        assert isinstance(w[0].message, warning)


class CheckStatusTest(unittest.TestCase):
    def test_success(self):
        return_a_checked_status(0)

    def test_get_known_error(self):
        with self.assertRaises(nifpga.FifoTimeoutError):
            return_a_checked_status(-50400)

    def test_get_known_warning(self):
        with assert_warns(nifpga.FifoTimeoutWarning):
            return_a_checked_status(50400)

    def test_get_unknown_error(self):
        with self.assertRaises(nifpga.UnknownError):
            return_a_checked_status(-1)

    def test_get_unknown_warning(self):
        with assert_warns(nifpga.UnknownWarning):
            return_a_checked_status(1)


class StatusCheckedLibraryTestCRunTime(unittest.TestCase):
    """
    Since we can't load NiFpga on a dev machine unless we have all its
    dependencies installed (i.e. a bunch of NI software we don't want on
    a dev machine), we'll cheat and use the C runtime library and
    atoi. atoi doesn't really return a NiFpga_Status, but we can pretend.
    """
    def setUp(self):
        self._c_runtime = StatusCheckedLibrary(
            "c",
            library_function_infos=[
                LibraryFunctionInfo(
                    pretty_name="c_atoi",
                    name_in_library="atoi",
                    named_argtypes=[
                        NamedArgtype("nptr", ctypes.c_char_p),
                    ])
            ])

    def test_success(self):
        self._c_runtime.c_atoi(b"0")
        self._c_runtime["c_atoi"](b"0")

    def test_get_unknown_error(self):
        with self.assertRaises(nifpga.UnknownError):
            self._c_runtime.c_atoi(b"-1")

    def test_get_unknown_warning(self):
        with warnings.catch_warnings(record=True) as w:
            self._c_runtime.c_atoi(b"1")

            assert len(w) == 1
            warning = w[0].message
            # Make sure all this propagates into the warning.
            self.assertEqual(1, warning.get_code())
            self.assertEqual(b"1", warning.get_args()["nptr"])

            # These make the warning message readable
            self.assertIn("atoi", str(warning))
            if python_version == 2:
                self.assertIn("nptr: '1'", str(warning))
            else:
                self.assertIn("nptr: b'1'", str(warning))


class StatusCheckedLibraryTestFunctionDoesntExist(unittest.TestCase):
    """
    New versions of NiFpga will have new functions.  We want the API to support
    old versions of NiFpga without erroring because it can't find certain symbols.
    So StatusCheckedLibrary will return VersionMismatchError for symbols it can't
    find.
    """
    def setUp(self):
        self._c_runtime = StatusCheckedLibrary(
            "c",
            library_function_infos=[
                LibraryFunctionInfo(
                    pretty_name="DoesntExist",
                    name_in_library="functionThatDoesntExist",
                    named_argtypes=[
                        NamedArgtype("nptr", ctypes.c_char_p),
                    ])
            ])

    def test_correct_error(self):
        with self.assertRaises(nifpga.VersionMismatchError):
            self._c_runtime.DoesntExist(b"0")
        with self.assertRaises(nifpga.VersionMismatchError):
            self._c_runtime["DoesntExist"](b"0")


class StatusCheckedLibraryTestMockedLibrary(unittest.TestCase):
    """
    Since we can't load NiFpga on a dev machine unless we have all its
    dependencies installed (i.e. a bunch of NI software we don't want on
    a dev machine), we'll monkey patch and use mocked libraries.
    """
    # so nose shows test names instead of docstrings
    def shortDescription(self):
        return None

    @mock.patch('nifpga.statuscheckedlibrary.ctypes.util.find_library')
    @mock.patch('nifpga.statuscheckedlibrary.ctypes.cdll')
    def setUp(self, mock_cdll, mock_find_library):
        """
        Setup up self._library so that self._library.AwesomeFunction(int, str)
        can be called, and the return value can be changed by setting
        self._mock_awesome_function.return_value.
        """
        mock_loaded_library = mock.Mock()
        mock_cdll.LoadLibrary.return_value = mock_loaded_library
        self._mock_awesome_function = mock.Mock()
        self._mock_awesome_function.__name__ = "Entrypoint_AwesomeFunction"
        mock_loaded_library.Entrypoint_AwesomeFunction = self._mock_awesome_function
        self._library = StatusCheckedLibrary(
            library_name="CoolLibrary",
            library_function_infos=[
                LibraryFunctionInfo(
                    pretty_name="AwesomeFunction",
                    name_in_library="Entrypoint_AwesomeFunction",
                    named_argtypes=[NamedArgtype("some_integer", ctypes.c_uint32),
                                    NamedArgtype("some_string", ctypes.c_char_p)])
            ])

    def test_good_error_message_from_memory_full_error(self):
        """ Tests a good error message from a library call that fails.
        1. Correctly converts -52000 to NiFpgaMemoryFullError
        2. An integer arg gets printed as hex (easier to debug than decimal)
        3. A string arg gets printed with quotes surrounding it (so it's obviously a string)
        """
        self._mock_awesome_function.return_value = -52000
        try:
            self._library.AwesomeFunction(ctypes.c_uint32(33), ctypes.c_char_p(b"2"))
            self.fail("AwesomeFunction should have raised MemoryFull")
        except nifpga.MemoryFullError as e:
            if python_version == 2:
                self.assertEqual(
                    "Error: MemoryFull (-52000) when calling 'Entrypoint_AwesomeFunction' with arguments:"
                    "\n\tsome_integer: 0x21L"
                    "\n\tsome_string: '2'", str(e))
            else:
                self.assertEqual(
                    "Error: MemoryFull (-52000) when calling 'Entrypoint_AwesomeFunction' with arguments:"
                    "\n\tsome_integer: 0x21"
                    "\n\tsome_string: b'2'", str(e))

    def test_success_when_library_function_is_success(self):
        """ Tests that a 0 status return value does not raise any errors. """
        self._mock_awesome_function.return_value = 0
        self._library.AwesomeFunction(ctypes.c_uint32(33), ctypes.c_char_p(b"2"))

    def test_good_error_message_if_wrong_number_of_arguments(self):
        """ Tests that calling a function with wrong number of arguments is error """
        try:
            self._library.AwesomeFunction(ctypes.c_uint32(33))
            self.fail("AwesomeFunction should have raised TypeError")
        except TypeError as e:
            self.assertEqual("Entrypoint_AwesomeFunction takes exactly 2 arguments (1 given)", str(e))


class NiFpgaTest(unittest.TestCase):
    def test_that_we_at_least_get_to_try_loading_library(self):
        # We can't do much without NiFpga and other NI software actually
        # being installed, but on a dev machine we can at least
        # catch a few more errors by trying to creating a NiFpga instance and
        # expect to fail when the library can't be found.
        try:
            nifpga.nifpga._NiFpga()
        except LibraryNotFoundError:
            pass
````

<!--NI_OSS_SOURCE repo=nifpga-python path=nifpga/VERSION sha256=72743dfc9b8a60d45cf579fbf36156844d580ba6142f3ad1e588bb0ea439786f bytes=8 -->
## FILE: nifpga/VERSION

- repository: `ni/nifpga-python`
- source_path: `nifpga/VERSION`
- sha256: `72743dfc9b8a60d45cf579fbf36156844d580ba6142f3ad1e588bb0ea439786f`
- bytes: 8

````text
22.0.0
````

<!--NI_OSS_SOURCE repo=nifpga-python path=README.md sha256=026e7942665a5004c811d96fc163ef54db2afca0fa37464b9bcf075a2d932d6e bytes=1709 -->
## FILE: README.md

- repository: `ni/nifpga-python`
- source_path: `README.md`
- sha256: `026e7942665a5004c811d96fc163ef54db2afca0fa37464b9bcf075a2d932d6e`
- bytes: 1709

````markdown
FPGA Interface Python API
=========================

[![Build Status](https://travis-ci.org/ni/nifpga-python.svg?branch=master)](https://travis-ci.org/ni/nifpga-python)

Overview
--------
The National Instruments FPGA Interface Python API is used for communication between processor and FPGA within NI reconfigurable I/O (RIO) hardware such as NI CompactRIO, NI Single-Board RIO, NI FlexRIO, and NI R Series multifunction RIO.

With the FPGA Interface Python API, developers can use LabVIEW FPGA to program the FPGA within NI hardware and communicate to it from Python running on a host computer. This gives engineers and scientists with Python expertise the ability to take advantage of compiled LabVIEW FPGA bitfiles, also the option to reuse existing Python code.

Installation
------------
NiFpga can be installed by cloning the master branch and then in a command
line in the directory of setup.py run:

    pip install --pre .

Or by installing from PyPI using:

    pip install nifpga
    
nifpga supports Python 3.5+.

Examples
--------

The FPGA Interface Python API is session based. LabVIEW FPGA will generate
bitfiles (.lvbitx) that can be used to program the hardware. For additional
information on sessions view our Read the docs documentation

Example usage of FPGA configuration functions:

    with Session(bitfile="BitfilePath.lvbitx", resource="RIO0") as session:
        session.reset()
        session.run()
        my_control = session.registers["MyControl"]
        my_control.write(4)
        data = my_control.read()


See our [readthedocs page](http://nifpga-python.readthedocs.io/en/latest/) for more detailed examples and documentation.
````

<!--NI_OSS_SOURCE repo=nifpga-python path=requirements.txt sha256=472ac778b57b66da828c96a9bc3c5e1052d758c09b536b092834193c868d73fe bytes=53 -->
## FILE: requirements.txt

- repository: `ni/nifpga-python`
- source_path: `requirements.txt`
- sha256: `472ac778b57b66da828c96a9bc3c5e1052d758c09b536b092834193c868d73fe`
- bytes: 53

````text
--index-url https://pypi.python.org/simple/

-e .
````

<!--NI_OSS_SOURCE repo=nifpga-python path=setup.py sha256=777397d8b9a7082d2ccde02cbc13bd740f9dcc01c08f9a1b59a8453058cd072b bytes=1970 -->
## FILE: setup.py

- repository: `ni/nifpga-python`
- source_path: `setup.py`
- sha256: `777397d8b9a7082d2ccde02cbc13bd740f9dcc01c08f9a1b59a8453058cd072b`
- bytes: 1970

````python
from setuptools import setup, find_packages
import os

# The VERSION file is codegned by the build.
# setup.py needs to be in version control, but checking versions into that is problematic
def get_version():
    version = None
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_dir = os.path.join(script_dir, "nifpga")
    if not os.path.exists(os.path.join(script_dir, "VERSION")):
        version = "1.0.0.dev0"
    else:
        with open(os.path.join(script_dir, "VERSION"), "r") as version_file:
            version = version_file.read().rstrip()
    return version


def get_long_description():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists("README.md"):
        return ""
    else:
        with open(os.path.join(this_dir, "README.md")) as readme:
            return readme.read().strip()


setup(name="nifpga",
      description="Python API for interacting with National Instrument's LabVIEW FPGA Devices",
      long_description=get_long_description(),
      long_description_content_type="text/markdown",
      version=get_version(),
      packages=find_packages(),
      install_requires=[],
      python_requires=">3.4",
      package_data={'nifpga': ['VERSION']},
      author="National Instruments",
      url="https://github.com/ni/nifpga-python",
      license="MIT",
      classifiers=[
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Hardware",
        "Topic :: System :: Hardware :: Hardware Drivers"]
      )
````
