====================
Git Setup
====================

.. toctree::
    :caption: Navigation

    git-setup


If you want to easily stay up-to-date with the latest version of Mysterious Messenger without disturbing your existing code, setting up a fork of the Mysterious Messenger repository will allow you to easily merge updates onto your existing code.

**What you need:**

* A GitHub account (https://github.com/)
* Git and Bash (http://opensourcerer.diy.org/challenge/3)

    * A more in-depth guide on installing Git Bash for Windows: https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows/


Instructions
=============

* First, go to https://github.com/shawna-p/mysterious-messenger and sign into GitHub.
* In the top-right corner of the page, click **Fork**.
* Open Git Bash (Windows) or Terminal (Mac)
* Change the current directory to the one where you want the cloned project to be. You can type ``ls`` (lowercase ``LS``) to see a list of directories available to you, and ``cd Documents`` to change to the Documents folder, for example.
* Type ``git clone https://github.com/YOUR-USERNAME/mysterious-messenger`` where ``YOUR-USERNAME`` is your GitHub username where you forked the repository. Press Enter.

You should now have a local copy of the mysterious-messenger repository. Next, you'll configure it to get the most recent update.

* Navigate in Git Bash/Terminal to the new directory where you cloned the repository. If you still have Git Bash/Terminal open, you should be able to type ``cd mysterious-messenger`` to open it.
* Type ``git remote -v`` and press Enter. You should see

.. code-block:: bash

    $ git remote -v
    > origin https://github.com/YOUR-USERNAME/mysterious-messenger.git (fetch)
    > origin https://github.com/YOUR-USERNAME/mysterious-messenger.git (push)

* Type ``git remote add upstream https://github.com/shawna-p/mysterious-messenger.git`` and press Enter.
* Type ``git remote -v`` and press Enter. It should now look like:

.. code-block:: bash

    $ git remote -v
    > origin https://github.com/YOUR-USERNAME/mysterious-messenger.git (fetch)
    > origin https://github.com/YOUR-USERNAME/mysterious-messenger.git (push)
    > upstream https://github.com/shawna-p/mysterious-messenger.git (fetch)
    > upstream https://github.com/shawna-p/mysterious-messenger.git (push)

Now you should make sure you get the most recent released version, which is currently v3.0.1

* Type ``git checkout v3.1.0`` and press Enter
* Next, type ``git merge tags/v3.1.0`` and press Enter.

You should now have v3.1.0 of Mysterious Messenger. In the future, you can use ``git checkout v3.1.0`` and ``git merge tags/v3.1.0`` with future version numbers to update to the latest version of Mysterious Messenger.

Further resources
==================

* How to fork a repo https://docs.github.com/en/github/getting-started-with-github/fork-a-repo
* Configuring a remote for a fork https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork
