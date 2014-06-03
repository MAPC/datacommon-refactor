MetroBoston DataCommon
======================

*The Refactoring*


We are refactoring the MetroBoston DataCommon with the following goals:

+ set up the MBDC as a single-site GeoNode project
+ decouple Weave from the application
+ create a git-based workflow with automated deploys

This refactor will not address:

+ design changes, apart from those required by the new GeoNode base styles
+ upgrades to functionality or redesign of workflows

This repository will include only the GeoNode project, and will not deal with GeoServer at all.


Contributing
------------

If you have push privileges, please push contributions as separate branches, and issue a pull request to the `MAPC:develop` branch. Please allow someone else (or assign them in GitHub if there is any urgency) to review the code before merging.

All development should be done on forks created from the `develop` branch. No pull requests should be pointed to `master`, nor should code be merged directly into `master`.

Please run `git pull <mapc-repo> develop` before pushing commits, in order to avoid merge conflicts in the pull request.


### Branches

`develop`: The branch to check out, create forks from, and issue pull requests into.

`staging`: This branch will be running on the staging server. It will eventually be available at http://staging.metrobostondatacommon.org.

`master`:  This branch will be running on the production server. It will eventually be avaialble at http://metrobostondatacommon.org



Structure & Style Guide
-----------------------

If there's any new code that we're writing, let's follow this guide: [Sandi Metz' Rules For Developers](http://robots.thoughtbot.com/sandi-metz-rules-for-developers)

In sum:

+ New classes (and maybe even ones we're refactoring) can be no longer than one hundred lines of code.
+ Methods can be no longer than five lines of code.
+ Pass no more than four parameters into a method. Hash options (keyword arguments) are parameters.
+ Views can only instatiate one object. Therefore, templates can only know about one instance variable and templates should only send messages to that object.

Just a few more things:

+ Use meaningful variable names.
+ Lines of code should be no longer than 80 characters.