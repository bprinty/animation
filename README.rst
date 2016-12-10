=========
animation
=========

Tools for terminal-based wait animations


Installation
============

.. code-block:: bash

    git clone http://github.com/bprinty/animation.git
    cd animation
    python setup.py install


Documentation
=============

Documentation for the package can be found at `Read The Docs <http://animation.readthedocs.org/>`_.


Usage
=====

The animation module provides decorators for doing terminal-based wait animations. To add a wait animation to a function that requires some processing time, simply decorate the function with the wait animation you want to use.

Here is an example of how to use it in a project:

.. code-block:: python

    import animation
    import time

    @animation.simple_wait
    def long_running_function():
        ... 5 seconds later ...
        return


This will print an animated waiting message like this (the elipses at the end of the text grow and shrink while the function executes):

.. code-block:: bash
    
    waiting ...


The animation types provided by default are:

* bar (simple bar that slides back and forth)
* spinner (a spinning line)
* dots (dots that move around in a sqare)
* elipses (elipses that grow and shrink)
* text with elipses (elipses with text in front of them)


And you can use any of these built-in animations like so:

.. code-block:: python

    import animation
    import time

    @animation.wait('bar')
    def long_running_function():
        ... 5 seconds later ...
        return

    @animation.wait('spinner')
    def long_running_function():
        ... 5 seconds later ...
        return


In addition to these default types, the module also supports custom animations. For example, to create an animation with a counter-clockwise spinning wheel:

.. code-block:: python

    wheel = ('-', '/', '|', '\\')
    @animation.wait(wheel)
    def long_running_function():
        ... 5 seconds later ...
        return


If you want to manually start and stop the wait animation, you can use the ```animation.Wait``` class:

.. code-block:: python

    wait = animation.Wait()
    wait.start()
    long_running_function()
    wait.stop()


Questions/Feedback
------------------

File an issue in the `GitHub issue tracker <https://github.com/bprinty/animation/issues>`_.
