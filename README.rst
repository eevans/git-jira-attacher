==============
git-jira-tools
==============

A collection of tools for managing patch-based workflows between Git
and JIRA_, designed for use with `Apache's JIRA installation`_.

.. _JIRA: http://www.atlassian.com/software/jira/
.. _`Apache's JIRA installation`: https://issues.apache.org/jira/

Description
-----------
git-jira-attacher
~~~~~~~~~~~~~~~~~
git-jira-attacher exports patches from Git using ``git format-patch``,
then attaches them to a JIRA issue using the SOAP API.

Run without arguments for usage.  ``GIT_RANGE`` is a commit range, like
master..HEAD.  git-jira-attacher expects commit messages to begin
with (e.g.) ``PROJECT-123.`` in order to identify the
relevant issue.  If all of the commits apply to a single issue,
only one needs to have the tag.  Otherwise, every commit needs a tag.

jira-am
~~~~~~~
This utility imports patches created by ``git-format-patch`` or
``git-jira-attacher`` (see above). You can think of this script as an
analog to ``git-am(1)``.

Run without arguments for usage.

jira-apply
~~~~~~~~~~
This utility imports patches attached to a Jira issue. You can think of
this script as an analog to ``git-apply(1)`` or ``patch(1)``.

Run without arguments for usage.

Configuration
-------------
Each of the above utilities accepts arguments for your Jira username, and
each interactively prompts for the password, but it is possible to
configure one or both of these values to keep from typing them repeatedly.

Create or edit the file ``~/.git-jira-tools`` and set values for
``username`` and ``password``. For example:

::

  username = jsmith
  password = 4unkym0nk3y

License
-------
This software is distributed under the MIT license.
See COPYING for details.
