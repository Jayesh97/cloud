## Checkpoint-1 

<p></p>

## User Stories Checkpoint-1 

<p></p>

| Checkpoint | Issue Number | Issue Name                                                | Task                                                                  | Created/Updated | Estimate | Assignees         | Completed   |
|-----------|--------------|-----------------------------------------------------------|-----------------------------------------------------------------------|-----------------|----------|-------------------|-------------|
| 1         | 1            | Setting up 'pipeline setup' CLI command                   | Modify package.json                                                   | 13 Feb 2020     | 4        | sjbondu           | Completed   |
|           |              |                                                           | Enable command pipeline setup                                         |                 |          |                   |             |
|           |              |                                                           | Create Ansible and Jenkins servers                                    |                 |          |                   |             |
|           |              |                                                           | Fix the Jenkins server IP                                             |                 |          |                   |             |
|           |              |                                                           |                                                                       |                 |          |                   |             |
| 1         | 2            | Ansible role to update jenkins serve                      | Add repo key                                                          | 13 Feb 2020     | 2        | lkhuran           | Completed   |
|           |              |                                                           | update source.list                                                    |                 |          |                   |             |
|           |              |                                                           |                                                                       |                 |          |                   |             |
| 1         | 3            | Configuring Jenkins server                                | Pass username, password, and vault-password in setup.js file.         | 14 Feb 2020     | 5        | vpmaddur          | Completed |
|           |              |                                                           | Modify run-ansible.sh and setup.js to accept arguments from the user. |                 |          |                   |             |
|           |              |                                                           | Run Jenkins on Port 9000                                              |                 |          |                   |             |
|           |              |                                                           | Handling authentication                                               |                 |          |                   |             |
|           |              |                                                           | Installing plugins                                                    | 14 Feb 2020     |          |                   |             |
|           |              |                                                           |                                                                       |                 |          |                   |             |
| 1         | 4            | Infra Documentation                                       |                                                                       | 14 Feb 2020     | 1        | sjbondu, vpmaddur | Completed |
|           |              |                                                           |                                                                       |                 |          |                   |             |
| 1         | 5            | Jenkins setup wizard                                      | Setting up Jenkins Setup wizard                                       | 13 Feb 2020     | 1        | sjbondu           | Closed      |
|           |              |                                                           |                                                                       |                 |          |                   |             |
| 1         | 6            | Resolving File Permission Issue for Ansible Playbook      | Resolving user permission issues                                      | 18 Feb 2020     | 1        | lkhuran           | Completed   |
|           |              |                                                           |                                                                       |                 |          |                   |             |
| 2         | 7            | Installing Mongodb - configuration enhancement            | Settings up Mongodb database for configuring build environment        | 19 Feb 2020     | 1        |                   | In Progress |
|           |              |                                                           |                                                                       |                 |          |                   |             |
| 2         | 8            | Create mongo user with password and readWrite role. Build | Create mongo user with password and readWrite role.                   | 19 Feb 2020     | 2        |                   | In Progress |
|           |              |                                                           | Define mongo port                                                     |                 |          |                   |             |
|           |              |                                                           |                                                                       |                 |          |                   |             |
| 2         | 9            | creating nodejs                                           | Installing nodejs and other variable dependencies like nginx          | 19 Feb 2020     | 1        |                   | In Progress |

<br/><br/>


#### Sprint Summary Planning Checkpoint-1;

* Setting up Infrastructure
* Configuring Jenkins setup, authentication
* Using ansible vault password file

<br/><br/>

![Phase1](/Images/initial.png)

<br/><br/>

![Task progress](/Images/phase1.png)

<br/><br/>

![Final](/Images/final.PNG)

<br/><br/>




## User Stories Checkpoint-2

