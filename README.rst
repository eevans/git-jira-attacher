=================
git-jira-attacher
=================
A script to upload patches from Git to JIRA_, designed for use with
`Apache's JIRA installation`_.

git-jira-attacher exports patches from Git using ``git format-patch``,
then attaches them to a JIRA issue using the SOAP API.

.. _JIRA: http://www.atlassian.com/software/jira/
.. _`Apache's JIRA installation`: https://issues.apache.org/jira/

Usage
-----
Run without arguments for usage.  ``GIT_RANGE`` is a commit range, like
master..HEAD.  git-jira-attacher expects commit messages to begin
with (e.g.) ``PROJECT-123.`` in order to identify the
relevant issue.  If all of the commits apply to a single issue,
only one needs to have the tag.  Otherwise, every commit needs a tag.

Thrift developers, don't forget to set *patch available* to true.

License
-------
This software is distributed under the MIT license.
See COPYING for details.
