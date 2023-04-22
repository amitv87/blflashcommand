Boufallo Lab Flash Command - Open Source Version
================================================

This repo contains the completed work of "open sourcing" the Boufallo Lab
flash command. This utility is provided in binary form under Apache 2.0 License.
It is a [pyinstaller]() executable, so I have unpacked the binary, run it
through several Python 3.7 decompilers, and made a few adjustments. Primary
changes:

* The libs/bflb_configobj.py file has been completely rewritten. It appears
  to have been a handwritten recursive descent parser for ini files that
  include the ability to have complex objects. In reality, the configuration
  that seems to exist for flashing is simple key/value pairs in sections,
  so 2k+ lines of code were removed and replaced with simple shims to the
  python standard library
* Some additional logs were added to the output to let the user know what
  files were being used. This was necessary to debug the decompiler output
  and I thought they were useful

I have licensed this as Apache 2.0 to reflect the origin license. This is tested
and working with BL616 MCU. The flashing host computer was running Linux. This
is good for my needs and it should work for other MCUs/other flashing hosts.
However, I do not intend to provide support for anything beyond my own needs.
I am happy to take pull requests!

Decompilers used
----------------

* [decompyle3](https://pypi.org/project/decompyle3/): This was the primary decompiler for the project
* [unpyc3](https://github.com/andrew-tavera/unpyc37.git): unpyc3 did a better job on 2 or 3 of the files (see logs)
* [pycdc](https://github.com/zrax/pycd): While not used on any files, it served
  as a useful comparison tool. A few miscompiles from decompyle3 were more
  obvious because both pycdc and unpyc3 disagreed with the decompyle3 output