| Checkpoint | Issue Number | Issue Name                                                | Task                                                           | Created/Updated | Estimate | Assignees         | Completed   |
|-----------|--------------|-----------------------------------------------------------|----------------------------------------------------------------|-----------------|----------|-------------------|-------------|
|           |              |                                                           |                                                                |                 |          |                   |             |
| 2         | 7            | Installing Mongodb - configuration enhancement            | Settings up Mongodb database for configuring build environment | 19 Feb 2020     | 1        | sjbondu           | completed   |
|           |              |                                                           |                                                                |                 |          |                   |             |
| 2         | 8            | Create mongo user with password and readWrite role. Build | Create mongo user with password and readWrite role.            | 19 Feb 2020     | 2        | vpmaddur          | completed   |
|           |              |                                                           | Define mongo port                                              |                 |          |                   |             |
|           |              |                                                           |                                                                |                 |          |                   |             |
| 2         | 9            | creating nodejs                                           | Installing nodejs and other variable dependencies like nginx   | 19 Feb 2020     | 1        | lkhuran           | completed   |
|           |              |                                                           |                                                                |                 |          |                   |             |
| 2         | 11           | checkpoint documentation                                  | Create and update the checkpoint-2 documentation               | 26 Feb 2020     | 1        | lkhuran           | completed   |
|           |              |                                                           |                                                                |                 |          |                   |             |
|           |              |                                                           |                                                                |                 |          |                   |             |
| 2         | 12           | Configure build environment                               | Configure the environment to run on the same build server      | 26 Feb 2020     | 1        | vpmaddur          | completed   |
|           |              |                                                           |                                                                |                 |          |                   |             |
|           |              |                                                           |                                                                |                 |          |                   |             |
| 2         | 13           | Automate build environment                                | construct build environment automatically                      | 26 Feb 2020     | 1        | lkhuran, sjbondu  | completed   |
|           |              |                                                           |                                                                |                 |          |                   |             |
|           |              |                                                           |                                                                |                 |          |                   |             |
| 3         | 12           | clone repo and install modules                            | clone repo                                                     | 26 Feb 2020     | 2        | vpmaddur          | In progress |
|           |              |                                                           | Install npm packages                                           |                 |          |                   |             |
|           |              |                                                           |                                                                |                 |          |                   |             |
|           |              |                                                           |                                                                |                 |          |                   |             |
| 3         | 13           | start mongodb and server.js                               | start mongodb                                                  | 26 Feb 2020     | 2        | lkhuran           | In progress |
|           |              |                                                           | start server.js                                                |                 |          |                   |             |
|           |              |                                                           |                                                                |                 |          |                   |             |
| 3         | 14           | passing npm test                                          | validating tests                                               | 26 Feb 2020     | 1        | sjbondu           | In progress |
|           |              |                                                           |                                                                |                 |          |                   |             |
| 3         | 15           | tear down services                                        | tearing down services                                          | 26 Feb 2020     | 1        | lkhuran, vpmaddur | In progress |



#### Sprint Summary Planning Checkpoint-2

* Setting up necessary dependencies like nodejs and mongodb

* Setting up the mongo-user and the password

* Creating documentation for Checkpoint-2

<br/><br/>

![Phase1](/Images/cp1.png)

<br/><br/>

![Final](/Images/cp2.png)




## user stories checkpoint-3


| Checkpoint | Issue Number | Issue Name                  | Task                                           | Created/Updated | Estimate | Assignees         | Completed   |
|------------|--------------|-----------------------------|------------------------------------------------|-----------------|----------|-------------------|-------------|
|            |              |                             |                                                |                 |          |                   |             |
| 3          | 13           | start mongodb and server.js | start mongodb                                  | 26 Feb 2020     | 2        | lkhuran           | In progress |
|            |              |                             | start server.js                                |                 |          |                   |             |
|            |              |                             |                                                |                 |          |                   |             |
| 3          | 14           | passing npm test            | validating tests                               | 26 Feb 2020     | 1        | sjbondu           | In progress |
|            |              |                             |                                                |                 |          |                   |             |
| 3          | 15           | tear down services          | tearing down services                          | 26 Feb 2020     | 1        | lkhuran, vpmaddur | In progress |
|            |              |                             |                                                |                 |          |                   |             |
| 3          | 18           | Fetch jenkins log           | Fetch the jenkins log via api call             | 2 Mar 2020      | 1        | sjbondu           | completed   |
|            |              |                             |                                                |                 |          |                   |             |
|            |              |                             |                                                |                 |          |                   |             |
| 3          | 19           | Fix pipeline build command  | fix pipeline build checkbox.io                 | 2 Mar 2020      | 2        | vpmaddur, lkhuran | completed   |
|            |              |                             | Check corner cases - invalid build name        |                 |          |                   |             |
|            |              |                             |                                                |                 |          |                   |             |
| 3          | 20           | Report Documentation        | Update the Readme and checkpoint documentation | 4 Mar 2020      | 1        | vpmaddur          | completed   |




#### Sprint Summary Planning Checkpoint-3

The overview of steps that we performed in the Milestone are:

* Installing the necessary apt packages such as pip, jenkins job builder, pm2

* Acquire crumb to genrate Access token for Jenkins

* Creating pipeline to install node modules, run the app, perform tests and teardown services

<br/><br/>

![Phase1](/Images/c31.png)

<br/><br/>

![phase2](/Images/c32.png)

<br/><br/>

![final](/Images/c33.png)


