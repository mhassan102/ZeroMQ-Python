Build Status: [![linux/mac](https://travis-ci.org/quiltdata/quilt-compiler.svg?branch=master)](https://travis-ci.org/quiltdata/quilt-compiler) [![Build status](https://ci.appveyor.com/api/projects/status/github/mhassan102/quilt-compiler?svg=true)](https://ci.appveyor.com/project/mhassan102/quilt-compiler)


## ZeroMQ-Python

Python zeromq example for PUB/SUB and PUSH/PULL case

Key difference:

In PUB/SUB, publisher is unware of subscriber for connection,
However In PUSH/PULL, manager only send message if worker is connected.
