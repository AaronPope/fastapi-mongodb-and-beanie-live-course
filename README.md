# FastAPI MongoDB and Beanie Live Course

https://maven.com/talk-python/modern-apis-with-fastapi-and-mongodb

This is my fork of the repo for the above course.

### Branches
* `main`: Standard main branch -- Completed, working code should be committed here.  It will also be updated with upstream updates.
* `2022-08`: Will ingest from "upstream" (the branch from which this repo was forked).  There should not be any updates make to this branch outside of syncing with "upstream."
* `local/*`: Typically used to try something out that may not be committed or to do a trial run of an involved commit.
* `exercise/[exercise-name]`: Working branches for assigned exercises.  These should get merged into `main` upon completion.

*Reminder to future self on how to handle updates from upstream*
https://stackoverflow.com/questions/7244321/how-do-i-update-or-sync-a-forked-repository-on-github

``` zsh
# adds a local reference to a remote named "upstream"
git remote add upstream https://github.com/talkpython/fastapi-mongodb-and-beanie-live-course.git

git fetch upstream

# checkout target branch
git checkout `2022-08`

# merge or rebase from upstream, as desired
git merge upstream/2022-08
```